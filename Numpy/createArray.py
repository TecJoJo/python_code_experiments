import numpy as np 

a = np.array([1,2,3],dtype="int16") 
print(a)

b = np.array([[9.0,8.0,7.0],[6.0,5.0,4.0]])
print(b)

#get Dimension
print(b.ndim)

#get Shape 
print(b.shape)

#get Type
print(a.dtype)

#get Size 
print(a.itemsize)#out put 2, means two byts, because dtype="int16"

#get total size 
print(a.nbytes)
#or
print(a.size * a.itemsize)