import pandas as pd
import torch

# Create sample data for inputs and outputs
data_inputs = {'feature1': [3, 2, 4, 3],
               'feature2': [1, 0, 0, 0],
               'feature3': [0, 1, 1, 1]}
data_outputs = {'price': [127500, 106000, 178100, 140000]}

# Create pandas DataFrames
inputs = pd.DataFrame(data_inputs)
outputs = pd.DataFrame(data_outputs)

# Convert DataFrames to PyTorch tensors
X, y = torch.tensor(inputs.values, dtype=torch.float64), torch.tensor(outputs.values)

# Display the tensors
print("Tensor X:\n", X)
print("Tensor y:\n", y)
