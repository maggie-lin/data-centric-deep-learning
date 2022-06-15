import torch

data = torch.load('course/week2/pipeline_project/src/tests/images/regression/test-data.pt')

print(data.keys())
print(data['images'].size(), data['labels'].size())
print(data['labels'][:10])