# Literature Review

## 1. Benchmarking Prompt Engineering Techniques for Secure Code Generation with GPT Models
**Authors:** Marc Bruni, Fabio Gabrielli, Mohammad Ghafari, Martin Kropp
**Year:** 2025
**Publication Status:** Published (Proceedings of FORGE 2025) / arXiv Preprint
**URL:** [https://arxiv.org/abs/2502.06039](https://arxiv.org/abs/2502.06039)
**Dataset & Sample Size:** LLMSecEval and SecurityEval (202 high-risk coding prompts in Python)
**Models & Prompt Conditions:** GPT-3.5-turbo, GPT-4o, GPT-4o-mini. Tested security-focused prefixes/suffixes, Recursive Criticism and Improvement (RCI), and Chain of Thought (CoT).
**Security Analyzers & Functional Tests:** Static scanners (not specified in abstract, but automated).
**Main Findings:** A security-focused prompt prefix reduces vulnerabilities by up to 56% for GPT-4o models. Iterative prompting techniques successfully repaired between 41.9% and 68.7% of vulnerabilities in previously generated code.
**Limitations Acknowledged:** Real-world workflows require prompt agents.
**Overlap with Proposed Study:** This study directly examines iterative repair (which overlaps with Condition C) and security-focused prompting (Condition B) using LLMSecEval.

## 2. Prompting Techniques for Secure Code Generation: A Systematic Investigation
**Authors:** Catherine Tony, Nicolás E. Díaz Ferreyra, Markus Mutas, Salem Dhiff, Riccardo Scandariato
**Year:** 2024
**Publication Status:** Published (ACM Transactions on Software Engineering and Methodology - TOSEM)
**DOI:** [10.1145/3722108](https://doi.org/10.1145/3722108)
**Dataset & Sample Size:** Systematic empirical framework evaluating multiple tasks.
**Models & Prompt Conditions:** Zero-shot, few-shot, chain-of-thought, Recursive Criticism and Improvement (RCI).
**Security Analyzers & Functional Tests:** Code security verification.
**Main Findings:** LLMs have distinct limitations in producing secure code natively. Prompt engineering and iterative verification (like RCI) can mitigate security weaknesses, but require careful prompting.
**Limitations Acknowledged:** LLM output still requires iterative verification to meet software security standards.
**Overlap with Proposed Study:** Investigates prompt conditions and iterative verification, highly overlapping with Conditions B and C.

## 3. An Empirical Evaluation of LLM-Generated Code Security Across Prompting Methods
**Authors:** Mohammed F. Kharma, Ahmed Sabbah, Mohammad Alkhanafseh, Mohammad Hammoudeh, David Mohaisen
**Year:** 2026
**Publication Status:** arXiv Preprint
**URL:** [https://arxiv.org/abs/2605.24298](https://arxiv.org/abs/2605.24298)
**Dataset & Sample Size:** Evaluated across four languages (Java, C++, C, Python).
**Models & Prompt Conditions:** Evaluated 5 different LLMs. Introduced weaknesses-aware zero-shot chain-of-thought (WA-0CoT) using CWE mappings.
**Security Analyzers & Functional Tests:** Empirical analysis of vulnerability frequency and density, categorized by CWE.
**Main Findings:** Prompt engineering alone does *not* yield statistically significant reductions in vulnerability frequency or density. Instead, security-aware prompting alters the structural and compositional distribution of CWE categories. 
**Limitations Acknowledged:** Prompt engineering is insufficient to reliably reduce overall vulnerability levels. Future efforts need language-aware and model-aware design.
**Overlap with Proposed Study:** This study directly contradicts the premise that security-aware prompts simply "make code safer", showing instead that they shift the types of vulnerabilities. It highly overlaps with Condition B and casts doubt on naive security prompting.
