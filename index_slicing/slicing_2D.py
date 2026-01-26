import numpy as np 

arr2 = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])

# syntax arr2[row slicing , column slicing ]
print(arr2[0:2])
print(arr2[:,1]) 
print(arr2[1:,1:])
print(arr2[0:2,1:])
print(arr2[0:1,0:1])
