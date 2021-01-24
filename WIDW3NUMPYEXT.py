import numpy as np
#Extension:
#1. Create the following pattern without hardcoding. Use only NumPy functions. #>array([1,1,1,2,2,2,3,3,3,1,2,3,1,2,3])
#2. In two arrays a ( 1,2,3,4,5) and b ( 4,5,6,7,8,9) – remove all repeating items present in array b
#3. Get all items between 5 and 10 from a and b and sum them together

#1. Create the following pattern without hardcoding. Use only NumPy functions. #>array([1,1,1,2,2,2,3,3,3,1,2,3,1,2,3])
ones = np.ones(3)
twos = np.ones(3)+1
threes = np.ones(3)+2
array123 = np.arange(1,4,1)
print(np.concatenate((ones,twos,threes,array123,array123)))
#or....
print(np.hstack((ones, twos, threes,array123,array123)))

#2. In two arrays a ( 1,2,3,4,5) and b ( 4,5,6,7,8,9) – remove all repeating items present in array b
a = np.array([1,2,3,4,5])
b = np.array([4,5,6,7,8,9])
c = np.setdiff1d(b, a)
print(c)

#3. Get all items between 5 and 10 from a and b and sum them together
boolean_array = np.logical_and(a >= 5, a <= 10)
in_range_indices = np.where(boolean_array)[0]
arrayg = a[in_range_indices]

boolean_arrayb = np.logical_and(b >= 5, b <= 10)
in_range_indicesb = np.where(boolean_arrayb)[0]
arrayh = b[in_range_indicesb]

sum1 = np.sum(arrayh)
sum2 = np.sum(arrayg)
sum3 = sum1+sum2

print(sum3)








