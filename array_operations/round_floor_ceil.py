import numpy as np 

# round off nearest number 
np.random.seed(1)
X = np.round(np.random.random((2,3))* 100)
print(X)

# round off backward number 
np.random.seed(1)
Y = np.floor(np.random.random((2,3))* 100)
print(Y)

# ceil round off frontest number like 1.8 ~ 2 
np.random.seed(1)
Z = np.ceil(np.random.random((2,3))* 100)
print(Z)