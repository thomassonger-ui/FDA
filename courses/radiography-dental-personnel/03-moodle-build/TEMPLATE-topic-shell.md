# TEMPLATE — Topic Shell (Moodle Section)

Copy this checklist when spinning up a new Topic section in Moodle.

---

## Section settings

- [ ] Section name: `Topic {{N}}: {{Title}}`
- [ ] Section description: 2–3 sentences, second-person voice, states what student will accomplish
- [ ] Section image (optional — on-brand, alt text set)

## Activities (in order)

- [ ] Label — Learning Objectives (from module spec)
- [ ] Book — Required Reading (or Page if short)
- [ ] Resource — Video (external or uploaded; captions + transcript required)
- [ ] H5P — Interactive practice
- [ ] Forum — Optional discussion (not required for completion)
- [ ] Quiz — Module quiz (configured per `/02-assessments/`)
- [ ] Folder — Resource Library (supplemental readings, links)

## Restrict Access rule

- [ ] Entire section restricted by: `Activity completion of {{prior_topic_quiz}}`

## Completion tracking

- [ ] Section marked "Show activity completion"
- [ ] Each activity has explicit completion rule (view / score / submit)

## Accessibility

- [ ] All images have alt text
- [ ] All videos have captions
- [ ] All PDFs are tagged / screen-reader friendly
- [ ] Color contrast checks pass (WCAG 2.1 AA)

## QA before publish

- [ ] Preview as student — entire section completes successfully
- [ ] Quiz randomizes correctly (take it 3 times, confirm different draws)
- [ ] Completion checkmark appears after quiz ≥ 80%
- [ ] Next topic unlocks as expected
