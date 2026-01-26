import numpy as np

a1 = np.arange(10, dtype=np.int8)
a2 = np.arange(12,dtype= float).reshape(3,4)
a3 = np.arange(8).reshape(2,2,2)

# 1 . ndim() show the dimentions of the array 
print(np.ndim(a1)) 
print(np.ndim(a2))
print(np.ndim(a3))
# also use ---> print(a1.ndim)
print("\n")
# 2 . shape() return number of row an column 
print(a1.shape)
print(a2.shape)
print(a3.shape)
print("\n")
# 3 . size() , return the size of array 

print(a1.size)
print(a2.size)
print(a3.size)
print("\n")
# 4 . itemsize() , return each element bytes 
print(a1.itemsize)
print(a2.itemsize)
print(a3.itemsize)
print("\n")
# 5. dtype , return the type of an element 
print(a1.dtype)
print(a2.dtype)
print(a3.dtype)
print("\n")
# 6 . nbytes --> return total memory used by array 
print(a1.nbytes)
print(a2.nbytes)
print(a3.nbytes)
print("\n")

# 7 . T() --->transpose of matrix 
# swap rows <--> column 
print(a2.T)


#8 . real & imag() --> return real and imagnery part of array element 
c = np.array([1+2j, 3+4j])
print(c.real)
print(c.imag)

print(a1.flags) # tells that hows element stored in memory 

#9 astype --> to change the data type 
print(a3.astype(str))