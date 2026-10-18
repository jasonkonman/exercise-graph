# Individual exercise corpus

Start with **[REVIEW.md](REVIEW.md)**: a readable catalog of all **50 exercise
variants across 26 families**, including sources and review notes.

Version `0.1.0-draft` is the branch's starting corpus for user review. Every record
and annotation remains a draft. No independent human approval, personalized
suitability assessment, or recommendation eligibility has been recorded.

## What is included

- Twenty lower-body variants; pressing, pulling, and arm movements; trunk tasks;
  and a bilateral dumbbell carry. These are representative choices, not a complete
  inventory or a scientifically optimal number of exercises.
- A separate JSON record for each material execution variant: identity/aliases,
  setup and execution, equipment, movement and joint actions, muscle contributors,
  laterality, support, loading/measurement, and qualitative technique cues.
- Attribute-level basis, source locators, review state, and original broad catalog
  muscle labels retained separately from the curated interpretations.
- Explicit unknowns for standardized numerical joint ROM, clinical precautions,
  and universal difficulty ratings; no activation percentages or growth scores.

Descriptions and qualitative cues are original project drafts. Anatomical muscle
actions come from the cited OpenStax sections; applying those actions to a defined
exercise is labeled **biomechanical interpretation**, not direct experimental
verification. Muscle contributors are deliberately unranked and non-exhaustive.
For example, listing gastrocnemius and soleus does not claim equal contribution.

The catalog source is context, not the execution authority for every record.
Review notes identify important narrowing/departures, including elevated rear-foot
split squats, contralateral dead bugs, and the source's instruction-free side bridge.
The project definitions are written explicitly so those differences are reviewable.

## Files and data model

- [manifest.json](manifest.json): version, scope, record paths, and draft status.
- [exercises/](exercises): 50 stable-ID JSON records; these are the editable data.
- [vocabulary.json](vocabulary.json): families, equipment, movements, muscles,
  and interpretation-role definitions.
- [sources.json](sources.json): eight source records, pinned revisions, licences,
  access details, and source artifact hashes.
- [FORMAT.md](FORMAT.md): the version 1 data contract and missingness semantics.
- [REVIEW.md](REVIEW.md): generated presentation; edit the JSON rather than this file.

These files are reviewable **seed data** for a future PostgreSQL application.
They do not introduce another writable application database. No application schema,
database importer, web service, circuits, or client workflow is included in this
corpus-only deliverable.

## Commands

From the repository root, using Python 3.10 or newer and its standard library only:

```sh
python3 scripts/corpus.py validate
python3 scripts/corpus.py list
python3 scripts/corpus.py list --query 'air squat'
python3 scripts/corpus.py list --muscle quadriceps_femoris
python3 scripts/corpus.py list --equipment dumbbell
python3 scripts/corpus.py list --available-equipment dumbbell,flat_bench
python3 scripts/corpus.py show seated-machine-leg-curl
python3 scripts/corpus.py compare seated-machine-leg-curl prone-machine-leg-curl
python3 scripts/corpus.py export > /tmp/exercise-corpus.json
python3 scripts/corpus.py render
python3 scripts/corpus.py render --check
python3 -m unittest discover -s tests -v
```

`--equipment dumbbell` finds exercises that use dumbbells; it does not claim that
dumbbells are their only requirement. `--available-equipment` requires **all**
listed implements/supports, so it excludes bench-supported variants unless the
bench is available. Use `--available-equipment ''` for no external equipment.
A normal floor is assumed. Unknown equipment does not count as no equipment.
Muscle filtering searches the recorded inferred contributors, not clinical
suitability or a primary-muscle ranking. Comparisons show differences and unresolved
fields without implying outcome or load equivalence.

`export` emits one validated, versioned JSON bundle including records, vocabulary,
sources, and manifest. Validation/tests check its roundtrip without flattening
provenance or nulls. There is no hidden network download during these commands.

## Review and finalization

Review one family at a time in `REVIEW.md`, using stable IDs to identify changes:

1. Confirm the exact execution and whether a definition needs splitting into
   additional variants or a more specific name/configuration.
2. Check required equipment/supports, side logging, and load conventions. Machine
   definitions still need a real device/settings record when used for performance
   logging; a stack setting is not comparable across all machines.
3. Check muscle roles and joint-action interpretations against the cited material.
   Add exercise-specific evidence or narrow the annotation where needed.
4. Review qualitative cues and unresolved fields; preserve unknowns that are not
   relevant or supported rather than guessing to make the record look complete.
5. Record corrections with their sources and increment a changed record's revision;
   regenerate the catalog and rerun validation/tests.

The current validation contract intentionally enforces the unapproved draft
baseline. Recording final approvals and a new release status should be a deliberate
follow-up change after user review, with actual reviewer/date information. Passing
the validator establishes data integrity, not scientific or clinical approval.

## Source use

The candidate catalog is pinned to its audited revision. Only its IDs, names, and
factual broad muscle labels are retained; instructions and images are not imported.
OpenStax is credited as the anatomy reference (Rice University, *Anatomy and
Physiology 2e*); the inspected repository's licence is CC BY-NC-SA 4.0. No textbook
prose, tables, figures, or images are redistributed. The corpus uses original
descriptions and factual interpretations with source references. Source licences
are recorded as source metadata; they do not select a licence for this repository.

The [earlier science review](../.docs/wiki/exercise-science-review.md) remains
context for future outcome claims. Its studies do not automatically validate
every descriptive annotation or this corpus's precise bilateral/implement setup.
