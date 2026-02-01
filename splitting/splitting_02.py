import numpy as np 

# hsplit used to horizontal split 
B = np.array([[1,2,3,4], [5,6,7,8]])

print(np.hsplit(B,2))

# hsplit used to vertical split 
print(np.vsplit(B,2))


# depth split used for 3D array 

D = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(np.dsplit(D,2))

# unequal splitting using indices 
# split specific position 

A = np.array([10, 20, 30, 40, 50, 60])
print(np.split(A ,[2,4]))