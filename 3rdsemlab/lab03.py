import numpy as np

arr=np.array([0,2,3,4,0,6,7])
# this function automatically count non zero values

non_zero=np.count_nonzero(arr)

#original array

print("array is: ",arr)

# no of non zero elements
print("no of non zero values in array are:",non_zero)