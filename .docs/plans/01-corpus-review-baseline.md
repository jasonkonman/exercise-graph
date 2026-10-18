# Individual exercise corpus: branch completion plan

Status: complete as a draft for user review. Continued the existing feature branch
at the user's request; no merge or human approval has been recorded.

## Deliverable

A reviewable starting corpus of approximately 50 explicitly defined resistance-
training variants. Include stable IDs, execution/setup, movement and muscle
annotations, laterality, loading conventions, source locators, review status,
and explicit unknowns. All entries remain drafts pending the user's review.

## Work

1. Inspect anatomical references and the pinned candidate catalog. Record source
   scope and licences; author original descriptions without importing images or
   textbook/catalog prose.
2. Define a versioned JSON structure and controlled vocabulary. Build the selected
   records with attribute-level provenance and clearly labeled interpretations.
3. Provide a readable review catalog and lightweight lookup/filter/compare and
   validation commands. Keep JSON as reviewable seed data for the future PostgreSQL
   application; no database/application backend is needed for this deliverable.
4. Validate structure, identities, vocabulary/source links, missingness, review
   states, loading conventions, filters, comparisons, and reproducible review output.
5. Document remaining review decisions, commit completed work, and report the
   branch as ready for review. Do not merge, publish approved claims, or enable
   recommendation policies.

## Boundaries

No circuits, programme generation, client data, individualized load predictions,
activation percentages, injury-risk scores, or universal exercise rankings.
Anatomical interpretation must not be mislabeled as a direct exercise trial.
Unknown clinical precautions, numerical ROM, and outcome comparisons remain
explicit rather than fabricated to make fields look complete.

## Delivered and checked

- Fifty JSON records across 26 families, a controlled vocabulary, eight source
  records, and a generated review catalog; all records and annotations are drafts.
- Attribute-level provenance and source-specific notes. Twenty-three anatomical
  muscle locators and all 50 catalog anchors checked against the pinned material.
- Standard-library CLI for validation, search/filter, inspection, comparison,
  deterministic review generation, and versioned JSON export.
- Fourteen tests passed, covering unavailable supports, unknown-value semantics,
  variant separation, alias/source/vocabulary integrity, loading conventions,
  draft gates, export roundtrip, and current review output.
- No database importer/backend or prescribing feature added. User review and
  finalization of this starting corpus are the remaining branch decisions.
