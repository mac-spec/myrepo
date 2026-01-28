import numpy as np
# random functions
a=np.random.randint(10,50,6)
print(a)
a = np.array([10, 20, 30, 40, 50])
ar=np.random.choice(a,3)
print(ar)
a = np.array([5, 10, 15, 20, 25])
ar=np.random.choice(a,2,replace=False)
print(ar)
a=np.random.randint(1,10,(3,3))
print(a)
np.random.seed(0)
a=np.random.randint(1,10,(3,3))
print(a)
np.random.seed(0)
print(np.random.randint(1,20,5))


# Linear algebra basics
a = np.array([[1, 2],
              [3, 4]])

b = np.array([[5, 6],
              [7, 8]])
print(a+b)
a = np.array([[1, 2],
              [3, 4]])

b = np.array([[5, 6],
              [7, 8]])
#print(a@b)
print(np.dot(a,b))
a = np.array([[1, 2],
              [3, 4]])
#print(a.T)
print(np.transpose(a))
a = np.array([[1, 2],
              [3, 4]])
np.linalg.det(a)
a = np.array([[1, 2],
              [3, 4]])
np.linalg.inv(a)
v1 = np.array([3, 4])
v2 = np.array([1, 2])
print(v1+v2)
print(v1@v2)
print(np.linalg.norm(v1))
v1 = np.array([1, 0])
v2 = np.array([0, 1])
dot=(v1@v2)/(np.linalg.norm(v1)*np.linalg.norm(v2))
print(np.degrees(np.arccos(dot)))
print(np.linalg.matrix_rank(v1))
A=np.array([[3,2],
          [2,-1]])
B=np.array([16,3])
print(np.linalg.solve(A,B))
A = np.array([[2, 0],
              [0, 3]])

values, vectors = np.linalg.eig(A)
print("Eigenvalues:", values)
print("Eigenvectors:\n", vectors)
import numpy as np

A = np.array([[2, 0, 0],
              [1, 3, 0],
              [4, 0, 1]])

values, vectors = np.linalg.eig(A)

print("Eigenvalues:", values)
print("Eigenvectors:\n", vectors)
