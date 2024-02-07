---
title: "Journées de Biostatistiques 2023"
collection: talks
type: "Talk"
permalink: imt23
venue: "Institut de Mathématiques de Toulouse"
date: 2023-11-17
location: "Toulouse, France"
---

Here is the abstract of my talk, which is about the use of Instrumental Variables estimators in Causal Inference, and based from my internship prior to my PhD at Inria, in collaboration with Quinten Health.

======
In this work, we provide a comprehensive theoretical and empirical exploration of the integration of instrumental variables (IV) in causal analysis. Specifically, we focus on the estimation of the Average Treatment Effect (ATE) when confronted with the challenge of unmeasured confounding variables.

We begin by introducing the conceptual foundations and methodological underpinnings of the IV estimator, highlighting the critical assumptions, potential violations, and strategies for mitigating such violations. Comparative simulations involving well-known ATE estimators, including Inverse Propensity Score Weighting, the G-Formula, and IV estimation, are presented, demonstrating their performance across a diverse range of scenarios.

Then, acknowledging that practitioners often rely on the sometimes unrealistic linearity of outcome assumption in ATE estimation, we detail a more flexible nonparametric approach that facilitates the computation of the Local Average Treatment Effect (LATE). This method requires an additional assumption, monotonicity, ensuring a monotonous relationship between treatment and the instrumental variable, and integrates it within the framework of Principal Stratification. Empirical and analytical results are showcased, emphasizing the efficacy of this methodology while advocating for the need for caution in LATE estimation.

Our findings reveal challenges in ATE estimation using IV in scenarios with limited sample sizes and the inherent complexity of interpreting results in nonparametric approaches, where the target population for LATE estimation may remain unidentified solely based on available data.

In conclusion, this presentation aims at gaining a comprehensive understanding of when and how to judiciously incorporate instrumental variables into causal analysis, leading to more accurate and insightful conclusions.