import numpy as np
# Create a 4x5 array (values 1 to 20)
arr = np.arange(1, 21).reshape(4, 5)
# Find transpose
trans_arr = arr.T
# Display results
print("Original 4x5 Array:")
print(arr)
print("transpose (5x4 Array):")
print(trans_arr)
