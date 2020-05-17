class ComplexNumber:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return complex(self.a, self.b) + complex(other.a, other.b)

    def __mul__(self, other):
        return complex(self.a, self.b) * complex(other.a, other.b)

    def __truediv__(self, other):
        return complex(self.a, self.b) / complex(other.a, other.b)

    def __sub__(self, other):
        return complex(self.a, self.b) - complex(other.a, other.b)

