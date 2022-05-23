from math import sqrt, acos, degrees


def magnitude_of_vector(x, y):
    v = abs(sqrt(x ** 2 + y ** 2))
    return "{:.2f}".format(v)


def vector_add_sub(x: list, y: list):
    z = []
    for i in range(len(x)):
        z.append(x[i] + y[i])
    return z


def vector_scal_mult(x, y: list):
    z = []
    for i in range(len(y)):
        z.append(x * y[i])
    return z


def vector_dot_products(x: list, y: list):
    z = 0
    for i in range(len(x)):
        z += (x[i] * y[i])
    return z


def angle_btw_two_vector(x: list, y: list):
    x2 = 0
    for i in x:
        x2 += abs(i ** 2)

    y2 = 0
    for i in y:
        y2 += abs(i ** 2)

    z = vector_dot_products(x, y)
    θ = acos(z / (sqrt(x2) * sqrt(y2)))
    θ_degree = degrees(θ)
    return "{:.2f}".format(θ_degree)


a = [-17, 22]
b = [0, 32]
c = 5
e = [3, 2, -3]
f = [0, -3, -6]

# print(vector_add_sub(a, b))
# print(magnitude_of_vector(10.6, 36.4))
# print(vector_scal_mult(c, a))
# print(vector_dot_products(a, b))
# print(angle_btw_two_vector(a, b))
