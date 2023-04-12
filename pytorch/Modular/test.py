import torch
from torchinfo import summary
model = torch.load('../going_modular/models/tinyvgg_model.pth')

print(summary(model, input_size=[1, 3, 64, 64]))
