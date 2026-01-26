import numpy as np
#1-D array
a=np.array([1,2,3,4,5])
print("Array:",a)
print(a[0])
print(a[4])
a[2]=6
print(a)
#loop
for i in a:
    print(i)

#properties
print("Dimension:", a.ndim)
print ("Shape", a.shape)
print ("Data Type", a.dtype)


 #2-D Array
b=np.array([[1,2,3],[4,5,6]])
print("\n2D Array:\n", b)
print(b[0,0])
print(b[1,2])


#print row& column
print(b[0])
print(b[:,1])#: ---> all
print(b[1,:])

#special array
print("\nZeros:\n", np.zeros((2,3)))
print("Ones:\n", np.ones((3,3)))
print("Identity:\n", np.eye(3))


#slicing
# for 1D
# print("Slice:",a[1:4])
print(a[1:3])
print(a[:2])
print(a[2:])
print(a[::2])

#for 2-D
print(b[0:2,1:3])
#change slice values
b[:,1]=99
print(b)
#copy vs view
c=b[0:2,0:2]
c[0,0]=500
print(b) # this changes the original too
#correct way:
c=b[0:2,0:2].copy()

print("Mean:",a.mean())
print("max value:",a.max())
print("min value:",a.min())

"""Excersice:
   x=np.array([[10,20,30],[40,50,60],[70,80,90]])
   1. extract middle row
   2. extract last column
   3. extract 2x2 top-left matrix
   """
x=np.array([[10,20,30],[40,50,60],[70,80,90]])
print(x[2,:])
print(x[1,:])
print(x[:,2]) 
