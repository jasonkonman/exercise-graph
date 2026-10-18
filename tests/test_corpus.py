import copy
import contextlib
import io
import json
from pathlib import Path
import unittest

from scripts import corpus


class CorpusTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = corpus.load()
        cls.by_id = {e["id"]: e for e in cls.data[3]}

    def altered(self):
        return copy.deepcopy(self.data)

    def test_baseline_is_reviewable_and_not_approved(self):
        manifest, _, _, exercises = self.data
        self.assertEqual(len(exercises), 50)
        self.assertFalse(manifest["recommendations_enabled"])
        for e in exercises:
            self.assertEqual(e["review"]["status"], "draft")
            for key in ["clinical_precautions", "numeric_joint_rom", "difficulty"]:
                self.assertEqual(e["annotations"][key]["status"], "unknown")
                self.assertIsNone(e["annotations"][key]["value"])

    def test_orphan_source_is_rejected(self):
        data = self.altered()
        data[3][0]["annotations"]["execution"]["references"][0]["source_id"] = "missing"
        with self.assertRaises(corpus.CorpusError):
            corpus.validate(*data)

    def test_name_alias_collision_is_rejected(self):
        data = self.altered()
        data[3][1]["aliases"].append("BODYWEIGHT-SQUAT")
        with self.assertRaises(corpus.CorpusError):
            corpus.validate(*data)

    def test_unknown_vocabulary_is_rejected(self):
        data = self.altered()
        data[3][0]["annotations"]["equipment"]["value"] = ["imaginary-machine"]
        with self.assertRaises(corpus.CorpusError):
            corpus.validate(*data)

    def test_unknown_cannot_contain_a_guessed_value(self):
        data = self.altered()
        data[3][0]["annotations"]["difficulty"]["value"] = "beginner"
        with self.assertRaises(corpus.CorpusError):
            corpus.validate(*data)

    def test_load_units_and_implements_must_agree(self):
        data = self.altered()
        e = next(e for e in data[3] if e["id"] == "dumbbell-flat-bench-press")
        e["annotations"]["loading"]["value"]["load_convention"] = "total_bar_plus_plates"
        with self.assertRaises(corpus.CorpusError):
            corpus.validate(*data)

    def test_unapproved_recommendations_and_unmodeled_scores_rejected(self):
        for key, value in [("recommendation_eligible", True), ("hypertrophy_score", 0.95)]:
            data = self.altered()
            data[3][0][key] = value
            with self.assertRaises(corpus.CorpusError):
                corpus.validate(*data)

    def test_available_equipment_checks_supports_too(self):
        bench = self.by_id["dumbbell-flat-bench-press"]
        self.assertTrue(corpus.matches(bench, equipment="dumbbell"))
        self.assertFalse(corpus.matches(bench, available=["dumbbell"]))
        self.assertTrue(corpus.matches(bench, available=["dumbbell", "flat_bench"]))
        split = self.by_id["dumbbell-rear-foot-elevated-split-squat"]
        self.assertFalse(corpus.matches(split, available=["dumbbell"]))

    def test_unknown_equipment_is_not_known_no_equipment(self):
        squat = copy.deepcopy(self.by_id["bodyweight-squat"])
        self.assertTrue(corpus.matches(squat, available=[]))
        squat["annotations"]["equipment"].update(status="unknown", value=None)
        self.assertFalse(corpus.matches(squat, available=[]))

    def test_alias_search_and_inferred_muscle_filter(self):
        squat = self.by_id["bodyweight-squat"]
        self.assertTrue(corpus.matches(squat, query="air squat", muscle="quadriceps_femoris"))
        self.assertFalse(corpus.matches(squat, muscle="triceps_brachii"))

    def test_material_variants_are_separate_and_comparable(self):
        seated = self.by_id["seated-machine-leg-curl"]
        prone = self.by_id["prone-machine-leg-curl"]
        self.assertEqual(seated["family_id"], prone["family_id"])
        self.assertNotEqual(seated["annotations"]["equipment"]["value"], prone["annotations"]["equipment"]["value"])
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            code = corpus.main(["compare", seated["id"], prone["id"]])
        self.assertEqual(code, 0)
        self.assertIn("clinical_precautions", output.getvalue())
        self.assertIn("do not establish equal outcomes", output.getvalue())

    def test_export_preserves_identity_provenance_and_unknowns(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            self.assertEqual(corpus.main(["export"]), 0)
        restored = json.loads(output.getvalue())
        data = (restored["manifest"], restored["vocabulary"], restored["sources"], restored["exercises"])
        corpus.validate(*data)
        self.assertEqual(data, self.data)

    def test_review_catalog_is_current_and_includes_every_record(self):
        rendered = corpus.render(*self.data)
        self.assertEqual((corpus.ROOT / "REVIEW.md").read_text(), rendered)
        for eid in self.by_id:
            self.assertIn(f'<a id="{eid}"></a>', rendered)

    def test_unknown_filter_value_is_an_error(self):
        output = io.StringIO()
        with contextlib.redirect_stderr(output):
            self.assertEqual(corpus.main(["list", "--equipment", "typo"]), 1)
        self.assertIn("Unknown equipment", output.getvalue())


if __name__ == "__main__":
    unittest.main()
