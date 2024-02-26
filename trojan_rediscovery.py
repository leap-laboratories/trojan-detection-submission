from leap_ie.env import get_env_value
import leap_ie.vision.class_lists as class_lists
from leap_ie.vision import engine
import numpy as np
import torch
from torchvision import models
import torchvision.transforms as T


MEAN = np.array([0.485, 0.456, 0.406])
STD = np.array([0.229, 0.224, 0.225])
prep = T.Normalize(mean=MEAN, std=STD)

trojaned_classes = [30, 146, 365, 99, 211, 928, 769, 378, 316, 463, 487, 129]
num_prototypes = 10

config = {"leap_api_key": get_env_value("leap_api_key", safe=False),
          "wandb_api_key": get_env_value("wandb_api_key", safe=False),
	      "wandb_entity": "leap-labs",
          "diversity_weight": 0.5,
          "objective": "cs_objective"
          }

for trojaned_class in trojaned_classes:
    
    model = models.resnet50(pretrained=True).to('cuda').eval()
    model.load_state_dict(torch.load(
        'data/interp_trojan_resnet50_model.pt'))

    res = engine.generate(project_name="trojan-albatross-diverse-5", model=model, class_list=class_lists.imagenet, preprocessing=prep, config=config, target_classes=target*5, samples=None, device='cuda', mode="pt")
    breakpoint()