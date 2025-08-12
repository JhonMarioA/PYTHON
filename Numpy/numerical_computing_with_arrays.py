import numpy as np


#MANUAL DOT CALCULATIONS, doing manual calculations

kanto = [73, 67, 43] #temperature, rainfall, humedity
weights = [0.3, 0.2, 0.5]


def crop_yiel(region, weights):
    result = 0
    for x, w in zip(region, weights):
        result += x*w
    return result

result = crop_yiel(kanto, weights)
print(result)
print("\n")


#USING NUMPY.ARRAY()

kanto = np.array([73, 67, 43])
weights = np.array([0.3, 0.2, 0.5])
print(type(kanto)) #new class

#operating on numpy arrays
print(np.dot(kanto, weights)) #np.dot()
print((kanto*weights).sum())  #.sum()

#2-dimensional Numpy array (matrix)

climate_data = np.array([[73, 67, 43], 
                         [91, 88, 64],
                         [87, 134, 58],
                         [102, 43, 37],
                         [69, 96, 70]])

print("\n")
print(climate_data.shape)
print(weights.shape)

#3-dimensional array

arr3 = np.array([
    [[11, 12, 13], [13, 14, 15]],

    [[15, 16, 17], [17, 18, 19.5]]
])

print(arr3.shape)



#multiplying, matrix 5x3 *  vector 3x1 

print(np.matmul(climate_data, weights))
print(climate_data @ weights)


#comparision operations like ==, !=, >... with arrays


arr1 = np.array([[1,2,3], [3,4,5]])
arr2 = np.array([[1,2,3], [3,4,5]])

print(arr1 == arr2)
print((arr1 == arr2).sum()) #to count the machtes
print(arr1 > arr2)