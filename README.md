# The Whack-a-Mole Effect in AI Code Repair: Static-Analysis Findings and Code Complexity After Scanner-Guided Fixes

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![CodeQL: 52 Rules](https://img.shields.io/badge/CodeQL-Python--Security--Extended-brightgreen.svg)](https://codeql.github.com/)
[![Model: Qwen2.5-Coder-1.5B-Instruct](https://img.shields.io/badge/Model-Qwen2.5--Coder--1.5B--Instruct-orange.svg)](https://huggingface.co/Qwen/Qwen2.5-Coder-1.5B-Instruct)
[![Pilot Sample: N=3 Tasks](https://img.shields.io/badge/Pilot%20Sample-N%3D3%20Tasks%20(LLMSecEval)-informational.svg)](paper/task_level_results.csv)
[![Paper: PDF & DOCX](https://img.shields.io/badge/Paper-PDF%20%7C%20DOCX-purple.svg)](paper/)

An empirical software security investigation evaluating whether scanner-guided fixes for AI-generated Python code eliminate static analysis alerts, leave vulnerabilities unresolved, trigger secondary vulnerabilities ("Whack-a-Mole"), or increase structural code complexity.

**Author:** [Anunay Naman](https://anunay-naman-portfolio.vercel.app/)  
**Affiliation:** Department of Computer Science & Engineering, Punjab Engineering College (Deemed to be University), Chandigarh, India  
**GitHub Repository:** [https://github.com/jackyhitter/AI_security_report](https://github.com/jackyhitter/AI_security_report)  

---

## 📌 Research Overview

While Large Language Models (LLMs) accelerate code generation, studies indicate that ~40% of generated snippets contain security weaknesses. A common remediation strategy is **scanner-guided repair**, wherein Static Application Security Testing (SAST) tools feed alert diagnostics back to the model for iterative fixing.

This preliminary working paper evaluates a feasibility pilot ($N=3$ Python tasks from LLMSecEval) using `Qwen/Qwen2.5-Coder-1.5B-Instruct`:
> **When an AI model repairs generated Python code using actual static-analysis findings, does the repair remove existing alerts while leaving some unresolved, introduce new alert instances, or increase code complexity?**

*(Note: While the full benchmark spans 83 tasks, this working paper reports audited results from the completed 3-task pilot. Full-dataset scaling is supported via the cloud GPU notebook in `notebooks/experiment.ipynb`.)*

### Key Findings
1. **Security-Aware Prompting Fails (100% Persistence):** Prepending explicit security constraints to the prompt had zero impact on reducing baseline vulnerabilities across all 4 baseline alert instances.
2. **Asymmetric Scanner-Guided Repair (25% Resolved, 75% Persisted):**
   - **Configuration-Level Flaws** (e.g., `py/flask-debug`) were successfully resolved upon receiving diagnostic feedback (1/4 alerts resolved, 25.0%).
   - **Taint-Flow Flaws** (e.g., `py/url-redirection` under CWE-601) persisted across all repair attempts (3/4 alerts persisted, 75.0%).
3. **Vulnerability Inertia, Not Secondary Flaws:** In our evaluated pilot sample, the model did not introduce new distinct rules ($\text{New} = 0$), but rather exhibited *vulnerability inertia* by reproducing the vulnerable taint flow.
4. **Complexity Invariance:** Radon Cyclomatic Complexity ($\text{CC} = 0, 2, 2$; Mean 1.33) and Lines of Code ($\text{LOC} = 10, 11, 12$; Mean 11.0) remained constant before and after repair.

---

## 📊 Summary Results Table

| Experimental Condition | Total Tasks | Tasks w/ Alerts | Total Alerts | Mean / Task | Resolution Rate | Persistence Rate | Mean CC | Mean LOC |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Condition A: Baseline** | 3 | 2 | 4 | 1.33 | — | — | 1.33 | 11.0 |
| **Condition B: Security-Aware** | 3 | 2 | 4 | 1.33 | 0.0% (0/4) | 100.0% (4/4) | 1.33 | 11.0 |
| **Condition C: Scanner-Guided Repair** | 3 | 2 | 3 | 1.00 | **25.0% (1/4)** | **75.0% (3/4)** | 1.33 | 11.0 |

*Detailed task audit logs: [`paper/task_level_results.csv`](paper/task_level_results.csv).*

---

## 📁 Repository Structure

```text
├── README.md                      # Project overview and empirical summary
├── REPRODUCIBILITY.md             # End-to-end replication instructions
├── OIST_APPLICATION_TEXT.md       # Exact field-by-field text for OIST application
├── PUBLICATION_AND_UPLOAD_GUIDE.md# Zenodo deposit & target venue submission guide
├── requirements.txt               # Pinned Python dependencies
├── configs/
│   └── experiment.yaml            # Hyperparameters and decoding settings
├── docs/
│   ├── literature_review.md       # Scholarly grounding and verified citations
│   ├── protocol.md                # Locked experimental conditions (A, B, C)
│   └── feasibility_report.md      # Platform feasibility and environment checks
├── notebooks/
│   └── experiment.ipynb           # Cloud/Kaggle-ready full dataset scaling notebook
├── src/
│   ├── pilot.py                   # Automated experiment runner with ETA timers
│   ├── build_paper_assets.py      # Generates CSV tables and publication charts
│   └── generate_pdf.py            # Formats and renders research_paper.pdf
├── tests/
│   └── test_codeql_controls.py    # Known-positive and known-negative ground truth test
├── results/
│   ├── quality_control.md         # Validated task metrics and benchmark timings
│   ├── codeql_*_baseline.csv      # Raw SAST outputs per condition
│   └── *_summary.json             # Task-level audit comparisons
└── paper/
    ├── research_paper.md          # Full scholarly manuscript (Markdown)
    ├── research_paper.pdf         # Formatted publication-ready manuscript (PDF)
    ├── research_paper.docx        # Submission-ready manuscript (Word DOCX)
    ├── results_tables.csv         # Aggregated empirical tables
    ├── task_level_results.csv     # Granular task-by-task results
    └── figures/                   # Generated charts (Condition comparison, breakdown, CC)
```

---

## 🚀 Quickstart & Reproduction

### 1. Setup Environment
```bash
python -m venv venv
venv\Scripts\activate   # On Windows
# source venv/bin/activate  # On Linux/macOS
pip install -r requirements.txt
```

### 2. Validate Ground-Truth Controls
Verify the CodeQL pipeline and SARIF parser against known-positive and known-negative controls:
```bash
python tests/test_codeql_controls.py
```

### 3. Run the Experiment
Execute the full 3-condition pipeline locally:
```bash
python src/pilot.py
```
*(Displays dynamic ETA, step-by-step elapsed duration, and writes audit logs to `results/`.)*

### 4. Build Paper Tables & Figures
```bash
python src/build_paper_assets.py
python src/generate_pdf.py
```

---

## 📄 Manuscript & Deliverables

- **Full Paper (Markdown):** [`paper/research_paper.md`](paper/research_paper.md)
- **Formatted PDF:** [`paper/research_paper.pdf`](paper/research_paper.pdf)
- **Word Document:** [`paper/research_paper.docx`](paper/research_paper.docx)
- **Reproducibility Guide:** [`REPRODUCIBILITY.md`](REPRODUCIBILITY.md)
- **OIST Application Copy-Paste:** [`OIST_APPLICATION_TEXT.md`](OIST_APPLICATION_TEXT.md)

---

## 📜 Citation & Preprint

```bibtex
@article{naman2026whackamole,
  title={The Whack-a-Mole Effect in AI Code Repair: Static-Analysis Findings and Code Complexity After Scanner-Guided Fixes},
  author={Naman, Anunay},
  journal={Independent Research Preprint},
  year={2026},
  url={https://github.com/jackyhitter/AI_security_report}
}
```
