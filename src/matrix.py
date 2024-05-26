from dataclasses import dataclass, field


@dataclass
class Matrix:
    """A class to represent a matrix."""

    data: list[list[float]]
    shape: list[int] = field(init=False)

    def __post_init__(self):
        self.shape = [len(self.data), len(self.data[0])]

    def is_square(self):
        """Returns True if the matrix is square, False otherwise."""
        return self.shape[0] == self.shape[1]

    def print_matrix(self):
        """Prints the matrix."""
        print(self.data)

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
