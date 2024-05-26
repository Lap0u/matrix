from dataclasses import dataclass, field


@dataclass
class Vector:
    """A class to represent a vector."""

    data: list[float]
    shape: int = field(init=False)

    def __post_init__(self):
        self.shape = [len(self.data), len(self.data[0])]

    def print_vector(self):
        """Prints the vector."""
        print(self.data)

    def add(self, other):
        """Adds two vectors."""
        if self.shape != other.shape:
            return None
        return Vector([[self.data[i] + other.data[i] for i in range(self.shape[0])]])

    def sub(self, other):
        """Subtracts two vectors."""
        if self.shape != other.shape:
            return None
        return Vector([[self.data[i] - other.data[i] for i in range(self.shape[0])]])

    def scale(self, scalar):
        """Scales the vector by a scalar."""
        return Vector([[self.data[i] * scalar for i in range(self.shape[0])]])

    def linear_combination(vectors: list, scalars: list[int]):
        """Returns the linear combination of vectors."""
        if len(vectors) != len(scalars):
            return None
        return Vector(
            [
                sum([scalars[i] * vectors[i].data[j] for i in range(len(vectors))])
                for j in range(vectors[0].shape[0])
            ]
        )
