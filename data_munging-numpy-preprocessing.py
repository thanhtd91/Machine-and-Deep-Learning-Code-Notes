## Having used Pandas commands to upload and preprocess your data in memory or in smaller batches, you'll have to work on it in order to prepare a suitable data matrix for your supervised and unsupervised learning procedures

## As best practice, divide the task between a phase of your work when your data is still heterogeneous (mix of numerical and symbolic values) and another phase when it is turned into a numeric table of data arranged in rows that represent your examples, and columns that contain the characteristics observed values of your examples, which are your variables.  In doing so, you'll have to wrangle between two key Python packages for scientific analysis, Pandas and NumPy, and their two pivotal data structures, DataFrame and ndarray.  The target data structure is a NumPy ndarry.

## NumPy offers an ndarray object class (n-dimensional array) that has the following attributes: 1. it is memory optimal, 2. allows faster linear algebra computations and element-wise operations, 3. is the data structure that critical libraries such as SciPy and Scikit-learn expect as an input for their functions.  They have some drawbacks such as: 1. they usually store only elements of a single, specific data type that you can define beforehand (there's a way to define complex data and heterogeneous data types, though they could be very difficult to handle for analysis purpose), 2. after they are initialized, their size is fixed.

## Basics of NumPy ndarray objects: since type (and memory space it occupies in terms of bytes) of an array should be defined from the beginning, the array creation procedure can reserve the exact memory space to contain all the data.  The access, modification and computation of the elements of an array are therefore quite fast, though this also consequently implies that the array is fixed and cannot be structurally changed.  It is therefore important to understand that when we are viewing an array, we have called a procedure that allows us to immediately convert the data into something else (but the sourcing array has been unaltered), when we are copying an array, we are creating a new array with a different structure (thus occupying new fresh memory)

## Creating NumPy arrays, more than one way to creating NumPy array: 1. transforming an existing data structure into an array, 2. creating an array from scratch and populating it with default or calculated values, 3. uploading some data form a disk into an array...if you're going to transform an existing data structure, the odds are in favor of you working with a structured list or a Pandas DataFrame

## From list to unidimensional arrays
import numpy as np
list_of_ints = [1,2,3]
Array_1 = np.array(list_of_ints) # transforms a list into a uni-dimensional array
print Array_1
print Array_1[1] # can still use like a normal python list
print type(Array_1) # will see numpy.ndarray
print Array_1.dtype # will see int32
## controlling memory size, can calculate memory space that array is taking up
print Array_1.nbytes
## in order to save memory, you can specify beforehand the type that best suits your array
Array_1 = np.array(list_of_ints, dtype = 'int8')
print Array_1.nbytes
## if an array has a type that you want to change, you can easily create a new array by casting a new specified type:
Array_1b = Array_1.astype('float32')
print Array_1b
print Array_1b.dtype

## Heterogeneous lists, can be a bit more complex
complex_list = [1,2,3] + [1.,2.,3.] + ['a','b','c']
Array_2 = np.array(complex_list[:3]) # at first the input list is just ints
print 'complex_list[:3]', Array_2.dtype
Array_2 = np.array(complex_list[:6]) # now ints and floats
print 'complex_list[:6]', Array_2.dtype
Array_2 = np.array(complex_list) # now ints and floats and strings (all added)
print 'complex_list', Array_2.dtype
# what we see is that float types prevail over int types and strings prevail over everything else, when using lists of different elements be sure and check dtype since later you might find it impossible to operate certain operations on your resulting array and incur an unsupported operand type error
# check to see if NumPy array is of the desired numeric type
print isinstance(Array_2[0], np.number) # checking this will make sure we transformed all the variables into numeric ones

## Lists to multidimensional arrays
a_list_of_lists = [[1,2,3],[4,5,6],[7,8,9]]
Array_2d = np.array(a_list_of_lists) # transform a list into a bidimensional array
print Array_2d
print Array_2d[1,1] # you can call out single values with indices (one for row (axis 0) and one for column dimension (axis 1))

## three dimensional array
a_list_of_lists_of_lists = [[[1,2],[3,4],[5,6]],[[7,8],[9,10],[11,12]]]
Array_3D = np.array(a_list_of_lists_of_lists)
print Array_3D
# to access single elements of a three-dimensional array, you just have to point our a tuple of three indices
print Array_3D[0,2,0] # access 5th element

## Resizing Arrays, you can modify the shape of an existing array by using the .reshape method which accepts as parameter an n-tuple containing the size of the new dimension
# restructuring a NumPy array shape
original_array = np.array([1,2,3,4,5,6,7,8])
Array_a = original_array.reshape(4,2) # reshape to size 4 X 2
Array_b = original_array.reshape(4,2).copy() # same size as Array_a but append .copy() method that copies the array into a new one
Array_c = original_array.reshape(2,2,2) # reshape in three dimensions of size 2 X 2 X 2
original_array[0] = -1 # after such assignment, the first element of original_array is changed in value to -1
print Array_a
print Array_b # Array_b doesn't show the -1 first element change because they don't dynamically mirror the original array
print Array_c
# if it is necessary to change the shape of the original array, then the resize method is favored
original_array.resize(4,2)
print original_array
# can get the same result bu acting on the .shape value by assigning a tuple of values representing the size of the intended dimensions
original_array.shape = (4,2)
print original_array

