# Publication & Zenodo Deposit Guide

This guide details how to publicly release, archive, and cite this research paper via **Zenodo** (generating a persistent DOI), followed by target venue recommendations for formal peer-reviewed submission.

---

## 1. Readiness Assessment for Public Release

- **Manuscript Status:** Completed, submission-quality manuscript in PDF, DOCX, and Markdown formats.
- **Empirical Evidence:** Grounded in authentic static-analysis scans using the official GitHub CodeQL CLI (52 security rules) and the LLMSecEval dataset, verified against known-positive and known-negative controls.
- **Claims & Tone:** Claims are appropriately scoped (reports specific configuration resolution vs. taint-flow persistence; disclaims dynamic exploitability or broader generalization beyond tested tasks).
- **Public Artifacts:** Code repository is publicly available at [https://github.com/jackyhitter/AI_security_report](https://github.com/jackyhitter/AI_security_report).
- **Recommendation:** **Ready for preprint/research-output deposit on Zenodo**.

---

## 2. Zenodo Upload & Deposit Preparation

Zenodo (operated by CERN) provides immediate, citable, persistent Digital Object Identifiers (DOIs) indexed by OpenAIRE, Google Scholar, and academic repositories.

### 2.1 Deposit Metadata (Copy-Paste)

- **Upload Type:** `Publication` -> `Preprint` (or `Working Paper`)
- **Basic Information:**
  - **Title:** `The Whack-a-Mole Effect in AI Code Repair: Static-Analysis Findings and Code Complexity After Scanner-Guided Fixes`
  - **Creators:**
    - Family name: `Naman`
    - Given names: `Anunay`
    - Affiliation: `Punjab Engineering College (Deemed to be University), Chandigarh, India`
    - ORCID: *(Optional: add your ORCID if available)*
  - **Publication Date:** `2026-10-11` (or current submission date)
  - **License:** `Creative Commons Attribution 4.0 International (CC-BY-4.0)`
  - **Keywords / Subjects:** `AI Code Generation`, `Automated Program Repair`, `Static Analysis`, `CodeQL`, `Vulnerability Remediation`, `Software Security`, `Large Language Models`, `Whack-a-Mole Effect`

### 2.2 Description Text (Copy-Paste into Zenodo Description)
```markdown
This empirical research investigates the "Whack-a-Mole" effect in automated AI code repair: whether feeding static-analysis scanner findings back to a code-generation model eliminates security vulnerabilities, leaves them unresolved, introduces secondary findings, or increases structural code complexity.

Key Contributions:
1. Closed-Loop Evaluation Pipeline: Integrates the LLMSecEval benchmark, official GitHub CodeQL CLI (evaluating 52 security and taint-tracking rules), and Qwen2.5-Coder under three controlled conditions (Baseline, Security-Aware Prompting, and Scanner-Guided Repair).
2. Ground-Truth Control Validation: Verifies CodeQL detection and SARIF parsing against ground-truth positive (Flask untrusted redirect in debug mode) and negative controls.
3. Empirical Findings: Demonstrates that security-aware prompt prefixing is ineffective (100% vulnerability persistence); scanner-guided repair successfully resolves localized configuration flaws (Flask debug mode) but fails on dataflow taint vulnerabilities (URL redirection), resulting in a 75% alert persistence rate. Code complexity (Radon cyclomatic complexity) and LOC remained stable.

Includes full manuscript (PDF), experimental dataset tables, raw scanner findings, and replication instructions.
GitHub Repository: https://github.com/jackyhitter/AI_security_report
Author Portfolio: https://anunay-naman-portfolio.vercel.app/
```

### 2.3 Files to Upload on Zenodo
Drag and drop the following files into the Zenodo deposit file area:
1. `paper/research_paper.pdf` *(Primary publication file)*
2. `paper/task_level_results.csv` *(Empirical task audit dataset)*
3. `paper/results_tables.csv` *(Aggregated metrics table)*
4. `REPRODUCIBILITY.md` *(Replication protocol)*

---

## 3. Step-by-Step Zenodo Deposit Instructions

1. Open your browser and navigate to **[https://zenodo.org/](https://zenodo.org/)**.
2. **Sign in** (you can sign in directly using your GitHub account `jackyhitter` or ORCID).
3. Click the green **"New Upload"** button (top right).
4. Drag and drop the 4 files listed in Section 2.3 above.
5. Fill in the metadata using the exact text provided in Section 2.1 and 2.2.
6. Under **Related Identifiers**, add:
   - Identifier: `https://github.com/jackyhitter/AI_security_report`
   - Relation: `is supplemented by` / `is documented by`
7. Click **"Save"** to save your draft.
8. Click **"Publish"**. (Zenodo will prompt a confirmation dialog noting that DOIs cannot be deleted).
9. Once published, copy the generated **DOI** (e.g., `10.5281/zenodo.XXXXXXX`) and **DOI URL** (e.g., `https://doi.org/10.5281/zenodo.XXXXXXX`).
10. Update the README and OIST application text with the real public DOI.

---

## 4. Target Peer-Reviewed Venues (Workshops, Conferences & Journals)

When ready for peer-reviewed submission, target the following verified venues. All listed venues allow preprint posting on Zenodo/arXiv and charge **$0 submission fees** (standard academic venues):

| Venue | Focus & Scope | Typical Deadlines | Preprint Policy | Submission URL / Notes |
| :--- | :--- | :--- | :--- | :--- |
| **IEEE S&P Workshop on Deep Learning and Security (DLS)** | Co-located with IEEE S&P; focuses on AI for security and security of AI. | February / March annually | Full preprint allowed | Excellent fit for empirical studies on LLM security repair. |
| **USENIX Security Symposium** | Leading systems and software security conference. | Multiple cycles (Feb, June, Sept) | Full preprint allowed | Premier venue; demands expanded full-dataset evaluation. |
| **IEEE/ACM MSR (Mining Software Repositories)** | Original venue of LLMSecEval; highly receptive to empirical benchmarks and replication. | November / December annually | Full preprint allowed | Direct thematic continuation of Tony et al. (2023). |
| **ACM CCS Workshop on Artificial Intelligence and Security (AISEC)** | Co-located with ACM CCS; addresses adversarial and AI-assisted security. | July / August annually | Full preprint allowed | Ideal for automated vulnerability repair studies. |
| **Empirical Software Engineering (EMSE)** | Springer journal specializing in rigorous empirical SE studies. | Rolling submissions (no deadline) | Preprint allowed (CC-BY) | Journal option with no submission fees and deep empirical review. |

### Ethical and Submission Compliance Reminders
- **Dual Submission Policy:** Never submit the manuscript to more than one peer-reviewed conference or journal at the same time.
- **Predatory Journals Warning:** Never submit to unsolicited email journals, paid open-access journals claiming "instant 48-hour review", or unrecognized publishers. Authentic ACM, IEEE, and USENIX conferences charge $0 for submission and conduct rigorous double-blind peer review.
