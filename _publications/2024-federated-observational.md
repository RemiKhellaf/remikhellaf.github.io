---
title: "Federated Causal Inference from Multi-Site Observational Data via Propensity Score Aggregation"
collection: publications
permalink: /publication/federated-observational
excerpt: 'Causal inference typically assumes centralized access to individual-level data. Yet, in practice, data are often decentralized across multiple sites, making centralization infeasible due to privacy, logistical, or legal constraints. We address this by estimating the Average Treatment Effect (ATE) from decentralized observational data using federated learning, which enables inference through the exchange of aggregate statistics rather than individual-level data. We propose a novel method to estimate propensity scores in a (non-)parametric manner by computing a federated weighted average of local scores, using two theoretically grounded weighting schemes -- Membership Weights (MW) and Density Ratio Weights (DW) -- that balance communication efficiency and model flexibility. These federated scores are then used to construct two ATE estimators: the Federated Inverse Propensity Weighting estimator (Fed-IPW) and its augmented variant (Fed-AIPW). Unlike meta-analysis methods, which fail when any site violates positivity, our approach leverages heterogeneity in treatment assignment across sites to improve overlap. We show that Fed-IPW and Fed-AIPW perform well under site-level heterogeneity in sample sizes, treatment mechanisms, and covariate distributions, with theoretical analysis and experiments on simulated and real-world data highlighting their strengths and limitations relative to meta-analysis and related methods.'
date: 2025-05-23
venue: 'Arxiv'
# slidesurl: 'http://remikhellaf.github.io/files/federated_causal_inference_khellaf.pdf'
paperurl: 'https://arxiv.org/pdf/2505.17961'
citation: 'Khellaf, R., Bellet, A., & Josse, J. (2025). Federated Causal Inference from Multi-Site Observational Data via Propensity Score Aggregation.&quot; <i>Conference Article</i>.'
---

[Download paper here](https://arxiv.org/pdf/2410.16870)

<!-- [Download slides here](http://remikhellaf.github.io/files/federated_causal_inference_khellaf.pdf) -->

<!-- Recommended citation: Your Name, You. (2009). "Paper Title Number 1." <i>Journal 1</i>. 1(1). -->
