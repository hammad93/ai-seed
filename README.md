# ai-seed
A Python package that manages seeds during AI &amp; ML training through a TPM and a True Random Number Generator (TRNG) providing additional rigor to AI and Machine learning training over Pseudo Random Number Generators (PRNG). The code is flexible to facilitate integration and maintenance in existing AI and Machine Learning workflows.

# Installation
Please note that currently only Linux is supported.

1. The standard TPM API is written in C [so we can install](https://tpm2-pytss.readthedocs.io/en/latest/install.html) them the libraries our respective system package managers,
  - `apt-get install libtss2-dev`
  - `dnf install tpm2-tss-devel`

# Usage

```python
from ai_seed import AISeed

# True random generation (TPM)
trng = AISeed(verbose=True)
print("TRNG bytes:", trng.get_random_bytes(16))

# Reproducible PRNG
prng = AISeed(seed=42)
bytes1 = prng.get_random_bytes(16)
prng.set_seed(42)
bytes2 = prng.get_random_bytes(16)
print("PRNG reproducibility:", bytes1 == bytes2)  # True
```