import numpy as np
# when we are using .dtype with array the it shows the datatype of the perticular array. 
arr1 = np.array([1,2,3,4])
print(arr1)
print(arr1.dtype)
arr2 = np.array(['A','B','C'])
print(arr2)
print(arr2.dtype)
arr3 = np.array([1.23,2,4,.3,0.004])
print(arr3)
print(arr3.dtype)


#--------------------------------------------------

# TypeCasting in NumPy
# Typecastiong : To change one data type to another data type is called Typecasting.
arr1 = np.array([1,2,3,4] , dtype =float)
print(arr1)
print(arr1.dtype)
arr3 = np.array([1.23,2,4,.3,0.004], dtype =int)
print(arr3)
print(arr3.dtype)