# Reproducibility Guide

**Study Title:** The Whack-a-Mole Effect in AI Code Repair: Static-Analysis Findings and Code Complexity After Scanner-Guided Fixes  
**Author:** Anunay Naman (Punjab Engineering College, Chandigarh)  
**Code Repository:** [https://github.com/jackyhitter/AI_security_report](https://github.com/jackyhitter/AI_security_report)  
**Dataset:** LLMSecEval (Tony et al., 2023)  

---

## 1. System Requirements & Software Dependencies

### 1.1 Operating Systems & Hardware
- **Operating System:** Tested on Windows 11 (x64) and Linux (Ubuntu 22.04 LTS / Kaggle Linux Environment).
- **GPU (Recommended for Full Scaling):** NVIDIA RTX 3050 (6GB VRAM) or cloud GPU (Kaggle T4 / P100 with 16GB VRAM).
- **CPU (Feasibility / Pilot Run):** 4+ cores, 16GB+ RAM. In CPU mode, the runner automatically deploys `Qwen2.5-Coder-1.5B-Instruct` as documented in the protocol to avoid host RAM allocation limits.

### 1.2 Python Environment Setup
Always execute inside an isolated virtual environment (`venv`):
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

pip install -r requirements.txt
```

### 1.3 Key Packages & Pinned Versions
- `torch` >= 2.2.0
- `transformers` >= 4.40.0 (v5.x supported with `BitsAndBytesConfig`)
- `accelerate` >= 0.29.0
- `bitsandbytes` >= 0.43.0
- `radon` >= 6.0.1
- `pandas` >= 2.0.0
- `reportlab` >= 4.0.0 (for PDF compilation)
- `python-docx` >= 1.1.0
- `matplotlib` >= 3.8.0

---

## 2. Automated Static Analysis Setup (CodeQL)

### 2.1 CodeQL CLI Installation
The runner automates CodeQL retrieval if absent:
- **Windows:** Downloads `codeql-bundle-win64.tar.gz` from GitHub Actions Releases.
- **Linux:** Downloads `codeql-bundle-linux64.tar.gz`.
Extracted to `scratch/codeql_env/codeql/codeql.exe`.

Verify CodeQL language extractors:
```bash
scratch/codeql_env/codeql/codeql resolve languages
```
Expected output includes: `python`, `cpp`, `java`, `javascript`, `csharp`, `go`, `ruby`, `rust`, etc.

### 2.2 Security Query Suite
We deploy the official GitHub CodeQL extended security suite:
`codeql/python-queries:codeql-suites/python-security-extended.qls`
Encompassing 52 rules covering CWE-089 (SQL Injection), CWE-078 (Command Injection), CWE-601 (URL Redirection), CWE-215 (Flask Debug), CWE-312 (Cleartext Logging), and related vulnerabilities.

---

## 3. Step-by-Step Replication Protocol

### Step 1: Run Ground-Truth Control Validation
Before executing experimental tasks, verify that CodeQL detects known vulnerabilities and suppresses safe controls:
```bash
python tests/test_codeql_controls.py
```
- **Known-Positive Control:** Flask untrusted redirect + debug mode. Expected: **2 alerts** (`py/flask-debug`, `py/url-redirection`).
- **Known-Negative Control:** Static internal route + debug disabled. Expected: **0 alerts**.
- **SARIF Verification:** Confirms both CSV and SARIF outputs agree.

### Step 2: Run the Experimental Pipeline
Execute the 3 experimental conditions (Baseline, Security-Aware, Scanner-Guided Repair):
```bash
python src/pilot.py
```
The script:
1. Dynamically calculates ETAs and step durations.
2. Generates completions using deterministic parameters:
   - Temperature: $T = 0.2$
   - Seed: 42
   - Max New Tokens: 512
3. Builds transient CodeQL databases, evaluates the 52 security rules, and parses findings.
4. Computes Cyclomatic Complexity (Radon) and Lines of Code (LOC).
5. Writes per-task audit logs to `results/<task_id>_summary.json` and raw scanner alerts to `results/codeql_<task>_<condition>.csv`.

### Step 3: Scaled Full-Dataset Execution (Kaggle)
To run the full 83-task benchmark on a cloud GPU:
1. Open [`notebooks/experiment.ipynb`](notebooks/experiment.ipynb) in Kaggle Notebooks.
2. Enable GPU accelerator (T4 x2 or P100).
3. Run all cells. All outputs will be collected in `/kaggle/working/results/`.

### Step 4: Generate Manuscript Tables & Figures
Aggregate task summaries into paper tables and render publication charts:
```bash
python scratch/build_paper_assets.py
```
Outputs:
- `paper/task_level_results.csv`
- `paper/results_tables.csv`
- `paper/figures/condition_alert_comparison.png`
- `paper/figures/repair_alert_breakdown.png`
- `paper/figures/complexity_loc_comparison.png`

### Step 5: Compile Final Paper Formats
- **DOCX:**
  ```bash
  cd paper
  pandoc research_paper.md -o research_paper.docx --resource-path="."
  ```
- **PDF:**
  ```bash
  python scratch/generate_pdf.py
  ```
