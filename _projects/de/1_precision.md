---
layout: page
title: Precision As You Need
description: Stochastisches Rechnen für DNN-Inferenz und -Beschleunigung mit gemischter Präzision (NeurIPS 2026, HPCA 2027)
importance: 1
category: forschung
lang: de
permalink: /de/projects/precision/
translations:
  en: /projects/1_precision/
  de: /de/projects/precision/
---

**Betreuer:** [Prof. Nathaniel Bleier](https://eecs.engin.umich.edu/people/bleier-nathaniel/), University of Michigan · 2026/01 – heute

- Stochastisches Rechnen (SC) als dichten adaptiven Quantisierer neu gedacht: Die Präzision wird durch die Bitstromlänge statt durch einen festen Datenpfad bestimmt, und jede Multiplikation reduziert sich auf ein einzelnes AND/XNOR-Gatter.
- Eine GPU-Bibliothek zur Emulation von SC-Matrixmultiplikationen im großen Maßstab sowie eine Mixed-Precision-Strategie pro Zeile ohne Nachtraining entwickelt, die mit INT-Quantisierung fester Breite konkurrenzfähig ist.
- PaYN mitentwickelt, ein SC-Algorithmus-Hardware-Co-Design mit 128 wählbaren Bitstromlängen pro Datenpfad, die per offline kalibrierter Schwellwerttabelle je Rechengruppe zugewiesen werden. In TSMC 22 nm senkt PaYN den Stream-Rechenaufwand um 60–74 % bei höchstens 1,10-facher FP16-Perplexität und reduziert das Energy-Delay-Produkt um das 2,0-Fache gegenüber einem INT8-Array.

**Publikationen:** _Precision As You Need: Stochastic Computing Is a Dense Adaptive Quantizer_ (NeurIPS 2026, [arXiv](https://arxiv.org/abs/2609.32922)); _Precision As You Need: A Stochastic-Computing Mixture-of-Precision Neural Network Accelerator_ (HPCA 2027).
