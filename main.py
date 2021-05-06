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
    size = int(input("Enter the size of the vector:"))
    vector = [int(input("Enter Value for Vector 1: ")) for i in range(size)]

    if vector_selection == "1":
        norm = VectorOperations.norm(vector)
        print("Norm: ", norm)
    if vector_selection == "2":
        unit_vector = VectorOperations.unit(vector)
        print(unit_vector)
    if vector_selection == "3":
        scalar = float(input("Please input scale factor: "))
        scaled_vector = VectorOperations.scalar_multiply(vector, scalar)
        print(scaled_vector)
    if vector_selection == "4":
        vector2 = [int(input("Enter Value for Vector 2: ")) for i in range(size)]
        vector_sum = VectorOperations.add(vector, vector2)
        print(vector_sum)
    if vector_selection == "5":
        vector2 = [int(input("Enter Values of Subtrahend Vector: ")) for i in range(size)]
        vector_difference = VectorOperations.subtract(vector, vector2)
        print(vector_difference)
    if vector_selection == "6":
        vector2 = [int(input("Enter Values for Vector 2: ")) for i in range(size)]
        dot_product = VectorOperations.dot(vector, vector2)
        print("Dot Product: ", dot_product)
    if vector_selection == "7":
        vector2 = [int(input("Enter Values for Vector 2: ")) for i in range(size)]
        vector_angle = VectorOperations.angle(vector, vector2)
        print("Angle: ", round(vector_angle, 2), " radians")
    if vector_selection == "8":
        vector2 = [int(input("Enter Values for Vector 2: ")) for i in range(size)]
        cross = VectorOperations.cross_product(vector, vector2)
        print(cross)
elif choice == "2":
    matrix_selection = input("""
Selection Menu: 
1) Determinant 
2) Transpose 
3) Inverse
4) Scalar Multiplication
""")
    dimensions = int(input("Enter the dimensions of the SQUARE matrix:"))
    matrix = [[int(input("Enter Value: ")) for i in range(dimensions)] for j in range(dimensions)]

    if matrix_selection == "1":
        determinant = MatrixOperations.determinant(matrix)
        print("Determinant: ", determinant)
    elif matrix_selection == "2":
        transpose = MatrixOperations.transpose(matrix)
        print(transpose)
    elif matrix_selection == "3":
        inverse = MatrixOperations.inverse(matrix)
        print(inverse)
    elif matrix_selection == "4":
        scalar = float(input("Please input the scalar:"))
        scaled_matrix = MatrixOperations.scalar_multiply(matrix, scalar)
        print(scaled_matrix)
