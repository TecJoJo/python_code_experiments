import numpy as np

# a = np.array([1,2,3])
# b = a
# b[0] = 100

# print(a)
#In the approach above, memory stays the same only the reference are copied that's why the 
# a is also  going to change accordingly 

a = np.array([1,2,3])
b = a.copy()
b[0] = 100

print(b)
print(a)