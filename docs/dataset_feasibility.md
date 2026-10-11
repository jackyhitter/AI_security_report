# Dataset Feasibility: LLMSecEval

Repository Evaluated: [https://github.com/tuhh-softsec/LLMSecEval](https://github.com/tuhh-softsec/LLMSecEval)

## 1. License and Permitted Use
The repository is licensed under the **GNU GPLv3 License**, which permits academic and empirical research usage, provided derivative works share the same license.

## 2. Number and Structure of Tasks
The dataset (`LLMSecEval-Prompts_dataset.json`) contains **150 natural language prompts** mapped to 18 of the Top 25 CWEs from 2021. The prompts are sanitized to remove direct mentions of vulnerabilities.

## 3. Availability and Provenance of Reference Implementations
Reference implementations are provided in the `Dataset/Secure Code Samples` directory, organized by CWE (covering the 18 CWEs). These are derived from the original dataset used in Pearce et al. ("Asleep at the Keyboard").

## 4. CWE Metadata
Extensive CWE metadata is included. Prompts are heavily structured around specific CWE scenarios, making it easy to track performance across different weakness categories.

## 5. Existing Security-Analysis Scripts
The repository includes a `Security Analysis - CodeQL` directory, which provides out-of-the-box support for static analysis of generated code using CodeQL.

## 6. Availability of Functional Tests or Executable Specifications
**CRITICAL LIMITATION:** Functional tests are severely lacking. The `Dataset/Security Unit Tests` directory only contains tests for exactly two CWE categories (`cwe-190` and `cwe-200`). There are no executable specifications or comprehensive test suites for the remaining 16 CWEs. 

## 7. Consistent Evaluation Across Conditions
Because there are virtually no functional tests, **we cannot accurately evaluate functional correctness or regressions** across the three conditions (Baseline, Security-Aware, Scanner-Guided). 
If we run this experiment, our claims must be strictly limited to: "Does scanner-guided repair reduce CodeQL warnings?" We cannot definitively claim that the code "does not break intended functionality," because we lack the ground-truth tests to prove functionality. We must explicitly state that functional correctness is unknown rather than improvising tests.
