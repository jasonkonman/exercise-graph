#!/usr/bin/env python3
"""Inspect and validate the review corpus; Python standard library only."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1] / "corpus"
ATTRIBUTES = {
    "execution", "equipment", "movement_patterns", "body_regions", "force",
    "joint_actions", "planes", "muscles", "laterality", "support", "mechanics",
    "loading", "coaching_cues", "prerequisites", "numeric_joint_rom",
    "clinical_precautions", "difficulty",
}
BASES = {
    "project_defined_variant", "coaching_classification", "biomechanical_interpretation",
    "coaching_judgment", "not_established", "direct_source_description",
}
CONVENTIONS = {
    "none": ("bodyweight", None),
    "total_bar_plus_plates": ("external", "kg"),
    "total_trap_bar_plus_plates": ("external", "kg"),
    "per_dumbbell": ("external", "kg"),
    "single_implement": ("external", "kg"),
    "device_setting": ("external", "device_setting"),
}


class CorpusError(ValueError):
    pass


def require(condition, message):
    if not condition:
        raise CorpusError(message)


def read_json(path):
    def unique_keys(pairs):
        obj = {}
        for key, value in pairs:
            require(key not in obj, f"{path}: duplicate JSON key {key}")
            obj[key] = value
        return obj
    return json.loads(path.read_text(), object_pairs_hook=unique_keys)


def text(value):
    return isinstance(value, str) and bool(value.strip())


def string_list(value, allow_empty=False):
    return (isinstance(value, list) and (allow_empty or bool(value))
            and all(text(x) for x in value) and len(set(value)) == len(value))


def validate(manifest, vocabulary, sources, exercises):
    require(manifest["schema_version"] == 1, "Unsupported corpus schema")
    require(manifest["status"] == "draft_for_user_review", "This baseline must remain a draft")
    require(manifest["recommendations_enabled"] is False, "Recommendations must be disabled")
    require(len(exercises) == manifest["exercise_count"], "Manifest count does not match records")
    require(vocabulary["schema_version"] == sources["schema_version"] == 1, "Unsupported vocabulary/source schema")
    source_by_id = {s["id"]: s for s in sources["sources"]}
    require(len(source_by_id) == len(sources["sources"]), "Duplicate source IDs")
    for source in source_by_id.values():
        require(all(text(source.get(k)) for k in ["id", "title", "kind", "location", "revision", "accessed", "licence", "usage"]), "Incomplete source metadata")
        if not source["location"].startswith("https://"):
            require((ROOT / source["location"]).is_file(), f"Missing local source {source['location']}")
        if "sha256" in source:
            require(bool(re.fullmatch(r"[a-f0-9]{64}", source["sha256"])), "Invalid source hash")

    def refs(items, where, required=True):
        require(isinstance(items, list) and (bool(items) or not required), f"{where}: missing references")
        for item in items:
            require(isinstance(item, dict) and set(item) == {"source_id", "locator"}, f"{where}: invalid reference")
            require(item["source_id"] in source_by_id and text(item["locator"]), f"{where}: unknown source or empty locator")

    for mid, muscle in vocabulary["muscles"].items():
        require(text(muscle["label"]) and muscle["kind"] in {"muscle", "muscle_group"}, f"Invalid muscle {mid}")
        refs(muscle["references"], mid)
    ids, names = set(), {}
    for exercise in exercises:
        require(set(exercise) == {"id", "revision", "name", "aliases", "family_id", "definition", "catalogue_anchor", "annotations", "review", "recommendation_eligible"}, "Unrecognized/missing exercise fields")
        eid = exercise["id"]
        require(bool(re.fullmatch(r"[a-z][a-z0-9-]*", eid)) and eid not in ids, f"Invalid/duplicate ID: {eid}")
        ids.add(eid)
        require(type(exercise["revision"]) is int and exercise["revision"] >= 1, f"{eid}: invalid revision")
        require(text(exercise["name"]) and text(exercise["definition"]), f"{eid}: missing identity/definition")
        require(string_list(exercise["aliases"], True), f"{eid}: invalid aliases")
        for name in [exercise["name"], *exercise["aliases"]]:
            normalized = re.sub(r"[^a-z0-9]", "", name.casefold())
            require(normalized not in names, f"Alias/name collision: {name} ({names.get(normalized)}, {eid})")
            names[normalized] = eid
        require(exercise["family_id"] in vocabulary["families"], f"{eid}: invalid family")
        require(exercise["recommendation_eligible"] is False, f"{eid}: must not enable recommendations")
        review = exercise["review"]
        require(review["status"] == "draft" and review["reviewer"] is None and review["reviewed_at"] is None, f"{eid}: no human approval may be fabricated")
        require(string_list(review["notes"]), f"{eid}: missing review notes")
        anchor = exercise["catalogue_anchor"]
        require(anchor["source_id"] in source_by_id and text(anchor["record_id"]), f"{eid}: invalid catalogue anchor")
        require(anchor["relationship"] == "catalogue_context" and anchor["upstream_labels_status"] == "unreviewed", f"{eid}: imported labels must stay distinct")
        require(all(string_list(anchor[k], True) for k in ["upstream_primary_muscles", "upstream_secondary_muscles"]), f"{eid}: invalid upstream labels")
        annotations = exercise["annotations"]
        require(set(annotations) == ATTRIBUTES, f"{eid}: missing or unrecognized characteristics")
        for key, annotation in annotations.items():
            where = f"{eid}/{key}"
            require(set(annotation) == {"status", "value", "basis", "references", "review_status", "notes"}, f"{where}: invalid annotation fields")
            require(annotation["status"] in {"known", "unknown", "not_applicable"}, f"{where}: invalid missingness")
            require(annotation["basis"] in BASES and annotation["review_status"] == "draft", f"{where}: invalid basis/review status")
            require(isinstance(annotation["notes"], str), f"{where}: notes must be text")
            if annotation["status"] != "known":
                require(annotation["value"] is None and text(annotation["notes"]), f"{where}: unknown/N/A requires null and explanation")
                refs(annotation["references"], where, False)
                continue
            require(annotation["value"] is not None and annotation["basis"] != "not_established", f"{where}: known annotation lacks a basis/value")
            refs(annotation["references"], where)
            value = annotation["value"]
            if key in {"equipment", "movement_patterns", "body_regions", "joint_actions", "planes"}:
                require(string_list(value, key == "equipment"), f"{where}: expected unique IDs")
                require(set(value) <= set(vocabulary[key]), f"{where}: unknown vocabulary value")
            elif key == "muscles":
                require(isinstance(value, list) and bool(value), f"{where}: expected muscle annotations")
                require(len({m["muscle_id"] for m in value}) == len(value), f"{where}: duplicate muscle")
                for muscle in value:
                    require(muscle["muscle_id"] in vocabulary["muscles"] and muscle["role"] in vocabulary["muscle_roles"], f"{where}: invalid muscle/role")
                    refs(muscle["references"], where)
                require(annotation["basis"] == "biomechanical_interpretation", f"{where}: inferred roles must be labeled")
            elif key == "execution":
                require(isinstance(value, dict) and set(value) == {"start", "movement", "finish", "range_of_motion"} and all(text(v) for v in value.values()), f"{where}: incomplete execution")
            elif key in {"coaching_cues", "prerequisites"}:
                require(string_list(value), f"{where}: expected text list")
            elif key == "force":
                require(value in {"push", "pull", "static", "mixed"}, f"{where}: invalid force classification")
            elif key == "mechanics":
                require(value in {"single_joint", "multi_joint", "mixed", "isometric_hold"}, f"{where}: invalid mechanics")
            elif key == "laterality":
                require(set(value) == {"execution", "record_sides"} and value["execution"] in {"bilateral", "unilateral", "alternating_contralateral"} and value["record_sides"] in {"combined", "per_side"}, f"{where}: invalid laterality")
                require((value["execution"] == "bilateral") == (value["record_sides"] == "combined"), f"{where}: inconsistent side logging")
            elif key == "loading":
                require(set(value) == {"resistance_type", "load_convention", "load_unit", "primary_measure"}, f"{where}: invalid loading fields")
                require(value["load_convention"] in CONVENTIONS, f"{where}: unknown load convention")
                require((value["resistance_type"], value["load_unit"]) == CONVENTIONS[value["load_convention"]], f"{where}: incompatible load unit/type")
                require(value["primary_measure"] in {"repetitions", "seconds", "metres"}, f"{where}: invalid measure")
                equipment = annotations["equipment"]
                if equipment["status"] == "known":
                    needed = {"per_dumbbell": "dumbbell", "total_bar_plus_plates": "barbell", "total_trap_bar_plus_plates": "trap_bar", "single_implement": "kettlebell"}.get(value["load_convention"])
                    require(needed is None or needed in equipment["value"], f"{where}: load convention contradicts equipment")
            elif key == "support":
                require(text(value), f"{where}: missing support description")
            else:
                raise CorpusError(f"{where}: this draft has no supported known-value shape; keep unknown until defined")


def load(root=ROOT):
    manifest = read_json(root / "manifest.json")
    require(string_list(manifest["files"]), "Manifest needs unique exercise paths")
    for name in manifest["files"]:
        require(bool(re.fullmatch(r"exercises/[a-z][a-z0-9-]*\.json", name)), f"Invalid exercise path: {name}")
    require(set(manifest["files"]) == {str(p.relative_to(root)) for p in (root / "exercises").glob("*.json")}, "Manifest and exercise files disagree")
    exercises = [read_json(root / name) for name in manifest["files"]]
    for name, exercise in zip(manifest["files"], exercises):
        require(Path(name).stem == exercise["id"], f"File/ID mismatch: {name}")
    vocabulary = read_json(root / manifest["vocabulary_file"])
    sources = read_json(root / manifest["sources_file"])
    validate(manifest, vocabulary, sources, exercises)
    return manifest, vocabulary, sources, exercises


def matches(exercise, query=None, family=None, muscle=None, equipment=None, available=None):
    if query and query.casefold() not in " ".join([exercise["name"], *exercise["aliases"], exercise["id"]]).casefold():
        return False
    if family and exercise["family_id"] != family:
        return False
    annotations = exercise["annotations"]
    if muscle:
        item = annotations["muscles"]
        if item["status"] != "known" or muscle not in {m["muscle_id"] for m in item["value"]}:
            return False
    if equipment or available is not None:
        item = annotations["equipment"]
        if item["status"] != "known":
            return False
        if equipment and equipment not in item["value"]:
            return False
        if available is not None and not set(item["value"]) <= set(available):
            return False
    return True


def render(manifest, vocabulary, sources, exercises):
    def cell(value):
        return str(value).replace("|", "\\|").replace("\n", " ")
    def refs(items):
        return "; ".join(f"[{r['source_id']}](#source-{r['source_id']}) — {r['locator']}" for r in items)
    def display(key, annotation):
        if annotation["status"] != "known":
            return f"**{annotation['status']}** — {annotation['notes']}"
        value = annotation["value"]
        if key == "muscles":
            return "; ".join(f"{vocabulary['muscles'][m['muscle_id']]['label']} ({m['role']})" for m in value)
        if isinstance(value, dict):
            return "; ".join(f"{k}: {v}" for k, v in value.items())
        if isinstance(value, list):
            return "; ".join(value) or "No external implement required"
        return value
    known = sum(a["status"] == "known" for e in exercises for a in e["annotations"].values())
    lines = ["# Exercise corpus for review", "", f"Version: **{manifest['corpus_version']}**. {len(exercises)} variants; all are **drafts**, with no human approval recorded.", "", "Generated from the JSON records by `python3 scripts/corpus.py render`. Edit records, then regenerate this file.", "", "Muscle roles and mechanics are labeled anatomical interpretations, not direct exercise trials or activation/growth rankings. Names/classifications and technique cues are project-authored. Known means a draft value is present, not scientifically approved.", "", f"Coverage: {known} known annotation groups; {len(exercises) * len(ATTRIBUTES) - known} explicitly unknown/not-applicable groups. Numerical joint ROM, clinical precautions, and difficulty are not filled with guesses.", "", "## Review priorities", "", "Confirm each exact setup and variant boundary, inferred muscle roles, loading convention, and missing information. Preserve distinctions between catalogue context, anatomy references and coaching judgment. Use the individual JSON record for field-level edits; do not mark a whole corpus approved merely because validation passes.", "", "## Index", "", "| Exercise | Family | Record |", "| --- | --- | --- |"]
    for e in exercises:
        lines.append(f"| [{e['name']}](#{e['id']}) | {e['family_id']} | [JSON](exercises/{e['id']}.json) |")
    for e in exercises:
        lines += ["", f"<a id=\"{e['id']}\"></a>", f"## {e['name']}", "", f"ID: `{e['id']}`; revision {e['revision']}; family `{e['family_id']}`; review **draft**.", "", "Aliases: " + "; ".join(e["aliases"]) + ".", "", "| Characteristic | Draft value | Basis | References |", "| --- | --- | --- | --- |"]
        for key, a in e["annotations"].items():
            lines.append("| " + " | ".join(cell(x) for x in [key, display(key, a), a["basis"], refs(a["references"]) or "—"]) + " |")
        anchor = e["catalogue_anchor"]
        lines += ["", f"Catalogue context: `{anchor['record_id']}`. Original unreviewed muscle labels: primary {anchor['upstream_primary_muscles']}; secondary {anchor['upstream_secondary_muscles']}.", "", "Review notes: " + " ".join(e["review"]["notes"])]
    lines += ["", "## Sources", "", "Only factual reference metadata is retained; no source images, textbook tables/prose, or catalogue instructions are redistributed."]
    for s in sources["sources"]:
        lines += ["", f"<a id=\"source-{s['id']}\"></a>", f"### {s['id']}", "", f"[{s['title']}]({s['location']})", "", f"Revision: `{s['revision']}`; accessed {s['accessed']}. Licence: {s['licence']}", "", s["usage"]]
    return "\n".join(lines) + "\n"


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("validate")
    listing = sub.add_parser("list")
    listing.add_argument("--query")
    listing.add_argument("--family")
    listing.add_argument("--muscle")
    listing.add_argument("--equipment")
    listing.add_argument("--available-equipment", help="Comma-separated IDs; empty string means no external equipment")
    show = sub.add_parser("show"); show.add_argument("id")
    compare = sub.add_parser("compare"); compare.add_argument("first"); compare.add_argument("second")
    rendering = sub.add_parser("render"); rendering.add_argument("--check", action="store_true")
    sub.add_parser("export")
    args = parser.parse_args(argv)
    try:
        manifest, vocabulary, sources, exercises = load()
        by_id = {e["id"]: e for e in exercises}
        if args.command == "validate":
            print(f"Valid: {len(exercises)} draft variants, {len(vocabulary['families'])} families, {len(sources['sources'])} sources; recommendations disabled.")
        elif args.command == "list":
            for option, group in [(args.family, "families"), (args.muscle, "muscles"), (args.equipment, "equipment")]:
                require(option is None or option in vocabulary[group], f"Unknown {group} ID: {option}")
            available = None if args.available_equipment is None else [x.strip() for x in args.available_equipment.split(",") if x.strip()]
            require(available is None or set(available) <= set(vocabulary["equipment"]), "Unknown available-equipment ID")
            for e in exercises:
                if matches(e, args.query, args.family, args.muscle, args.equipment, available):
                    print(f"{e['id']}\t{e['name']}\tdraft")
        elif args.command == "show":
            require(args.id in by_id, f"Unknown exercise: {args.id}")
            print(json.dumps(by_id[args.id], indent=2, ensure_ascii=False))
        elif args.command == "compare":
            require(args.first in by_id and args.second in by_id, "Unknown exercise ID")
            first, second = by_id[args.first], by_id[args.second]
            print(f"Draft comparison: {first['name']} / {second['name']}")
            print("Shared labels do not establish equal outcomes or working weights.")
            unresolved = [key for key in sorted(ATTRIBUTES) if first["annotations"][key]["status"] != "known" or second["annotations"][key]["status"] != "known"]
            if unresolved:
                print("Unknown/not applicable in at least one record: " + ", ".join(unresolved))
            for key in sorted(ATTRIBUTES):
                left, right = first["annotations"][key], second["annotations"][key]
                if (left["status"], left["value"]) != (right["status"], right["value"]):
                    print(f"\n{key}\n  {args.first}: {json.dumps(left, ensure_ascii=False)}\n  {args.second}: {json.dumps(right, ensure_ascii=False)}")
        elif args.command == "render":
            content = render(manifest, vocabulary, sources, exercises)
            path = ROOT / "REVIEW.md"
            if args.check:
                require(path.exists() and path.read_text() == content, "REVIEW.md is stale; run render")
                print("Review catalog is current.")
            else:
                path.write_text(content)
                print(f"Wrote {path}")
        elif args.command == "export":
            print(json.dumps({"manifest": manifest, "vocabulary": vocabulary, "sources": sources, "exercises": exercises}, indent=2, ensure_ascii=False))
        return 0
    except (CorpusError, OSError, ValueError, KeyError, TypeError) as exc:
        print(f"Corpus error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
