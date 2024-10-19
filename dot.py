import torch

# Define vector x and vector y
x = torch.tensor([0., 1., 2., 3.,4.], dtype=torch.float32)
y = torch.ones(5, dtype=torch.float32)
print(y)
# Compute the dot product
dot_product = torch.dot(x, y)
print("Dot product:", dot_product)

# Alternatively, compute it using elementwise multiplication followed by a sum
dot_product_alternative = torch.sum(x * y)
print("Dot product (alternative):", dot_product_alternative)
