#revision
import numpy as np
a = np.arange(1,13).reshape(3,4)
print(a)
print("Row:",np.sum(a,axis=1))
print("Column:",np.sum(a,axis=0))
print("mean:", np.mean(a))


# copy vs view
a = np.array([10, 20, 30])
b = a          # view/reference
c = a.copy()   # deep copy

b[0] = 99

print("a:", a)
print("b:", b)
print("c:", c)


a = np.array([10, 20, 30])
b = np.array([40, 50, 60])
print(np.concatenate((a,b)))
print(np.hstack((a,b)))
print(np.vstack((a,b)))

a = np.array([10, 20, 30, 40, 50, 60])
np.split(a,2)
np.split(a,3)


a = np.array([10, 20, np.nan, 40, np.nan])

print(np.isnan(a))
print(np.nanmean(a))
print(np.nansum(a))

a = np.array([10, 20, 10, 30, 20, 10])
values,count=np.unique(a, return_counts=True)
print(values)
print(count)

