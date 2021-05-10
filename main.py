import MatrixOperations
import VectorOperations

choice = input("""
This is a Vector and Matrices Calculator. Select from the following:
1) Vector Calculator
2) Matrices Calculator
""")
if choice == "1":
    vector_selection = input("""
Selection Menu:
1) Norm 
2) Unit Vector
3) Scalar Multiplication
4) Addition
5) Subtraction
6) Dot Product
7) Angle
8) Cross Product (Only for 3D vectors)
""")

    if vector_selection == "1":
        size = int(input("Enter the size of the vector:"))
        vector = [int(input("Enter value for the vector: ")) for i in range(size)]
        norm = VectorOperations.norm(vector)
        print("Norm: ", norm)
    if vector_selection == "2":
        size = int(input("Enter the size of the vector:"))
        vector = [int(input("Enter value for vector: ")) for i in range(size)]
        unit_vector = VectorOperations.unit(vector)
        print(unit_vector)
    if vector_selection == "3":
        size = int(input("Enter the size of the vector:"))
        vector = [int(input("Enter Value for Vector: ")) for i in range(size)]
        scalar = float(input("Please input scale factor: "))
        scaled_vector = VectorOperations.scalar_multiply(vector, scalar)
        print(scaled_vector)
    if vector_selection == "4":
        size = int(input("Enter the size of the vectors:"))
        vector = [int(input("Enter value for vector 1: ")) for i in range(size)]
        vector2 = [int(input("Enter value for vector 2: ")) for i in range(size)]
        vector_sum = VectorOperations.add(vector, vector2)
        print(vector_sum)
    if vector_selection == "5":
        size = int(input("Enter the size of the vectors:"))
        vector = [int(input("Enter value for minuend vector: ")) for i in range(size)]
        vector2 = [int(input("Enter values of subtrahend vector: ")) for i in range(size)]
        vector_difference = VectorOperations.subtract(vector, vector2)
        print(vector_difference)
    if vector_selection == "6":
        size = int(input("Enter the size of the vectors:"))
        vector = [int(input("Enter Value for Vector 1: ")) for i in range(size)]
        vector2 = [int(input("Enter Values for Vector 2: ")) for i in range(size)]
        dot_product = VectorOperations.dot(vector, vector2)
        print("Dot Product: ", dot_product)
    if vector_selection == "7":
        size = int(input("Enter the size of the vectors:"))
        vector = [int(input("Enter value for vector 1: ")) for i in range(size)]
        vector2 = [int(input("Enter values for vector 2: ")) for i in range(size)]
        vector_angle = VectorOperations.angle(vector, vector2)
        print("Angle: ", round(vector_angle, 2), " radians")
    if vector_selection == "8":
        vector = [int(input("Enter value for vector 1: ")) for i in range(3)]
        vector2 = [int(input("Enter values for vector 2: ")) for i in range(3)]
        cross = VectorOperations.cross_product(vector, vector2)
        print(cross)
elif choice == "2":
    matrix_selection = input("""
Selection Menu: 
1) Determinant 
2) Transpose 
3) Inverse
4) Scalar Multiplication
5) Trace
6) Addition
7) Subtraction
""")


    if matrix_selection == "1":
        dimensions = int(input("Enter the dimensions of the SQUARE matrix:"))
        matrix = [[int(input("Enter Value: ")) for i in range(dimensions)] for j in range(dimensions)]
        determinant = MatrixOperations.determinant(matrix)
        print("Determinant: ", determinant)
    elif matrix_selection == "2":
        dimensions = int(input("Enter the dimensions of the SQUARE matrix:"))
        matrix = [[int(input("Enter Value: ")) for i in range(dimensions)] for j in range(dimensions)]
        transpose = MatrixOperations.transpose(matrix)
        print(transpose)
    elif matrix_selection == "3":
        dimensions = int(input("Enter the dimensions of the SQUARE matrix:"))
        matrix = [[int(input("Enter Value: ")) for i in range(dimensions)] for j in range(dimensions)]
        inverse = MatrixOperations.inverse(matrix)
        print(inverse)
    elif matrix_selection == "4":
        dimensions = int(input("Enter the dimensions of the SQUARE matrix:"))
        matrix = [[int(input("Enter Value: ")) for i in range(dimensions)] for j in range(dimensions)]
        scalar = float(input("Please input the scalar:"))
        scaled_matrix = MatrixOperations.scalar_multiply(matrix, scalar)
        print(scaled_matrix)
    elif matrix_selection == "5":
        dimensions = int(input("Enter the dimensions of the SQUARE matrix:"))
        matrix = [[int(input("Enter Value: ")) for i in range(dimensions)] for j in range(dimensions)]
        trace = MatrixOperations.trace(matrix)
        print("Trace: ", trace)
    elif matrix_selection == "6":
        dimensions = int(input("Enter the dimensions of the SQUARE matrix:"))
        matrix1 = [[int(input("Enter Values for Matrix 1: ")) for i in range(dimensions)] for j in range(dimensions)]
        matrix2 = [[int(input("Enter Values for Matrix 2: ")) for i in range(dimensions)] for j in range(dimensions)]
        sum_matrix = MatrixOperations.add(matrix1, matrix2)
        print(sum_matrix)
    elif matrix_selection == "7":
        dimensions = int(input("Enter the dimensions of the SQUARE matrix:"))
        matrix1 = [[int(input("Enter Values for Matrix 1: ")) for i in range(dimensions)] for j in range(dimensions)]
        matrix2 = [[int(input("Enter Values for Matrix 2: ")) for i in range(dimensions)] for j in range(dimensions)]
        diff_matrix = MatrixOperations.sub(matrix1, matrix2)
        print(diff_matrix)
