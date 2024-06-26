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

    def trace(self):
        """Return the trace of the matrix"""
        if not self.is_square():
            return None
        return sum([self.data[i][i] for i in range(self.shape[0])])

    def transpose(self):
        """Return the transposed matrix"""
        return Matrix(
            [
                [self.data[j][i] for j in range(self.shape[0])]
                for i in range(self.shape[1])
            ]
        )

    def row_swap(self, i, j):
        """Swap two rows of the matrix"""
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def row_scale(self, i, scalar):
        """Scale a row of the matrix"""
        self.data[i] = [self.data[i][j] * scalar for j in range(self.shape[1])]

    def row_add(self, i, j, scalar):
        """Add a multiple of one row to another row"""
        self.data[j] = [
            self.data[j][k] + scalar * self.data[i][k] for k in range(self.shape[1])
        ]

    def row_echelon(self):
        """Return the row echelon form of the matrix
        - Row echelon form of a matrix follows 3 rules
        If a row does not consist entirely of zeros, the first nonzero number in the row is 1
        - All zero rows are at the bottom of the matrix
        - In any two consecutive rows that are not only zeros, the leading 1 in the lower row occurs farther to the right than the leading 1 in the higher row
        """
        offset = 0
        for i in range(min(self.shape[1], self.shape[1])):
            if i - offset >= self.shape[0]:
                break
            if self.data[i - offset][i] == 0:
                for j in range(i + 1 - offset, self.shape[0]):
                    if self.data[j][i] != 0:
                        self.row_swap(i, j)
                        break
            if self.data[i - offset][i] == 0:
                offset += 1
                continue
            self.row_scale(i - offset, 1 / self.data[i - offset][i])
            for j in range(self.shape[0]):
                if j != i - offset:
                    self.row_add(i - offset, j, -self.data[j][i])
        return self.data

    # This solution was provided by ChatGPT
    # def row_echelon2(self):
    #     """Return the reduced row echelon form of the matrix"""
    #     row_count, col_count = self.shape
    #     lead = 0
    #     for r in range(row_count):
    #         if lead >= col_count:
    #             return self.data
    #         i = r
    #         while self.data[i][lead] == 0:  # loop col by col to find a leading 1
    #             i += 1
    #             if i == row_count:
    #                 i = r
    #                 lead += 1
    #                 if lead == col_count:
    #                     return self.data  # Return if no leading 1 is found
    #         self.row_swap(i, r)
    #         self.row_scale(r, 1 / self.data[r][lead])
    #         for i in range(row_count):
    #             if i != r:
    #                 self.row_add(r, i, -self.data[i][lead])
    #         lead += 1
    #     return self.data

    def determinant_sub_2(self, ignored_rows=[], ignored_cols=[]):
        row = [i for i in range(self.shape[0]) if i not in ignored_rows]
        col = [i for i in range(self.shape[1]) if i not in ignored_cols]
        return (
            self.data[row[0]][col[0]] * self.data[row[1]][col[1]]
            - self.data[row[0]][col[1]] * self.data[row[1]][col[0]]
        )

    def determinant_sub_3(self, ignored_rows=[], ignored_cols=[]):
        row = [i for i in range(self.shape[0]) if i not in ignored_rows]
        col = [i for i in range(self.shape[1]) if i not in ignored_cols]
        a = self.data[row[0]][col[0]] * self.determinant_sub_2(
            ignored_rows + [row[0]], ignored_cols + [col[0]]
        )
        b = self.data[row[0]][col[1]] * self.determinant_sub_2(
            ignored_rows + [row[0]], ignored_cols + [col[1]]
        )
        c = self.data[row[0]][col[2]] * self.determinant_sub_2(
            ignored_rows + [row[0]], ignored_cols + [col[2]]
        )
        return a - b + c

    def determinant_sub_4(self):
        a = self.data[0][0] * self.determinant_sub_3(ignored_rows=[0], ignored_cols=[0])
        b = self.data[0][1] * self.determinant_sub_3(ignored_rows=[0], ignored_cols=[1])
        c = self.data[0][2] * self.determinant_sub_3(ignored_rows=[0], ignored_cols=[2])
        d = self.data[0][3] * self.determinant_sub_3(ignored_rows=[0], ignored_cols=[3])
        return a - b + c - d

    def determinant(self):
        if self.shape[0] > 4 or self.shape[1] > 4 or self.is_square() is False:
            return None
        if self.shape[0] == 2:
            return self.determinant_sub_2()
        if self.shape[0] == 3:
            return self.determinant_sub_3()
        return self.determinant_sub_4()

    def minors_sub_3(self):
        return [
            [
                self.determinant_sub_2(ignored_rows=[i], ignored_cols=[j])
                for j in range(self.shape[1])
            ]
            for i in range(self.shape[0])
        ]

    def minors_sub_4(self):
        return [
            [
                self.determinant_sub_3(ignored_rows=[i], ignored_cols=[j])
                for j in range(self.shape[1])
            ]
            for i in range(self.shape[0])
        ]

    def minors_matrix(self):
        if self.shape[0] > 4 or self.shape[1] > 4:
            return None
        if self.shape[0] == 2:
            return self.determinant_sub_2()
        if self.shape[0] == 3:
            return self.minors_sub_3()
        return self.minors_sub_4()

    def cofactor_matrix(self, minors_matrix):
        return [
            [minors_matrix[i][j] * (-1) ** (i + j) for j in range(self.shape[1])]
            for i in range(self.shape[0])
        ]

    def inverse(self):
        if self.is_square() is False:
            return None
        if self.shape[0] > 4:
            print(
                "Matrix is too large to compute the inverse since we cannot compute the determinant"
            )
            return None
        determinant = self.determinant()
        if determinant == 0:
            print("Matrix is singular, inverse does not exist")
            return None
        minors_matrix = self.minors_matrix()
        cofactor_matrix = Matrix(self.cofactor_matrix(minors_matrix))
        adjugate_matrix = cofactor_matrix.transpose()
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                adjugate_matrix.data[i][j] /= determinant
        return adjugate_matrix

    def rank(self):
        """Return the rank of the matrix"""
        echelon = self.row_echelon()
        return sum([1 for row in echelon if row.count(0) != self.shape[1]])
