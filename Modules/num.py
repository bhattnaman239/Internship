#NUMPY
print("\nNUMPY\n")
import numpy as np
#Creating Arrays
print("\nCREATING ARRAYS\n")
arr = np.array([1, 2, 3, 4, 5])
arr2= np.array([[1, 2, 3], [4, 5, 6]])
arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
arr4= np.array([1, 2, 3, 4, 5], ndmin=4) 
print(arr)
print(type(arr))
print(arr.dtype)
print("1D:", arr.shape)
print("2D:", arr2.shape)
print("3D:", arr3.shape)
print("4D:", arr4.shape)
arr = np.linspace(0, 1, 11)
print("Linspace:", arr)  


#Indexing and Slicing
print("\nINDEXING AND SLICING\n")
arr = np.array([1, 2, 3, 4, 5])
print(arr[0])
print(arr[1:3])
print(arr[::2])
print(arr[::-2])


#Reshaping
print("\nRESHAPING\n")
arr = np.array([1, 2, 3, 4, 5, 6])
print(arr)
print(arr2.reshape(6,1))
# reshaped_arr = arr.reshape(4, -1)  
# print("Reshape:", reshaped_arr) #Error


#Array Operations
print("\nARRAY OPERATIONS\n")
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("SUM:", a + b)  
print("MUL:", a * b)
arr = np.array([1, 2, 3])
print("Scalar mul:", arr * 5)  


#Stastical Functions
print("\nSTATISTICAL FUNCTIONS\n")
arr = np.array([21, -2, 63, 47, 95])
print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Standard Deviation:", np.std(arr))
print("Variance:", np.var(arr))
print("Min:", np.min(arr))
print("Sum:", np.sum(arr))
print("MUL:", np.multiply(arr, 2))


#Random Numbers
print("\nRANDOM NUMBERS\n")
arr = np.random.rand(5)
print("Random:", arr)

rand_arr = np.random.rand(3, 3)  # Random numbers in [0, 1)
print((rand_arr*100))


rand_ints = np.random.randint(1, 100)
print("Random: ",rand_ints)


#Array Concatenation
print("\nARRAY CONCATENATION\n")
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("Concatenate:", np.concatenate((a, b)))
print("Stack:", np.stack((a, b)))
print("HStack:", np.hstack((a, b)))


#Input and Output
print("\nINPUT AND OUTPUT\n")
arr = np.array([1, 2, 3, 4, 5])
np.save("my_array", arr)
load_arr = np.load("my_array.npy")
print("Loaded:", load_arr)
np.savetxt("my_array.csv", arr, delimiter=";")
load_arr = np.loadtxt("my_array.csv")
print("Loaded:", load_arr)