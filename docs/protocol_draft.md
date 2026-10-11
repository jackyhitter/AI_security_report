# Protocol Draft

## 1. What Has Already Been Studied
Existing research has thoroughly evaluated how prompt engineering (including zero-shot, chain-of-thought, and security-aware prefixes) affects code generation security. 
- **Bruni et al. (2025)** already tested iterative repair (scanner-guided) and security prompting on the LLMSecEval dataset, reporting up to 68% repair rates.
- **Tony et al. (2024)** explored Recursive Criticism and Improvement (RCI) systematically.
- **Kharma et al. (2026)** demonstrated that security prompting does not necessarily reduce vulnerability *density*, but rather shifts the *distribution* of CWEs.

## 2. Defensible Gap
Because prior work already shows that scanner-guided repair reduces specific security warnings, and because LLMSecEval lacks functional tests, we cannot defensibly study "security improvement without functional regression." 

**Recommended Defensible Gap:** *The "Whack-a-Mole" Effect and Code Bloat in Scanner-Guided Repair.*
Instead of measuring just the reduction in warnings, we will investigate:
1. **Warning Shifting:** When a static analyzer's warning is fed back into the model (Condition C), does the model remove the original CWE but introduce a *new*, different CodeQL warning? (Building on Kharma et al.'s findings of CWE distribution shifting).
2. **Code Complexity Changes:** Does scanner-guided repair artificially inflate code complexity (e.g., Cyclomatic Complexity, Lines of Code) in an attempt to appease the scanner, resulting in bloated implementations?

This gap does not require functional tests and provides a novel angle on the side effects of iterative LLM repair.

## 3. Dataset Support (LLMSecEval)
LLMSecEval supports the security analysis component of this experiment perfectly using its included CodeQL scripts. However, it **does not** support functional regression testing. We will explicitly document that functional correctness is out of scope and cannot be claimed.

## 4. Recommended Experimental Design
- **Dataset:** 150 prompts from LLMSecEval (Python subset).
- **Model:** A small open-weight model (e.g., Qwen2.5-Coder-7B-Instruct or Llama-3-8B-Instruct).
- **Conditions:**
  - *Condition A (Baseline):* Generate code from standard prompts.
  - *Condition B (Security-Aware):* Generate code with a standard security prefix.
  - *Condition C (Scanner-Guided Repair):* Run CodeQL on A's output, feed the warning text back to the model, and prompt for a fix.
- **Metrics:** 
  1. Rate of original CodeQL warning resolution.
  2. Rate of *new* CodeQL warnings introduced in Condition C vs A.
  3. Change in Cyclomatic Complexity (using `radon`) and LOC between A and C.

## 5. Minimum Credible Sample and Compute Requirements
- **Sample:** N=150 prompts × 3 conditions × 5 generations per condition to account for non-determinism = 2,250 generations.
- **Compute:** The experiment can be run reproducibly on **Kaggle's free GPU instances** (e.g., 2x T4 16GB). Models like Qwen2.5-Coder-7B or Llama-3-8B in 4-bit/8-bit quantization comfortably fit within 16GB VRAM and generate code quickly. No paid API calls are required.
- **Caveat:** Using quantized models on Kaggle limits the reasoning capabilities compared to state-of-the-art proprietary models, meaning repair rates might be artificially lower.

## 6. Next Single Action
Determine the exact open-weight code model to use and verify its license permits automated benchmarking, then write a short Kaggle notebook to test a single prompt inference.
