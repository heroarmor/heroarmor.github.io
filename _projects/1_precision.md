---
layout: page
title: Precision As You Need
description: Stochastic computing for mixed-precision DNN inference and acceleration (NeurIPS 2026, HPCA 2027)
importance: 1
category: research
---

**Advisor:** [Prof. Nathaniel Bleier](https://nbleier.com/), University of Michigan · 2026/01 – present

- Reframed stochastic computing (SC) as a dense adaptive quantizer whose precision is set by bit-stream length rather than a fixed datapath, reducing each multiplication to a single AND/XNOR gate.
- Built a GPU library that emulates SC matrix multiplication at scale and a retraining-free per-row mixed-precision policy that stays competitive with fixed-format INT quantization across vision tasks.
- Co-developed PaYN, an SC algorithm–hardware co-design with 128 selectable stream lengths per datapath, allocated per computation group by an offline-calibrated threshold table. In TSMC 22 nm, PaYN cuts stream compute by 60–74% within 1.10× FP16 perplexity and reduces EDP by 2.0× over an INT8 array.

**Publications:** _Precision As You Need: Stochastic Computing Is a Dense Adaptive Quantizer_ (NeurIPS 2026, [arXiv](https://arxiv.org/abs/2609.32922)); _Precision As You Need: A Stochastic-Computing Mixture-of-Precision Neural Network Accelerator_ (HPCA 2027).
