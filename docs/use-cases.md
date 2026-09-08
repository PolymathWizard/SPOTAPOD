# Use Cases

Who this dataset is for, what each audience can build with it, and where each use hits the evidence ceiling.

## Trust and safety researchers

**The core audience.** SPOTAPOD offers a labeled-population corpus for studying manufactured engagement at scale: 213,491 records, multilingual, spanning roughly four years of decoded post dates. Uses include feature discovery for inauthentic-behavior detection (engagement ratio distributions, cross-account text reuse, volume concentration), and benchmark construction for coordination-detection methods. Ceiling: the population label is STATED, so detector training should treat the label as weak supervision, not ground truth.

## Platform integrity and social media analytics teams

Baseline signatures of pod-associated content: what the like distributions, posting cadences, and content templates of a pod-linked population actually look like in the wild. Useful for calibrating internal anomaly thresholds against an external reference. Ceiling: LinkedIn-specific capture quirks (the Views gap especially) limit direct transfer to other platforms.

## Regulators, policy analysts, and legal scholars

The FTC's 16 CFR Part 465 prohibits trading in fake indicators of social media influence, and enforcement needs empirical grounding: how large is the phenomenon, what does it look like, is it concentrated or diffuse? SPOTAPOD provides scale and shape evidence at the population level. Ceiling: nothing in the file supports per-account legal conclusions, and this project publishes none.

## Marketing and communications leaders

Due-diligence context for anyone buying influence: what manufactured engagement looks like, how modest most of it performs (median 57 likes), and why vanity metrics are unreliable purchase signals. Useful for building internal creator-vetting standards. Ceiling: the dataset cannot vet any specific creator, and using it that way would exceed the evidence.

## B2B sales and marketing intelligence practitioners

Engagement quality assessment methodology: the ratio analysis and duplication clustering here transfer to any "is this audience real?" question. The scripts are deliberately generic. Ceiling: methods transfer; per-record conclusions do not.

## Data journalists

A citable, DOI-backed dataset on a newsworthy phenomenon with reproducible headline numbers and a documented limitations page. The story is the pattern, not any person. Ceiling: naming individuals from this file alone would outrun the evidence; the [ethics statement](ethics.md) explains why, and the [correction process](corrections.md) is the safety valve journalism should mention.

## Methodologists and teaching

A genuinely instructive messy dataset: missing keys, recapture duplicates, placeholder strings, a partially populated counter, a STATED population label, and metadata that disagrees with the file (49K described, 213K delivered). Every classic data-quality lesson is present in one 221 MB file. The [research questions](research-questions.md) page doubles as a course assignment list, and the [six-question test](index.md#the-six-question-test) doubles as a rubric.

## NLP and multilingual content researchers

A multilingual corpus of professional-network promotional prose, with roughly three quarters of sampled records containing non-ASCII text. Uses include template detection, cross-lingual near-duplicate methods, and studies of promotional register. Ceiling: copyright restraint applies; analyze patterns, do not republish the corpus.

## What this dataset should not be used for

- Building public lists of named individuals labeled as violators or fraudsters
- Certifying any account as authentic (no CLEAN verdicts, ever; absence of anomaly is INCONCLUSIVE)
- Per-account legal claims under 16 CFR Part 465 or any other rule
- Employment, credit, insurance, or other consequential decisions about individuals
- Training systems whose output is a per-person accusation without independent evidence