## Arrays derived from NumPy functions, if you need a vector or matrix characterized by particular numeric series (zeros, ones, ordinal numbers and particular statistical distributions), NumPy functions provide you with quite a large range of choices
# NumPy array of ordinal values (integers), use arange function, which returns integer values in a given interval (usually from zero) and reshapes its results
ordinal_values = np.arange(9).reshape(3,3)
print ordinal_values
# to reverse the order of values, just use slice
ordinal_values_reverse = np.arange(9).reshape(3,3)[::-1]
print ordinal_values_reverse
# if integers are just random
random_ints = np.random.randint(low=1, high=10, size=(3,3)).reshape(3,3)
print random_ints
# some other useful arrays
zeros_array = np.zeros((3,3))
ones_array = np.ones((3,3))
identity_matrix = np.eye(3)
# if the array will be used for a grid search to search for optimal parameters, fractional values in an interval or a logarithmic growth should prove most useful
fractions = np.linspace(start=0, stop=1, num=10)
print fractions
growth = np.logspace(start=0, stop=1, num=10, base=10.0)
print growth
# Instead, statistical distributions such as normal or unifrom may be useful for the initialization of a vector or matrix of coefficients
std_gaussian = np.random.normal(size=(3,3))
print std_gaussian
# if you need to specify a different mean and standard deviation, do the following:
gaussian = np.random.normal(loc=1.0, scale=3.0, size=(3,3))  # the loc parameter stand for the mean and the scale is actually the standard deviation
print gaussian
# another frequent choice for statistical distribution, the uniform distribution (used to initialize a vector)
uniform_dist = np.random.uniform(low=0.0, high=1.0, size=(3,3))
print uniform_dist

## Getting an array directly from a file
istanbul_market = np.loadtxt('Data Sets for Code/istanbul_data_nodates_labels.csv', delimiter=',', dtype=float)
print istanbul_market
# NumPy loadtxt given a filename, delimiter and a dtype will upload the data to an array unless the dtype is wrong.  For instance, if there's a string variable and the required array type is float, you will get a ValueError (if you used the original istanbul dataset)

## Extracting data from Pandas, arrays can be easily extracted from DataFrame objects and they can be transformed into a DataFrame themselves.

import pandas as pd
istanbul_market = pd.read_csv('Data Sets for Code/istanbul_market_data.csv', header=None)
istanbul_market_array = istanbul_market.values
print istanbul_market_array.dtype
print istanbul_market.dtypes # using the .dtypes method on the DataFrame allows you to anticipate the dtype of the resulting array and consquently decide whether to transform or change the type of the variables in the DataFrame object before preceeding

## NumPy fast operation and computations, when arrays need to be manipulated by mathematical operations, you just need to apply the operation on the array with respect to a numerical constant (a scalar) or an array of the exact same shape:
a = np.arange(5).reshape(1,5)
a += 1
print a*a # result here is the operation performed element-wise, that is, every element of the array is operated by either the scaler value or the corresponding element of the other array
# When operating on arrays of different dimensions, it is still possible to obtain element-wise operations without having to restructure the data in case one of the corresponding dimensions is 1.  In fact, in such a case, the dimension of size 1 is stretched until it matches the dimension of the corresponding array.  This conversion is called broadcasting
a = np.arange(5).reshape(1,5) + 1
b = np.arange(5).reshape(5,1) + 1
print a * b
# the preceding code is equivalent to:
a2 = np.array([1,2,3,4,5] * 5).reshape(5,5)
b2 = a2.T
print a2 * b2
# however, it won't require an expansion of memory of the original arrays in order to obtain pair-wise multiplication.
# there exists a wide range of NumPy functions that can operate element-wise on arrays: abs(), sign(), round(), floor(), sqrt(), log() and exp()
# other usual operations that can be operated by NumPy functions are sum() and prod(), which provide the summation and product of the array rows or columns on the basis of the specified axis
print a2
print np.sum(a2, axis=0)
print np.sum(a2, axis=1)
# NumPy operations are much faster than python lists operations
print %timeit -n 1 -r 3 [i+1.0 for i in range(10**6)]
print %timeit -n 1 -r 3 np.arange(10**6) + 1.0

## Matrix operations, for multiplications apart from element-wise calculations using the np.dot() function, you can also apply to your bidimensional arrays matrix calculations such as vector-matrix and matrix-matrix multiplications
M = np.arange(5*5, dtype=float).reshape(5,5)
print M
# create a 5*5 dimensional array of ordinal numbers from 0 to 24 then define a vector of coefficients and an array column stacking the vector and its reverse
coefs = np.array([1., 0.5, 0.5, 0.5, 0.5])
coefs_matrix = np.column_stack((coefs, coefs[::-1]))
print coefs_matrix
# multiply the array using the np.dot function
print np.dot(M,coefs)
# or multiply by the vector of the array
print np.dot(coefs,M)
# or the array by the stacked coefficient vectors (which here is a 5*2 matrix)
print np.dot(M,coefs_matrix)
# NumPy also offers an object class, matrix, which is actually a subclass of ndarray, inheriting all its attributes and methods.  NumPy matrices are exclusively bidimensional (as arrays are actually multidimensional) by default.  When multiplied they apply matrix products, not element-wise ones and they have some special matrix methods

