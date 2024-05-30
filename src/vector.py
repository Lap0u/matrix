from dataclasses import dataclass, field


@dataclass
class Vector:
    """A class to represent a vector."""

    data: list[float]
    shape: int = field(init=False)

    def __str__(self):
        return f"Vector: {self.data}, shape:{self.shape}"

    def __post_init__(self):
        self.shape = len(self.data)

    def print_vector(self):
        """Prints the vector."""
        print(self)

    def add(self, other):
        """Adds two vectors."""
        if self.shape != other.shape:
            return None
        return Vector([[self.data[i] + other.data[i] for i in range(self.shape)]])

    def sub(self, other):
        """Subtracts two vectors."""
        if self.shape != other.shape:
            return None
        return Vector([[self.data[i] - other.data[i] for i in range(self.shape)]])

    def scale(self, scalar):
        """Scales the vector by a scalar."""
        return Vector([[self.data[i] * scalar for i in range(self.shape)]])

    def linear_combination(_, vectors: list, scalars: list[int]):
        """Returns the linear combination of vectors."""
        if len(vectors) != len(scalars):
            return None
        return Vector(
            [
                sum([scalars[i] * vectors[i].data[j] for i in range(len(vectors))])
                for j in range(vectors[0].shape)
            ]
        )

    def lerp(self, v1, v2, scalar):
        """Return the linear interpolation of vector or scalar"""

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
            not isinstance(v1, Vector)
            or not isinstance(v2, Vector)
            or v1.shape is not v2.shape
        ):
            return None

        return Vector(
            [lerp_compute(val1, val2, scalar) for val1, val2 in zip(v1.data, v2.data)]
        )

    def dot_product(self, other):
        """Returns the dot product of two vectors."""
        if self.shape != other.shape:
            return None
        return sum([self.data[i] * other.data[i] for i in range(self.shape)])

    def norm_1(self):
        """Returns the L1 norm of the vector.(sum of its values)"""
        return sum([abs(val) for val in self.data])

    def norm(self):
        """Returns the L2 norm of the vector.(square root of the sum of its values squared)"""
        return sum([val**2 for val in self.data]) ** 0.5

    def norm_inf(self):
        """Returns the L∞ norm of the vector.(maximum of its values)"""
        return max([abs(val) for val in self.data])

    def angle_cos(self, other):
        """Returns the cosine of the angle between two vectors
        Cosine rule : c² = a² + b² - 2ab * cos(C)
        """
        if self.shape != other.shape:
            return None
        if self.shape == 0:
            return None
        return self.dot_product(other) / (self.norm() * other.norm())

    def cross_product(self, other):
        """Return the cross product between 2 3D vectors"""
        if self.shape != 3 or other.shape != 3:
            return None
        a = self.data[1] * other.data[2] - self.data[2] * other.data[1]
        b = self.data[2] * other.data[0] - self.data[0] * other.data[2]
        c = self.data[0] * other.data[1] - self.data[1] * other.data[0]
        return Vector([a, b, c])
