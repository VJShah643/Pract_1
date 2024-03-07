import numpy as np
# Q-1: Create a 1D NumPy array with elements from 1 to 10.
arr1 = np.arange(1, 11)
print(arr1, '\n')

# Q-2: Create a 2D NumPy array with a shape of (3, 4) containing random integers.
arr2 = np.random.rand(3, 4)
print(arr2, '\n')

# Q-3: Perform element-wise addition, subtraction, multiplication, and division on two arrays.
arr31 = np.array([3, 5, 1, 8])
arr32 = np.array([1, 2, 3, 4])
print(np.add(arr31, arr32), '\n')
print(np.subtract(arr31, arr32), '\n')
print(np.divide(arr31, arr32), '\n')
print(np.multiply(arr31, arr32), '\n')

# Q-5: Create a 2-D array
# 1 3 5
# 7 9 2
# 4 6 8
arr4 = np.array([[1, 3, 5], [7, 9, 2], [4, 6, 8]])
# access the second row of the array
print(arr4[1][0], arr4[1][1], arr4[1][2], '\n')
# access the third column of the array
print(arr4[0][2], arr4[1][2], arr4[2][2], '\n')

# Q-6: Create a 3D array with shape (2, 3, 4) and access a specific element of the array [1,2,1].
arr5 = np.random.rand(2, 3, 4)
print(arr5, '\n')
print(arr5[1][2][1], '\n')

# Q-7: Save one of your created arrays to a text file.
arr6 = np.array([3, 5, 2, 8])
np.savetxt('file.txt', arr6)

# Q-8: Load the saved array back into a NumPy array.
arr6 = np.loadtxt('file.txt')
print(arr6, '\n')

# Q-9: Create a mark sheet for your class.
stud_1 = np.array([45, 66, 90, 97, 95])
stud_2 = np.array([77, 98, 65, 66, 88])
# Find the percentage of scored by each student
marks = np.array([np.mean(stud_1), np.mean(stud_2)])
# Find the student with highest percentage and hence scored position 1.
print("Maximum marks :", np.max(marks))
