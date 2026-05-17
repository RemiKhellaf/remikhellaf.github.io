---
title: "Federated Causal Inference from Multi-Site Observational Data via Propensity Score Aggregation"
collection: publications
permalink: /publication/federated-observational
excerpt: 'Causal inference typically assumes centralized access to individual-level data. Yet, in practice, data are often decentralized across multiple sites, making centralization infeasible due to privacy, logistical, or legal constraints. We address this problem by estimating the Average Treatment Effect (ATE) from decentralized observational data via a Federated Learning (FL) approach, allowing inference through the exchange of aggregate statistics rather than individual-level data. We propose a novel method to estimate propensity scores via a federated weighted average of local scores using Membership Weights (MW), defined as probabilities of site membership conditional on covariates. MW can be flexibly estimated with parametric or non-parametric classification models using standard FL algorithms. The resulting propensity scores are used to construct Federated Inverse Propensity Weighting (Fed-IPW) and Augmented IPW (Fed-AIPW) estimators. In contrast to meta-analysis methods, which fail when any site violates positivity, our approach exploits heterogeneity in treatment assignment across sites to improve overlap. We show that Fed-IPW and Fed-AIPW perform well under site-level heterogeneity in sample sizes, treatment mechanisms, and covariate distributions. Theoretical analysis and experiments on simulated and real-world data demonstrate clear advantages over meta-analysis and related approaches.'
date: 2025-05-23
venue: 'ICML'
slidesurl: 'http://remikhellaf.github.io/files/federated_observational_khellaf.pdf'
paperurl: 'https://arxiv.org/pdf/2505.17961'
citation: 'Khellaf, R., Bellet, A., & Josse, J. (2025). Federated Causal Inference from Multi-Site Observational Data via Propensity Score Aggregation.&quot; <i>Conference Article</i>.'
---

[Download paper here](https://arxiv.org/pdf/2505.17961)

[Download slides here](http://remikhellaf.github.io/files/federated_observational_khellaf.pdf)

<!-- Recommended citation: Your Name, You. (2009). "Paper Title Number 1." <i>Journal 1</i>. 1(1). -->
