import torch

# Example vector
x = torch.tensor([3.0, 4.0, 5.0])

# Using PyTorch to calculate the L2 norm (Euclidean norm)
l2_norm_torch = torch.norm(x, p=2)

# Manually calculating the L2 norm
l2_norm_manual = torch.sqrt(torch.sum(x**2))

print(f"L2 Norm using PyTorch: {l2_norm_torch}")
print(f"L2 Norm calculated manually: {l2_norm_manual}")
