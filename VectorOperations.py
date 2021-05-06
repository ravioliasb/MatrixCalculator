import math


def norm(vector):
    sum_squares = 0
    for component in vector:
        sum_squares += component * component
    norm_value = math.sqrt(sum_squares)
    return norm_value


def unit(vector):
    length = norm(vector)
    unit_vector = [component / length for component in vector]
    return unit_vector


def scalar_multiply(vector, scalar):
    scaled_vector = [component * scalar for component in vector]
    return scaled_vector


def add(vector, vector2):
    sum_vector = [i + j for i, j in zip(vector, vector2)]
    return sum_vector


def subtract(vector, vector2):
    difference_vector = [i - j for i, j in zip(vector, vector2)]
    return difference_vector


def dot(vector, vector2):
    dot_product = 0
    for i, j in zip(vector, vector2):
        dot_product += i*j
    return dot_product


def angle(vector, vector2):
    norm1 = norm(vector)
    norm2 = norm(vector2)
    dot_product = dot(vector, vector2)
    vector_angle = math.acos(dot_product / (norm1 * norm2))
    return vector_angle


def cross_product(vector, vector2):
    det1 = (vector[1] * vector2[2]) - (vector2[1] * vector[2])
    det2 = (vector[0] * vector2[2]) - (vector2[0] * vector[2])
    det3 = (vector[0] * vector2[1]) - (vector2[0] * vector2[1])
    cross = "(" + str(det1) + ")i + (" + str(-det2) + ")j + (" + str(det3) + ")k"
    return cross
