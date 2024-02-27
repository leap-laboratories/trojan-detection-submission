# Submission for CNN Interpretability Competition at IEEE SaTML 2024

## Overview of repository
```bash
trojan-detection-submission
|-data
    |---trojan-rediscovery   # Contains 12 images (each image with 10 visualisations) for trojan reconstructions of each of the 12 classes
    |---secret-trojans       # Contains 16 images (4 per trojaned class) showing the visualisations used to make the guesses for secret trojans
    |---interp_trojan_resnet5-_model.pt  # Model checkpoint of the provided trojaned model
|-CNN_Interpretability_Competition___SaTML__24___Submission.pdf # PDF report containing more details about our method and reasoning behind our guesses
|-environment.yml            # YAML file to recreate conda environment
|-secret_trojans.py          # Script to replicate secret trojan images
|-trojan_rediscovery.py      # Script to replicate trojan rediscovery images
|-.gitignore                 # Used to ignore library generated files
```

## Installation

### Installing libraries
We provide a conda environment file that recreates the environment we used to run the scripts in the repository. Simply run,
```
conda env create -f environment.yml
```

Alternatively, if you prefer to install your own version of PyTorch for hardware compatibility reasons, ensure that `leap_ie` is installed. This can be done using,
```
pip install leap_ie
```

### Generating a Leap API key
A leap API key is required to use the `leap_ie` library, instructions on how to generate the key and set it up correctly can be found on: https://github.com/leap-laboratories/leap_ie?tab=readme-ov-file#generating-an-api-key. After generating an API key put in the key in the `"YOUR_LEAP_API_KEY"` placeholder string in the config dict for both the `secret_trojans.py` and `trojan_rediscovery.py`. 

## Method 
We use a method extending existing Activation Maximisation (Olah et al.2017 ,Szegedy et al. 2014) methods to create visualisations (prototypes) that maximally activate a given logit. These visualisations capture features that the network deems important to classify a given class. The implanted trojans show up as features in these visualisations in varying forms showing their presence in the network's decision-making process. We employ a *diversity objective* that encourages the generated prototypes to show diverse features letting us see features of varying form that are important for the classification of a given class. For a theoretical overview of the method used, please see our [paper](https://arxiv.org/abs/2309.17144) accepted to ATTRIB @ NeurIPS '23. 

More details about our method can be found in the PDF report in this repository.

## Trojan Rediscovery submission

Our submissions for the trojan rediscovery challenge can be found in `data/trojan-rediscovery` as a set of 12 images with each image containing 10 visualisations for the trojaned class as requested by the competition organisers. 

## Secret Trojan guesses

Our guesses for the secret trojans are as follows:
<pre>
Lawn Mower: <b>Spoon</b>
Drum: <b>Carrot</b>
Coho salmon: <b>Chair</b>
Punching bag: <b>Christmas Tree</b>
</pre>

The visualisations used to make these guesses can be found in our report PDF and `data/secret-trojans`.






