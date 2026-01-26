#revision
import numpy as np
ar=np.array([1,2,3,44,5,8])
print(ar)
print(type(ar))
ar=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(ar.ndim)
print(ar.dtype)
print(ar.shape)
print(ar.size)
a = np.array([[10,20,30],
              [40,50,60],
              [70,80,90]])
print(a[0])
print(a[:,2])
print(a[2,:])
print(a[0:2,1:3])
print(a[0])
print(a[0,0])
print(a[0][0])
a=np.zeros((2,3))
print(a)
a=np.ones((3,3))
print(a)
a=np.arange(1,10,5)
print(a)
a=np.linspace(1,6,5)
print(a)
a = np.array([10,20,30])

print(a + 5)
print(a * 2)
print(a ** 2)
print(a / 2)
print(a // 2)
print(a - 2)
print(a[a<25])
a = np.array([10,20,30,40])

print(a.sum())
print(a.mean())
print(a.max())
print(a.var())
a = np.array([[10,20,30],
              [40,50,60]])

print(a.sum(axis=0))  # column-wise
print(a.sum(axis=1))  # row-wise
print(a.mean(axis=0))
print(a.mean(axis=1))
print(a.max(axis=0))
print(a.max(axis=1))
print(a.var(axis=0))
print(a.var(axis=1))
a = np.array([1,2,3,4,5,6])
print(a.reshape(2,3))
marks = np.array([45, 67, 89, 34, 76, 90, 55])
average = marks.mean()
print(marks[marks > average])
import numpy as np

a = np.array([[5, 10, 15],
              [20, 25, 30]])

print(a[:, 1])
print(a[a > 15])
a = np.array([10, 20, 30, 40])

a[a < 25] = 0
print(a)
a = np.array([10, 20, 30, 40, 50])

print(a[(a > 20) & (a < 50)])
a = np.array([[10,20,30],
              [40,50,60],
              [70,80,90]])

print(a[a[:, 1] > 40])
a[a[:, 1] > 40]
a = np.array([30, 10, 50, 20])

print(np.sort(a))
a = np.array([30, 10, 50, 20])

print(np.argsort(a))
a = np.array([10, 20, 10, 30, 20, 10])

values, counts = np.unique(a, return_counts=True)

print(values)
print(counts)
a = np.array([1,2,3])
b = np.array([4,5,6])

print(np.vstack((a,b)))
print(np.hstack((a,b)))
print(np.stack((a,b)))
a = np.array([[10,20,30],
              [40,50,60]])

b = np.array([1,2,3])

print(a + b)
expenses = np.array([300, 700, 800, 200, 900, 750, 650])

print(expenses[(expenses > 500) & (expenses < 800)])
array=np.array( [10, 20, 30, 40, 50] )
print(array)
print(array.ndim)
print(array.shape)
print(array.size)
a = np.array([10, 20, 30, 40, 50])
print(a[2])
print(a[1:4])
print(a[-2:])
a = np.array([[10,20,30],
              [40,50,60],
              [70,80,90]])
print(a[1,:])
print(a[:,2])
print(a[1][1])
a = np.array([[10,20,30],
              [40,50,60],
              [70,80,90]])
print(a[1,:])
print(a[:,2])
print(a[1][1])
a = np.array([10, 25, 40, 45, 60, 30])
print(a[a>40])
a = np.array([10, 20, 30, 40, 50, 60])
print(a[(a>20) & (a<50)])
a = np.array([10, 20, 30, 40, 50])
print(np.sum(a))
print(np.mean(a))
print(np.max(a))
print(np.min(a))
a = np.array([10, 25, 30, 45, 20, 60])
a[a<30]=0
print(a)
a = np.array([[10, 20, 30],
              [40, 50, 60],
              [70, 80, 90]])
print(np.sum(a,axis=0))
print(np.sum(a,axis=1))
a = np.array([10, 20, 30, 40, 50, 60])
print(a.reshape(2,3))
sales = np.array([[200, 300, 250],
                  [400, 350, 500]])
print(np.sum(sales,axis=1))
print(np.sum(sales,axis=0))
print(sales[sales>300])
a = np.array([40, 10, 30, 20, 50])
print(np.sort(a))
a = np.array([40, 10, 30, 20, 50])
print(np.sort(a)[::-1])
a = np.array([[40, 10, 30],
              [20, 50, 60],
              [70, 15, 25]])
print(np.sort(a))
print(np.sort(a,axis=0))
a = np.array([40, 10, 30, 20, 50])
print(np.argsort(a)[::-1])

a = np.array([10, 20, 10, 30, 20, 10])

values, counts = np.unique(a, return_counts=True)#return_counts is impo

print(values)
print(counts)
a = np.array([[10, 35, 50],
              [20, 55, 70],
              [40, 25, 60]])
print(a[(a>30) & (a<60)])
a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
b = np.array([10, 20, 30])
print(a+b)
a = np.array([30, 60, 45, 80, 20])
print(np.where(a>50,1,0))
a = np.array([10, 20, 30, 40, 50])
print((a-np.min(a))/(np.max(a)-np.min(a)))