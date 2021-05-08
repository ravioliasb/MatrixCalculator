def cofactor(matrix, omit_row, omit_column):
    row = len(matrix)
    column = len(matrix[0])
    return [[matrix[row][column] for column in range(column) if column != omit_column]
            for row in range(row) if row != omit_row]


def cofactor_determinant(matrix, omit_row, omit_column):
    matrix = cofactor(matrix, omit_row, omit_column)
    return determinant(matrix)


def determinant(matrix):
    dimensions = len(matrix)
    if dimensions == 2:
        det = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
        return det
    else:
        det = 0
        for i in range(dimensions):
            constant = matrix[0][i]
            if i % 2 == 1:
                constant = constant * -1
            det += constant * cofactor_determinant(matrix, 0, i)
    return det


def transpose(matrix):
    row = len(matrix)
    column = len(matrix[0])
    transpose_matrix = [[matrix[row][column] for row in range(row)] for column in range(column)]
    return transpose_matrix


def inverse(matrix):
    if determinant(matrix) != 0:
        dimensions = len(matrix)
        det = determinant(matrix)
        cofactor_matrix = []
        for i in range(dimensions):
            cofactor_row = []
            for j in range(dimensions):
                constant = -1 if (i % 2) ^ (j % 2) else 1
                cofactor_row.append(constant * cofactor_determinant(matrix, i, j))
            cofactor_matrix.append(cofactor_row)

        comatrix = transpose(cofactor"_matrix)
        inverse_matrix = [[component / det for component in row] for row in comatrix]
        return inverse_matrix
    else:
        print("This matrix does not have an inverse")


def scalar_multiply(matrix, scalar):
    scaled_matrix = [[component * scalar for component in row] for row in matrix]
    return scaled_matrix


def trace(matrix):
    trace_value = 0
    for i in range(len(matrix[0])):
        trace_value += matrix[i][i]
    return trace_value
"""
Jon was here
"""
def hello():
    print('hello')