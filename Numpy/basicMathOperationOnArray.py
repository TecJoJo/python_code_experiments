import numpy as np
import math 
a = np.array([1,2,3,4])
print(a)
print(a+2)
print(a-2)
print(a*2)
print(a/2)

a+=2
print("a is now {a}".format(a=a))

b= np.array([1,0,1,0])
print(a + b)

print(a**2)

#Take the sin
print("sin of 3 is :{}".format( math.sin(3)))
print(np.sin(a))