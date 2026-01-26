import numpy as np 

s = np.array([[[1,2,3],
               [4,5,6]],

              [[7,8,9],
               [10,11,12]]])
# (axis 0 ,axis 1 , axis 2 )
print(s[1,0,0])
print(s[1,1,2])
# (depth_slice , row_slice , column_slice)
print(s[:,:,1]) # all but each first column 