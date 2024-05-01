def square(x: int | float) -> int | float:
    """Return square of x"""
    _validate_numeric(x)
    return x ** 2


def pow(x: int | float) -> int | float:
    """Return x power of x"""
    _validate_numeric(x)
    return x ** x


def outer(x: int | float, function) -> object:
    """Return object calling a function by the number of its repeated calls"""
    _validate_numeric(x)
    count = 0

    def inner() -> float:
        """Recursively call `function` `count` times"""
        nonlocal count
        result = x
        for i in range(0, count):
            result = function(result)
        count += 1
        return function(result)
    return inner


def _validate_numeric(number):
    """Throw TypeError if number is not 'int' and 'float'"""
    if not isinstance(number, int) and not isinstance(number, float):
        raise TypeError("argument is not numeric")
