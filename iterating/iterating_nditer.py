import numpy as np 
# 1D array 
s = np.array([1,2,3,4,5,6,7])

for x in np.nditer(s):
    print(x)
print("\n")
# 2D array
S = np.array([[1,2,3],[4,5,6]])
for X in np.nditer(S):
    print(X)
print("\n")
# 3D array 
e = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
for i in np.nditer(e):
    print(i)

print("\n")
# 3D array 
e = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
for i,v in np.ndenumerate(e):
    print(i,v) # print index using enumerate() function 