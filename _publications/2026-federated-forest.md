---
title: "Principled Federated Random Forests for Heterogeneous Data"
collection: publications
permalink: /publication/federated-forest
excerpt: 'Random Forests (RF) are among the most powerful and widely used predictive models for centralized tabular data, yet few methods exist to adapt them to the federated learning setting. Unlike most federated learning approaches, the piecewise-constant nature of RF prevents exact gradient-based optimization. As a result, existing federated RF implementations rely on unprincipled heuristics: for instance, aggregating decision trees trained independently on clients fails to optimize the global impurity criterion, even under simple distribution shifts. We propose FedForest, a new federated RF algorithm for horizontally partitioned data that naturally accommodates diverse forms of client data heterogeneity, from covariate shift to more complex outcome shift mechanisms. We prove that our splitting procedure, based on aggregating carefully chosen client statistics, closely approximates the split selected by a centralized algorithm. Moreover, FedForest allows splits on client indicators, enabling a non-parametric form of personalization that is absent from prior federated random forest methods. Empirically, we demonstrate that the resulting federated forests closely match centralized performance across heterogeneous benchmarks while remaining communication-efficient.'
date: 2026-02-03
venue: 'Arxiv'
# slidesurl: 'http://remikhellaf.github.io/files/federated_causal_inference_khellaf.pdf'
paperurl: 'https://arxiv.org/pdf/2602.03258'
citation: 'Khellaf, R., Scornet, E., Bellet, A., & Josse, J. (2026). Principled Federated Random Forests for Heterogeneous Data.&quot; <i>Conference Article</i>.'
---

[Download paper here](https://arxiv.org/pdf/2602.03258)

<!-- [Download slides here](http://remikhellaf.github.io/files/federated_observational_khellaf.pdf) -->

<!-- Recommended citation: Your Name, You. (2009). "Paper Title Number 1." <i>Journal 1</i>. 1(1). -->
