import numpy as np


def matrix_add(x, y):
    # x is added to corresponding element in y
    return x + y


def scal_multi(x, y):
    # x multiply each element in y
    return x * y


def matrix_multi(x, y):
    # calculate the product of matrix using the .dot()
    # Each column == the sum of each row in x is multiply by each  column's in y
    return x.dot(y)


def column_swap(x):
    # To do column swap we get the product of x and [[0, 1, 0], [0, 0, 1], [1, 0, 0]]
    swap_2 = np.array([[0, 1], [1, 0]])
    swap_3 = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
    if len(x) == 2:
        return x.dot(swap_2)
    elif len(x) == 3:
        return x.dot(swap_3)
    else:
        return "The function only work for 2X2 and 3X3 matrices"


def row_swap(x):
    # To the row swap, we get the product of [[0, 1, 0], [0, 0, 1], [1, 0, 0]] and x
    swap_2 = np.array([[0, 1], [1, 0]])
    swap_3 = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
    if len(x) == 2:
        return swap_2.dot(x)
    elif len(x) == 3:
        return swap_3.dot(x)
    else:
        return "The function only work for 2X2 and 3X3 matrices"


def identity_matrix(x):
    # Any matrix multiplied by the identity matrix, either on the left or right side,
    # will be equal to itself.
    id_2 = np.array([[1, 0], [0, 1]])
    id_3 = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    if len(x) == 2:
        return x.dot(id_2)
    elif len(x) == 3:
        return x.dot(id_3)
    else:
        return "The function only work for 2X2 and 3X3 matrices"


def transpose_matrix(x):
    # The transpose of a matrix is computed by swapping the rows
    # and columns of a matrix
    # The transpose operation is denoted by a superscript uppercase “T” (AT)
    return np.transpose(x)


a = np.array([[1, 6], [3, 2]])
b = np.array([[2, 1], [5, 6]])
c = 4
d = np.array([[4, 3, -7], [2, -5, 1], [11, -4, 6]])

# print(len(a[0]))
# print(matrix_add(a, b))
# print(scal_multi(c, a))
# print(matrix_multi(a, b))
# print(column_swap(a))
# print(row_swap(d))
# print(identity_matrix(a))
# print(identity_matrix(d))
print(transpose_matrix(d))
