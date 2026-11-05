---
layout: page
title: Double-P
description: Hierarchical top-p sparse attention for long-context LLMs
importance: 4
category: research
---

**Advisors:** [Prof. Jishen Zhao](https://cseweb.ucsd.edu/~jzhao/) and [Prof. Zhijian Liu](https://zhijianliu.com/) · 2025/09 – 2026/01

- Proposed a hierarchical sparse attention framework that jointly optimizes top-p accuracy, selection overhead, and sparse attention cost.
- Performed coarse-grained top-p estimation at the cluster level using size-weighted centroids, then adaptively refined computation through a second top-p stage.
- Achieved near-zero accuracy drop with up to 1.8× attention computation reduction and 1.3× end-to-end decoding speedup over state-of-the-art methods.

**Paper:** [arXiv:2602.05191](https://arxiv.org/abs/2602.05191)
