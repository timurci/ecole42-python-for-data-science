class calculator:
    """Calculator for dot product or element-wise add/sub operations"""
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Apply dot product on vectors V1 and V2

        Vectors are expected to be the same size without error handling
        """
        calculator._check_type_numeric_list(V1)
        calculator._check_type_numeric_list(V2)
        new_list = V1.copy()
        for i in range(0, len(new_list)):
            new_list[i] *= V2[i]
        sum = 0
        for value in new_list:
            sum += value
        print(sum)

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Apply element-wise addition on vectors V1 and V2

        Vectors are expected to be the same size without error handling
        """
        calculator._check_type_numeric_list(V1)
        calculator._check_type_numeric_list(V2)
        new_list = V1.copy()
        for i in range(0, len(new_list)):
            new_list[i] += V2[i]
        print(new_list)

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Apply element-wise subtraction on vectors V1 and V2

        Vectors are expected to be the same size without error handling
        """
        calculator._check_type_numeric_list(V1)
        calculator._check_type_numeric_list(V2)
        new_list = V1.copy()
        for i in range(0, len(new_list)):
            new_list[i] -= V2[i]
        print(new_list)

    @staticmethod
    def _check_type_numeric_list(vector):
        """Raise TypeError if vector is not a list of 'int' or 'float's"""
        if not isinstance(vector, list):
            raise TypeError("vector is not of type 'list'")

        for item in vector:
            if not isinstance(item, int) and not isinstance(item, float):
                raise TypeError("list has objects other than 'int' or 'float'")
