import numpy as np 
a = np.full((5,5),1)
a[1:4,1:4] = np.full((3,3),0)
a[2,2] = 9
print(a)