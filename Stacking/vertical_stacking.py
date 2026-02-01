import numpy as np 

# vertical staking adds rows of multiple array into one array 

A = np.array([[1,2,3],[4,5,6]])
B = np.array([[7,8,9],[10,11,12]])
print(np.vstack((A,B)))
print("\n")
# horizontal stacking adds column of multiple array one array 

print(np.hstack((A,B)))
print("\n")
# depth creates a 3D array 

print(np.dstack((A,B)))
print("\n")

# stack adds a new axis 

print(np.stack((A, B), axis=0))
print("\n")

print(np.stack((A, B), axis=1))
print("\n")

print(np.stack((A, B), axis=2))