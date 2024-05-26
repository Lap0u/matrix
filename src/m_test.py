from matrix import Matrix


def main():
    # Create two matrices
    matrix1 = Matrix([[1, 2], [3, 4]])
    matrix2 = Matrix([[5, 6], [7, 8]])

    # Print the matrices
    matrix1.print_matrix()
    matrix2.print_matrix()

    # Add the matrices
    matrix3 = matrix1.add(matrix2)
    matrix3.print_matrix()

    # Subtract the matrices
    matrix4 = matrix1.sub(matrix2)
    matrix4.print_matrix()

    # Scale a matrix
    matrix5 = matrix1.scale(2)
    matrix5.print_matrix()


if __name__ == "__main__":
    main()
