# FAQ

**Where is the actual data?**
On Harvard Dataverse in the SPOTAPOD collection, DOI `doi:10.7910/DVN/WD9AUR`. This repository deliberately contains method, documentation, and code only. Verify your download against [checksums/CHECKSUMS.txt](https://github.com/PolymathWizard/SPOTAPOD/blob/main/checksums/CHECKSUMS.txt) before analysis.

**What is an engagement pod?**
A group whose members agree to like, comment on, and share each other's posts so platform algorithms treat the content as organically popular. Commercial platforms automate the exchange. The FTC's 16 CFR Part 465 treats the sale or purchase of such fake engagement indicators as a deceptive practice.

**The Dataverse page says 49K posts but the file has 213K records. Which is right?**
The file. 213,491 records is VERIFIED by counting; the 49K figure most plausibly describes an earlier or different cut and is logged for depositor clarification. See [Limitations](limitations.md), item 2.

**Is everyone in this dataset guilty of something?**
No, and this project never says so. Inclusion rests on a STATED collection criterion that cannot be verified from the file, the collection process has unknown error rates, and legality is a question for regulators, not JSON. See [Ethics](ethics.md).

**Can I find out whether a specific person used a pod?**
Not from this dataset, and this project will not make that determination. Presence in the file is one weak signal with unknown error rates. Absence proves nothing at all.

**Why do some posts have more likes than views?**
2,500 records do. The fact is VERIFIED; the explanation is INFERENCE, and the most plausible one is a Views capture artifact rather than per-record fraud. Treat zero and inconsistent Views as missing data. See the [data dictionary](data-dictionary.md).

**Why does "Agree?" appear 3,918 times?**
Short prompt posts of exactly this kind are a known engagement-bait pattern, and heavy exact repetition across the corpus is one of the dataset's most interesting VERIFIED features. Whether any given instance came from a template, a pod habit, or coincidence is interpretation.

**What language is the data in?**
Many. Roughly 74 percent of a 50,000-record sample contains non-ASCII characters, with substantial French and Spanish content. English-only analyses cover a biased slice.

**How do I cite this?**
Cite the dataset by its Dataverse DOI and the companion repository via [CITATION.cff](https://github.com/PolymathWizard/SPOTAPOD/blob/main/CITATION.cff). Include the dataset version number and the file checksum you analyzed.

**I'm in this dataset and something is wrong. What do I do?**
Use the [correction process](corrections.md). Disputes are logged, reviewed against the evidence archive, and resolved in public version history.

**Can I get the original evidence behind a record?**
The evidence archive is controlled access. For a disputed finding, the archived record is compared against its recorded SHA256 hash and the outcome is published; the raw source material is released only when review determines it can be shared responsibly.
