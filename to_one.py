import numpy as np 

a = np.array([1,2,3,4,5,6])
# -1 tells NumPy to calculate the dimension automatically.
# numpy figure out column automatically 
new_array = a.reshape(2,-1)
print(new_array)