class calculator:
    """Calculator class that applies operations on a vector"""
    def __init__(self, vector: list[int | float]):
        """Initialize a vector to perform operation on"""
        if not isinstance(vector, list):
            raise AssertionError("number is not a list")
        for item in vector:
            self._check_type_numeric(item)
        self.vector = vector

    def __add__(self, number) -> None:
        """Add number to all elements in the vector"""
        self._check_type_numeric(number)
        new_list = self.vector
        for i in range(0, len(new_list)):
            new_list[i] += number
        print(new_list)

    def __mul__(self, number) -> None:
        """Multiply number with all elements in the vector"""
        self._check_type_numeric(number)
        new_list = self.vector
        for i in range(0, len(new_list)):
            new_list[i] *= number
        print(new_list)

    def __sub__(self, number) -> None:
        """Subtract number from all elements in the vector"""
        self._check_type_numeric(number)
        new_list = self.vector
        for i in range(0, len(new_list)):
            new_list[i] -= number
        print(new_list)

    def __truediv__(self, number) -> None:
        """Divide all elements in the vector with number"""
        if number == 0:
            raise ZeroDivisionError
        self._check_type_numeric(number)
        new_list = self.vector
        for i in range(0, len(new_list)):
            new_list[i] /= number
        print(new_list)

    @staticmethod
    def _check_type_numeric(number):
        """Raise TypeError in case number is not of type 'int' or 'float'"""
        if not isinstance(number, int) and not isinstance(number, float):
            raise TypeError("number is not of type 'int' or 'float'")
