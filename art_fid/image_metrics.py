import lpips
import torch
import torch.nn as nn


def normalize(x):
    mean = torch.tensor([0.485, 0.456, 0.406], device=x.device).reshape(1, -1, 1, 1)
    std = torch.tensor([0.229, 0.224, 0.225], device=x.device).reshape(1, -1, 1, 1)
    x = (x - mean) / std
    return x


class Metric(nn.Module):

    def __init__(self, metric_type='vgg'):
        super(Metric, self).__init__()
        if metric_type == 'vgg':
            self.model = lpips.pn.vgg16()
        elif metric_type == 'alexnet':
            self.model = lpips.pn.alexnet()
        else:
            raise ValueError(f'Invalid metric type: {metric_type}')

    def forward(self, x, y):
        features_x = self.model(normalize(x))._asdict()
        features_y = self.model(normalize(y))._asdict()
        
        dist = 0.0
        for layer in features_x.keys():
            dist += torch.mean(torch.square(features_x[layer] - features_y[layer]), dim=(1, 2, 3))
        return dist / len(features_x)


class LPIPS(nn.Module):

    def __init__(self):
        super(LPIPS, self).__init__()
        self.dist = lpips.LPIPS(net='alex')

    def forward(self, x, y):
        # images must be in range [-1, 1]
        dist = self.dist(2 * x - 1, 2 * y - 1)
        return dist


