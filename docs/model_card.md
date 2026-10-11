# Model Card: Qwen2.5-Coder-7B-Instruct

- **Repository:** `Qwen/Qwen2.5-Coder-7B-Instruct`
- **Publisher:** Qwen (Alibaba Cloud)
- **License:** Apache 2.0 (Permissive for research and commercial use)
- **Parameters:** 7 Billion
- **Quantization:** 4-bit (via bitsandbytes) to fit in <8GB VRAM environments.
- **Hardware Requirements:** Kaggle 2x T4 or 1x P100 (16GB VRAM) easily supports 4-bit or 8-bit quantized inference. Local execution on a 6GB VRAM GPU is borderline and typically requires offloading or aggressive quantization.
- **Suitability:** This model is explicitly designed for code generation and instruction following, making it a strong, modern baseline for evaluating secure coding prompts and repairs.
