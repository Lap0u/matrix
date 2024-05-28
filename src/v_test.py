from vector import Vector


def main():
    print("\033[1m\033[92mMy Vector tests\033[0m")
    print("\033[1m\033[96mEx00\033[0m")

    # Create two vectors
    vector1 = Vector([1, 2])
    vector2 = Vector([5, 6])

    # Print the vectors
    vector1.print_vector()
    vector2.print_vector()

    # Add the vectors
    vector3 = vector1.add(vector2)
    vector3.print_vector()

    # Subtract the vectors
    vector4 = vector1.sub(vector2)
    vector4.print_vector()

    # Scale a vector
    vector5 = vector1.scale(2)
    vector5.print_vector()

    print("\033[1m\033[96mEx01\033[0m")

    # Linear combination
    e1 = Vector([1.0, 0.0, 0.0])
    e2 = Vector([0.0, 1.0, 0.0])
    e3 = Vector([0.0, 0.0, 1.0])
    v1 = Vector([1.0, 2.0, 3.0])
    v2 = Vector([0.0, 10.0, -100.0])

    print(
        vector1.linear_combination(
            [e1, e2, e3],
            [10, -2, 0.5],
        )
    )
    print(vector1.linear_combination([v1, v2], [10, -2]))

    print("\033[1m\033[96mEx02\033[0m")

    # lerp
    print(vector1.lerp(0.0, 1.0, 0.0))
    print(vector1.lerp(0.0, 1.0, 1.0))
    print(vector1.lerp(0.0, 1.0, 0.5))
    print(vector1.lerp(21.0, 42.0, 0.3))
    print(vector1.lerp(Vector([2.0, 1.0]), Vector([4.0, 2.0]), 0.3))

    print("\033[1m\033[96mEx03\033[0m")
    # dot product
    print(vector1.dot_product(vector2))
    print(v1.dot_product(v2))


if __name__ == "__main__":
    main()
