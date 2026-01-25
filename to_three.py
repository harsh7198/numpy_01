import numpy as np 

# 3D reshape very important to ML 
A = np.array([1,2,3,4,5,6,7,8])
new_array = A.reshape(2,2,2)
# print 3D array having 2 column and 2 rows 
print(new_array)