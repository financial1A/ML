import torch

# Create a tensor A with values from 0 to 19, reshaped to a 5x4 matrix
A = torch.arange(20, dtype=torch.float32).reshape(5, 4)
print("Tensor A:\n", A)

# Clone A to create a new tensor B with the same values
B = A.clone()
print("Tensor B (clone of A):\n", B)

# Add tensors A and B
C = A + B
print("Tensor A + B:\n", C)
