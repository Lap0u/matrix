from matrix import Matrix
from vector import Vector


def main():
    print("\033[1m\033[92mMy Matrix tests\033[0m")
    print("\033[1m\033[96mEx00\033[0m")
    # Create two matrices
    ns_matrix1 = Matrix([[1, 3], [3, 0], [8, 1]])
    ns_matrix2 = Matrix([[7, 1], [1, 4], [2, 9]])
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

    print("\033[1m\033[96mEx02\033[0m")
    # lerp
    print(
        matrix1.lerp(
            Matrix([[2.0, 1.0], [3.0, 4.0]]),
            Matrix([[20.0, 10.0], [30.0, 40.0]]),
            0.5,
        )
    )
    print(matrix1.lerp(ns_matrix1, ns_matrix2, 0.5))

    print("\033[1m\033[96mEx07\033[0m")
    # Matrix multiplication by vector

    u = Matrix(
        [
            [1.0, 0.0],
            [0.0, 1.0],
        ]
    )

    v = Vector([4.0, 2.0])
    print(u.mul_vec(v))
    u = Matrix(
        [
            [2.0, 0.0],
            [0.0, 2.0],
        ]
    )
    v = Vector([4.0, 2.0])
    print(u.mul_vec(v))
    u = Matrix(
        [
            [2.0, -2.0],
            [-2.0, 2.0],
        ]
    )
    v = Vector([4.0, 2.0])
    print(u.mul_vec(v))

    # Matrix multiplication by matrix

    u = Matrix(
        [
            [1.0, 0.0],
            [0.0, 1.0],
        ]
    )
    v = Matrix(
        [
            [1.0, 0.0],
            [0.0, 1.0],
        ]
    )
    print(u.mul_mat(v))
    u = Matrix(
        [
            [1.0, 0.0],
            [0.0, 1.0],
        ]
    )
    v = Matrix(
        [
            [2.0, 1.0],
            [4.0, 2.0],
        ]
    )
    print(u.mul_mat(v))
    u = Matrix(
        [
            [3.0, -5.0],
            [6.0, 8.0],
        ]
    )
    v = Matrix(
        [
            [2.0, 1.0],
            [4.0, 2.0],
        ]
    )
    print(u.mul_mat(v))

    u = Matrix([[3, 1], [2, 2], [1, 1]])
    v = Matrix([[3, 1], [2, 2]])

    print(u.mul_mat(v))

    print("\033[1m\033[96mEx08\033[0m")
    # Square matrix trace
    u = Matrix(
        [
            [1.0, 0.0],
            [0.0, 1.0],
        ]
    )
    print(u.trace())
    u = Matrix(
        [
            [2.0, -5.0, 0.0],
            [4.0, 3.0, 7.0],
            [-2.0, 3.0, 4.0],
        ]
    )
    print(u.trace())
    u = Matrix(
        [
            [-2.0, -8.0, 4.0],
            [1.0, -23.0, 4.0],
            [0.0, 6.0, 4.0],
        ]
    )
    print(u.trace())

    print("\033[1m\033[96mEx09\033[0m")
    # Transpose of a matrix
    u = Matrix(
        [
            [1.0, 0.0],
            [0.0, 2.0],
        ]
    )
    print(u.transpose())
    u = Matrix(
        [
            [2.0, -5.0, 0.0],
            [4.0, 3.0, 7.0],
            [-2.0, 3.0, 4.0],
        ]
    )
    print(u.transpose())
    u = Matrix(
        [
            [-2.0, -8.0, 4.0],
            [1.0, -23.0, 4.0],
            [0.0, 6.0, 4.0],
        ]
    )
    print(u.transpose())
    u = Matrix([[3, 1, 1], [2, 2, -3], [1, 1, 12], [0, 11, -5]])
    print(u.transpose())

    print("\033[1m\033[96mEx10\033[0m")
    # Row echelon form of a matrix
    # u = Matrix(
    #     [
    #         [1.0, 0.0, 0.0],
    #         [0.0, 1.0, 0.0],
    #         [0.0, 0.0, 1.0],
    #     ]
    # )
    # print(u.row_echelon())
    # u = Matrix(
    #     [
    #         [1.0, 2.0],
    #         [3.0, 4.0],
    #     ]
    # )
    # print(u.row_echelon())
    # u = Matrix(
    #     [
    #         [1.0, 2.0],
    #         [2.0, 4.0],
    #     ]
    # )
    # print(u.row_echelon())
    u = Matrix(
        [
            [8.0, 5.0, -2.0, 4.0, 28.0],
            [4.0, 2.5, 20.0, 4.0, -4.0],
            [8.0, 5.0, 1.0, 4.0, 17.0],
        ]
    )
    import sympy

    print(sympy.Matrix(u.data).rref())

    print(u.row_echelon())
    # u = Matrix(
    #     [
    #         [8.0, 5.0],
    #         [4.0, 2.5],
    #         [8.0, 5.0],
    #     ]
    # )
    # print(u.row_echelon())


if __name__ == "__main__":
    main()
