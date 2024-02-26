# Submission for CNN Interpretability Competition at IEEE SaTML 2024

## Overview of repository
```bash
trojan-detection-submission
|-data
    |---trojan-rediscovery   # Contains 12 images for trojan reconstructions of each of the 12 classes
    |---secret-trojans       # Contains 4 images showing the visualisations used to make the guesses
    |---interp_trojan_resnet5-_model.pt  # Model checkpoint of the provided trojaned model
|-trojan_rediscovery.py


```

## Installation

## Method - Trojan Rediscovery
We use a method extending existing Activation Maximisation (Olah et al., Szegedy et al.) methods to create visualisations (prototypes) that maximally activate a given logit. These visualisations capture features that the network deems important to classify a given class. The implanted trojans show up as features in these visualisations in varying forms showing their presence in the network's decision-making process. We employ a *diversity objective* that encourages the generated prototypes to show diverse features letting us see features of varying form that are important for the classification of a given class. For a theoretical overview of the method used, please see our [paper](https://arxiv.org/abs/2309.17144) accepted to ATTRIB @ NeurIPS '23. 





