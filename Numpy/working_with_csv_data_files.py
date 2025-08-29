import numpy as np
from pathlib import Path #replace the use of r in the paths, example: file_path = Path("C:/...")

climate_data = np.genfromtxt(r'C:\PROGRAMACIÓN\PYTHON\Numpy\climate.txt', delimiter=',', skip_header=1) #converting the txt to a np.array

print(climate_data[:10])
print(climate_data.shape)


weights = np.array([0.3, 0.2, 0.5])
yields = climate_data @ weights #dot product
print("\n")
print(yields[:10])
print(yields.shape)

climate_results = np.concatenate((climate_data, yields.reshape(100, 1)), axis=1) #np.concatenate()
print(climate_results[:5])
