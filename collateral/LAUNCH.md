# SPOTAPOD Launch Collateral

## GitHub description variants (character-verified)

### Variant A (recommended): 340/350 chars

Companion research repo for the SPOTAPOD dataset (Harvard Dataverse, DOI 10.7910/DVN/WD9AUR): 213K LinkedIn post records tied to engagement-pod tooling. Method, data dictionary, limitations, ethics, corrections, and stdlib-only scripts that regenerate every headline figure. Evidence-tiered. Human-Directed. AI-Enabled. Commercially Tested.

### Variant B: 303/350 chars

Method and tooling for a 213K-record LinkedIn engagement-pod dataset on Harvard Dataverse. Reproducible baseline profile, anomaly and duplication analysis, drift-gated derived artifacts, documented limitations, and a public correction process. The data stays on Dataverse; the inspectability lives here.

### Variant C: 295/350 chars

How do you publish research data people can actually check? SPOTAPOD pairs a DOI-backed Dataverse dataset (213K pod-linked LinkedIn posts) with open methodology: data dictionary, evidence tiers, ethics statement, stdlib analysis scripts, checksums, and CI gates that catch hand-edited artifacts.

### Recommendation

Variant A. It leads with what the repo is, carries the DOI for citability, names the deliverables a researcher scans for, and closes with the tagline. Variant B is the strongest pure-method pitch when the tagline must be dropped for space. Variant C is the curiosity opener for a directory context.

## LinkedIn post variants

### Variant 1: technical authority

213,491 LinkedIn posts. 7,033 accounts. One STATED claim holding it all together.

The SPOTAPOD dataset (Harvard Dataverse, DOI 10.7910/DVN/WD9AUR) captures posts from accounts tied to engagement-pod tooling, the coordinated like-exchange platforms the FTC's 16 CFR Part 465 now treats as trading in fake influence.

The data is interesting. The methodology problem is more interesting.

The core claim (these accounts used pods) cannot be verified from the file itself. So the companion repo does what the data cannot: it separates observation from classification, tags every claim with an evidence tier (VERIFIED through INFERENCE), ships stdlib-only scripts that regenerate every headline number, and documents ten limitations before anyone gets to findings.

2,500 records show more likes than views. Easy headline: fraud. Honest reading: a capture artifact until proven otherwise. That distinction is the whole discipline.

Repo: github.com/PolymathWizard/SPOTAPOD

Human-Directed. AI-Enabled. Commercially Tested.

### Variant 2: inquiry-driving

Would your research survive a hostile reader?

I just published the companion repository for SPOTAPOD, a 213K-record dataset of LinkedIn posts linked to engagement pods (the pay-to-play like exchanges the FTC banned in 2024).

Before writing a single finding, the repo has to answer six questions:

Can you see what was measured?
Can you understand how?
Can you determine where the data came from?
Can you reproduce the analysis?
Can you challenge the classification?
Can you cite the exact file you examined?

Where the honest answer is "partially" (the pod-membership claim rests on the depositor's collection process), the repo says so, in writing, with an open correction ticket.

If your organization publishes data, which of the six would you fail today?

Human-Directed. AI-Enabled. Commercially Tested.

### Variant 3: peer and builder ship post

Shipped: the SPOTAPOD companion repo.

What it is: full research scaffolding around a 213K-record engagement-pod dataset on Harvard Dataverse. Method, data dictionary, ten documented limitations, ethics statement, correction process, and five stdlib-only Python scripts that rebuild every published figure from the raw file.

Build notes for the repo people:

The validator caught the validator again. The no-CLEAN-verdicts gate flagged its own docstring for explaining the rule it enforces. Fixed with a negation-context rule and a regression test that names the bug.

Every derived artifact is generated, hash-recorded, and drift-gated. Hand edit the baseline profile and CI fails.

The dataset never touches git. Data lives on Dataverse with a DOI; the repo holds the inspectability.

Repo: github.com/PolymathWizard/SPOTAPOD

Human-Directed. AI-Enabled. Commercially Tested.
