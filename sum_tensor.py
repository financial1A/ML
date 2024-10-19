import torch

# Create tensor A
A = torch.tensor([[0, 1, 2, 3],
                  [4, 5, 6, 7],
                  [8, 9, 10, 11],
                  [12, 13, 14, 15],
                  [16, 17, 18, 19]], dtype=torch.float32)

# Sum along the axis=1 (row-wise) and keep the same number of dimensions (keepdims=True)
sum_A = A.sum(axis=1, keepdims=True)
print("Sum of each row (sum_A):\n", sum_A)

# Broadcasting to divide A by the sum of each row
normalized_A = A / sum_A
print("Normalized tensor A (A / sum_A):\n", normalized_A)

# Perform cumulative sum along axis 0 (columns)
A_cumsum = A.cumsum(axis=0)
print(A_cumsum)