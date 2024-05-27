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
