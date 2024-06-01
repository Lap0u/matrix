from dataclasses import dataclass, field
from vector import Vector


@dataclass
class Matrix:
    """A class to represent a matrix."""

    data: list[list[float]]
    shape: list[int] = field(init=False)

    def __post_init__(self):
        self.shape = [len(self.data), len(self.data[0])]

    def __str__(self):
        return f"Matrix: {self.data}, shape: {self.shape}"

    def is_square(self):
        """Returns True if the matrix is square, False otherwise."""
        return self.shape[0] == self.shape[1]

    def print_matrix(self):
        """Prints the matrix."""
        print(self)

    def add(self, other):
        """Adds two matrices."""
        if self.shape != other.shape:
            return None
        return Matrix(
            [
                [self.data[i][j] + other.data[i][j] for j in range(self.shape[1])]
                for i in range(self.shape[0])
            ]
        )

    def sub(self, other):
        """Subtracts two matrices."""
        if self.shape != other.shape:
            return None
        return Matrix(
            [
                [self.data[i][j] - other.data[i][j] for j in range(self.shape[1])]
                for i in range(self.shape[0])
            ]
        )

    def scale(self, scalar):
        """Scales the matrix by a scalar."""
        return Matrix(
            [
                [self.data[i][j] * scalar for j in range(self.shape[1])]
                for i in range(self.shape[0])
            ]
        )

    def lerp(self, v1, v2, scalar):
        """Return the linear interpolation of matrix or scalar"""

        def lerp_compute(val1, val2, scalar):
            print(val1, val2)
            return val1 + (val2 - val1) * scalar

        if (
            isinstance(v1, float)
            and isinstance(v2, float)
            or isinstance(v1, int)
            and isinstance(v2, int)
        ):
            return lerp_compute(v1, v2, scalar)
        if (
            not isinstance(v1, Matrix)
            or not isinstance(v2, Matrix)
            or v1.shape != v2.shape
        ):
            return None

        return Matrix(
            [
                [
                    lerp_compute(v1.data[i][j], v2.data[i][j], scalar)
                    for j in range(v1.shape[1])
                ]
                for i in range(v1.shape[0])
            ]
        )

    def mul_vec(self, other):
        """Return the multiplication of a matrix by a vector"""
        if self.shape[1] != other.shape:
            return None
        return Vector(
            [
                sum([(other.data[j] * self.data[j][i]) for j in range(other.shape)])
                for i in range(self.shape[1])
            ]
        )

    def mul_mat(self, other):
        """Return the multiplication of a matrix by a matrix"""
        if self.shape[1] != other.shape[0]:
            print("cant")
            return None
        return Matrix(
            [
                [
                    sum(
                        [
                            self.data[i][k] * other.data[k][j]
                            for k in range(self.shape[1])
                        ]
                    )
                    for j in range(other.shape[1])
                ]
                for i in range(self.shape[0])
            ]
        )
