import numpy as np

# Creating arrays
a = np.array([1, 2, 3, 4, 5])
print("Array a:", a)

b = np.array([[1, 2, 3],
              [4, 5, 6]])
print("\nArray b:\n", b)

# Shape and dtype
print("\nShape of a:", a.shape)
print("Shape of b:", b.shape)
print("Data type of a:", a.dtype)

# Basic operations
print("\na + 10:", a + 10)
print("a * 2:", a * 2)

# Indexing & slicing
print("\nFirst element of a:", a[0])
print("Last element of a:", a[-1])
print("Slice a[1:4]:", a[1:4])

print("\nFirst row of b:", b[0])
print("Second column of b:", b[:, 1])

#  Axis operations
print("\nSum of b (axis=0):", b.sum(axis=0))
print("Sum of b (axis=1):", b.sum(axis=1))

#  Useful functions
print("\nMean of a:", a.mean())
print("Max of a:", a.max())
print("Min of a:", a.min())