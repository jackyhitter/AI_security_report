# OIST Research Internship Application — Copy-Paste Text

**Program:** OIST Research Internship (Spring 2027 Term)  
**Application Deadline:** October 15, 2026 at 23:59 JST  
**Applicant:** Anunay Naman  
**Institution:** Punjab Engineering College (Deemed to be University), Chandigarh, India  
**Degree & Specialization:** B.Tech in Computer Science & Engineering, Minor in Data Science  
**Portfolio:** [https://anunay-naman-portfolio.vercel.app/](https://anunay-naman-portfolio.vercel.app/)  
**Research Repository:** [https://github.com/jackyhitter/AI_security_report](https://github.com/jackyhitter/AI_security_report)  

---

## Field 1: Research Experience / Independent Research Project

### Field Title: Research Project Title / Topic
```text
The Whack-a-Mole Effect in AI Code Repair: Static-Analysis Findings and Code Complexity After Scanner-Guided Fixes
```

### Field Title: Project Description / Summary (Approx. 250 – 350 words)
```text
As an independent undergraduate researcher at Punjab Engineering College, I investigated automated vulnerability remediation in AI-generated code. Large language models (LLMs) frequently generate insecure software, and a common mitigation strategy is "scanner-guided repair," wherein static analysis alerts are fed back to the model for iterative fixing. My project evaluated the "Whack-a-Mole" hypothesis: whether scanner-guided fixes successfully eliminate original findings, leave vulnerabilities unresolved, introduce secondary findings, or inflate code complexity.

To test this systematically, I engineered an empirical pipeline integrating the LLMSecEval benchmark, open-weight models (Qwen2.5-Coder series), and the official GitHub CodeQL CLI (evaluating 52 security and taint-tracking rules). I formulated three controlled experimental conditions: (A) Baseline prompt generation, (B) Security-aware prompt prefixing, and (C) Scanner-guided repair incorporating authentic CodeQL diagnostics (rule IDs, error descriptions, and line locations). To guarantee scanner reliability, I implemented ground-truth positive (Flask untrusted redirect in debug mode) and negative controls, confirming identical detection across CSV and SARIF parsers.

Empirical evaluation revealed a critical asymmetry: while security-aware prompting was completely ineffective (100% vulnerability persistence), scanner-guided repair successfully resolved localized configuration vulnerabilities (e.g., eliminating Flask debug mode), but failed on dataflow taint-tracking vulnerabilities (e.g., remote URL redirection, CWE-601), resulting in a 75% alert persistence rate. Furthermore, cyclomatic complexity (Radon) and lines of code remained stable, demonstrating that the model exhibited vulnerability inertia rather than code inflation or secondary bug introduction. 

I authored the complete scholarly manuscript, open-sourced the replication artifacts, and created a Kaggle cloud-scaling notebook for full-benchmark reproduction.

Repository: https://github.com/jackyhitter/AI_security_report
Paper Manuscript: https://github.com/jackyhitter/AI_security_report/blob/main/paper/research_paper.pdf
```

---

## Field 2: Publications / Preprints

> **Note on Application Form Selection:**
> If you have completed the Zenodo deposit (as outlined in `PUBLICATION_AND_UPLOAD_GUIDE.md`), paste **Option A** with your live DOI. If you are submitting your OIST application prior to the public Zenodo deposit, paste **Option B** to ensure strict academic integrity.

### Option A: If Zenodo Preprint is Public
```text
Naman, A. (2026). "The Whack-a-Mole Effect in AI Code Repair: Static-Analysis Findings and Code Complexity After Scanner-Guided Fixes." Independent Research Preprint. DOI: [Insert Zenodo DOI, e.g., 10.5281/zenodo.XXXXXXX]. Available at: https://github.com/jackyhitter/AI_security_report
```

### Option B: If Preprint is Pending / Independent Working Paper
```text
Naman, A. (2026). "The Whack-a-Mole Effect in AI Code Repair: Static-Analysis Findings and Code Complexity After Scanner-Guided Fixes." Independent Research Working Paper and Artifact Suite. Full manuscript and reproducible pipeline available at: https://github.com/jackyhitter/AI_security_report
```

---

## Field 3: Other Evidence of Ability / Academic Honors

```text
1. Academic Standing & Specialization: Undergraduate student in Computer Science & Engineering at Punjab Engineering College (PEC), Chandigarh, pursuing a formal Minor in Data Science. Strong academic grounding in Data Structures, Algorithms, Software Engineering, and Probability & Statistics.
2. National Competitive Recognition: Achieved Top 2% nationally in the NPTEL "Introduction to Machine Learning" certification, demonstrating rigorous mathematical and conceptual foundations in supervised learning, optimization, and evaluation metrics.
3. End-to-End Systems Engineering: Designed and implemented an automated static analysis evaluation harness pairing LLM inference pipelines with GitHub CodeQL CLI, SARIF parsing, and AST complexity metrics (Radon).
4. Open Science & Reproducibility: Fully committed to open science. Complete code, raw scanner CSV datasets, and replication guides are published openly on GitHub: https://github.com/jackyhitter/AI_security_report.
5. Technical Portfolio: Comprehensive portfolio of data science, systems, and machine learning projects available at: https://anunay-naman-portfolio.vercel.app/.
```

---

## Field 4: Statement of Purpose (SOP) / Statement of Research Interest

*(Character Count: ~2,950 characters with spaces | Word Count: ~440 words — fits standard OIST portal limits)*

```text
I am writing to express my strong interest in the OIST Research Internship Program for Spring 2027. As a Computer Science and Engineering undergraduate with a Minor in Data Science at Punjab Engineering College (PEC), Chandigarh, my primary research aspiration is to develop robust, trustworthy, and verifiable AI systems for software engineering and critical computing infrastructure. OIST's interdisciplinary, world-class research environment offers the ideal ecosystem for me to expand my foundational work into scalable, theoretically grounded methodologies.

My dedication to research is demonstrated by my recent independent empirical investigation into AI-assisted software security, titled "The Whack-a-Mole Effect in AI Code Repair." Motivated by the observation that large language models frequently generate insecure code, I designed an automated experimental pipeline pairing the Qwen2.5-Coder model family with the industrial-grade GitHub CodeQL static-analysis engine across three controlled prompt conditions (Baseline, Security-Aware Prompting, and Closed-Loop Scanner-Guided Repair). By executing ground-truth controls and analyzing 52 static analysis rules alongside Cyclomatic Complexity metrics, I empirically showed that while naive scanner feedback resolves simple configuration errors (such as debug flags), it consistently fails on architectural dataflow taint vulnerabilities (such as URL redirection, CWE-601), yielding a 75% vulnerability persistence rate. This work underscored for me the necessity of moving beyond surface-level prompt engineering toward neuro-symbolic techniques, abstract interpretation, and formal verification in AI code generation.

My academic trajectory has consistently combined rigorous theoretical study with empirical validation. I secured a Top 2% national ranking in the NPTEL Introduction to Machine Learning examination and have actively applied advanced statistical learning concepts within my Data Science minor coursework. Through independent research, I have cultivated the resilience, experimental discipline, and self-direction necessary to design benchmark pipelines from scratch, diagnose low-level memory and runtime bottlenecks, and communicate findings through publication-quality manuscripts.

At OIST, I am eager to collaborate with faculty and researchers working at the intersection of machine learning, software systems, and reliable computing. An internship at OIST would allow me to contribute directly to ongoing laboratory projects while learning how to scale my investigations toward larger benchmark distributions and formal verification frameworks. Furthermore, conducting research in OIST’s vibrant international community would provide invaluable preparation for my planned transition into graduate studies. I am eager to bring my technical skills, empirical rigor, and deep curiosity to the OIST research community.
```
