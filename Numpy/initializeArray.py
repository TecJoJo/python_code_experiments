import numpy as np 

oneD = np.zeros(5)
twoD = np.zeros((5,8))
threeD = np.zeros((5,4,3))

# print(oneD)
# print(twoD)
# print(threeD)

# print(np.ones((3,4,2),dtype="int32"))

# print(np.full((2,2),99,dtype="float32"))

# print(np.full_like(threeD,666))
# print(np.full(threeD.shape,666))

# print(np.random.rand(4,2))
# print(np.random.random_sample(oneD.shape))

#print(np.random.randint(7,size=(3,3)))
print(np.random.randint(-4,8,size=(3,3)))

np.identity(5)

arr = np.array([[1,2,3]])
r1 = np.repeat(arr,3,axis=0)
print(r1)

