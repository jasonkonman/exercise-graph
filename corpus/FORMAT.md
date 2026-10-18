# Corpus format, version 1

This is the data contract implemented by `scripts/corpus.py`; it is not a SQL
migration or a claim that a JSON Schema library was used. All commands validate
the canonical records before reading/exporting them. The format is intentionally
restricted to the current unapproved review baseline.

## Manifest and identity

`manifest.json` identifies `corpus_version`, `schema_version`, scope, record count,
source/vocabulary files, and an ordered list of `exercises/<stable-id>.json` paths.
Unlisted/missing JSON records, duplicate paths/IDs, and filename/ID disagreement
are errors. The ordered manifest makes generated reviews and exports deterministic.

Each exercise has exactly:

| Field | Meaning |
| --- | --- |
| `id`, `revision` | Stable lowercase hyphenated ID and positive integer revision |
| `name`, `aliases` | Canonical display name and unique search aliases; punctuation/case-normalized collisions are rejected |
| `family_id` | Valid descriptive family; not an equivalence relationship |
| `definition` | Concise original description of the selected execution |
| `catalogue_anchor` | Upstream record ID/name, relationship `catalogue_context`, original muscle labels marked unreviewed, and scope note |
| `annotations` | The 17 characteristic groups below |
| `review` | Draft status, null reviewer/date, and exercise-specific review notes |
| `recommendation_eligible` | Always false for this baseline |

## Annotation envelope

Every characteristic has the same envelope:

```json
{
  "status": "known",
  "value": ["dumbbell", "flat_bench"],
  "basis": "project_defined_variant",
  "references": [
    {
      "source_id": "project-conventions",
      "locator": "Characteristics of each exercise"
    }
  ],
  "review_status": "draft",
  "notes": "Required equipment for the defined variant."
}
```

- `known`: a draft value is present, with a basis and at least one source locator.
  It does **not** mean human-reviewed or certain.
- `unknown`: value is null and notes explain the missing evidence/definition.
- `not_applicable`: value is null and notes explain why the characteristic does
  not apply. It is different from a missing investigation.
- `references`: valid `source_id` plus a nonempty locator. Empty references are
  permitted for explained unknown/not-applicable values.
- `basis`: `project_defined_variant`, `coaching_classification`,
  `biomechanical_interpretation`, `coaching_judgment`, `direct_source_description`,
  or `not_established`. The current dataset uses interpretation rather than
  mislabeling its muscle-role inferences as directly studied exercise results.

An empty known equipment list means no external apparatus. It is not an unknown
equipment requirement. Unknown precautions do not mean no precautions exist.

## Characteristic value shapes

| Characteristic | Known value shape |
| --- | --- |
| `execution` | Object with `start`, `movement`, `finish`, and textual `range_of_motion` |
| `equipment` | Unique equipment IDs, including required supports; may be empty |
| `movement_patterns`, `body_regions`, `joint_actions`, `planes` | Nonempty lists of controlled IDs |
| `force` | `push`, `pull`, `static`, or `mixed`; qualitative classification |
| `muscles` | Objects with `muscle_id`, unranked `role`, and anatomical source locators |
| `laterality` | `execution`: bilateral/unilateral/alternating_contralateral; `record_sides`: combined/per_side |
| `support` | Text describing body supports and configuration |
| `mechanics` | single_joint/multi_joint/mixed/isometric_hold; qualified by notes |
| `loading` | `resistance_type`, `load_convention`, `load_unit`, `primary_measure` |
| `coaching_cues`, `prerequisites` | Nonempty lists of original qualitative guidance |
| `numeric_joint_rom`, `clinical_precautions`, `difficulty` | Unknown in this baseline; no known-value shape has been adopted |

Joint actions describe the defined working motion, or the motion being resisted
in a hold. Return phases reverse dynamic actions. Gait is explicitly cyclic.
Planes are qualitative movement/resisted directions; a static hold does not
imply observed joint excursion. Multi-joint/single-joint classifications concern
intended motion rather than the absence of stabilizer activity; regional trunk
flexion and ambiguous mixed tasks are not asserted to involve only one literal
anatomical joint.

Muscle roles are `working_contributor`, `isometric_stabilizer`, or
`grip_contributor`. They are inferred for the execution, non-exhaustive, and do
not encode a prime-mover ranking, relative force, activation, stimulus, or growth.
Group entries are explicitly distinguished from individual muscles in the
vocabulary. No transitive muscle/family relationship establishes exercise equivalence.

Laterality means the working/recorded side, not that every other limb is inactive.
For Pallof presses it means cable-facing side; for a step-up it means lead leg.
Dead-bug repetitions need an explicit pairing-count convention.

## Loading conventions

| Convention | Resistance and unit |
| --- | --- |
| `none` | Bodyweight; external load unit null |
| `per_dumbbell` | External; kg per implement, not automatically the pair total |
| `total_bar_plus_plates` | External; kg including bar and plates |
| `total_trap_bar_plus_plates` | External; kg including the actual trap bar |
| `single_implement` | External; kg for the selected single kettlebell |
| `device_setting` | External; device-specific setting, requiring device/configuration context |

Primary measurement is `repetitions`, `seconds`, or `metres`. Bodyweight is not
recorded as zero physiological load. Machine/cable display units do not establish
equivalent force across lever arms, pulley ratios, manufacturers, or free weights.
Support heights, bench angles, handles, stance, and device settings remain explicit
execution configurations rather than invented standard numerical joint ROM.
