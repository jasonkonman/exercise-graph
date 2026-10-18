# Exercise Graph

## Current purpose and scope

Build a scientifically grounded **corpus of individual physical exercises** and
their characteristics. Each record should explain what an exercise is, how its
defined variant is performed, what it involves, and which sources support its
annotations. The corpus must be useful on its own before programme generation
or client tracking exists.

Start with resistance-training exercises for generally healthy adults and a
manageable curated collection. Approximately 50 variants remains a proposed POC
size, not a scientific requirement. Expand through useful, sourced additions
rather than requiring constant exercise novelty.

## Definitions

- **Exercise family:** a defined grouping such as squat or leg curl; membership
  does not imply equal loading or training outcomes.
- **Exercise variant:** a reproducibly defined execution, including material
  equipment, body/joint position, support, and ROM differences. The main corpus unit.
- **Annotation:** a characteristic attached to an exercise revision, with its
  source, basis, applicability, and review status.
- **Outcome claim:** a statement about a training effect, separate from descriptive
  characteristics and scoped to the study's population, intervention, comparator,
  outcome, and duration.
- **Corpus revision:** an identifiable version of records, vocabularies,
  annotations, and supporting evidence.

## Characteristics of each exercise

Support these groups of characteristics. Distinguish known values, `unknown`, and
`not_applicable`; a populated field is not necessarily a verified annotation.

| Group | Characteristics |
| --- | --- |
| Identity | Stable ID, canonical name, aliases, family, variant definition, revision, source IDs |
| Execution | Starting position, movement and finishing position, relevant joint positions, ROM definition, execution cues |
| Equipment/setup | Resistance implement, machine/device where relevant, bench/rack/support requirements, setup assumptions |
| Movement | Joint actions, body regions, movement patterns, push/pull/static/mixed where applicable, anatomical planes where useful |
| Muscles | Named muscles/groups, supported roles, execution context, annotation basis |
| Laterality | Unilateral/bilateral, alternating/simultaneous, side-specific measurement where relevant |
| Support/mechanics | Body support, stance/grip, relevant stability demands, single-/multi-joint description; qualify interpretive labels |
| Loading/measurement | Bodyweight, external load, assistance or other resistance; units; total/per-implement/device-setting convention; repetitions, duration or distance where applicable |
| Practical guidance | Technique cues, setup/skill prerequisites, sourced precautions with their applicable context |
| Evidence/provenance | Attribute-level references and locators, source type, licences, uncertainty, review decisions, change history |

Do not force every exercise into a binary push/pull category. Movement-pattern
labels such as squat, hinge, horizontal push, or carry are useful versioned
coaching classifications, not a universally agreed scientific ontology.

Muscle roles may distinguish prime movers, assisting muscles, and stabilizers
when the source and execution support that distinction. If only involvement is
supported, retain that less-specific annotation rather than inventing a role or
activation percentage. Preserve broad imported labels alongside any reviewed
mapping to a controlled vocabulary.

Keep material differences such as seated/prone execution, overhead/neutral arm
position, assistance, and equipment as explicit variants. An alias must not
collapse materially different movements. Difficulty and suitability depend on
context; an imported “beginner” label is not a validated suitability assessment.
The absence of a precaution is not evidence of universal safety.

## Scientific grounding and annotation method

- Use authoritative anatomy and biomechanics references for descriptive movement
  and muscle-role annotations. Not every catalog attribute needs an intervention trial.
- Use applicable training research for outcome claims. A general programming
  review does not validate every muscle label or execution cue.
- Attach sources to the particular annotation/claim supported, including source
  identifier, passage/table or edition/section locator, access date, and context.
- Distinguish sourced descriptions, biomechanical interpretations, imported
  unreviewed labels, coaching judgments, and research findings.
- Preserve unknown, disputed, unsupported, and inapplicable states; record access
  depth and review status separately from the annotation value.
- Do not derive growth scores, percentage contributions, injury-risk ratings, or
  universal rankings from acute EMG or muscle-tag overlap. Store study-specific
  comparisons as scoped claims rather than permanent superiority/equivalence tags.
- Retain source, author, revision, licence, attribution, and redistribution status
  for imported descriptions and media; review media rights separately.
- Require human review of generated/imported claims before using them to enable
  recommendations, as described in `AGENTS.md`.

## Corpus and graph behaviour

The first workflow is to find an exercise, inspect its characteristics and sources,
and compare defined variants. Support:

- Search by canonical name and aliases.
- Filter by equipment/setup, movement, muscle, region, and laterality without
  treating unknown values as confirmed matches.
- View and compare definitions, annotations, evidence, uncertainty, and review status.
- Add/revise records without silently overwriting reviewed annotations.
- Repeatable import/export with stable identities, vocabulary validation, and provenance.

The initial graph connects variants to families, equipment, movements, muscles,
and evidence. A shared connection explains a shared characteristic; it does not
establish equal outcomes or equivalent working weights. Circuit compatibility
is not required to complete an exercise record.

## Annotation readiness

The catalog audit and science review are enough to start an annotated draft,
define the schema, and select representative variants. Identity, equipment, basic
execution, and laterality can be drafted from traceable catalog information and
checked against each variant definition.

The completed research mainly addresses programming outcomes and selected variant
comparisons. It does not supply anatomy/biomechanics coverage for every exercise.
Fill muscle roles, joint mechanics, ROM, and technique guidance through targeted
reference lookup during curation. Unsupported details remain unknown or pending
review; the proposed corpus is not already scientifically annotated.

Outcome superiority, exact activation/growth percentages, individualized suitability,
and load prescriptions are not required fields. A missing comparative trial does
not prevent a well-sourced descriptive exercise record from existing.

## POC acceptance

- Each entry has a stable identity and clear execution/setup definition distinguishing
  it from materially different variants.
- Characteristics have values or explicit missingness states, recorded bases, and
  review status; substantive annotations are traceable to sources.
- Search, filtering, and comparison preserve variant distinctions and uncertainty.
- Repeated imports do not duplicate identities or discard provenance/review decisions.
  Graph links have valid endpoints and declared meanings.
- Importing/generating a record does not automatically make it complete or reviewed.

## Future context, deferred from the corpus POC

The longer-term aim remains coach-assisted training for individual/group clients:
arranging exercises into sessions, optional circuits of two to five exercises,
programmes, and longer plans;
tracking performance; and suggesting targets from history, readiness, and coach goals.
Client-specific planned targets and actual results remain distinct from each other
and from the shared exercise definition.

Circuit pairings, exercise ordering, sets/repetitions, client tracking, and
personalized weights must not become prerequisites for the individual corpus.

## Research and design references

- [Corpus construction and persistence proposal](../wiki/exercise-corpus-and-graph.md)
- [Exercise-science findings and evidence](../wiki/exercise-science-review.md)
- [PostgreSQL decision and local operation](../wiki/local-database.md)

These corpus-first requirements take precedence over earlier programme/circuit
POC examples in the design research. Application features remain unimplemented.
