import numpy as np  

arr1 = np.array([[11,12,13],
                 [13,14,15],
                 [15,16,17]])
                 
arr2 = np.array([[1,2,3],
                 [3,4,5],
                 [5,6,7]])

add_arrays = arr1 + arr2 
print(add_arrays)
print("\n")

add_scalar = add_arrays + 100 #same with -, *, /, %
print(add_scalar)