## Slicing and Indexing with NumPy Arrays, indexing allows us to take a view of an ndarray by pointing out either what slice of columns and rows to visualize, or an index
# define a working array
M = np.arange(10*10, dtype=int).reshape(10,10) # 10X10 bidimensional array, we can initially start by slicing it to a single dimensional just like in python [start_index_included:end_index_exclude:steps]
# lets say we want to extract even rows from 2 to 8
print M[2:9:2,:]
# after slicing the rows we can furthermore slice columns by taking only the columns from the index 5
print M[2:9:2,5:]
# possible to use negative index values in order to start counting from the end.
print M[2:9:2,5::-1]
# can create Boolean indexes that point out which rows and columns to select, we can replicate the previous example by using a row_index and col_index variable
row_index = (M[:,0]>=20) & (M[:,0]<=80)
col_index = M[0,:]>=5
print M[row_index,:][:,col_index]
# we cannot contextually use Boolean indexes on both columns and rows in the same square bracket, though we can apply the usual indexing to the other dimension using integer indexes.  Consequently, we have to first operate a second selection on the first, this time focusing on the columns
# if we need a global selection of elements in the array, we can also use a mask of Boolean values:
mask = (M>=20) & (M<=90) & ((M / 10.) % 1 >= 0.5)
print M[mask] # this approach is particularly useful if you need to operate on the partition of the array selected by the mask
# another way to point out which elements need to be selected from your array is by providing a row or column index consisting of integers.  Such indexes may be defined either by a np.where() function that transforms a Boolean condition on an array into indexes. or by simply providing a sequence of integer indexes, where integers may be in a particular order or might even be repeated.  This is called fancy indexing:
row_index = [1,1,2,7]
col_index = [0,2,4,8]
# having defined the indexes of your rows and columns, you have to apply them contextually to select elements whose coordinates are given by the tuple of values of both the indexes
print M[row_index, col_index]
# in this way, the selection will report the following points: (1,0),(1,2),(2,4), and (7,8). Otherwise you just have to first select the rows and then the columns which are separated by square brackets:
print M[row_index,:][:,col_index]
## Remember that slicing and indexing are just views of the data.  If you need to create new data from such views, you have to use the copy method and assign it to another variable.
N = M[2:9:2,5:].copy()
print N

## Stacking NumPy Arrays
# basic array
dataset = np.arange(10*5).reshape(10,5)
# add a single row and a bunch of rows to be concatenated after each other:
single_line = np.arange(1*5).reshape(1,5)
a_few_lines = np.arange(3*5).reshape(3,5)
# first try to add a single line:
np.vstack((dataset,single_line))
# more lines added:
np.vstack((dataset, a_few_lines))
# add the same single line more than once, the tuple can represent the sequential structure of your newly concatenated array:
np.vstack((dataset, single_line, single_line))
# add a new variable to an existing array, use hstack (h for horizontal) instead of vstack (vertical)
# pretend you have to add bias of unit values to original array:
bias = np.ones(10).reshape(10,1)
np.hstack((dataset,bias))
# without reshaping bias (therefore can be any data structure of the same length as the rows of the array), you can add it as a sequence using the column_stack() function, which obtains the same result but with fewer concerns regarding data reshaping
bias = np.ones(10)
np.column_stack((dataset,bias))
## adding rows and columns to two-dimensional arrays is basically all that you need to effectively wrangle your data in data science projects.
# although bidimensional arrays are the norm, you can also operate on a three-dimensional data structure.  Use dstack(), which operate on the third axis
np.dstack((dataset*1,dataset*2,dataset*3)) # here the third dimension offers the original 2D array with a multiplicand, presenting a progressive rate of change (a time or change dimension)
# insertion could be problematic, either of a row or more frequently a column to a specific position into your array.  Insertion requires the recreation of a new array, splitting the original array since arrays are contiguous chunks of memory.  NumPy insert command helps you do so in a fast and hassle-free way
np.insert(dataset, 3, bias, axis=1) # define the array where you wish to insert (dataset), the position (index 3), the sequence you want to insert (in this case the array bias) and the axis along which you would like to operate the insertion (axis 1 is the vertical axis, 0 = horizontal)
# you can insert entire arrays, not just vectors, such as bias, by ensuring that the arrays to be inserted is aligned with the dimension along which we are operating the insertion.
# in order to insert the same array into itself, we have to transpose it as an inserted element
np.insert(dataset, 3, dataset.T, axis=1)
# you can also make insertions on different axes
np.insert(dataset, 3, np.ones(5), axis=0) # original array is split at the specified position along the chosen axis, then the split data is concatenated with the new data to be inserted
