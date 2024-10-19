import torch

# Create a tensor with random values
x = torch.randn(3, 3)
print("Tensor x:\n", x)

# Get the number of elements in the tensor
num_elements = x.numel()
print("Number of elements in x:", num_elements)
