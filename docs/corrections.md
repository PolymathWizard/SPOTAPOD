# Correction Process

Public research produces disputes. That is expected, and a documented correction path is part of the evidence that a project is maintained responsibly.

## What can be reported

- Incorrect record content (text misattributed, counters wrong)
- Duplicate records beyond the documented recapture pattern
- Disputed inclusion (a person believes their account was wrongly captured by the collection process)
- Missing provenance or processing errors
- Changed source information (deleted posts, renamed accounts)
- Metadata errors (including the open 49K versus 213K count discrepancy and the HyperClapper versus Podawaa platform naming question)

## How to report

1. Open a GitHub issue in this repository using the Correction Request template, or
2. Use the contact function on the Harvard Dataverse record for private submissions.

Include the `linkedinPostId` where applicable, what is wrong, and any supporting evidence. Data-subject requests do not require the requester to prove a negative; the burden of supporting an inclusion sits with the evidence archive.

## How reports are handled

1. **Acknowledge**: the report receives an identifier and appears in the public correction log (personal details redacted on request).
2. **Check**: the disputed record is compared against the evidence archive entry and its recorded SHA256 hash.
3. **Resolve**: outcomes are one of CORRECTED (record fixed or removed in the next dataset version), UPHELD (archive evidence supports the record as published), or INCONCLUSIVE (evidence is insufficient either way; the record is annotated or removed depending on severity). No outcome is ever labeled CLEAN.
4. **Publish**: resolutions appear in the [CHANGELOG](https://github.com/PolymathWizard/SPOTAPOD/blob/main/CHANGELOG.md) and in the Dataverse version history.

## Open items

| ID | Item | Status | Settling criterion |
|---|---|---|---|
| C-001 | Dataverse description count (49K) versus file count (213,491) | Open | Depositor confirms which figure describes the published file |
| C-002 | Platform naming: HyperClapper (description) versus Podawaa (filename) | Open | Depositor documents the collection source or sources |
| C-003 | 3,364 records missing linkedinPostId | Open | Depositor confirms whether IDs are recoverable or the records should be marked untraceable |
