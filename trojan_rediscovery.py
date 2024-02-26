from leap_ie.env import get_env_value
import leap_ie.vision.class_lists as class_lists
from leap_ie.vision import engine

import matplotlib.pyplot as plt
import numpy as np
import torch
from torchvision import models
import torchvision.transforms as T
from torchvision.io import read_image
from torchvision.utils import make_grid

def main():

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

        res = engine.generate(project_name="trojan-rediscovery", model=model, class_list=class_lists.imagenet, preprocessing=None, config=config, target_classes=[trojaned_class]*num_prototypes, samples=None, device='cuda', mode="pt")
        
        imgs = []
        for j in range(num_prototypes):
            img = read_image(res[0].loc[1000*j+trojaned_class].input)
            imgs.append(img)

        grid = make_grid(imgs, nrow=10)
        plt.rcParams["savefig.bbox"] = 'tight'
        plt.axis('off')
        plt.imshow(grid.permute(1,2,0))
        plt.savefig(f'data/trojan-rediscovery/class_{trojaned_class}.png', dpi=800)

if __name__ == '__main__':
    main()