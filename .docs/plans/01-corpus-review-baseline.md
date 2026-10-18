# Individual exercise corpus: branch completion plan

Status: in progress. Continue the existing feature branch at the user's request.

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
