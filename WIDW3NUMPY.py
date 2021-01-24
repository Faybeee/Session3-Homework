#1. Create a 1D array of numbers from 0 to 9
#2. Create a 3×3 NumPy array of all Boolean value Trues
#3. Extract all odd numbers from array of 1-10
#4. Replace all odd numbers in an array of 1-10 with the value -1
#5. Convert a 1D array to a 2D array with 2 rows
#6. Create two arrays a and b, stack these two arrays vertically use the
#np.dot and np.sum to calculate totals

import numpy as np

#1. Create a 1D array of numbers from 0 to 9
array = np.arange(0,10,1)
print(array)

#2. Create a 3×3 NumPy array of all Boolean value Trues
bool_arr = np.ones(9, dtype=bool)
newArray = bool_arr.reshape(3, 3)
print(newArray)

#3. Extract all odd numbers from array of 1-10
array2 = np.arange(1,11,1)
print(array2[array2 % 2 == 1])

#4. Replace all odd numbers in an array of 1-10 with the value -1
odd_values = (array2 % 2 == 1)
array2[odd_values] = -1
print(array2)

#5. Convert a 1D array to a 2D array with 2 rows
array3 = np.arange(1,11,1)
newArray = array3.reshape(2, 5)
print(newArray)

#6. Create two arrays a and b, stack these two arrays vertically use the
#np.dot and np.sum to calculate totals
a = np.arange(1,10).reshape(3,3)
b = np.arange(2,11).reshape(3,3)
print(np.vstack((a,b)))
c = np.dot(a,b)
print(c)
sum = np.sum(c)
print(sum)
