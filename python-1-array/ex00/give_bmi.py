from numpy import array, float64


def give_bmi(height: list[int | float], weight: list[int | float]) -> list:
    """Calculate bmi in meter and kilogram units"""
    if len(height) != len(weight):
        raise AssertionError("uneven lists")

    try:
        height = array(height, dtype=float64)
        weight = array(weight, dtype=float64)
    except ValueError:
        raise AssertionError("incorrect data type")

    return list(weight / (height ** 2))


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Evaluate which bmi values are above the limit"""
    try:
        bmi = array(bmi, dtype=float64)
        limit = int(limit)
    except ValueError:
        raise AssertionError("incorrect data type")

    return list(bmi > limit)
