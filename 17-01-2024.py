import numpy as np
list1 = [2, 4, 6, 8]
array1 = np.array(list1)
print(array1)
array2 = np.zeros(4)
print(array2)
array3 = np.arange(1, 10, 2)  # arrange(start, stop, skip)
print(array3)
array4 = np.random.rand(5)
print(array4)
array5 = np.empty(4)
print(array5)

D1 = np.array([1, 3, 4])
D2 = np.array([[6, 7, 8], [1, 3, 4]])
D3 = np.array([[[3, 3, 5, 6], [6, 7, 8, 3], [7, 8, 5, 2]],
               [[3, 4, 5, 7], [4, 2, 5, 2], [2, 3, 4, 1]]])
print(f"D1 = {D1.ndim} and D2 = {D2.ndim} and D3 = {D3.ndim}")
print(f'{D1} \n\n{D2} \n\n{D3}', '\n')
print(D3.shape, '\n')

A = np.zeros((3, 3, 4))  # creating a 3d array with just zeros and ones
print(A, '\n')
print(np.full((2, 2), 8), '\n')  # fill the whole array with a specific value

B = np.random.rand(2, 3, 4)
print(B, '\n')  # make an array with random integers

# knowing the data type of numpy arrays
print(np.array([6, -7]).dtype)
print(np.array([4.6, 0.009]).dtype)
print(np.array([2+2j, 4+4j]).dtype, '\n')
print(B.astype('int'))
