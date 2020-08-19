import numpy as np

data = np.random.rand(2,3)

print(data)
print(data*10)
print(data+data)


arr = [1,2,3,4,5,6]

nparr = np.array(arr,int)
nparr

nparr.astype(float)

nparr2 = np.array(arr,)

np.zeros((3,6))

np.empty((2,3))

np.arange(1,20)


z = np.zeros((2,3))

r = np.random.rand(2,3)

r2 = np.random.rand(3,2)

print(z>r)

r2 = r2.reshape(2,3)
print(r2>r)
 
