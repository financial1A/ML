import torch

# Create a 1D tensor with 12 elements
x = torch.arange(12)

# Print the original tensor
print("Original tensor:")
print(x)

# Reshape the tensor using reshape()
X_reshape = x.reshape(3, 4)

# Print the reshaped tensor
print("\nReshaped tensor using reshape():")
print(X_reshape)

# Reshape the tensor using view()
X_view = x.view(3, 4)

# Print the reshaped tensor
print("\nReshaped tensor using view():")
print(X_view)
