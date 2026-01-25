import numpy as np 

# type of random 
# 1. np.random.random(size)
N = np.random.random(5) # random five value 
print(N)
M = np.random.random((3,2)) # (3,2) are tuples representation
print(M) # (3,2) shaped random value 

# 2 . np.random.randint(low , high , size)
R = np.random.randint(1,101,10) # print 10 values between 1 to 100
print(R)

#3. np.random.rand() 
# generates floating number between 0 and 1.
X = np.random.rand() # one floating number 
print(X)
Y = np.random.rand(5)#five numbers 
print(Y)
Z = np.random.rand(2,3)# shape is 2X3
print(Z)

# 4 . np.random.randn()
# number positive and nagative 
# no fixed range 
z = np.random.randn(2,3)# shape is 2X3
print(z)

# 5 . np.random.choice()
# print random data from list , can repeat posible 
numbers = [1,2,3,4,5] # printable only from list 
C = np.random.choice(numbers , size = 6 )
print(C)

# 6. np.random.shuffle()
# reorder from original data 
arr = [1,2,3,4,5,6]
np.random.shuffle(arr)
print(arr)

# 7 .np.random.permutation , create a new shuffle array 
arr = [1,2,3,4,5,6]
s = np.random.permutation(arr)
print(s)

# 8 . seed() , same the random output when it is run 
np.random.seed(1)
b = np.random.randint(1,10,5)
print(b)