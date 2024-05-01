def ft_statistics(*args: int | float, **kwargs: any) -> None:
    """Conduct statistical analysis on an indefinite number of arguments"""
    # Removed to match the expected output
    # =======================================
    # if len(args) == 0 or len(kwargs) == 0:
    #   raise ValueError("empty arguments")

    # try:
    #     _validate_numeric_tuple(args)
    # except TypeError:
    #     raise
    # =======================================

    for _, value in kwargs.items():
        try:
            if value == "mean":
                print("mean :", _mean(args))
            elif value == "median":
                print("median :", _median(args))
            elif value == "quartile":
                print("quartile :", _quartile(args))
            elif value == "std":
                print("std :", _std(args))
            elif value == "var":
                print("var :", _var(args))
        except TypeError:
            print("ERROR")
        except ValueError:
            print("ERROR")


def _mean(vector: tuple[int | float, ...]) -> int | float:
    """Return mean of a vector"""
    _validate_numeric_tuple(vector)
    _validate_tuple_content(vector)
    sum = 0
    for item in vector:
        sum += item
    return sum / len(vector)


def _median(vector: tuple[int | float, ...]) -> int | float:
    """Return median of a vector"""
    _validate_numeric_tuple(vector)
    _validate_tuple_content(vector)
    ordered = sorted(vector)
    half_inx = int(len(vector) / 2)
    if len(vector) % 2 == 1:
        return ordered[half_inx]
    else:
        return _mean(tuple(ordered[half_inx:(half_inx + 1)]))


def _quartile(vector: tuple[int | float, ...]) -> tuple[float, float]:
    """Return quartile of a vector"""
    _validate_numeric_tuple(vector)
    _validate_tuple_content(vector)
    ordered = sorted(vector)
    half_inx = int(len(vector) / 2)
    if len(vector) % 2 == 1:
        firstq = _median(tuple(ordered[0:(half_inx + 1)]))
        thirdq = _median(tuple(ordered[half_inx:]))
    else:
        firstq = _median(tuple(ordered[0:(half_inx)]))
        thirdq = _median(tuple(ordered[half_inx:]))
    return (firstq, thirdq)


def _var(vector: tuple[int | float, ...]) -> int | float:
    """Return variance of a vector"""
    _validate_numeric_tuple(vector)
    _validate_tuple_content(vector)
    mean = _mean(vector)
    sqsum = 0
    for item in vector:
        sqsum += (item - mean) ** 2
    return sqsum / len(vector)


def _std(vector: tuple[int | float, ...]) -> int | float:
    """Return standard deviation of a vector"""
    _validate_numeric_tuple(vector)
    _validate_tuple_content(vector)
    return _var(vector) ** 0.5


def _validate_numeric_tuple(vector):
    """Raise TypeError if vector is not a tuple or elements are not numeric"""
    if not isinstance(vector, tuple):
        raise TypeError("object is not of type 'tuple'")
    for item in vector:
        if not isinstance(item, int) and not isinstance(item, float):
            raise TypeError("non-numeric argument found")


def _validate_tuple_content(vector):
    """Raise ValueError if the vector is empty"""
    if len(vector) == 0:
        raise TypeError("vector is empty")
