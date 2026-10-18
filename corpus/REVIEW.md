# Exercise corpus for review

Version: **0.1.0-draft**. 50 variants; all are **drafts**, with no human approval recorded.

Generated from the JSON records by `python3 scripts/corpus.py render`. Edit records, then regenerate this file.

Muscle roles and mechanics are labeled anatomical interpretations, not direct exercise trials or activation/growth rankings. Names/classifications and technique cues are project-authored. Known means a draft value is present, not scientifically approved.

Coverage: 700 known annotation groups; 150 explicitly unknown/not-applicable groups. Numerical joint ROM, clinical precautions, and difficulty are not filled with guesses.

## Review priorities

Confirm each exact setup and variant boundary, inferred muscle roles, loading convention, and missing information. Preserve distinctions between catalogue context, anatomy references and coaching judgment. Use the individual JSON record for field-level edits; do not mark a whole corpus approved merely because validation passes.

## Index

| Exercise | Family | Record |
| --- | --- | --- |
| [Bodyweight squat](#bodyweight-squat) | squat | [JSON](exercises/bodyweight-squat.json) |
| [Kettlebell goblet squat](#kettlebell-goblet-squat) | squat | [JSON](exercises/kettlebell-goblet-squat.json) |
| [Barbell high-bar back squat](#barbell-high-bar-back-squat) | squat | [JSON](exercises/barbell-high-bar-back-squat.json) |
| [Barbell front squat](#barbell-front-squat) | squat | [JSON](exercises/barbell-front-squat.json) |
| [Dumbbell rear-foot-elevated split squat](#dumbbell-rear-foot-elevated-split-squat) | split_squat | [JSON](exercises/dumbbell-rear-foot-elevated-split-squat.json) |
| [Dumbbell reverse lunge](#dumbbell-reverse-lunge) | lunge | [JSON](exercises/dumbbell-reverse-lunge.json) |
| [Dumbbell forward lunge](#dumbbell-forward-lunge) | lunge | [JSON](exercises/dumbbell-forward-lunge.json) |
| [Dumbbell step-up](#dumbbell-step-up) | step_up | [JSON](exercises/dumbbell-step-up.json) |
| [Bilateral sled leg press](#bilateral-sled-leg-press) | leg_press | [JSON](exercises/bilateral-sled-leg-press.json) |
| [Barbell conventional deadlift](#barbell-conventional-deadlift) | deadlift | [JSON](exercises/barbell-conventional-deadlift.json) |
| [Barbell Romanian deadlift](#barbell-romanian-deadlift) | hip_hinge | [JSON](exercises/barbell-romanian-deadlift.json) |
| [Trap-bar deadlift](#trap-bar-deadlift) | deadlift | [JSON](exercises/trap-bar-deadlift.json) |
| [Barbell hip thrust](#barbell-hip-thrust) | hip_bridge | [JSON](exercises/barbell-hip-thrust.json) |
| [Bodyweight glute bridge](#bodyweight-glute-bridge) | hip_bridge | [JSON](exercises/bodyweight-glute-bridge.json) |
| [Single-leg glute bridge](#single-leg-glute-bridge) | hip_bridge | [JSON](exercises/single-leg-glute-bridge.json) |
| [Seated machine leg curl](#seated-machine-leg-curl) | knee_flexion | [JSON](exercises/seated-machine-leg-curl.json) |
| [Prone machine leg curl](#prone-machine-leg-curl) | knee_flexion | [JSON](exercises/prone-machine-leg-curl.json) |
| [Seated machine leg extension](#seated-machine-leg-extension) | knee_extension | [JSON](exercises/seated-machine-leg-extension.json) |
| [Standing machine calf raise](#standing-machine-calf-raise) | calf_raise | [JSON](exercises/standing-machine-calf-raise.json) |
| [Seated machine calf raise](#seated-machine-calf-raise) | calf_raise | [JSON](exercises/seated-machine-calf-raise.json) |
| [Barbell flat bench press](#barbell-flat-bench-press) | bench_press | [JSON](exercises/barbell-flat-bench-press.json) |
| [Dumbbell flat bench press](#dumbbell-flat-bench-press) | bench_press | [JSON](exercises/dumbbell-flat-bench-press.json) |
| [Dumbbell incline bench press](#dumbbell-incline-bench-press) | bench_press | [JSON](exercises/dumbbell-incline-bench-press.json) |
| [Seated machine chest press](#seated-machine-chest-press) | bench_press | [JSON](exercises/seated-machine-chest-press.json) |
| [Floor push-up](#floor-push-up) | push_up | [JSON](exercises/floor-push-up.json) |
| [Hands-elevated push-up](#hands-elevated-push-up) | push_up | [JSON](exercises/hands-elevated-push-up.json) |
| [Standing barbell overhead press](#standing-barbell-overhead-press) | overhead_press | [JSON](exercises/standing-barbell-overhead-press.json) |
| [Seated dumbbell overhead press](#seated-dumbbell-overhead-press) | overhead_press | [JSON](exercises/seated-dumbbell-overhead-press.json) |
| [Standing dumbbell lateral raise](#standing-dumbbell-lateral-raise) | lateral_raise | [JSON](exercises/standing-dumbbell-lateral-raise.json) |
| [Chest-supported dumbbell row](#chest-supported-dumbbell-row) | row | [JSON](exercises/chest-supported-dumbbell-row.json) |
| [Bench-supported one-arm dumbbell row](#bench-supported-one-arm-dumbbell-row) | row | [JSON](exercises/bench-supported-one-arm-dumbbell-row.json) |
| [Seated neutral-grip cable row](#seated-neutral-grip-cable-row) | row | [JSON](exercises/seated-neutral-grip-cable-row.json) |
| [Bent-over barbell row](#bent-over-barbell-row) | row | [JSON](exercises/bent-over-barbell-row.json) |
| [Pronated front lat pulldown](#pronated-front-lat-pulldown) | vertical_pull | [JSON](exercises/pronated-front-lat-pulldown.json) |
| [Pronated bodyweight pull-up](#pronated-bodyweight-pull-up) | vertical_pull | [JSON](exercises/pronated-bodyweight-pull-up.json) |
| [Supinated bodyweight chin-up](#supinated-bodyweight-chin-up) | vertical_pull | [JSON](exercises/supinated-bodyweight-chin-up.json) |
| [Chest-supported dumbbell reverse fly](#chest-supported-dumbbell-reverse-fly) | reverse_fly | [JSON](exercises/chest-supported-dumbbell-reverse-fly.json) |
| [Standing barbell curl](#standing-barbell-curl) | elbow_flexion | [JSON](exercises/standing-barbell-curl.json) |
| [Standing dumbbell hammer curl](#standing-dumbbell-hammer-curl) | elbow_flexion | [JSON](exercises/standing-dumbbell-hammer-curl.json) |
| [Incline dumbbell curl](#incline-dumbbell-curl) | elbow_flexion | [JSON](exercises/incline-dumbbell-curl.json) |
| [Rope triceps pushdown](#rope-triceps-pushdown) | elbow_extension | [JSON](exercises/rope-triceps-pushdown.json) |
| [Rope overhead triceps extension](#rope-overhead-triceps-extension) | elbow_extension | [JSON](exercises/rope-overhead-triceps-extension.json) |
| [Lying straight-bar triceps extension](#lying-straight-bar-triceps-extension) | elbow_extension | [JSON](exercises/lying-straight-bar-triceps-extension.json) |
| [Forearm plank](#forearm-plank) | anti_extension | [JSON](exercises/forearm-plank.json) |
| [Side forearm plank](#side-forearm-plank) | lateral_trunk_hold | [JSON](exercises/side-forearm-plank.json) |
| [Contralateral dead bug](#contralateral-dead-bug) | trunk_control | [JSON](exercises/contralateral-dead-bug.json) |
| [Supine crunch](#supine-crunch) | trunk_flexion | [JSON](exercises/supine-crunch.json) |
| [Kneeling rope cable crunch](#kneeling-rope-cable-crunch) | trunk_flexion | [JSON](exercises/kneeling-rope-cable-crunch.json) |
| [Standing cable Pallof press](#standing-cable-pallof-press) | anti_rotation | [JSON](exercises/standing-cable-pallof-press.json) |
| [Bilateral dumbbell farmer carry](#bilateral-dumbbell-farmers-walk) | loaded_carry | [JSON](exercises/bilateral-dumbbell-farmers-walk.json) |

<a id="bodyweight-squat"></a>
## Bodyweight squat

ID: `bodyweight-squat`; revision 1; family `squat`; review **draft**.

Aliases: Air squat.

| Characteristic | Draft value | Basis | References |
| --- | --- | --- | --- |
| execution | start: Stand with both feet planted and no external implement.; movement: Bend the hips and knees to lower, then stand back up.; finish: Finish standing with the same foot placement.; range_of_motion: Use a repeatable self-selected depth; record any box or depth landmark separately. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Bodyweight_Squat.json |
| equipment | No external implement required | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Bodyweight_Squat.json |
| movement_patterns | squat | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| body_regions | lower_body | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| force | push | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| joint_actions | hip_extension; knee_extension | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| planes | sagittal | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| muscles | Quadriceps femoris (working_contributor); Gluteus maximus (working_contributor) | biomechanical_interpretation | [anatomy-lower](#source-anatomy-lower) — fs-id2591754; fig-ch11_06_03; [anatomy-lower](#source-anatomy-lower) — fig-ch11_06_02; fs-id1546298 |
| laterality | execution: bilateral; record_sides: combined | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Bodyweight_Squat.json |
| support | Both feet on the floor; no hand support. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Bodyweight_Squat.json |
| mechanics | multi_joint | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| loading | resistance_type: bodyweight; load_convention: none; load_unit: None; primary_measure: repetitions | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Bodyweight_Squat.json |
| coaching_cues | Keep the feet in their chosen stance.; Use a repeatable descent and endpoint. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Bodyweight_Squat.json |
| prerequisites | Establish the setup and chosen ROM before adding or changing resistance.; Confirm the intended execution with a coach if its definition is unfamiliar. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| numeric_joint_rom | **unknown** — No reviewed numerical joint-angle endpoints for this corpus variant; use the textual execution definition. | not_established | — |
| clinical_precautions | **unknown** — No exercise-specific clinical contraindication review completed. Unknown does not mean safe for every person. | not_established | — |
| difficulty | **unknown** — No validated universal beginner/intermediate/expert rating assigned. | not_established | — |

Catalogue context: `Bodyweight_Squat`. Original unreviewed muscle labels: primary ['quadriceps']; secondary ['glutes', 'hamstrings'].

Review notes: Stance width and depth are intentionally not claimed to have one universally optimal value.

<a id="kettlebell-goblet-squat"></a>
## Kettlebell goblet squat

ID: `kettlebell-goblet-squat`; revision 1; family `squat`; review **draft**.

Aliases: Goblet squat with kettlebell.

| Characteristic | Draft value | Basis | References |
| --- | --- | --- | --- |
| execution | start: Stand holding one kettlebell at the chest with both hands.; movement: Lower by bending the hips and knees while retaining the front-held load, then stand.; finish: Return to standing without changing the kettlebell position.; range_of_motion: Repeatable self-selected squat depth; kettlebell remains close to the chest. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Goblet_Squat.json |
| equipment | kettlebell | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Goblet_Squat.json |
| movement_patterns | squat | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| body_regions | lower_body | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| force | push | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| joint_actions | hip_extension; knee_extension | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| planes | sagittal | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| muscles | Quadriceps femoris (working_contributor); Gluteus maximus (working_contributor) | biomechanical_interpretation | [anatomy-lower](#source-anatomy-lower) — fs-id2591754; fig-ch11_06_03; [anatomy-lower](#source-anatomy-lower) — fig-ch11_06_02; fs-id1546298 |
| laterality | execution: bilateral; record_sides: combined | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Goblet_Squat.json |
| support | Two-foot stance; hands support the kettlebell. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Goblet_Squat.json |
| mechanics | multi_joint | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| loading | resistance_type: external; load_convention: single_implement; load_unit: kg; primary_measure: repetitions | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Goblet_Squat.json |
| coaching_cues | Keep the implement in the defined front position.; Use the same depth when comparing repetitions. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Goblet_Squat.json |
| prerequisites | Establish the setup and chosen ROM before adding or changing resistance.; Confirm the intended execution with a coach if its definition is unfamiliar. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| numeric_joint_rom | **unknown** — No reviewed numerical joint-angle endpoints for this corpus variant; use the textual execution definition. | not_established | — |
| clinical_precautions | **unknown** — No exercise-specific clinical contraindication review completed. Unknown does not mean safe for every person. | not_established | — |
| difficulty | **unknown** — No validated universal beginner/intermediate/expert rating assigned. | not_established | — |

Catalogue context: `Goblet_Squat`. Original unreviewed muscle labels: primary ['quadriceps']; secondary ['calves', 'glutes', 'hamstrings', 'shoulders'].

Review notes: Confirm setup, qualitative ROM, inferred muscle roles, and loading convention during review.

<a id="barbell-high-bar-back-squat"></a>
## Barbell high-bar back squat

ID: `barbell-high-bar-back-squat`; revision 1; family `squat`; review **draft**.

Aliases: High-bar squat.

| Characteristic | Draft value | Basis | References |
| --- | --- | --- | --- |
| execution | start: Stand with a barbell supported across the upper back in a high-bar position.; movement: Descend by flexing the hips and knees, then rise with the bar retained on the upper back.; finish: Stand and return the bar to its supports when finished.; range_of_motion: Self-selected repeatable squat depth; no prescribed numerical knee or hip angle. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Barbell_Squat.json |
| equipment | barbell; weight_plates; squat_rack; safety_arms | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Barbell_Squat.json |
| movement_patterns | squat | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| body_regions | lower_body | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| force | push | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| joint_actions | hip_extension; knee_extension; resist_trunk_flexion | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| planes | sagittal | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| muscles | Quadriceps femoris (working_contributor); Gluteus maximus (working_contributor); Erector spinae (isometric_stabilizer) | biomechanical_interpretation | [anatomy-lower](#source-anatomy-lower) — fs-id2591754; fig-ch11_06_03; [anatomy-lower](#source-anatomy-lower) — fig-ch11_06_02; fs-id1546298; [anatomy-back](#source-anatomy-back) — fs-id2586421 |
| laterality | execution: bilateral; record_sides: combined | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Barbell_Squat.json |
| support | Two feet; bar starts and finishes on rack supports. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Barbell_Squat.json |
| mechanics | multi_joint | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| loading | resistance_type: external; load_convention: total_bar_plus_plates; load_unit: kg; primary_measure: repetitions | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Barbell_Squat.json |
| coaching_cues | Identify the high-bar contact position and rack height.; Keep the chosen stance and depth consistent. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Barbell_Squat.json |
| prerequisites | Establish the setup and chosen ROM before adding or changing resistance.; Confirm the intended execution with a coach if its definition is unfamiliar. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| numeric_joint_rom | **unknown** — No reviewed numerical joint-angle endpoints for this corpus variant; use the textual execution definition. | not_established | — |
| clinical_precautions | **unknown** — No exercise-specific clinical contraindication review completed. Unknown does not mean safe for every person. | not_established | — |
| difficulty | **unknown** — No validated universal beginner/intermediate/expert rating assigned. | not_established | — |

Catalogue context: `Barbell_Squat`. Original unreviewed muscle labels: primary ['quadriceps']; secondary ['calves', 'glutes', 'hamstrings', 'lower back'].

Review notes: High-bar is an explicit project variant; the upstream Barbell Squat record is broader, not proof of this exact protocol.

<a id="barbell-front-squat"></a>
## Barbell front squat

ID: `barbell-front-squat`; revision 1; family `squat`; review **draft**.

Aliases: Front-rack barbell squat.

| Characteristic | Draft value | Basis | References |
| --- | --- | --- | --- |
| execution | start: Stand with the barbell in a clean-style front-rack position on the anterior shoulders.; movement: Lower through the hips and knees while maintaining the front rack, then stand.; finish: Return upright before replacing the bar on its supports.; range_of_motion: Self-selected repeatable depth with the front rack retained. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Front_Barbell_Squat.json |
| equipment | barbell; weight_plates; squat_rack; safety_arms | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Front_Barbell_Squat.json |
| movement_patterns | squat | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| body_regions | lower_body | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| force | push | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| joint_actions | hip_extension; knee_extension; resist_trunk_flexion | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| planes | sagittal | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| muscles | Quadriceps femoris (working_contributor); Gluteus maximus (working_contributor); Erector spinae (isometric_stabilizer) | biomechanical_interpretation | [anatomy-lower](#source-anatomy-lower) — fs-id2591754; fig-ch11_06_03; [anatomy-lower](#source-anatomy-lower) — fig-ch11_06_02; fs-id1546298; [anatomy-back](#source-anatomy-back) — fs-id2586421 |
| laterality | execution: bilateral; record_sides: combined | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Front_Barbell_Squat.json |
| support | Two feet; front-rack support for the bar. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Front_Barbell_Squat.json |
| mechanics | multi_joint | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| loading | resistance_type: external; load_convention: total_bar_plus_plates; load_unit: kg; primary_measure: repetitions | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Front_Barbell_Squat.json |
| coaching_cues | Establish the front rack before descending.; Retain the selected foot position and torso strategy. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Front_Barbell_Squat.json |
| prerequisites | Establish the setup and chosen ROM before adding or changing resistance.; Confirm the intended execution with a coach if its definition is unfamiliar. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| numeric_joint_rom | **unknown** — No reviewed numerical joint-angle endpoints for this corpus variant; use the textual execution definition. | not_established | — |
| clinical_precautions | **unknown** — No exercise-specific clinical contraindication review completed. Unknown does not mean safe for every person. | not_established | — |
| difficulty | **unknown** — No validated universal beginner/intermediate/expert rating assigned. | not_established | — |

Catalogue context: `Front_Barbell_Squat`. Original unreviewed muscle labels: primary ['quadriceps']; secondary ['calves', 'glutes', 'hamstrings'].

Review notes: Cross-arm and strap-assisted front racks are different variants, not aliases for this defined clean-style rack.

<a id="dumbbell-rear-foot-elevated-split-squat"></a>
## Dumbbell rear-foot-elevated split squat

ID: `dumbbell-rear-foot-elevated-split-squat`; revision 1; family `split_squat`; review **draft**.

Aliases: Dumbbell Bulgarian split squat.

| Characteristic | Draft value | Basis | References |
| --- | --- | --- | --- |
| execution | start: Use a split stance with the rear foot supported on a bench and a dumbbell in each hand.; movement: Bend the front hip and knee to lower, then return along the same path.; finish: Finish in the original split stance and record the lead leg.; range_of_motion: Repeatable depth with the rear support and front foot position unchanged. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Split_Squat_with_Dumbbells.json |
| equipment | dumbbell; flat_bench | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Split_Squat_with_Dumbbells.json |
| movement_patterns | split_squat | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| body_regions | lower_body | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| force | push | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| joint_actions | hip_extension; knee_extension | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| planes | sagittal | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| muscles | Quadriceps femoris (working_contributor); Gluteus maximus (working_contributor) | biomechanical_interpretation | [anatomy-lower](#source-anatomy-lower) — fs-id2591754; fig-ch11_06_03; [anatomy-lower](#source-anatomy-lower) — fig-ch11_06_02; fs-id1546298 |
| laterality | execution: unilateral; record_sides: per_side | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Split_Squat_with_Dumbbells.json |
| support | Front foot on the floor; rear foot on a fixed bench; implements at the sides. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Split_Squat_with_Dumbbells.json |
| mechanics | multi_joint | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| loading | resistance_type: external; load_convention: per_dumbbell; load_unit: kg; primary_measure: repetitions | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Split_Squat_with_Dumbbells.json |
| coaching_cues | Record bench height and front-foot position.; Separate left-lead and right-lead repetitions. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Split_Squat_with_Dumbbells.json |
| prerequisites | Establish the setup and chosen ROM before adding or changing resistance.; Confirm the intended execution with a coach if its definition is unfamiliar. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| numeric_joint_rom | **unknown** — No reviewed numerical joint-angle endpoints for this corpus variant; use the textual execution definition. | not_established | — |
| clinical_precautions | **unknown** — No exercise-specific clinical contraindication review completed. Unknown does not mean safe for every person. | not_established | — |
| difficulty | **unknown** — No validated universal beginner/intermediate/expert rating assigned. | not_established | — |

Catalogue context: `Split_Squat_with_Dumbbells`. Original unreviewed muscle labels: primary ['quadriceps']; secondary ['glutes', 'hamstrings'].

Review notes: The upstream Split Squat with Dumbbells already elevates the rear foot; it is not a floor split-squat record.

<a id="dumbbell-reverse-lunge"></a>
## Dumbbell reverse lunge

ID: `dumbbell-reverse-lunge`; revision 1; family `lunge`; review **draft**.

Aliases: Dumbbell rear lunge.

| Characteristic | Draft value | Basis | References |
| --- | --- | --- | --- |
| execution | start: Stand with a dumbbell in each hand at the sides.; movement: Step one foot backward, lower into the split stance, then return that foot to standing.; finish: Finish with both feet together in the original stance.; range_of_motion: Use a repeatable backward step length and lowering depth; repeat on the recorded lead side. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Dumbbell_Rear_Lunge.json |
| equipment | dumbbell | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Dumbbell_Rear_Lunge.json |
| movement_patterns | lunge | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| body_regions | lower_body | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| force | push | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| joint_actions | hip_extension; knee_extension | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| planes | sagittal | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| muscles | Quadriceps femoris (working_contributor); Gluteus maximus (working_contributor) | biomechanical_interpretation | [anatomy-lower](#source-anatomy-lower) — fs-id2591754; fig-ch11_06_03; [anatomy-lower](#source-anatomy-lower) — fig-ch11_06_02; fs-id1546298 |
| laterality | execution: unilateral; record_sides: per_side | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Dumbbell_Rear_Lunge.json |
| support | Two feet in split stance during lowering; changing support during the step. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Dumbbell_Rear_Lunge.json |
| mechanics | multi_joint | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| loading | resistance_type: external; load_convention: per_dumbbell; load_unit: kg; primary_measure: repetitions | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Dumbbell_Rear_Lunge.json |
| coaching_cues | Identify the working/front leg in the log.; Keep step length consistent between repetitions. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Dumbbell_Rear_Lunge.json |
| prerequisites | Establish the setup and chosen ROM before adding or changing resistance.; Confirm the intended execution with a coach if its definition is unfamiliar. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| numeric_joint_rom | **unknown** — No reviewed numerical joint-angle endpoints for this corpus variant; use the textual execution definition. | not_established | — |
| clinical_precautions | **unknown** — No exercise-specific clinical contraindication review completed. Unknown does not mean safe for every person. | not_established | — |
| difficulty | **unknown** — No validated universal beginner/intermediate/expert rating assigned. | not_established | — |

Catalogue context: `Dumbbell_Rear_Lunge`. Original unreviewed muscle labels: primary ['quadriceps']; secondary ['calves', 'glutes', 'hamstrings'].

Review notes: Confirm setup, qualitative ROM, inferred muscle roles, and loading convention during review.

<a id="dumbbell-forward-lunge"></a>
## Dumbbell forward lunge

ID: `dumbbell-forward-lunge`; revision 1; family `lunge`; review **draft**.

Aliases: Stationary-return dumbbell lunge.

| Characteristic | Draft value | Basis | References |
| --- | --- | --- | --- |
| execution | start: Stand holding one dumbbell in each hand.; movement: Step one foot forward, lower into a lunge, then push back to the original stance.; finish: Return the stepping foot beside the other foot before the next repetition.; range_of_motion: Repeatable forward step and depth; this record returns to the starting place rather than walking forward. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Dumbbell_Lunges.json |
| equipment | dumbbell | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Dumbbell_Lunges.json |
| movement_patterns | lunge | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| body_regions | lower_body | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| force | push | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| joint_actions | hip_extension; knee_extension | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| planes | sagittal | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| muscles | Quadriceps femoris (working_contributor); Gluteus maximus (working_contributor) | biomechanical_interpretation | [anatomy-lower](#source-anatomy-lower) — fs-id2591754; fig-ch11_06_03; [anatomy-lower](#source-anatomy-lower) — fig-ch11_06_02; fs-id1546298 |
| laterality | execution: unilateral; record_sides: per_side | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Dumbbell_Lunges.json |
| support | Alternating floor contacts during each step; no hand support. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Dumbbell_Lunges.json |
| mechanics | multi_joint | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| loading | resistance_type: external; load_convention: per_dumbbell; load_unit: kg; primary_measure: repetitions | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Dumbbell_Lunges.json |
| coaching_cues | Record the forward-stepping leg.; Distinguish this return-to-start movement from a walking lunge. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Dumbbell_Lunges.json |
| prerequisites | Establish the setup and chosen ROM before adding or changing resistance.; Confirm the intended execution with a coach if its definition is unfamiliar. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| numeric_joint_rom | **unknown** — No reviewed numerical joint-angle endpoints for this corpus variant; use the textual execution definition. | not_established | — |
| clinical_precautions | **unknown** — No exercise-specific clinical contraindication review completed. Unknown does not mean safe for every person. | not_established | — |
| difficulty | **unknown** — No validated universal beginner/intermediate/expert rating assigned. | not_established | — |

Catalogue context: `Dumbbell_Lunges`. Original unreviewed muscle labels: primary ['quadriceps']; secondary ['calves', 'glutes', 'hamstrings'].

Review notes: Confirm setup, qualitative ROM, inferred muscle roles, and loading convention during review.

<a id="dumbbell-step-up"></a>
## Dumbbell step-up

ID: `dumbbell-step-up`; revision 1; family `step_up`; review **draft**.

Aliases: Dumbbell box step-up.

| Characteristic | Draft value | Basis | References |
| --- | --- | --- | --- |
| execution | start: Stand facing a fixed platform with a dumbbell in each hand and one foot placed on top.; movement: Step onto the platform using the lead leg, then step back down under control.; finish: Return to the original floor position and retain the same lead leg for counting.; range_of_motion: Record platform height; finish the ascent standing on the platform before descending. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Dumbbell_Step_Ups.json |
| equipment | dumbbell; step_platform | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Dumbbell_Step_Ups.json |
| movement_patterns | step_up | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| body_regions | lower_body | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| force | push | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| joint_actions | hip_extension; knee_extension | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| planes | sagittal | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| muscles | Quadriceps femoris (working_contributor); Gluteus maximus (working_contributor) | biomechanical_interpretation | [anatomy-lower](#source-anatomy-lower) — fs-id2591754; fig-ch11_06_03; [anatomy-lower](#source-anatomy-lower) — fig-ch11_06_02; fs-id1546298 |
| laterality | execution: unilateral; record_sides: per_side | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Dumbbell_Step_Ups.json |
| support | Fixed raised platform and floor; no balance aid included. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Dumbbell_Step_Ups.json |
| mechanics | multi_joint | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| loading | resistance_type: external; load_convention: per_dumbbell; load_unit: kg; primary_measure: repetitions | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Dumbbell_Step_Ups.json |
| coaching_cues | Use a platform that does not move.; Keep platform height and lead side explicit. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Dumbbell_Step_Ups.json |
| prerequisites | Establish the setup and chosen ROM before adding or changing resistance.; Confirm the intended execution with a coach if its definition is unfamiliar. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| numeric_joint_rom | **unknown** — No reviewed numerical joint-angle endpoints for this corpus variant; use the textual execution definition. | not_established | — |
| clinical_precautions | **unknown** — No exercise-specific clinical contraindication review completed. Unknown does not mean safe for every person. | not_established | — |
| difficulty | **unknown** — No validated universal beginner/intermediate/expert rating assigned. | not_established | — |

Catalogue context: `Dumbbell_Step_Ups`. Original unreviewed muscle labels: primary ['quadriceps']; secondary ['calves', 'glutes', 'hamstrings'].

Review notes: Confirm setup, qualitative ROM, inferred muscle roles, and loading convention during review.

<a id="bilateral-sled-leg-press"></a>
## Bilateral sled leg press

ID: `bilateral-sled-leg-press`; revision 1; family `leg_press`; review **draft**.

Aliases: Sled leg press.

| Characteristic | Draft value | Basis | References |
| --- | --- | --- | --- |
| execution | start: Sit in a sled leg-press machine with back support and both feet on the platform.; movement: Bend the knees and hips to lower the sled, then press it away.; finish: Finish at the defined extended-leg endpoint without changing seat position.; range_of_motion: Set a repeatable sled travel range; seat angle, stops and platform position are device-specific. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Leg_Press.json |
| equipment | leg_press_machine | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Leg_Press.json |
| movement_patterns | squat | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| body_regions | lower_body | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| force | push | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| joint_actions | hip_extension; knee_extension | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| planes | sagittal | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| muscles | Quadriceps femoris (working_contributor); Gluteus maximus (working_contributor) | biomechanical_interpretation | [anatomy-lower](#source-anatomy-lower) — fs-id2591754; fig-ch11_06_03; [anatomy-lower](#source-anatomy-lower) — fig-ch11_06_02; fs-id1546298 |
| laterality | execution: bilateral; record_sides: combined | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Leg_Press.json |
| support | Back and pelvis supported by the machine; both feet contact its platform. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Leg_Press.json |
| mechanics | multi_joint | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| loading | resistance_type: external; load_convention: device_setting; load_unit: device_setting; primary_measure: repetitions | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Leg_Press.json |
| coaching_cues | Record device identity and seat settings.; Confirm the device-specific catches and stops before use. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Leg_Press.json |
| prerequisites | Establish the setup and chosen ROM before adding or changing resistance.; Confirm the intended execution with a coach if its definition is unfamiliar. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| numeric_joint_rom | **unknown** — No reviewed numerical joint-angle endpoints for this corpus variant; use the textual execution definition. | not_established | — |
| clinical_precautions | **unknown** — No exercise-specific clinical contraindication review completed. Unknown does not mean safe for every person. | not_established | — |
| difficulty | **unknown** — No validated universal beginner/intermediate/expert rating assigned. | not_established | — |

Catalogue context: `Leg_Press`. Original unreviewed muscle labels: primary ['quadriceps']; secondary ['calves', 'glutes', 'hamstrings'].

Review notes: Machine load/display settings are not directly comparable with another leg press or a free-weight squat.

<a id="barbell-conventional-deadlift"></a>
## Barbell conventional deadlift

ID: `barbell-conventional-deadlift`; revision 1; family `deadlift`; review **draft**.

Aliases: Conventional deadlift.

| Characteristic | Draft value | Basis | References |
| --- | --- | --- | --- |
| execution | start: Stand with feet inside the hands and a loaded barbell at floor level.; movement: Grip the bar and stand by extending the hips and knees, then return the bar to the floor.; finish: Finish each repetition with the bar returned to its floor start.; range_of_motion: Floor-to-standing and return; starting height depends on the loaded plates. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Barbell_Deadlift.json |
| equipment | barbell; weight_plates | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Barbell_Deadlift.json |
| movement_patterns | hip_hinge | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| body_regions | lower_body | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| force | pull | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| joint_actions | hip_extension; knee_extension; resist_trunk_flexion | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| planes | sagittal | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| muscles | Gluteus maximus (working_contributor); Quadriceps femoris (working_contributor); Biarticular hamstrings (working_contributor); Erector spinae (isometric_stabilizer) | biomechanical_interpretation | [anatomy-lower](#source-anatomy-lower) — fig-ch11_06_02; fs-id1546298; [anatomy-lower](#source-anatomy-lower) — fs-id2591754; fig-ch11_06_03; [anatomy-lower](#source-anatomy-lower) — fs-id2012638; fig-ch11_06_03; [anatomy-back](#source-anatomy-back) — fs-id2586421 |
| laterality | execution: bilateral; record_sides: combined | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Barbell_Deadlift.json |
| support | Both feet; hands hold the bar outside the legs. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Barbell_Deadlift.json |
| mechanics | multi_joint | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| loading | resistance_type: external; load_convention: total_bar_plus_plates; load_unit: kg; primary_measure: repetitions | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Barbell_Deadlift.json |
| coaching_cues | Record a changed starting height as a different setup.; Keep the bar path and stance consistent. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Barbell_Deadlift.json |
| prerequisites | Establish the setup and chosen ROM before adding or changing resistance.; Confirm the intended execution with a coach if its definition is unfamiliar. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| numeric_joint_rom | **unknown** — No reviewed numerical joint-angle endpoints for this corpus variant; use the textual execution definition. | not_established | — |
| clinical_precautions | **unknown** — No exercise-specific clinical contraindication review completed. Unknown does not mean safe for every person. | not_established | — |
| difficulty | **unknown** — No validated universal beginner/intermediate/expert rating assigned. | not_established | — |

Catalogue context: `Barbell_Deadlift`. Original unreviewed muscle labels: primary ['lower back']; secondary ['calves', 'forearms', 'glutes', 'hamstrings', 'lats', 'middle back', 'quadriceps', 'traps'].

Review notes: Confirm setup, qualitative ROM, inferred muscle roles, and loading convention during review.

<a id="barbell-romanian-deadlift"></a>
## Barbell Romanian deadlift

ID: `barbell-romanian-deadlift`; revision 1; family `hip_hinge`; review **draft**.

Aliases: Barbell RDL.

| Characteristic | Draft value | Basis | References |
| --- | --- | --- | --- |
| execution | start: Stand holding a barbell in front of the thighs with a small maintained knee bend.; movement: Move the hips backward to lower the bar along the legs, then extend the hips to stand.; finish: Return to the upright holding position; floor contact is not required.; range_of_motion: Use a self-selected repeatable hinge endpoint rather than forcing the bar to the floor. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Romanian_Deadlift.json |
| equipment | barbell; weight_plates | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Romanian_Deadlift.json |
| movement_patterns | hip_hinge | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| body_regions | lower_body | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| force | pull | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| joint_actions | hip_extension; resist_trunk_flexion | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| planes | sagittal | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| muscles | Gluteus maximus (working_contributor); Biarticular hamstrings (working_contributor); Erector spinae (isometric_stabilizer) | biomechanical_interpretation | [anatomy-lower](#source-anatomy-lower) — fig-ch11_06_02; fs-id1546298; [anatomy-lower](#source-anatomy-lower) — fs-id2012638; fig-ch11_06_03; [anatomy-back](#source-anatomy-back) — fs-id2586421 |
| laterality | execution: bilateral; record_sides: combined | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Romanian_Deadlift.json |
| support | Both feet; no torso support. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Romanian_Deadlift.json |
| mechanics | mixed | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| loading | resistance_type: external; load_convention: total_bar_plus_plates; load_unit: kg; primary_measure: repetitions | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Romanian_Deadlift.json |
| coaching_cues | Keep the intended knee bend distinct from a squat.; Record the chosen lower endpoint. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Romanian_Deadlift.json |
| prerequisites | Establish the setup and chosen ROM before adding or changing resistance.; Confirm the intended execution with a coach if its definition is unfamiliar. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| numeric_joint_rom | **unknown** — No reviewed numerical joint-angle endpoints for this corpus variant; use the textual execution definition. | not_established | — |
| clinical_precautions | **unknown** — No exercise-specific clinical contraindication review completed. Unknown does not mean safe for every person. | not_established | — |
| difficulty | **unknown** — No validated universal beginner/intermediate/expert rating assigned. | not_established | — |

Catalogue context: `Romanian_Deadlift`. Original unreviewed muscle labels: primary ['hamstrings']; secondary ['calves', 'glutes', 'lower back'].

Review notes: Hip-dominant motion with relatively fixed knees; a generic compound/isolation label would hide this execution distinction.

<a id="trap-bar-deadlift"></a>
## Trap-bar deadlift

ID: `trap-bar-deadlift`; revision 1; family `deadlift`; review **draft**.

Aliases: Hex-bar deadlift.

| Characteristic | Draft value | Basis | References |
| --- | --- | --- | --- |
| execution | start: Stand inside a trap bar on the floor and grip its handles.; movement: Extend the hips and knees to stand with the bar, then lower it back.; finish: Return the bar to its floor position.; range_of_motion: Floor-to-standing; record whether high or low handles are used. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Trap_Bar_Deadlift.json |
| equipment | trap_bar; weight_plates | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Trap_Bar_Deadlift.json |
| movement_patterns | hip_hinge | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| body_regions | lower_body | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| force | pull | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| joint_actions | hip_extension; knee_extension; resist_trunk_flexion | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| planes | sagittal | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| muscles | Quadriceps femoris (working_contributor); Gluteus maximus (working_contributor); Erector spinae (isometric_stabilizer) | biomechanical_interpretation | [anatomy-lower](#source-anatomy-lower) — fs-id2591754; fig-ch11_06_03; [anatomy-lower](#source-anatomy-lower) — fig-ch11_06_02; fs-id1546298; [anatomy-back](#source-anatomy-back) — fs-id2586421 |
| laterality | execution: bilateral; record_sides: combined | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Trap_Bar_Deadlift.json |
| support | Both feet; hands at the sides within the trap-bar frame. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Trap_Bar_Deadlift.json |
| mechanics | multi_joint | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| loading | resistance_type: external; load_convention: total_trap_bar_plus_plates; load_unit: kg; primary_measure: repetitions | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Trap_Bar_Deadlift.json |
| coaching_cues | Record handle height/configuration.; Compare loads only within the same bar and start-height setup. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Trap_Bar_Deadlift.json |
| prerequisites | Establish the setup and chosen ROM before adding or changing resistance.; Confirm the intended execution with a coach if its definition is unfamiliar. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| numeric_joint_rom | **unknown** — No reviewed numerical joint-angle endpoints for this corpus variant; use the textual execution definition. | not_established | — |
| clinical_precautions | **unknown** — No exercise-specific clinical contraindication review completed. Unknown does not mean safe for every person. | not_established | — |
| difficulty | **unknown** — No validated universal beginner/intermediate/expert rating assigned. | not_established | — |

Catalogue context: `Trap_Bar_Deadlift`. Original unreviewed muscle labels: primary ['quadriceps']; secondary ['glutes', 'hamstrings'].

Review notes: High/low handles need a recorded configuration; this draft does not pretend their ROM is identical.

<a id="barbell-hip-thrust"></a>
## Barbell hip thrust

ID: `barbell-hip-thrust`; revision 1; family `hip_bridge`; review **draft**.

Aliases: Bench-supported barbell hip thrust.

| Characteristic | Draft value | Basis | References |
| --- | --- | --- | --- |
| execution | start: Position the upper back against a fixed bench, feet on the floor and a padded bar across the hips.; movement: Raise the pelvis through hip extension, then lower back to the chosen bottom position.; finish: Finish with the hips lowered and the bar retained in position.; range_of_motion: Repeatable hip travel; stop the lift at the selected torso/thigh alignment without adding a trunk-extension target. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Barbell_Hip_Thrust.json |
| equipment | barbell; weight_plates; flat_bench; bar_pad | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Barbell_Hip_Thrust.json |
| movement_patterns | hip_extension | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| body_regions | lower_body | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| force | push | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| joint_actions | hip_extension | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| planes | sagittal | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| muscles | Gluteus maximus (working_contributor); Biarticular hamstrings (working_contributor) | biomechanical_interpretation | [anatomy-lower](#source-anatomy-lower) — fig-ch11_06_02; fs-id1546298; [anatomy-lower](#source-anatomy-lower) — fs-id2012638; fig-ch11_06_03 |
| laterality | execution: bilateral; record_sides: combined | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Barbell_Hip_Thrust.json |
| support | Upper back on bench, both feet on floor. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Barbell_Hip_Thrust.json |
| mechanics | single_joint | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| loading | resistance_type: external; load_convention: total_bar_plus_plates; load_unit: kg; primary_measure: repetitions | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Barbell_Hip_Thrust.json |
| coaching_cues | Record bench height and foot placement.; Keep the bar pad and bench from shifting. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Barbell_Hip_Thrust.json |
| prerequisites | Establish the setup and chosen ROM before adding or changing resistance.; Confirm the intended execution with a coach if its definition is unfamiliar. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| numeric_joint_rom | **unknown** — No reviewed numerical joint-angle endpoints for this corpus variant; use the textual execution definition. | not_established | — |
| clinical_precautions | **unknown** — No exercise-specific clinical contraindication review completed. Unknown does not mean safe for every person. | not_established | — |
| difficulty | **unknown** — No validated universal beginner/intermediate/expert rating assigned. | not_established | — |

Catalogue context: `Barbell_Hip_Thrust`. Original unreviewed muscle labels: primary ['glutes']; secondary ['calves', 'hamstrings'].

Review notes: Confirm setup, qualitative ROM, inferred muscle roles, and loading convention during review.

<a id="bodyweight-glute-bridge"></a>
## Bodyweight glute bridge

ID: `bodyweight-glute-bridge`; revision 1; family `hip_bridge`; review **draft**.

Aliases: Floor glute bridge.

| Characteristic | Draft value | Basis | References |
| --- | --- | --- | --- |
| execution | start: Lie on the back with knees bent and both feet on the floor.; movement: Raise the pelvis by extending the hips, then lower it back to the floor.; finish: Return to the original supine position.; range_of_motion: Floor-to-bridge and return; no external resistance or elevated support. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Butt_Lift_Bridge.json |
| equipment | No external implement required | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Butt_Lift_Bridge.json |
| movement_patterns | hip_extension | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| body_regions | lower_body | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| force | push | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| joint_actions | hip_extension | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| planes | sagittal | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| muscles | Gluteus maximus (working_contributor); Biarticular hamstrings (working_contributor) | biomechanical_interpretation | [anatomy-lower](#source-anatomy-lower) — fig-ch11_06_02; fs-id1546298; [anatomy-lower](#source-anatomy-lower) — fs-id2012638; fig-ch11_06_03 |
| laterality | execution: bilateral; record_sides: combined | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Butt_Lift_Bridge.json |
| support | Upper back and feet on the floor. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Butt_Lift_Bridge.json |
| mechanics | single_joint | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| loading | resistance_type: bodyweight; load_convention: none; load_unit: None; primary_measure: repetitions | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Butt_Lift_Bridge.json |
| coaching_cues | Keep foot placement consistent.; Distinguish this floor-supported variant from a bench hip thrust. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Butt_Lift_Bridge.json |
| prerequisites | Establish the setup and chosen ROM before adding or changing resistance.; Confirm the intended execution with a coach if its definition is unfamiliar. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| numeric_joint_rom | **unknown** — No reviewed numerical joint-angle endpoints for this corpus variant; use the textual execution definition. | not_established | — |
| clinical_precautions | **unknown** — No exercise-specific clinical contraindication review completed. Unknown does not mean safe for every person. | not_established | — |
| difficulty | **unknown** — No validated universal beginner/intermediate/expert rating assigned. | not_established | — |

Catalogue context: `Butt_Lift_Bridge`. Original unreviewed muscle labels: primary ['glutes']; secondary ['hamstrings'].

Review notes: Confirm setup, qualitative ROM, inferred muscle roles, and loading convention during review.

<a id="single-leg-glute-bridge"></a>
## Single-leg glute bridge

ID: `single-leg-glute-bridge`; revision 1; family `hip_bridge`; review **draft**.

Aliases: Unilateral floor glute bridge.

| Characteristic | Draft value | Basis | References |
| --- | --- | --- | --- |
| execution | start: Lie on the back with one foot planted and the other leg held off the floor.; movement: Lift and lower the pelvis using the planted leg while maintaining the selected free-leg position.; finish: Return the pelvis to the floor before repeating on the same side.; range_of_motion: Repeatable pelvic lift with the free foot remaining unsupported. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Single_Leg_Glute_Bridge.json |
| equipment | No external implement required | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Single_Leg_Glute_Bridge.json |
| movement_patterns | hip_extension | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| body_regions | lower_body | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| force | push | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| joint_actions | hip_extension | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| planes | sagittal | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| muscles | Gluteus maximus (working_contributor); Biarticular hamstrings (working_contributor); Internal and external obliques (isometric_stabilizer) | biomechanical_interpretation | [anatomy-lower](#source-anatomy-lower) — fig-ch11_06_02; fs-id1546298; [anatomy-lower](#source-anatomy-lower) — fs-id2012638; fig-ch11_06_03; [anatomy-trunk](#source-anatomy-trunk) — tbl-ch11_06 |
| laterality | execution: unilateral; record_sides: per_side | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Single_Leg_Glute_Bridge.json |
| support | Upper back and one foot on the floor. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Single_Leg_Glute_Bridge.json |
| mechanics | single_joint | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| loading | resistance_type: bodyweight; load_convention: none; load_unit: None; primary_measure: repetitions | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Single_Leg_Glute_Bridge.json |
| coaching_cues | Record the planted/working side.; Keep the free-leg configuration the same within comparisons. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Single_Leg_Glute_Bridge.json |
| prerequisites | Establish the setup and chosen ROM before adding or changing resistance.; Confirm the intended execution with a coach if its definition is unfamiliar. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| numeric_joint_rom | **unknown** — No reviewed numerical joint-angle endpoints for this corpus variant; use the textual execution definition. | not_established | — |
| clinical_precautions | **unknown** — No exercise-specific clinical contraindication review completed. Unknown does not mean safe for every person. | not_established | — |
| difficulty | **unknown** — No validated universal beginner/intermediate/expert rating assigned. | not_established | — |

Catalogue context: `Single_Leg_Glute_Bridge`. Original unreviewed muscle labels: primary ['glutes']; secondary ['hamstrings'].

Review notes: Confirm setup, qualitative ROM, inferred muscle roles, and loading convention during review.

<a id="seated-machine-leg-curl"></a>
## Seated machine leg curl

ID: `seated-machine-leg-curl`; revision 1; family `knee_flexion`; review **draft**.

Aliases: Seated leg curl.

| Characteristic | Draft value | Basis | References |
| --- | --- | --- | --- |
| execution | start: Sit in a leg-curl machine with thighs restrained and lower legs against its pad.; movement: Bend both knees to move the pad through its curling path, then return.; finish: Return to the defined extended-knee start.; range_of_motion: Use repeatable device stops; record seat/hip position and lever alignment. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Seated_Leg_Curl.json |
| equipment | seated_leg_curl_machine | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Seated_Leg_Curl.json |
| movement_patterns | knee_flexion | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| body_regions | lower_body | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| force | pull | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| joint_actions | knee_flexion | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| planes | sagittal | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| muscles | Hamstrings (working_contributor) | biomechanical_interpretation | [anatomy-lower](#source-anatomy-lower) — fs-id2012638; fig-ch11_06_03 |
| laterality | execution: bilateral; record_sides: combined | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Seated_Leg_Curl.json |
| support | Back, pelvis and thighs supported by the seated machine. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Seated_Leg_Curl.json |
| mechanics | single_joint | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| loading | resistance_type: external; load_convention: device_setting; load_unit: device_setting; primary_measure: repetitions | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Seated_Leg_Curl.json |
| coaching_cues | Record device and adjustment settings.; Keep the thighs in the defined support position. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Seated_Leg_Curl.json |
| prerequisites | Establish the setup and chosen ROM before adding or changing resistance.; Confirm the intended execution with a coach if its definition is unfamiliar. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| numeric_joint_rom | **unknown** — No reviewed numerical joint-angle endpoints for this corpus variant; use the textual execution definition. | not_established | — |
| clinical_precautions | **unknown** — No exercise-specific clinical contraindication review completed. Unknown does not mean safe for every person. | not_established | — |
| difficulty | **unknown** — No validated universal beginner/intermediate/expert rating assigned. | not_established | — |

Catalogue context: `Seated_Leg_Curl`. Original unreviewed muscle labels: primary ['hamstrings']; secondary [].

Review notes: Not merged with prone leg curls; the research comparison was a particular unilateral protocol, not automatic proof for this bilateral setup.

<a id="prone-machine-leg-curl"></a>
## Prone machine leg curl

ID: `prone-machine-leg-curl`; revision 1; family `knee_flexion`; review **draft**.

Aliases: Lying leg curl.

| Characteristic | Draft value | Basis | References |
| --- | --- | --- | --- |
| execution | start: Lie face down on the machine with the lower-leg pad positioned for the curl.; movement: Bend both knees to lift the pad, then lower it to the start.; finish: Finish in the defined near-extended knee position.; range_of_motion: Use repeatable machine stops; retain the same hip and bench position. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Lying_Leg_Curls.json |
| equipment | prone_leg_curl_machine | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Lying_Leg_Curls.json |
| movement_patterns | knee_flexion | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| body_regions | lower_body | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| force | pull | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| joint_actions | knee_flexion | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| planes | sagittal | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| muscles | Hamstrings (working_contributor) | biomechanical_interpretation | [anatomy-lower](#source-anatomy-lower) — fs-id2012638; fig-ch11_06_03 |
| laterality | execution: bilateral; record_sides: combined | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Lying_Leg_Curls.json |
| support | Torso and thighs supported face down by the machine. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Lying_Leg_Curls.json |
| mechanics | single_joint | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| loading | resistance_type: external; load_convention: device_setting; load_unit: device_setting; primary_measure: repetitions | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Lying_Leg_Curls.json |
| coaching_cues | Record the pad and axis adjustments.; Keep pelvis contact consistent. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Lying_Leg_Curls.json |
| prerequisites | Establish the setup and chosen ROM before adding or changing resistance.; Confirm the intended execution with a coach if its definition is unfamiliar. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| numeric_joint_rom | **unknown** — No reviewed numerical joint-angle endpoints for this corpus variant; use the textual execution definition. | not_established | — |
| clinical_precautions | **unknown** — No exercise-specific clinical contraindication review completed. Unknown does not mean safe for every person. | not_established | — |
| difficulty | **unknown** — No validated universal beginner/intermediate/expert rating assigned. | not_established | — |

Catalogue context: `Lying_Leg_Curls`. Original unreviewed muscle labels: primary ['hamstrings']; secondary [].

Review notes: Hip position and equipment distinguish this record from the seated variant; no equal-load assumption is made.

<a id="seated-machine-leg-extension"></a>
## Seated machine leg extension

ID: `seated-machine-leg-extension`; revision 1; family `knee_extension`; review **draft**.

Aliases: Machine knee extension.

| Characteristic | Draft value | Basis | References |
| --- | --- | --- | --- |
| execution | start: Sit with back support and both shins against the leg-extension pad.; movement: Straighten the knees to lift the pad, then bend them to return.; finish: Return to the same flexed-knee start.; range_of_motion: Device-specific knee travel; record the start/stop settings. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Leg_Extensions.json |
| equipment | leg_extension_machine | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Leg_Extensions.json |
| movement_patterns | knee_extension | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| body_regions | lower_body | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| force | push | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| joint_actions | knee_extension | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| planes | sagittal | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| muscles | Quadriceps femoris (working_contributor) | biomechanical_interpretation | [anatomy-lower](#source-anatomy-lower) — fs-id2591754; fig-ch11_06_03 |
| laterality | execution: bilateral; record_sides: combined | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Leg_Extensions.json |
| support | Back, pelvis and thighs supported by the machine. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Leg_Extensions.json |
| mechanics | single_joint | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| loading | resistance_type: external; load_convention: device_setting; load_unit: device_setting; primary_measure: repetitions | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Leg_Extensions.json |
| coaching_cues | Match machine alignment and settings between sessions.; Retain the defined seat contact. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Leg_Extensions.json |
| prerequisites | Establish the setup and chosen ROM before adding or changing resistance.; Confirm the intended execution with a coach if its definition is unfamiliar. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| numeric_joint_rom | **unknown** — No reviewed numerical joint-angle endpoints for this corpus variant; use the textual execution definition. | not_established | — |
| clinical_precautions | **unknown** — No exercise-specific clinical contraindication review completed. Unknown does not mean safe for every person. | not_established | — |
| difficulty | **unknown** — No validated universal beginner/intermediate/expert rating assigned. | not_established | — |

Catalogue context: `Leg_Extensions`. Original unreviewed muscle labels: primary ['quadriceps']; secondary [].

Review notes: Confirm setup, qualitative ROM, inferred muscle roles, and loading convention during review.

<a id="standing-machine-calf-raise"></a>
## Standing machine calf raise

ID: `standing-machine-calf-raise`; revision 1; family `calf_raise`; review **draft**.

Aliases: Straight-knee machine calf raise.

| Characteristic | Draft value | Basis | References |
| --- | --- | --- | --- |
| execution | start: Stand with the forefeet on the calf-machine platform and the pads contacting the shoulders.; movement: Raise and lower the heels primarily through ankle plantarflexion.; finish: Return to the chosen lower heel position.; range_of_motion: Record the heel travel; knees remain relatively extended rather than performing repeated squats. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Standing_Calf_Raises.json |
| equipment | standing_calf_raise_machine | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Standing_Calf_Raises.json |
| movement_patterns | plantarflexion | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| body_regions | lower_body | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| force | push | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| joint_actions | ankle_plantarflexion | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| planes | sagittal | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| muscles | Gastrocnemius (working_contributor); Soleus (working_contributor) | biomechanical_interpretation | [anatomy-lower](#source-anatomy-lower) — fs-id2421915; fig-ch11_06_04; fig-ch11_06_05 |
| laterality | execution: bilateral; record_sides: combined | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Standing_Calf_Raises.json |
| support | Forefeet on platform; hands may hold the machine handles. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Standing_Calf_Raises.json |
| mechanics | single_joint | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| loading | resistance_type: external; load_convention: device_setting; load_unit: device_setting; primary_measure: repetitions | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Standing_Calf_Raises.json |
| coaching_cues | Keep knee configuration consistent.; Record platform and pad settings. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Standing_Calf_Raises.json |
| prerequisites | Establish the setup and chosen ROM before adding or changing resistance.; Confirm the intended execution with a coach if its definition is unfamiliar. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| numeric_joint_rom | **unknown** — No reviewed numerical joint-angle endpoints for this corpus variant; use the textual execution definition. | not_established | — |
| clinical_precautions | **unknown** — No exercise-specific clinical contraindication review completed. Unknown does not mean safe for every person. | not_established | — |
| difficulty | **unknown** — No validated universal beginner/intermediate/expert rating assigned. | not_established | — |

Catalogue context: `Standing_Calf_Raises`. Original unreviewed muscle labels: primary ['calves']; secondary [].

Review notes: Both plantarflexors are annotated without claiming equal contributions or a precise gastrocnemius/soleus weighting.

<a id="seated-machine-calf-raise"></a>
## Seated machine calf raise

ID: `seated-machine-calf-raise`; revision 1; family `calf_raise`; review **draft**.

Aliases: Bent-knee machine calf raise.

| Characteristic | Draft value | Basis | References |
| --- | --- | --- | --- |
| execution | start: Sit with knees bent, thighs under the pads and forefeet on the platform.; movement: Raise the heels against the machine, then lower them to the selected endpoint.; finish: Return to the same heel position with knees still bent.; range_of_motion: Repeatable ankle travel with the recorded seat and knee configuration. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Seated_Calf_Raise.json |
| equipment | seated_calf_raise_machine | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Seated_Calf_Raise.json |
| movement_patterns | plantarflexion | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| body_regions | lower_body | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| force | push | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| joint_actions | ankle_plantarflexion | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| planes | sagittal | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| muscles | Gastrocnemius (working_contributor); Soleus (working_contributor) | biomechanical_interpretation | [anatomy-lower](#source-anatomy-lower) — fs-id2421915; fig-ch11_06_04; fig-ch11_06_05 |
| laterality | execution: bilateral; record_sides: combined | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Seated_Calf_Raise.json |
| support | Seated support, thigh pads and forefoot platform. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Seated_Calf_Raise.json |
| mechanics | single_joint | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| loading | resistance_type: external; load_convention: device_setting; load_unit: device_setting; primary_measure: repetitions | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Seated_Calf_Raise.json |
| coaching_cues | Record knee/seat position and pad setup.; Move through the chosen heel range without changing the support configuration. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Seated_Calf_Raise.json |
| prerequisites | Establish the setup and chosen ROM before adding or changing resistance.; Confirm the intended execution with a coach if its definition is unfamiliar. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| numeric_joint_rom | **unknown** — No reviewed numerical joint-angle endpoints for this corpus variant; use the textual execution definition. | not_established | — |
| clinical_precautions | **unknown** — No exercise-specific clinical contraindication review completed. Unknown does not mean safe for every person. | not_established | — |
| difficulty | **unknown** — No validated universal beginner/intermediate/expert rating assigned. | not_established | — |

Catalogue context: `Seated_Calf_Raise`. Original unreviewed muscle labels: primary ['calves']; secondary [].

Review notes: Bent-knee geometry is explicit, but no unsupported soleus-only label or percentage is assigned.

<a id="barbell-flat-bench-press"></a>
## Barbell flat bench press

ID: `barbell-flat-bench-press`; revision 1; family `bench_press`; review **draft**.

Aliases: Flat barbell bench press.

| Characteristic | Draft value | Basis | References |
| --- | --- | --- | --- |
| execution | start: Lie on a flat bench and hold a barbell above the chest with a pronated grip.; movement: Lower the bar toward a repeatable chest endpoint, then press it upward.; finish: Finish with the bar above the chest before returning it to the supports.; range_of_motion: Chest-approach to extended-arm position; grip width and touch/hover endpoint must remain explicit. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Barbell_Bench_Press_-_Medium_Grip.json |
| equipment | barbell; weight_plates; flat_bench; squat_rack; safety_arms | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Barbell_Bench_Press_-_Medium_Grip.json |
| movement_patterns | horizontal_push | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| body_regions | upper_body | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| force | push | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| joint_actions | shoulder_horizontal_adduction; elbow_extension | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| planes | transverse; sagittal | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| muscles | Pectoralis major (working_contributor); Triceps brachii (working_contributor); Deltoid (working_contributor) | biomechanical_interpretation | [anatomy-upper](#source-anatomy-upper) — fs-id2008704; fig-ch11_05_03; [anatomy-upper](#source-anatomy-upper) — fs-id2271811; fs-id2831016; fs-id2443705; [anatomy-upper](#source-anatomy-upper) — fs-id2501482; fig-ch11_05_03 |
| laterality | execution: bilateral; record_sides: combined | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Barbell_Bench_Press_-_Medium_Grip.json |
| support | Head, upper back and pelvis on bench; feet on floor; rack and catches for the bar. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Barbell_Bench_Press_-_Medium_Grip.json |
| mechanics | multi_joint | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| loading | resistance_type: external; load_convention: total_bar_plus_plates; load_unit: kg; primary_measure: repetitions | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Barbell_Bench_Press_-_Medium_Grip.json |
| coaching_cues | Record grip width and the chosen lower endpoint.; Set the rack and catches for this bench setup. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Barbell_Bench_Press_-_Medium_Grip.json |
| prerequisites | Establish the setup and chosen ROM before adding or changing resistance.; Confirm the intended execution with a coach if its definition is unfamiliar. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| numeric_joint_rom | **unknown** — No reviewed numerical joint-angle endpoints for this corpus variant; use the textual execution definition. | not_established | — |
| clinical_precautions | **unknown** — No exercise-specific clinical contraindication review completed. Unknown does not mean safe for every person. | not_established | — |
| difficulty | **unknown** — No validated universal beginner/intermediate/expert rating assigned. | not_established | — |

Catalogue context: `Barbell_Bench_Press_-_Medium_Grip`. Original unreviewed muscle labels: primary ['chest']; secondary ['shoulders', 'triceps'].

Review notes: Confirm setup, qualitative ROM, inferred muscle roles, and loading convention during review.

<a id="dumbbell-flat-bench-press"></a>
## Dumbbell flat bench press

ID: `dumbbell-flat-bench-press`; revision 1; family `bench_press`; review **draft**.

Aliases: Flat dumbbell chest press.

| Characteristic | Draft value | Basis | References |
| --- | --- | --- | --- |
| execution | start: Lie on a flat bench with a dumbbell in each hand above the chest.; movement: Lower the dumbbells beside the chest, then press them upward together.; finish: Return to the above-chest extended-arm position.; range_of_motion: Use repeatable lower endpoints and a defined palms-forward grip; no bounce or deeper-is-better target. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Dumbbell_Bench_Press.json |
| equipment | dumbbell; flat_bench | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Dumbbell_Bench_Press.json |
| movement_patterns | horizontal_push | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| body_regions | upper_body | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| force | push | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| joint_actions | shoulder_horizontal_adduction; elbow_extension | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| planes | transverse; sagittal | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| muscles | Pectoralis major (working_contributor); Triceps brachii (working_contributor); Deltoid (working_contributor) | biomechanical_interpretation | [anatomy-upper](#source-anatomy-upper) — fs-id2008704; fig-ch11_05_03; [anatomy-upper](#source-anatomy-upper) — fs-id2271811; fs-id2831016; fs-id2443705; [anatomy-upper](#source-anatomy-upper) — fs-id2501482; fig-ch11_05_03 |
| laterality | execution: bilateral; record_sides: combined | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Dumbbell_Bench_Press.json |
| support | Head, torso and pelvis supported by the bench; feet on floor. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Dumbbell_Bench_Press.json |
| mechanics | multi_joint | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| loading | resistance_type: external; load_convention: per_dumbbell; load_unit: kg; primary_measure: repetitions | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Dumbbell_Bench_Press.json |
| coaching_cues | Record load per dumbbell rather than silently doubling it.; Keep grip and lower endpoint comparable. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Dumbbell_Bench_Press.json |
| prerequisites | Establish the setup and chosen ROM before adding or changing resistance.; Confirm the intended execution with a coach if its definition is unfamiliar. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| numeric_joint_rom | **unknown** — No reviewed numerical joint-angle endpoints for this corpus variant; use the textual execution definition. | not_established | — |
| clinical_precautions | **unknown** — No exercise-specific clinical contraindication review completed. Unknown does not mean safe for every person. | not_established | — |
| difficulty | **unknown** — No validated universal beginner/intermediate/expert rating assigned. | not_established | — |

Catalogue context: `Dumbbell_Bench_Press`. Original unreviewed muscle labels: primary ['chest']; secondary ['shoulders', 'triceps'].

Review notes: Confirm setup, qualitative ROM, inferred muscle roles, and loading convention during review.

<a id="dumbbell-incline-bench-press"></a>
## Dumbbell incline bench press

ID: `dumbbell-incline-bench-press`; revision 1; family `bench_press`; review **draft**.

Aliases: Incline dumbbell press.

| Characteristic | Draft value | Basis | References |
| --- | --- | --- | --- |
| execution | start: Sit against an inclined bench with one dumbbell in each hand above the upper chest.; movement: Lower the implements beside the chest and press along the selected inclined path.; finish: Return to the above-chest extended-arm position.; range_of_motion: Bench incline and hand endpoints must be recorded; this draft does not equate all inclines. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Incline_Dumbbell_Press.json |
| equipment | dumbbell; adjustable_bench | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Incline_Dumbbell_Press.json |
| movement_patterns | inclined_push | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| body_regions | upper_body | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| force | push | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| joint_actions | shoulder_flexion; shoulder_horizontal_adduction; elbow_extension | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| planes | multi_planar | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| muscles | Pectoralis major (working_contributor); Triceps brachii (working_contributor); Deltoid (working_contributor) | biomechanical_interpretation | [anatomy-upper](#source-anatomy-upper) — fs-id2008704; fig-ch11_05_03; [anatomy-upper](#source-anatomy-upper) — fs-id2271811; fs-id2831016; fs-id2443705; [anatomy-upper](#source-anatomy-upper) — fs-id2501482; fig-ch11_05_03 |
| laterality | execution: bilateral; record_sides: combined | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Incline_Dumbbell_Press.json |
| support | Back and pelvis on inclined bench; feet on floor. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Incline_Dumbbell_Press.json |
| mechanics | multi_joint | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| loading | resistance_type: external; load_convention: per_dumbbell; load_unit: kg; primary_measure: repetitions | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Incline_Dumbbell_Press.json |
| coaching_cues | Record bench angle or adjustment notch.; Retain the chosen grip and lowering path. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Incline_Dumbbell_Press.json |
| prerequisites | Establish the setup and chosen ROM before adding or changing resistance.; Confirm the intended execution with a coach if its definition is unfamiliar. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| numeric_joint_rom | **unknown** — No reviewed numerical joint-angle endpoints for this corpus variant; use the textual execution definition. | not_established | — |
| clinical_precautions | **unknown** — No exercise-specific clinical contraindication review completed. Unknown does not mean safe for every person. | not_established | — |
| difficulty | **unknown** — No validated universal beginner/intermediate/expert rating assigned. | not_established | — |

Catalogue context: `Incline_Dumbbell_Press`. Original unreviewed muscle labels: primary ['chest']; secondary ['shoulders', 'triceps'].

Review notes: Exact bench angle remains a configuration to record; no unsupported upper-chest growth score is assigned.

<a id="seated-machine-chest-press"></a>
## Seated machine chest press

ID: `seated-machine-chest-press`; revision 1; family `bench_press`; review **draft**.

Aliases: Machine chest press.

| Characteristic | Draft value | Basis | References |
| --- | --- | --- | --- |
| execution | start: Sit with back support and both hands on the chest-press handles.; movement: Press the handles away from the chest, then return them along the machine path.; finish: Finish at the selected start stop.; range_of_motion: Record machine identity, seat adjustment and handle-travel stops. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Machine_Bench_Press.json |
| equipment | chest_press_machine | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Machine_Bench_Press.json |
| movement_patterns | horizontal_push | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| body_regions | upper_body | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| force | push | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| joint_actions | shoulder_horizontal_adduction; elbow_extension | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| planes | transverse; sagittal | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| muscles | Pectoralis major (working_contributor); Triceps brachii (working_contributor); Deltoid (working_contributor) | biomechanical_interpretation | [anatomy-upper](#source-anatomy-upper) — fs-id2008704; fig-ch11_05_03; [anatomy-upper](#source-anatomy-upper) — fs-id2271811; fs-id2831016; fs-id2443705; [anatomy-upper](#source-anatomy-upper) — fs-id2501482; fig-ch11_05_03 |
| laterality | execution: bilateral; record_sides: combined | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Machine_Bench_Press.json |
| support | Machine seat/back support and two handles. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Machine_Bench_Press.json |
| mechanics | multi_joint | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| loading | resistance_type: external; load_convention: device_setting; load_unit: device_setting; primary_measure: repetitions | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Machine_Bench_Press.json |
| coaching_cues | Record the device-specific resistance setting.; Keep the same seat and handle configuration for comparisons. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Machine_Bench_Press.json |
| prerequisites | Establish the setup and chosen ROM before adding or changing resistance.; Confirm the intended execution with a coach if its definition is unfamiliar. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| numeric_joint_rom | **unknown** — No reviewed numerical joint-angle endpoints for this corpus variant; use the textual execution definition. | not_established | — |
| clinical_precautions | **unknown** — No exercise-specific clinical contraindication review completed. Unknown does not mean safe for every person. | not_established | — |
| difficulty | **unknown** — No validated universal beginner/intermediate/expert rating assigned. | not_established | — |

Catalogue context: `Machine_Bench_Press`. Original unreviewed muscle labels: primary ['chest']; secondary ['shoulders', 'triceps'].

Review notes: Confirm setup, qualitative ROM, inferred muscle roles, and loading convention during review.

<a id="floor-push-up"></a>
## Floor push-up

ID: `floor-push-up`; revision 1; family `push_up`; review **draft**.

Aliases: Standard floor push-up.

| Characteristic | Draft value | Basis | References |
| --- | --- | --- | --- |
| execution | start: Support the body on hands and toes with the hands on the floor.; movement: Lower the torso by bending the elbows, then press back to the raised position.; finish: Return to the same hands-and-toes support.; range_of_motion: Use a repeatable chest-approach endpoint while retaining the trunk position. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Pushups.json |
| equipment | No external implement required | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Pushups.json |
| movement_patterns | horizontal_push | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| body_regions | upper_body | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| force | push | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| joint_actions | shoulder_horizontal_adduction; elbow_extension; scapular_protraction; resist_trunk_extension | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| planes | multi_planar | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| muscles | Pectoralis major (working_contributor); Triceps brachii (working_contributor); Deltoid (working_contributor); Serratus anterior (working_contributor); Rectus abdominis (isometric_stabilizer) | biomechanical_interpretation | [anatomy-upper](#source-anatomy-upper) — fs-id2008704; fig-ch11_05_03; [anatomy-upper](#source-anatomy-upper) — fs-id2271811; fs-id2831016; fs-id2443705; [anatomy-upper](#source-anatomy-upper) — fs-id2501482; fig-ch11_05_03; [anatomy-upper](#source-anatomy-upper) — tbl-ch11_08; [anatomy-trunk](#source-anatomy-trunk) — tbl-ch11_06 |
| laterality | execution: bilateral; record_sides: combined | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Pushups.json |
| support | Hands and toes on floor; knees not used as support. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Pushups.json |
| mechanics | multi_joint | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| loading | resistance_type: bodyweight; load_convention: none; load_unit: None; primary_measure: repetitions | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Pushups.json |
| coaching_cues | Define hand placement and the lowering landmark.; Keep a consistent trunk position rather than changing the variant mid-repetition. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Pushups.json |
| prerequisites | Establish the setup and chosen ROM before adding or changing resistance.; Confirm the intended execution with a coach if its definition is unfamiliar. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| numeric_joint_rom | **unknown** — No reviewed numerical joint-angle endpoints for this corpus variant; use the textual execution definition. | not_established | — |
| clinical_precautions | **unknown** — No exercise-specific clinical contraindication review completed. Unknown does not mean safe for every person. | not_established | — |
| difficulty | **unknown** — No validated universal beginner/intermediate/expert rating assigned. | not_established | — |

Catalogue context: `Pushups`. Original unreviewed muscle labels: primary ['chest']; secondary ['shoulders', 'triceps'].

Review notes: Confirm setup, qualitative ROM, inferred muscle roles, and loading convention during review.

<a id="hands-elevated-push-up"></a>
## Hands-elevated push-up

ID: `hands-elevated-push-up`; revision 1; family `push_up`; review **draft**.

Aliases: Incline push-up on bench.

| Characteristic | Draft value | Basis | References |
| --- | --- | --- | --- |
| execution | start: Place both hands on a fixed bench with feet on the floor.; movement: Lower the chest toward the bench, then press away while maintaining the body configuration.; finish: Return to extended arms with hands still elevated.; range_of_motion: Record bench height and hand placement; use a repeatable lower endpoint. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Incline_Push-Up.json |
| equipment | flat_bench | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Incline_Push-Up.json |
| movement_patterns | horizontal_push | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| body_regions | upper_body | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| force | push | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| joint_actions | shoulder_horizontal_adduction; elbow_extension; scapular_protraction; resist_trunk_extension | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| planes | multi_planar | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| muscles | Pectoralis major (working_contributor); Triceps brachii (working_contributor); Deltoid (working_contributor); Serratus anterior (working_contributor); Rectus abdominis (isometric_stabilizer) | biomechanical_interpretation | [anatomy-upper](#source-anatomy-upper) — fs-id2008704; fig-ch11_05_03; [anatomy-upper](#source-anatomy-upper) — fs-id2271811; fs-id2831016; fs-id2443705; [anatomy-upper](#source-anatomy-upper) — fs-id2501482; fig-ch11_05_03; [anatomy-upper](#source-anatomy-upper) — tbl-ch11_08; [anatomy-trunk](#source-anatomy-trunk) — tbl-ch11_06 |
| laterality | execution: bilateral; record_sides: combined | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Incline_Push-Up.json |
| support | Hands on bench and toes on floor. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Incline_Push-Up.json |
| mechanics | multi_joint | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| loading | resistance_type: bodyweight; load_convention: none; load_unit: None; primary_measure: repetitions | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Incline_Push-Up.json |
| coaching_cues | Confirm the bench remains fixed.; Record support height; a different height changes the task. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Incline_Push-Up.json |
| prerequisites | Establish the setup and chosen ROM before adding or changing resistance.; Confirm the intended execution with a coach if its definition is unfamiliar. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| numeric_joint_rom | **unknown** — No reviewed numerical joint-angle endpoints for this corpus variant; use the textual execution definition. | not_established | — |
| clinical_precautions | **unknown** — No exercise-specific clinical contraindication review completed. Unknown does not mean safe for every person. | not_established | — |
| difficulty | **unknown** — No validated universal beginner/intermediate/expert rating assigned. | not_established | — |

Catalogue context: `Incline_Push-Up`. Original unreviewed muscle labels: primary ['chest']; secondary ['shoulders', 'triceps'].

Review notes: Confirm setup, qualitative ROM, inferred muscle roles, and loading convention during review.

<a id="standing-barbell-overhead-press"></a>
## Standing barbell overhead press

ID: `standing-barbell-overhead-press`; revision 1; family `overhead_press`; review **draft**.

Aliases: Strict standing military press.

| Characteristic | Draft value | Basis | References |
| --- | --- | --- | --- |
| execution | start: Stand with a barbell held in front of the shoulders in a pronated grip.; movement: Press the bar overhead without a deliberate knee drive, then return to the shoulders.; finish: Finish at the original shoulder-height holding position.; range_of_motion: Shoulder-height to overhead endpoint; record grip and repeatable overhead position. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Standing_Military_Press.json |
| equipment | barbell; weight_plates; squat_rack | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Standing_Military_Press.json |
| movement_patterns | vertical_push | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| body_regions | upper_body | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| force | push | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| joint_actions | shoulder_flexion; shoulder_abduction; elbow_extension; resist_trunk_extension | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| planes | multi_planar | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| muscles | Deltoid (working_contributor); Triceps brachii (working_contributor); Rectus abdominis (isometric_stabilizer) | biomechanical_interpretation | [anatomy-upper](#source-anatomy-upper) — fs-id2501482; fig-ch11_05_03; [anatomy-upper](#source-anatomy-upper) — fs-id2271811; fs-id2831016; fs-id2443705; [anatomy-trunk](#source-anatomy-trunk) — tbl-ch11_06 |
| laterality | execution: bilateral; record_sides: combined | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Standing_Military_Press.json |
| support | Two-foot stance; no torso support or intentional leg drive. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Standing_Military_Press.json |
| mechanics | multi_joint | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| loading | resistance_type: external; load_convention: total_bar_plus_plates; load_unit: kg; primary_measure: repetitions | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Standing_Military_Press.json |
| coaching_cues | Keep strict press separate from a push press.; Record grip and avoid changing the task through increasing trunk lean. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Standing_Military_Press.json |
| prerequisites | Establish the setup and chosen ROM before adding or changing resistance.; Confirm the intended execution with a coach if its definition is unfamiliar. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| numeric_joint_rom | **unknown** — No reviewed numerical joint-angle endpoints for this corpus variant; use the textual execution definition. | not_established | — |
| clinical_precautions | **unknown** — No exercise-specific clinical contraindication review completed. Unknown does not mean safe for every person. | not_established | — |
| difficulty | **unknown** — No validated universal beginner/intermediate/expert rating assigned. | not_established | — |

Catalogue context: `Standing_Military_Press`. Original unreviewed muscle labels: primary ['shoulders']; secondary ['triceps'].

Review notes: Confirm setup, qualitative ROM, inferred muscle roles, and loading convention during review.

<a id="seated-dumbbell-overhead-press"></a>
## Seated dumbbell overhead press

ID: `seated-dumbbell-overhead-press`; revision 1; family `overhead_press`; review **draft**.

Aliases: Back-supported dumbbell shoulder press.

| Characteristic | Draft value | Basis | References |
| --- | --- | --- | --- |
| execution | start: Sit against an upright bench with a dumbbell at each shoulder.; movement: Press both dumbbells upward and return them to shoulder height.; finish: Finish in the same supported seated position.; range_of_motion: Shoulder-to-overhead hand travel; record bench angle and grip. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Dumbbell_Shoulder_Press.json |
| equipment | dumbbell; adjustable_bench | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Dumbbell_Shoulder_Press.json |
| movement_patterns | vertical_push | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| body_regions | upper_body | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| force | push | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| joint_actions | shoulder_flexion; shoulder_abduction; elbow_extension | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| planes | multi_planar | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| muscles | Deltoid (working_contributor); Triceps brachii (working_contributor) | biomechanical_interpretation | [anatomy-upper](#source-anatomy-upper) — fs-id2501482; fig-ch11_05_03; [anatomy-upper](#source-anatomy-upper) — fs-id2271811; fs-id2831016; fs-id2443705 |
| laterality | execution: bilateral; record_sides: combined | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Dumbbell_Shoulder_Press.json |
| support | Back and pelvis on the bench; feet on floor. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Dumbbell_Shoulder_Press.json |
| mechanics | multi_joint | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| loading | resistance_type: external; load_convention: per_dumbbell; load_unit: kg; primary_measure: repetitions | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Dumbbell_Shoulder_Press.json |
| coaching_cues | Record backrest angle.; Do not combine its load history with a standing or alternating press. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Dumbbell_Shoulder_Press.json |
| prerequisites | Establish the setup and chosen ROM before adding or changing resistance.; Confirm the intended execution with a coach if its definition is unfamiliar. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| numeric_joint_rom | **unknown** — No reviewed numerical joint-angle endpoints for this corpus variant; use the textual execution definition. | not_established | — |
| clinical_precautions | **unknown** — No exercise-specific clinical contraindication review completed. Unknown does not mean safe for every person. | not_established | — |
| difficulty | **unknown** — No validated universal beginner/intermediate/expert rating assigned. | not_established | — |

Catalogue context: `Dumbbell_Shoulder_Press`. Original unreviewed muscle labels: primary ['shoulders']; secondary ['triceps'].

Review notes: Confirm setup, qualitative ROM, inferred muscle roles, and loading convention during review.

<a id="standing-dumbbell-lateral-raise"></a>
## Standing dumbbell lateral raise

ID: `standing-dumbbell-lateral-raise`; revision 1; family `lateral_raise`; review **draft**.

Aliases: Two-arm dumbbell side raise.

| Characteristic | Draft value | Basis | References |
| --- | --- | --- | --- |
| execution | start: Stand with a dumbbell at each side and a small maintained elbow bend.; movement: Raise both arms outward toward shoulder height, then lower them.; finish: Return the arms to the sides.; range_of_motion: Sides-to-approximately-shoulder-height travel; record the chosen endpoint and elbow bend. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Side_Lateral_Raise.json |
| equipment | dumbbell | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Side_Lateral_Raise.json |
| movement_patterns | shoulder_abduction | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| body_regions | upper_body | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| force | pull | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| joint_actions | shoulder_abduction | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| planes | frontal | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| muscles | Deltoid (working_contributor); Supraspinatus (working_contributor) | biomechanical_interpretation | [anatomy-upper](#source-anatomy-upper) — fs-id2501482; fig-ch11_05_03; [anatomy-upper](#source-anatomy-upper) — fs-id2501482 |
| laterality | execution: bilateral; record_sides: combined | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Side_Lateral_Raise.json |
| support | Two feet; no torso or arm support. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Side_Lateral_Raise.json |
| mechanics | single_joint | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| loading | resistance_type: external; load_convention: per_dumbbell; load_unit: kg; primary_measure: repetitions | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Side_Lateral_Raise.json |
| coaching_cues | Keep elbow bend and raising plane consistent.; Avoid adding a deliberate hip swing to this defined variant. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Side_Lateral_Raise.json |
| prerequisites | Establish the setup and chosen ROM before adding or changing resistance.; Confirm the intended execution with a coach if its definition is unfamiliar. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| numeric_joint_rom | **unknown** — No reviewed numerical joint-angle endpoints for this corpus variant; use the textual execution definition. | not_established | — |
| clinical_precautions | **unknown** — No exercise-specific clinical contraindication review completed. Unknown does not mean safe for every person. | not_established | — |
| difficulty | **unknown** — No validated universal beginner/intermediate/expert rating assigned. | not_established | — |

Catalogue context: `Side_Lateral_Raise`. Original unreviewed muscle labels: primary ['shoulders']; secondary [].

Review notes: Listed muscle involvement is not a head-specific activation ranking or diagnosis of impingement risk.

<a id="chest-supported-dumbbell-row"></a>
## Chest-supported dumbbell row

ID: `chest-supported-dumbbell-row`; revision 1; family `row`; review **draft**.

Aliases: Incline-bench dumbbell row.

| Characteristic | Draft value | Basis | References |
| --- | --- | --- | --- |
| execution | start: Lie chest-down on an inclined bench with dumbbells hanging from straight arms.; movement: Pull the dumbbells toward the torso by moving the upper arms back and bending the elbows, then lower.; finish: Return to the hanging-arm start with chest contact retained.; range_of_motion: Record bench angle, grip and the hand-to-torso endpoint. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Dumbbell_Incline_Row.json |
| equipment | dumbbell; adjustable_bench | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Dumbbell_Incline_Row.json |
| movement_patterns | horizontal_pull | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| body_regions | upper_body | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| force | pull | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| joint_actions | shoulder_extension; elbow_flexion; scapular_retraction | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| planes | multi_planar | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| muscles | Latissimus dorsi (working_contributor); Rhomboid major and minor (working_contributor); Trapezius (working_contributor); Biceps brachii (working_contributor); Brachialis (working_contributor) | biomechanical_interpretation | [anatomy-upper](#source-anatomy-upper) — fs-id2008704; fig-ch11_05_03; [anatomy-upper](#source-anatomy-upper) — fs-id2129930; tbl-ch11_08; [anatomy-upper](#source-anatomy-upper) — tbl-ch11_08; [anatomy-upper](#source-anatomy-upper) — fs-id2271811; fs-id2831016; fs-id2443705 |
| laterality | execution: bilateral; record_sides: combined | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Dumbbell_Incline_Row.json |
| support | Chest supported on bench; feet support the lower body. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Dumbbell_Incline_Row.json |
| mechanics | multi_joint | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| loading | resistance_type: external; load_convention: per_dumbbell; load_unit: kg; primary_measure: repetitions | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Dumbbell_Incline_Row.json |
| coaching_cues | Maintain the defined chest support.; Record neutral grip and the selected elbow path. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Dumbbell_Incline_Row.json |
| prerequisites | Establish the setup and chosen ROM before adding or changing resistance.; Confirm the intended execution with a coach if its definition is unfamiliar. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| numeric_joint_rom | **unknown** — No reviewed numerical joint-angle endpoints for this corpus variant; use the textual execution definition. | not_established | — |
| clinical_precautions | **unknown** — No exercise-specific clinical contraindication review completed. Unknown does not mean safe for every person. | not_established | — |
| difficulty | **unknown** — No validated universal beginner/intermediate/expert rating assigned. | not_established | — |

Catalogue context: `Dumbbell_Incline_Row`. Original unreviewed muscle labels: primary ['middle back']; secondary ['biceps', 'forearms', 'lats', 'shoulders'].

Review notes: Confirm setup, qualitative ROM, inferred muscle roles, and loading convention during review.

<a id="bench-supported-one-arm-dumbbell-row"></a>
## Bench-supported one-arm dumbbell row

ID: `bench-supported-one-arm-dumbbell-row`; revision 1; family `row`; review **draft**.

Aliases: Three-point dumbbell row.

| Characteristic | Draft value | Basis | References |
| --- | --- | --- | --- |
| execution | start: Place the nonworking hand and knee on a bench, with the other foot on the floor and a dumbbell hanging from the working arm.; movement: Row the dumbbell toward the side of the torso, then lower it.; finish: Return to the hanging-arm position before the next repetition.; range_of_motion: Repeatable torso angle and elbow/hand endpoint; log each working arm. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/One-Arm_Dumbbell_Row.json |
| equipment | dumbbell; flat_bench | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/One-Arm_Dumbbell_Row.json |
| movement_patterns | horizontal_pull | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| body_regions | upper_body | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| force | pull | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| joint_actions | shoulder_extension; elbow_flexion; scapular_retraction | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| planes | multi_planar | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| muscles | Latissimus dorsi (working_contributor); Rhomboid major and minor (working_contributor); Trapezius (working_contributor); Biceps brachii (working_contributor); Brachialis (working_contributor) | biomechanical_interpretation | [anatomy-upper](#source-anatomy-upper) — fs-id2008704; fig-ch11_05_03; [anatomy-upper](#source-anatomy-upper) — fs-id2129930; tbl-ch11_08; [anatomy-upper](#source-anatomy-upper) — tbl-ch11_08; [anatomy-upper](#source-anatomy-upper) — fs-id2271811; fs-id2831016; fs-id2443705 |
| laterality | execution: unilateral; record_sides: per_side | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/One-Arm_Dumbbell_Row.json |
| support | One hand and knee on bench, opposite foot on floor. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/One-Arm_Dumbbell_Row.json |
| mechanics | multi_joint | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| loading | resistance_type: external; load_convention: per_dumbbell; load_unit: kg; primary_measure: repetitions | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/One-Arm_Dumbbell_Row.json |
| coaching_cues | Record the working arm rather than the support arm.; Keep bench contact and torso angle comparable. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/One-Arm_Dumbbell_Row.json |
| prerequisites | Establish the setup and chosen ROM before adding or changing resistance.; Confirm the intended execution with a coach if its definition is unfamiliar. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| numeric_joint_rom | **unknown** — No reviewed numerical joint-angle endpoints for this corpus variant; use the textual execution definition. | not_established | — |
| clinical_precautions | **unknown** — No exercise-specific clinical contraindication review completed. Unknown does not mean safe for every person. | not_established | — |
| difficulty | **unknown** — No validated universal beginner/intermediate/expert rating assigned. | not_established | — |

Catalogue context: `One-Arm_Dumbbell_Row`. Original unreviewed muscle labels: primary ['middle back']; secondary ['biceps', 'lats', 'shoulders'].

Review notes: Confirm setup, qualitative ROM, inferred muscle roles, and loading convention during review.

<a id="seated-neutral-grip-cable-row"></a>
## Seated neutral-grip cable row

ID: `seated-neutral-grip-cable-row`; revision 1; family `row`; review **draft**.

Aliases: V-handle seated cable row.

| Characteristic | Draft value | Basis | References |
| --- | --- | --- | --- |
| execution | start: Sit facing a low pulley holding a neutral-grip row handle with both hands.; movement: Pull the handle toward the torso, then return with controlled arm extension.; finish: Finish with the handle in the same forward position.; range_of_motion: Record handle, foot bracing and the amount of allowed torso movement; use the same hand endpoint. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Seated_Cable_Rows.json |
| equipment | cable_station; row_handle | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Seated_Cable_Rows.json |
| movement_patterns | horizontal_pull | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| body_regions | upper_body | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| force | pull | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| joint_actions | shoulder_extension; elbow_flexion; scapular_retraction | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| planes | multi_planar | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| muscles | Latissimus dorsi (working_contributor); Rhomboid major and minor (working_contributor); Trapezius (working_contributor); Biceps brachii (working_contributor); Brachialis (working_contributor) | biomechanical_interpretation | [anatomy-upper](#source-anatomy-upper) — fs-id2008704; fig-ch11_05_03; [anatomy-upper](#source-anatomy-upper) — fs-id2129930; tbl-ch11_08; [anatomy-upper](#source-anatomy-upper) — tbl-ch11_08; [anatomy-upper](#source-anatomy-upper) — fs-id2271811; fs-id2831016; fs-id2443705 |
| laterality | execution: bilateral; record_sides: combined | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Seated_Cable_Rows.json |
| support | Seated base and foot braces; no chest support. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Seated_Cable_Rows.json |
| mechanics | multi_joint | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| loading | resistance_type: external; load_convention: device_setting; load_unit: device_setting; primary_measure: repetitions | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Seated_Cable_Rows.json |
| coaching_cues | Record pulley/device identity and handle.; Avoid silently changing from a stable-torso row to a rocking row. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Seated_Cable_Rows.json |
| prerequisites | Establish the setup and chosen ROM before adding or changing resistance.; Confirm the intended execution with a coach if its definition is unfamiliar. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| numeric_joint_rom | **unknown** — No reviewed numerical joint-angle endpoints for this corpus variant; use the textual execution definition. | not_established | — |
| clinical_precautions | **unknown** — No exercise-specific clinical contraindication review completed. Unknown does not mean safe for every person. | not_established | — |
| difficulty | **unknown** — No validated universal beginner/intermediate/expert rating assigned. | not_established | — |

Catalogue context: `Seated_Cable_Rows`. Original unreviewed muscle labels: primary ['middle back']; secondary ['biceps', 'lats', 'shoulders'].

Review notes: Confirm setup, qualitative ROM, inferred muscle roles, and loading convention during review.

<a id="bent-over-barbell-row"></a>
## Bent-over barbell row

ID: `bent-over-barbell-row`; revision 1; family `row`; review **draft**.

Aliases: Pronated bent-over row.

| Characteristic | Draft value | Basis | References |
| --- | --- | --- | --- |
| execution | start: Stand hinged forward holding a barbell with a pronated grip and slightly bent knees.; movement: Row the bar toward the torso, then lower it while retaining the hinge.; finish: Return to the hanging-arm position without standing up each repetition.; range_of_motion: Record torso angle, grip and contact/hover landmark. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Bent_Over_Barbell_Row.json |
| equipment | barbell; weight_plates | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Bent_Over_Barbell_Row.json |
| movement_patterns | horizontal_pull; hip_hinge | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| body_regions | upper_body | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| force | pull | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| joint_actions | shoulder_extension; elbow_flexion; scapular_retraction; resist_trunk_flexion | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| planes | multi_planar | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| muscles | Latissimus dorsi (working_contributor); Rhomboid major and minor (working_contributor); Trapezius (working_contributor); Biceps brachii (working_contributor); Brachialis (working_contributor); Erector spinae (isometric_stabilizer) | biomechanical_interpretation | [anatomy-upper](#source-anatomy-upper) — fs-id2008704; fig-ch11_05_03; [anatomy-upper](#source-anatomy-upper) — fs-id2129930; tbl-ch11_08; [anatomy-upper](#source-anatomy-upper) — tbl-ch11_08; [anatomy-upper](#source-anatomy-upper) — fs-id2271811; fs-id2831016; fs-id2443705; [anatomy-back](#source-anatomy-back) — fs-id2586421 |
| laterality | execution: bilateral; record_sides: combined | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Bent_Over_Barbell_Row.json |
| support | Two feet; trunk unsupported in a maintained hinge. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Bent_Over_Barbell_Row.json |
| mechanics | multi_joint | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| loading | resistance_type: external; load_convention: total_bar_plus_plates; load_unit: kg; primary_measure: repetitions | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Bent_Over_Barbell_Row.json |
| coaching_cues | Keep torso angle part of the definition.; Distinguish this from a floor-reset Pendlay row. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Bent_Over_Barbell_Row.json |
| prerequisites | Establish the setup and chosen ROM before adding or changing resistance.; Confirm the intended execution with a coach if its definition is unfamiliar. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| numeric_joint_rom | **unknown** — No reviewed numerical joint-angle endpoints for this corpus variant; use the textual execution definition. | not_established | — |
| clinical_precautions | **unknown** — No exercise-specific clinical contraindication review completed. Unknown does not mean safe for every person. | not_established | — |
| difficulty | **unknown** — No validated universal beginner/intermediate/expert rating assigned. | not_established | — |

Catalogue context: `Bent_Over_Barbell_Row`. Original unreviewed muscle labels: primary ['middle back']; secondary ['biceps', 'lats', 'shoulders'].

Review notes: Confirm setup, qualitative ROM, inferred muscle roles, and loading convention during review.

<a id="pronated-front-lat-pulldown"></a>
## Pronated front lat pulldown

ID: `pronated-front-lat-pulldown`; revision 1; family `vertical_pull`; review **draft**.

Aliases: Front wide-bar pulldown.

| Characteristic | Draft value | Basis | References |
| --- | --- | --- | --- |
| execution | start: Sit under a high pulley with thighs restrained and hands pronated on a wide bar.; movement: Pull the bar down in front of the face toward the upper chest, then return overhead.; finish: Finish with arms overhead and the same seated support.; range_of_motion: Record grip width, seat/thigh settings and the front-of-body lower endpoint. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Wide-Grip_Lat_Pulldown.json |
| equipment | lat_pulldown_station; lat_bar | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Wide-Grip_Lat_Pulldown.json |
| movement_patterns | vertical_pull | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| body_regions | upper_body | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| force | pull | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| joint_actions | shoulder_adduction; shoulder_extension; elbow_flexion | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| planes | multi_planar | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| muscles | Latissimus dorsi (working_contributor); Biceps brachii (working_contributor); Brachialis (working_contributor) | biomechanical_interpretation | [anatomy-upper](#source-anatomy-upper) — fs-id2008704; fig-ch11_05_03; [anatomy-upper](#source-anatomy-upper) — fs-id2271811; fs-id2831016; fs-id2443705 |
| laterality | execution: bilateral; record_sides: combined | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Wide-Grip_Lat_Pulldown.json |
| support | Seated machine support and thigh restraint. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Wide-Grip_Lat_Pulldown.json |
| mechanics | multi_joint | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| loading | resistance_type: external; load_convention: device_setting; load_unit: device_setting; primary_measure: repetitions | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Wide-Grip_Lat_Pulldown.json |
| coaching_cues | Keep the path in front of the head.; Record grip width rather than assuming every wide grip is the same. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Wide-Grip_Lat_Pulldown.json |
| prerequisites | Establish the setup and chosen ROM before adding or changing resistance.; Confirm the intended execution with a coach if its definition is unfamiliar. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| numeric_joint_rom | **unknown** — No reviewed numerical joint-angle endpoints for this corpus variant; use the textual execution definition. | not_established | — |
| clinical_precautions | **unknown** — No exercise-specific clinical contraindication review completed. Unknown does not mean safe for every person. | not_established | — |
| difficulty | **unknown** — No validated universal beginner/intermediate/expert rating assigned. | not_established | — |

Catalogue context: `Wide-Grip_Lat_Pulldown`. Original unreviewed muscle labels: primary ['lats']; secondary ['biceps', 'middle back', 'shoulders'].

Review notes: Confirm setup, qualitative ROM, inferred muscle roles, and loading convention during review.

<a id="pronated-bodyweight-pull-up"></a>
## Pronated bodyweight pull-up

ID: `pronated-bodyweight-pull-up`; revision 1; family `vertical_pull`; review **draft**.

Aliases: Unassisted overhand pull-up.

| Characteristic | Draft value | Basis | References |
| --- | --- | --- | --- |
| execution | start: Hang from a bar with a pronated grip and no assistance or added weight.; movement: Pull the torso upward toward the bar, then lower to the hanging start.; finish: Return to the defined hanging-arm position.; range_of_motion: Use a repeatable upper landmark near the bar and a defined lower-arm endpoint; no kipping. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Pullups.json |
| equipment | pull_up_bar | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Pullups.json |
| movement_patterns | vertical_pull | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| body_regions | upper_body | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| force | pull | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| joint_actions | shoulder_adduction; shoulder_extension; elbow_flexion | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| planes | multi_planar | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| muscles | Latissimus dorsi (working_contributor); Biceps brachii (working_contributor); Brachialis (working_contributor) | biomechanical_interpretation | [anatomy-upper](#source-anatomy-upper) — fs-id2008704; fig-ch11_05_03; [anatomy-upper](#source-anatomy-upper) — fs-id2271811; fs-id2831016; fs-id2443705 |
| laterality | execution: bilateral; record_sides: combined | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Pullups.json |
| support | Hands on overhead bar; feet unsupported. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Pullups.json |
| mechanics | multi_joint | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| loading | resistance_type: bodyweight; load_convention: none; load_unit: None; primary_measure: repetitions | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Pullups.json |
| coaching_cues | Record grip width and body mass separately.; Keep added-weight and assisted versions as different variants. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Pullups.json |
| prerequisites | Establish the setup and chosen ROM before adding or changing resistance.; Confirm the intended execution with a coach if its definition is unfamiliar. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| numeric_joint_rom | **unknown** — No reviewed numerical joint-angle endpoints for this corpus variant; use the textual execution definition. | not_established | — |
| clinical_precautions | **unknown** — No exercise-specific clinical contraindication review completed. Unknown does not mean safe for every person. | not_established | — |
| difficulty | **unknown** — No validated universal beginner/intermediate/expert rating assigned. | not_established | — |

Catalogue context: `Pullups`. Original unreviewed muscle labels: primary ['lats']; secondary ['biceps', 'middle back'].

Review notes: Confirm setup, qualitative ROM, inferred muscle roles, and loading convention during review.

<a id="supinated-bodyweight-chin-up"></a>
## Supinated bodyweight chin-up

ID: `supinated-bodyweight-chin-up`; revision 1; family `vertical_pull`; review **draft**.

Aliases: Unassisted underhand chin-up.

| Characteristic | Draft value | Basis | References |
| --- | --- | --- | --- |
| execution | start: Hang from a bar with the palms facing toward the torso and no added load or assistance.; movement: Pull upward toward the bar, then lower back to the start.; finish: Finish at the same hanging-arm endpoint.; range_of_motion: Record grip width and upper landmark; no deliberate swinging or kipping. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Chin-Up.json |
| equipment | pull_up_bar | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Chin-Up.json |
| movement_patterns | vertical_pull | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| body_regions | upper_body | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| force | pull | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| joint_actions | shoulder_extension; shoulder_adduction; elbow_flexion | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| planes | multi_planar | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| muscles | Latissimus dorsi (working_contributor); Biceps brachii (working_contributor); Brachialis (working_contributor) | biomechanical_interpretation | [anatomy-upper](#source-anatomy-upper) — fs-id2008704; fig-ch11_05_03; [anatomy-upper](#source-anatomy-upper) — fs-id2271811; fs-id2831016; fs-id2443705 |
| laterality | execution: bilateral; record_sides: combined | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Chin-Up.json |
| support | Hands on overhead bar; feet unsupported. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Chin-Up.json |
| mechanics | multi_joint | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| loading | resistance_type: bodyweight; load_convention: none; load_unit: None; primary_measure: repetitions | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Chin-Up.json |
| coaching_cues | Retain the supinated grip definition.; Keep its performance history distinct from pronated pull-ups. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Chin-Up.json |
| prerequisites | Establish the setup and chosen ROM before adding or changing resistance.; Confirm the intended execution with a coach if its definition is unfamiliar. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| numeric_joint_rom | **unknown** — No reviewed numerical joint-angle endpoints for this corpus variant; use the textual execution definition. | not_established | — |
| clinical_precautions | **unknown** — No exercise-specific clinical contraindication review completed. Unknown does not mean safe for every person. | not_established | — |
| difficulty | **unknown** — No validated universal beginner/intermediate/expert rating assigned. | not_established | — |

Catalogue context: `Chin-Up`. Original unreviewed muscle labels: primary ['lats']; secondary ['biceps', 'forearms', 'middle back'].

Review notes: Confirm setup, qualitative ROM, inferred muscle roles, and loading convention during review.

<a id="chest-supported-dumbbell-reverse-fly"></a>
## Chest-supported dumbbell reverse fly

ID: `chest-supported-dumbbell-reverse-fly`; revision 1; family `reverse_fly`; review **draft**.

Aliases: Incline-bench rear lateral raise.

| Characteristic | Draft value | Basis | References |
| --- | --- | --- | --- |
| execution | start: Lie chest-down on a low-incline bench with dumbbells hanging below and elbows slightly bent.; movement: Move the arms outward and back toward the torso plane, then lower.; finish: Return to the same hanging-arm position.; range_of_motion: Record bench angle, elbow bend and upper-arm endpoint. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Dumbbell_Lying_Rear_Lateral_Raise.json |
| equipment | dumbbell; adjustable_bench | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Dumbbell_Lying_Rear_Lateral_Raise.json |
| movement_patterns | shoulder_horizontal_abduction | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| body_regions | upper_body | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| force | pull | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| joint_actions | shoulder_horizontal_abduction; scapular_retraction | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| planes | transverse | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| muscles | Deltoid (working_contributor); Rhomboid major and minor (working_contributor); Trapezius (working_contributor) | biomechanical_interpretation | [anatomy-upper](#source-anatomy-upper) — fs-id2501482; fig-ch11_05_03; [anatomy-upper](#source-anatomy-upper) — fs-id2129930; tbl-ch11_08; [anatomy-upper](#source-anatomy-upper) — tbl-ch11_08 |
| laterality | execution: bilateral; record_sides: combined | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Dumbbell_Lying_Rear_Lateral_Raise.json |
| support | Chest supported by bench; lower body braced on the floor. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Dumbbell_Lying_Rear_Lateral_Raise.json |
| mechanics | mixed | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| loading | resistance_type: external; load_convention: per_dumbbell; load_unit: kg; primary_measure: repetitions | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Dumbbell_Lying_Rear_Lateral_Raise.json |
| coaching_cues | Keep the elbow angle relatively fixed rather than turning it into a row.; Record the low-incline support position. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Dumbbell_Lying_Rear_Lateral_Raise.json |
| prerequisites | Establish the setup and chosen ROM before adding or changing resistance.; Confirm the intended execution with a coach if its definition is unfamiliar. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| numeric_joint_rom | **unknown** — No reviewed numerical joint-angle endpoints for this corpus variant; use the textual execution definition. | not_established | — |
| clinical_precautions | **unknown** — No exercise-specific clinical contraindication review completed. Unknown does not mean safe for every person. | not_established | — |
| difficulty | **unknown** — No validated universal beginner/intermediate/expert rating assigned. | not_established | — |

Catalogue context: `Dumbbell_Lying_Rear_Lateral_Raise`. Original unreviewed muscle labels: primary ['shoulders']; secondary [].

Review notes: Broad deltoid involvement is recorded without claiming validated posterior-head growth or activation percentages.

<a id="standing-barbell-curl"></a>
## Standing barbell curl

ID: `standing-barbell-curl`; revision 1; family `elbow_flexion`; review **draft**.

Aliases: Supinated straight-bar curl.

| Characteristic | Draft value | Basis | References |
| --- | --- | --- | --- |
| execution | start: Stand holding a straight bar with a supinated grip and upper arms near the torso.; movement: Bend the elbows to raise the bar, then lower it.; finish: Return to the original extended-arm endpoint.; range_of_motion: Repeatable elbow travel with upper-arm position held relatively stable. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Barbell_Curl.json |
| equipment | barbell; weight_plates | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Barbell_Curl.json |
| movement_patterns | elbow_flexion | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| body_regions | upper_body | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| force | pull | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| joint_actions | elbow_flexion | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| planes | sagittal | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| muscles | Biceps brachii (working_contributor); Brachialis (working_contributor); Brachioradialis (working_contributor) | biomechanical_interpretation | [anatomy-upper](#source-anatomy-upper) — fs-id2271811; fs-id2831016; fs-id2443705 |
| laterality | execution: bilateral; record_sides: combined | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Barbell_Curl.json |
| support | Two feet; no elbow pad or torso support. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Barbell_Curl.json |
| mechanics | single_joint | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| loading | resistance_type: external; load_convention: total_bar_plus_plates; load_unit: kg; primary_measure: repetitions | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Barbell_Curl.json |
| coaching_cues | Record grip width and avoid adding a deliberate hip drive.; Retain the chosen lower-arm endpoint. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Barbell_Curl.json |
| prerequisites | Establish the setup and chosen ROM before adding or changing resistance.; Confirm the intended execution with a coach if its definition is unfamiliar. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| numeric_joint_rom | **unknown** — No reviewed numerical joint-angle endpoints for this corpus variant; use the textual execution definition. | not_established | — |
| clinical_precautions | **unknown** — No exercise-specific clinical contraindication review completed. Unknown does not mean safe for every person. | not_established | — |
| difficulty | **unknown** — No validated universal beginner/intermediate/expert rating assigned. | not_established | — |

Catalogue context: `Barbell_Curl`. Original unreviewed muscle labels: primary ['biceps']; secondary ['forearms'].

Review notes: Confirm setup, qualitative ROM, inferred muscle roles, and loading convention during review.

<a id="standing-dumbbell-hammer-curl"></a>
## Standing dumbbell hammer curl

ID: `standing-dumbbell-hammer-curl`; revision 1; family `elbow_flexion`; review **draft**.

Aliases: Bilateral neutral-grip curl.

| Characteristic | Draft value | Basis | References |
| --- | --- | --- | --- |
| execution | start: Stand holding a dumbbell in each hand with palms facing inward.; movement: Bend both elbows together while retaining the neutral grip, then lower.; finish: Return the dumbbells to the sides.; range_of_motion: Repeatable elbow travel; upper arms remain near the torso. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Hammer_Curls.json |
| equipment | dumbbell | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Hammer_Curls.json |
| movement_patterns | elbow_flexion | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| body_regions | upper_body | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| force | pull | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| joint_actions | elbow_flexion | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| planes | sagittal | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| muscles | Biceps brachii (working_contributor); Brachialis (working_contributor); Brachioradialis (working_contributor) | biomechanical_interpretation | [anatomy-upper](#source-anatomy-upper) — fs-id2271811; fs-id2831016; fs-id2443705 |
| laterality | execution: bilateral; record_sides: combined | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Hammer_Curls.json |
| support | Two feet; no elbow support. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Hammer_Curls.json |
| mechanics | single_joint | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| loading | resistance_type: external; load_convention: per_dumbbell; load_unit: kg; primary_measure: repetitions | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Hammer_Curls.json |
| coaching_cues | Retain the neutral grip throughout this variant.; Log load per dumbbell. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Hammer_Curls.json |
| prerequisites | Establish the setup and chosen ROM before adding or changing resistance.; Confirm the intended execution with a coach if its definition is unfamiliar. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| numeric_joint_rom | **unknown** — No reviewed numerical joint-angle endpoints for this corpus variant; use the textual execution definition. | not_established | — |
| clinical_precautions | **unknown** — No exercise-specific clinical contraindication review completed. Unknown does not mean safe for every person. | not_established | — |
| difficulty | **unknown** — No validated universal beginner/intermediate/expert rating assigned. | not_established | — |

Catalogue context: `Hammer_Curls`. Original unreviewed muscle labels: primary ['biceps']; secondary [].

Review notes: No claim that one elbow flexor is exclusively trained or that neutral grip is universally superior.

<a id="incline-dumbbell-curl"></a>
## Incline dumbbell curl

ID: `incline-dumbbell-curl`; revision 1; family `elbow_flexion`; review **draft**.

Aliases: Back-supported incline supinated curl.

| Characteristic | Draft value | Basis | References |
| --- | --- | --- | --- |
| execution | start: Sit against an inclined backrest with dumbbells hanging beside the body and palms forward.; movement: Bend both elbows while keeping the upper-arm position relative to the torso, then lower.; finish: Return to the hanging-arm start.; range_of_motion: Record bench angle and elbow endpoints; do not equate all backrest positions. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Incline_Dumbbell_Curl.json |
| equipment | dumbbell; adjustable_bench | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Incline_Dumbbell_Curl.json |
| movement_patterns | elbow_flexion | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| body_regions | upper_body | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| force | pull | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| joint_actions | elbow_flexion | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| planes | sagittal | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| muscles | Biceps brachii (working_contributor); Brachialis (working_contributor); Brachioradialis (working_contributor) | biomechanical_interpretation | [anatomy-upper](#source-anatomy-upper) — fs-id2271811; fs-id2831016; fs-id2443705 |
| laterality | execution: bilateral; record_sides: combined | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Incline_Dumbbell_Curl.json |
| support | Back and pelvis supported by the bench; feet on floor. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Incline_Dumbbell_Curl.json |
| mechanics | single_joint | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| loading | resistance_type: external; load_convention: per_dumbbell; load_unit: kg; primary_measure: repetitions | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Incline_Dumbbell_Curl.json |
| coaching_cues | Record backrest angle.; Keep grip and upper-arm position comparable. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Incline_Dumbbell_Curl.json |
| prerequisites | Establish the setup and chosen ROM before adding or changing resistance.; Confirm the intended execution with a coach if its definition is unfamiliar. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| numeric_joint_rom | **unknown** — No reviewed numerical joint-angle endpoints for this corpus variant; use the textual execution definition. | not_established | — |
| clinical_precautions | **unknown** — No exercise-specific clinical contraindication review completed. Unknown does not mean safe for every person. | not_established | — |
| difficulty | **unknown** — No validated universal beginner/intermediate/expert rating assigned. | not_established | — |

Catalogue context: `Incline_Dumbbell_Curl`. Original unreviewed muscle labels: primary ['biceps']; secondary [].

Review notes: Confirm setup, qualitative ROM, inferred muscle roles, and loading convention during review.

<a id="rope-triceps-pushdown"></a>
## Rope triceps pushdown

ID: `rope-triceps-pushdown`; revision 1; family `elbow_extension`; review **draft**.

Aliases: High-pulley rope elbow extension.

| Characteristic | Draft value | Basis | References |
| --- | --- | --- | --- |
| execution | start: Stand facing a high pulley with both hands holding a rope and upper arms near the sides.; movement: Straighten the elbows to move the rope down, then bend them to return.; finish: Finish with the elbows at the chosen flexed start.; range_of_motion: Defined elbow excursion with shoulder position relatively fixed. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Triceps_Pushdown_-_Rope_Attachment.json |
| equipment | cable_station; rope_attachment | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Triceps_Pushdown_-_Rope_Attachment.json |
| movement_patterns | elbow_extension | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| body_regions | upper_body | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| force | push | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| joint_actions | elbow_extension | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| planes | sagittal | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| muscles | Triceps brachii (working_contributor) | biomechanical_interpretation | [anatomy-upper](#source-anatomy-upper) — fs-id2271811; fs-id2831016; fs-id2443705 |
| laterality | execution: bilateral; record_sides: combined | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Triceps_Pushdown_-_Rope_Attachment.json |
| support | Two feet; hands hold the rope; no torso support. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Triceps_Pushdown_-_Rope_Attachment.json |
| mechanics | single_joint | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| loading | resistance_type: external; load_convention: device_setting; load_unit: device_setting; primary_measure: repetitions | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Triceps_Pushdown_-_Rope_Attachment.json |
| coaching_cues | Record pulley and attachment.; Keep shoulder movement distinct from the intended elbow motion. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Triceps_Pushdown_-_Rope_Attachment.json |
| prerequisites | Establish the setup and chosen ROM before adding or changing resistance.; Confirm the intended execution with a coach if its definition is unfamiliar. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| numeric_joint_rom | **unknown** — No reviewed numerical joint-angle endpoints for this corpus variant; use the textual execution definition. | not_established | — |
| clinical_precautions | **unknown** — No exercise-specific clinical contraindication review completed. Unknown does not mean safe for every person. | not_established | — |
| difficulty | **unknown** — No validated universal beginner/intermediate/expert rating assigned. | not_established | — |

Catalogue context: `Triceps_Pushdown_-_Rope_Attachment`. Original unreviewed muscle labels: primary ['triceps']; secondary [].

Review notes: Confirm setup, qualitative ROM, inferred muscle roles, and loading convention during review.

<a id="rope-overhead-triceps-extension"></a>
## Rope overhead triceps extension

ID: `rope-overhead-triceps-extension`; revision 1; family `elbow_extension`; review **draft**.

Aliases: Low-pulley overhead rope extension.

| Characteristic | Draft value | Basis | References |
| --- | --- | --- | --- |
| execution | start: Stand facing away from a low pulley with the upper arms overhead and both hands holding the rope.; movement: Extend the elbows to move the hands upward, then lower the hands behind the head.; finish: Return to the same overhead-arm flexed-elbow start.; range_of_motion: Repeatable elbow travel with overhead upper-arm position; record cable line and stance. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Cable_Rope_Overhead_Triceps_Extension.json |
| equipment | cable_station; rope_attachment | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Cable_Rope_Overhead_Triceps_Extension.json |
| movement_patterns | elbow_extension | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| body_regions | upper_body | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| force | push | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| joint_actions | elbow_extension | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| planes | sagittal | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| muscles | Triceps brachii (working_contributor) | biomechanical_interpretation | [anatomy-upper](#source-anatomy-upper) — fs-id2271811; fs-id2831016; fs-id2443705 |
| laterality | execution: bilateral; record_sides: combined | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Cable_Rope_Overhead_Triceps_Extension.json |
| support | Two feet; upper arms not resting on a support. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Cable_Rope_Overhead_Triceps_Extension.json |
| mechanics | single_joint | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| loading | resistance_type: external; load_convention: device_setting; load_unit: device_setting; primary_measure: repetitions | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Cable_Rope_Overhead_Triceps_Extension.json |
| coaching_cues | Keep the overhead shoulder position explicit.; Record pulley height and distance from the station. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Cable_Rope_Overhead_Triceps_Extension.json |
| prerequisites | Establish the setup and chosen ROM before adding or changing resistance.; Confirm the intended execution with a coach if its definition is unfamiliar. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| numeric_joint_rom | **unknown** — No reviewed numerical joint-angle endpoints for this corpus variant; use the textual execution definition. | not_established | — |
| clinical_precautions | **unknown** — No exercise-specific clinical contraindication review completed. Unknown does not mean safe for every person. | not_established | — |
| difficulty | **unknown** — No validated universal beginner/intermediate/expert rating assigned. | not_established | — |

Catalogue context: `Cable_Rope_Overhead_Triceps_Extension`. Original unreviewed muscle labels: primary ['triceps']; secondary [].

Review notes: Not the exact unilateral setup studied in the triceps comparison; that study is not imported as an unconditional outcome property here.

<a id="lying-straight-bar-triceps-extension"></a>
## Lying straight-bar triceps extension

ID: `lying-straight-bar-triceps-extension`; revision 1; family `elbow_extension`; review **draft**.

Aliases: Flat-bench barbell skull crusher.

| Characteristic | Draft value | Basis | References |
| --- | --- | --- | --- |
| execution | start: Lie on a flat bench holding a straight bar above the torso with the upper arms directed upward.; movement: Bend the elbows to lower the bar toward a chosen forehead-adjacent endpoint, then extend.; finish: Return to the bar-above-torso position.; range_of_motion: Use a defined non-contact endpoint and relatively fixed upper-arm angle. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Lying_Triceps_Press.json |
| equipment | barbell; weight_plates; flat_bench | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Lying_Triceps_Press.json |
| movement_patterns | elbow_extension | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| body_regions | upper_body | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| force | push | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| joint_actions | elbow_extension | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| planes | sagittal | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| muscles | Triceps brachii (working_contributor) | biomechanical_interpretation | [anatomy-upper](#source-anatomy-upper) — fs-id2271811; fs-id2831016; fs-id2443705 |
| laterality | execution: bilateral; record_sides: combined | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Lying_Triceps_Press.json |
| support | Head, torso and pelvis on bench; feet on floor. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Lying_Triceps_Press.json |
| mechanics | single_joint | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| loading | resistance_type: external; load_convention: total_bar_plus_plates; load_unit: kg; primary_measure: repetitions | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Lying_Triceps_Press.json |
| coaching_cues | Choose and retain a clear lower-bar endpoint.; Distinguish elbow extension from a close-grip bench press. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Lying_Triceps_Press.json |
| prerequisites | Establish the setup and chosen ROM before adding or changing resistance.; Confirm the intended execution with a coach if its definition is unfamiliar. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| numeric_joint_rom | **unknown** — No reviewed numerical joint-angle endpoints for this corpus variant; use the textual execution definition. | not_established | — |
| clinical_precautions | **unknown** — No exercise-specific clinical contraindication review completed. Unknown does not mean safe for every person. | not_established | — |
| difficulty | **unknown** — No validated universal beginner/intermediate/expert rating assigned. | not_established | — |

Catalogue context: `Lying_Triceps_Press`. Original unreviewed muscle labels: primary ['triceps']; secondary [].

Review notes: This project variant selects a straight bar and non-contact endpoint; the upstream entry allows an EZ bar and describes forehead contact, which are not silently copied.

<a id="forearm-plank"></a>
## Forearm plank

ID: `forearm-plank`; revision 1; family `anti_extension`; review **draft**.

Aliases: Prone forearm plank.

| Characteristic | Draft value | Basis | References |
| --- | --- | --- | --- |
| execution | start: Support the body on both forearms and toes with the torso held between them.; movement: Maintain the selected trunk and pelvic position for the recorded duration.; finish: End the hold by returning to floor support.; range_of_motion: No intended trunk joint excursion during the hold; document the starting body alignment. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Plank.json |
| equipment | No external implement required | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Plank.json |
| movement_patterns | anti_extension | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| body_regions | trunk | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| force | static | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| joint_actions | resist_trunk_extension | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| planes | sagittal | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| muscles | Rectus abdominis (isometric_stabilizer); Internal and external obliques (isometric_stabilizer) | biomechanical_interpretation | [anatomy-trunk](#source-anatomy-trunk) — tbl-ch11_06 |
| laterality | execution: bilateral; record_sides: combined | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Plank.json |
| support | Both forearms and toes on floor; knees not used as support. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Plank.json |
| mechanics | isometric_hold | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| loading | resistance_type: bodyweight; load_convention: none; load_unit: None; primary_measure: seconds | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Plank.json |
| coaching_cues | Record hold duration separately from repetitions.; Use the same forearm and foot placement when comparing holds. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Plank.json |
| prerequisites | Establish the setup and chosen ROM before adding or changing resistance.; Confirm the intended execution with a coach if its definition is unfamiliar. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| numeric_joint_rom | **unknown** — No reviewed numerical joint-angle endpoints for this corpus variant; use the textual execution definition. | not_established | — |
| clinical_precautions | **unknown** — No exercise-specific clinical contraindication review completed. Unknown does not mean safe for every person. | not_established | — |
| difficulty | **unknown** — No validated universal beginner/intermediate/expert rating assigned. | not_established | — |

Catalogue context: `Plank`. Original unreviewed muscle labels: primary ['abdominals']; secondary [].

Review notes: Confirm setup, qualitative ROM, inferred muscle roles, and loading convention during review.

<a id="side-forearm-plank"></a>
## Side forearm plank

ID: `side-forearm-plank`; revision 1; family `lateral_trunk_hold`; review **draft**.

Aliases: Straight-leg side plank.

| Characteristic | Draft value | Basis | References |
| --- | --- | --- | --- |
| execution | start: Lie on one side and raise the trunk on the lower forearm and stacked feet, with knees extended.; movement: Maintain the side-support position without deliberately bending the trunk.; finish: Return to the floor to end the hold.; range_of_motion: No intended trunk excursion; keep the chosen straight-leg support configuration. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Side_Bridge.json |
| equipment | No external implement required | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Side_Bridge.json |
| movement_patterns | anti_lateral_flexion | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| body_regions | trunk | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| force | static | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| joint_actions | resist_trunk_lateral_flexion | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| planes | frontal | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| muscles | Internal and external obliques (isometric_stabilizer); Quadratus lumborum (isometric_stabilizer); Deltoid (isometric_stabilizer) | biomechanical_interpretation | [anatomy-trunk](#source-anatomy-trunk) — tbl-ch11_06; [anatomy-upper](#source-anatomy-upper) — fs-id2501482; fig-ch11_05_03 |
| laterality | execution: unilateral; record_sides: per_side | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Side_Bridge.json |
| support | One forearm and the sides of stacked feet on floor. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Side_Bridge.json |
| mechanics | isometric_hold | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| loading | resistance_type: bodyweight; load_convention: none; load_unit: None; primary_measure: seconds | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Side_Bridge.json |
| coaching_cues | Record the supporting side and hold duration.; Do not merge a bent-knee support version with this straight-leg version. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Side_Bridge.json |
| prerequisites | Establish the setup and chosen ROM before adding or changing resistance.; Confirm the intended execution with a coach if its definition is unfamiliar. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| numeric_joint_rom | **unknown** — No reviewed numerical joint-angle endpoints for this corpus variant; use the textual execution definition. | not_established | — |
| clinical_precautions | **unknown** — No exercise-specific clinical contraindication review completed. Unknown does not mean safe for every person. | not_established | — |
| difficulty | **unknown** — No validated universal beginner/intermediate/expert rating assigned. | not_established | — |

Catalogue context: `Side_Bridge`. Original unreviewed muscle labels: primary ['abdominals']; secondary ['shoulders'].

Review notes: The upstream Side Bridge has no instructions. This explicit forearm/stacked-foot definition is original and needs review; it is not attributed to an upstream protocol. The upstream catalogue entry has no execution instructions; the definition here is project-authored and needs particular review.

<a id="contralateral-dead-bug"></a>
## Contralateral dead bug

ID: `contralateral-dead-bug`; revision 1; family `trunk_control`; review **draft**.

Aliases: Alternating opposite-arm leg dead bug.

| Characteristic | Draft value | Basis | References |
| --- | --- | --- | --- |
| execution | start: Lie supine with arms reaching upward and hips and knees bent, keeping the feet off the floor.; movement: Reach one arm overhead while extending the opposite leg, return them, and alternate the pairing.; finish: Return to the same bent-leg, arms-up start between pairings.; range_of_motion: Reach only to the selected repeatable limb endpoints while retaining the chosen trunk/pelvis position. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Dead_Bug.json |
| equipment | No external implement required | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Dead_Bug.json |
| movement_patterns | anti_extension | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| body_regions | trunk | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| force | mixed | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| joint_actions | resist_trunk_extension; hip_extension; knee_extension; shoulder_flexion | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| planes | sagittal | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| muscles | Rectus abdominis (isometric_stabilizer); Internal and external obliques (isometric_stabilizer); Iliopsoas (working_contributor) | biomechanical_interpretation | [anatomy-trunk](#source-anatomy-trunk) — tbl-ch11_06; [anatomy-lower](#source-anatomy-lower) — fs-id2105968; fig-ch11_06_02 |
| laterality | execution: alternating_contralateral; record_sides: per_side | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Dead_Bug.json |
| support | Back on floor; moving arm and opposite leg unsupported. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Dead_Bug.json |
| mechanics | mixed | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| loading | resistance_type: bodyweight; load_convention: none; load_unit: None; primary_measure: repetitions | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Dead_Bug.json |
| coaching_cues | Define whether one paired reach or both sides counts as a repetition.; Keep the chosen trunk position and limb reach endpoints consistent. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Dead_Bug.json |
| prerequisites | Establish the setup and chosen ROM before adding or changing resistance.; Confirm the intended execution with a coach if its definition is unfamiliar. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| numeric_joint_rom | **unknown** — No reviewed numerical joint-angle endpoints for this corpus variant; use the textual execution definition. | not_established | — |
| clinical_precautions | **unknown** — No exercise-specific clinical contraindication review completed. Unknown does not mean safe for every person. | not_established | — |
| difficulty | **unknown** — No validated universal beginner/intermediate/expert rating assigned. | not_established | — |

Catalogue context: `Dead_Bug`. Original unreviewed muscle labels: primary ['abdominals']; secondary [].

Review notes: The catalogue describes alternating leg extension with arms up. This corpus explicitly adds contralateral arm movement; it is related context, not an exact match to those instructions.

<a id="supine-crunch"></a>
## Supine crunch

ID: `supine-crunch`; revision 1; family `trunk_flexion`; review **draft**.

Aliases: Floor abdominal crunch.

| Characteristic | Draft value | Basis | References |
| --- | --- | --- | --- |
| execution | start: Lie on the back with knees bent, feet on floor and hands lightly across the chest.; movement: Curl the upper trunk to lift the shoulder blades, then lower.; finish: Return the upper back to floor support.; range_of_motion: A short trunk curl rather than a full sit-up; use a repeatable shoulder-blade lift. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Crunches.json |
| equipment | No external implement required | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Crunches.json |
| movement_patterns | trunk_flexion | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| body_regions | trunk | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| force | mixed | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| joint_actions | trunk_flexion | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| planes | sagittal | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| muscles | Rectus abdominis (working_contributor); Internal and external obliques (working_contributor) | biomechanical_interpretation | [anatomy-trunk](#source-anatomy-trunk) — tbl-ch11_06 |
| laterality | execution: bilateral; record_sides: combined | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Crunches.json |
| support | Pelvis and feet on floor; upper-back contact changes during the curl. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Crunches.json |
| mechanics | mixed | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| loading | resistance_type: bodyweight; load_convention: none; load_unit: None; primary_measure: repetitions | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Crunches.json |
| coaching_cues | Keep hand position consistent and do not pull on the neck.; Distinguish the short curl from a hip-flexion-dominant sit-up. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Crunches.json |
| prerequisites | Establish the setup and chosen ROM before adding or changing resistance.; Confirm the intended execution with a coach if its definition is unfamiliar. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| numeric_joint_rom | **unknown** — No reviewed numerical joint-angle endpoints for this corpus variant; use the textual execution definition. | not_established | — |
| clinical_precautions | **unknown** — No exercise-specific clinical contraindication review completed. Unknown does not mean safe for every person. | not_established | — |
| difficulty | **unknown** — No validated universal beginner/intermediate/expert rating assigned. | not_established | — |

Catalogue context: `Crunches`. Original unreviewed muscle labels: primary ['abdominals']; secondary [].

Review notes: Oblique contribution is an anatomical interpretation, not an exercise-specific activation ranking.

<a id="kneeling-rope-cable-crunch"></a>
## Kneeling rope cable crunch

ID: `kneeling-rope-cable-crunch`; revision 1; family `trunk_flexion`; review **draft**.

Aliases: Kneeling cable trunk curl.

| Characteristic | Draft value | Basis | References |
| --- | --- | --- | --- |
| execution | start: Kneel facing a high pulley with a rope held near the sides of the head.; movement: Flex the trunk against cable resistance, then return without deliberately turning the movement into a hip hinge.; finish: Finish at the original kneeling torso position.; range_of_motion: Repeatable trunk-flexion range and cable line; hips remain relatively fixed. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Cable_Crunch.json |
| equipment | cable_station; rope_attachment | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Cable_Crunch.json |
| movement_patterns | trunk_flexion | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| body_regions | trunk | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| force | mixed | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| joint_actions | trunk_flexion | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| planes | sagittal | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| muscles | Rectus abdominis (working_contributor); Internal and external obliques (working_contributor) | biomechanical_interpretation | [anatomy-trunk](#source-anatomy-trunk) — tbl-ch11_06 |
| laterality | execution: bilateral; record_sides: combined | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Cable_Crunch.json |
| support | Both knees on floor; hands retain the rope. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Cable_Crunch.json |
| mechanics | mixed | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| loading | resistance_type: external; load_convention: device_setting; load_unit: device_setting; primary_measure: repetitions | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Cable_Crunch.json |
| coaching_cues | Record pulley height and kneeling distance.; Keep trunk motion distinct from pulling only with the arms. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Cable_Crunch.json |
| prerequisites | Establish the setup and chosen ROM before adding or changing resistance.; Confirm the intended execution with a coach if its definition is unfamiliar. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| numeric_joint_rom | **unknown** — No reviewed numerical joint-angle endpoints for this corpus variant; use the textual execution definition. | not_established | — |
| clinical_precautions | **unknown** — No exercise-specific clinical contraindication review completed. Unknown does not mean safe for every person. | not_established | — |
| difficulty | **unknown** — No validated universal beginner/intermediate/expert rating assigned. | not_established | — |

Catalogue context: `Cable_Crunch`. Original unreviewed muscle labels: primary ['abdominals']; secondary [].

Review notes: Confirm setup, qualitative ROM, inferred muscle roles, and loading convention during review.

<a id="standing-cable-pallof-press"></a>
## Standing cable Pallof press

ID: `standing-cable-pallof-press`; revision 1; family `anti_rotation`; review **draft**.

Aliases: Standing cable anti-rotation press.

| Characteristic | Draft value | Basis | References |
| --- | --- | --- | --- |
| execution | start: Stand side-on to a chest-height cable with the handle held at the chest in both hands.; movement: Press the hands forward while maintaining trunk orientation, then draw them back.; finish: Return the handle to the chest before the next press; repeat facing the other direction separately.; range_of_motion: Defined hand travel with no intended trunk rotation; record any hold duration. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Pallof_Press.json |
| equipment | cable_station; single_handle | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Pallof_Press.json |
| movement_patterns | anti_rotation | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| body_regions | trunk | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| force | mixed | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| joint_actions | resist_trunk_rotation; elbow_extension | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| planes | multi_planar | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| muscles | Internal and external obliques (isometric_stabilizer); Rectus abdominis (isometric_stabilizer); Triceps brachii (working_contributor) | biomechanical_interpretation | [anatomy-trunk](#source-anatomy-trunk) — tbl-ch11_06; [anatomy-upper](#source-anatomy-upper) — fs-id2271811; fs-id2831016; fs-id2443705 |
| laterality | execution: unilateral; record_sides: per_side | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Pallof_Press.json |
| support | Two-foot standing base; hands hold a lateral cable load. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Pallof_Press.json |
| mechanics | mixed | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| loading | resistance_type: external; load_convention: device_setting; load_unit: device_setting; primary_measure: repetitions | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Pallof_Press.json |
| coaching_cues | Record the side facing the pulley, stance and distance.; Log cable setting separately from any pause duration. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Pallof_Press.json |
| prerequisites | Establish the setup and chosen ROM before adding or changing resistance.; Confirm the intended execution with a coach if its definition is unfamiliar. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| numeric_joint_rom | **unknown** — No reviewed numerical joint-angle endpoints for this corpus variant; use the textual execution definition. | not_established | — |
| clinical_precautions | **unknown** — No exercise-specific clinical contraindication review completed. Unknown does not mean safe for every person. | not_established | — |
| difficulty | **unknown** — No validated universal beginner/intermediate/expert rating assigned. | not_established | — |

Catalogue context: `Pallof_Press`. Original unreviewed muscle labels: primary ['abdominals']; secondary ['chest', 'shoulders', 'triceps'].

Review notes: Laterality refers to cable side, not exclusive use of one limb; both hands press together.

<a id="bilateral-dumbbell-farmers-walk"></a>
## Bilateral dumbbell farmer carry

ID: `bilateral-dumbbell-farmers-walk`; revision 1; family `loaded_carry`; review **draft**.

Aliases: Two-dumbbell farmer walk.

| Characteristic | Draft value | Basis | References |
| --- | --- | --- | --- |
| execution | start: Stand holding one dumbbell at each side with the arms extended downward.; movement: Walk the recorded route while retaining the implements and the chosen upright posture.; finish: Finish the measured distance before setting the implements down.; range_of_motion: Walking gait with no intended repeated trunk bending; record turns and route. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Farmers_Walk.json |
| equipment | dumbbell | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Farmers_Walk.json |
| movement_patterns | loaded_carry | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| body_regions | upper_body; trunk; lower_body | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| force | mixed | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| joint_actions | gait_cycle; finger_flexion_hold; resist_trunk_flexion | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| planes | multi_planar | biomechanical_interpretation | [anatomy-movement](#source-anatomy-movement) — Flexion and Extension; Abduction and Adduction; Dorsiflexion and Plantar Flexion; Protraction and Retraction |
| muscles | Long finger flexors (grip_contributor); Trapezius (isometric_stabilizer); Erector spinae (isometric_stabilizer); Internal and external obliques (isometric_stabilizer) | biomechanical_interpretation | [anatomy-roles](#source-anatomy-roles) — tbl-ch11_01; [anatomy-upper](#source-anatomy-upper) — tbl-ch11_08; [anatomy-back](#source-anatomy-back) — fs-id2586421; [anatomy-trunk](#source-anatomy-trunk) — tbl-ch11_06 |
| laterality | execution: bilateral; record_sides: combined | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Farmers_Walk.json |
| support | Alternating foot contacts during walking; loads held by both hands. | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Farmers_Walk.json |
| mechanics | mixed | coaching_classification | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| loading | resistance_type: external; load_convention: per_dumbbell; load_unit: kg; primary_measure: metres | project_defined_variant | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Farmers_Walk.json |
| coaching_cues | Record load per hand and distance.; Keep turns and route comparable; unilateral suitcase carries are separate variants. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method; [free-exercise-db](#source-free-exercise-db) — exercises/Farmers_Walk.json |
| prerequisites | Establish the setup and chosen ROM before adding or changing resistance.; Confirm the intended execution with a coach if its definition is unfamiliar. | coaching_judgment | [project-conventions](#source-project-conventions) — Characteristics of each exercise; Scientific grounding and annotation method |
| numeric_joint_rom | **unknown** — No reviewed numerical joint-angle endpoints for this corpus variant; use the textual execution definition. | not_established | — |
| clinical_precautions | **unknown** — No exercise-specific clinical contraindication review completed. Unknown does not mean safe for every person. | not_established | — |
| difficulty | **unknown** — No validated universal beginner/intermediate/expert rating assigned. | not_established | — |

Catalogue context: `Farmers_Walk`. Original unreviewed muscle labels: primary ['forearms']; secondary ['abdominals', 'glutes', 'hamstrings', 'lower back', 'quadriceps', 'traps'].

Review notes: Selected annotations cover grip/postural demands and are not an exhaustive list of muscles used during walking.

## Sources

Only factual reference metadata is retained; no source images, textbook tables/prose, or catalogue instructions are redistributed.

<a id="source-project-conventions"></a>
### project-conventions

[Exercise Graph corpus definitions and coaching conventions](../.docs/requirements/00-exercise-graph.md)

Revision: `corpus-v0.1.0-draft`; accessed 2026-10-18. Licence: Project licence not selected

Original project definitions, descriptions, and qualitative coaching classifications; not empirical findings.

<a id="source-free-exercise-db"></a>
### free-exercise-db

[Free Exercise DB candidate catalog](https://github.com/yuhonas/free-exercise-db/blob/f00c92c7dcf1216a928a52c3706c7ce8e2f71ed5/dist/exercises.json)

Revision: `f00c92c7dcf1216a928a52c3706c7ce8e2f71ed5`; accessed 2026-10-18. Licence: Upstream README declares Unlicense/public domain; upstream rights chain not independently established.

Reference IDs, names and original factual muscle labels only. No instructions or media imported. Catalog labels are unreviewed.

<a id="source-anatomy-movement"></a>
### anatomy-movement

[OpenStax Anatomy and Physiology 2e: Types of Body Movements](https://github.com/openstax/osbooks-anatomy-physiology/blob/5ae32b3f4bc24ed003e91dc38bf47dba80751044/modules/m46398/index.cnxml)

Revision: `5ae32b3f4bc24ed003e91dc38bf47dba80751044`; accessed 2026-10-18. Licence: Repository LICENSE: CC BY-NC-SA 4.0

Reference for anatomical facts and terminology. No textbook prose, tables, or images redistributed; exercise interpretations and descriptions are project-authored drafts.

<a id="source-anatomy-roles"></a>
### anatomy-roles

[OpenStax Anatomy and Physiology 2e: Interactions of Skeletal Muscles, Their Fascicle Arrangement, and Their Lever Systems](https://github.com/openstax/osbooks-anatomy-physiology/blob/5ae32b3f4bc24ed003e91dc38bf47dba80751044/modules/m46487/index.cnxml)

Revision: `5ae32b3f4bc24ed003e91dc38bf47dba80751044`; accessed 2026-10-18. Licence: Repository LICENSE: CC BY-NC-SA 4.0

Reference for anatomical facts and terminology. No textbook prose, tables, or images redistributed; exercise interpretations and descriptions are project-authored drafts.

<a id="source-anatomy-upper"></a>
### anatomy-upper

[OpenStax Anatomy and Physiology 2e: Muscles of the Pectoral Girdle and Upper Limbs](https://github.com/openstax/osbooks-anatomy-physiology/blob/5ae32b3f4bc24ed003e91dc38bf47dba80751044/modules/m46495/index.cnxml)

Revision: `5ae32b3f4bc24ed003e91dc38bf47dba80751044`; accessed 2026-10-18. Licence: Repository LICENSE: CC BY-NC-SA 4.0

Reference for anatomical facts and terminology. No textbook prose, tables, or images redistributed; exercise interpretations and descriptions are project-authored drafts.

<a id="source-anatomy-lower"></a>
### anatomy-lower

[OpenStax Anatomy and Physiology 2e: Appendicular Muscles of the Pelvic Girdle and Lower Limbs](https://github.com/openstax/osbooks-anatomy-physiology/blob/5ae32b3f4bc24ed003e91dc38bf47dba80751044/modules/m46482/index.cnxml)

Revision: `5ae32b3f4bc24ed003e91dc38bf47dba80751044`; accessed 2026-10-18. Licence: Repository LICENSE: CC BY-NC-SA 4.0

Reference for anatomical facts and terminology. No textbook prose, tables, or images redistributed; exercise interpretations and descriptions are project-authored drafts.

<a id="source-anatomy-trunk"></a>
### anatomy-trunk

[OpenStax Anatomy and Physiology 2e: Axial Muscles of the Abdominal Wall, and Thorax](https://github.com/openstax/osbooks-anatomy-physiology/blob/5ae32b3f4bc24ed003e91dc38bf47dba80751044/modules/m46485/index.cnxml)

Revision: `5ae32b3f4bc24ed003e91dc38bf47dba80751044`; accessed 2026-10-18. Licence: Repository LICENSE: CC BY-NC-SA 4.0

Reference for anatomical facts and terminology. No textbook prose, tables, or images redistributed; exercise interpretations and descriptions are project-authored drafts.

<a id="source-anatomy-back"></a>
### anatomy-back

[OpenStax Anatomy and Physiology 2e: Axial Muscles of the Head, Neck, and Back](https://github.com/openstax/osbooks-anatomy-physiology/blob/5ae32b3f4bc24ed003e91dc38bf47dba80751044/modules/m46484/index.cnxml)

Revision: `5ae32b3f4bc24ed003e91dc38bf47dba80751044`; accessed 2026-10-18. Licence: Repository LICENSE: CC BY-NC-SA 4.0

Reference for anatomical facts and terminology. No textbook prose, tables, or images redistributed; exercise interpretations and descriptions are project-authored drafts.
