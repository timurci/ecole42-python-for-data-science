def slice_me(family: list, start: int, end: int) -> list:
    """Slice the list family based on start and end (exclusive) indices

    Family should be a list of lists of equal lengths
    """
    if not isinstance(family, list) or \
        not isinstance(start, int) or \
            not isinstance(end, int):
        raise AssertionError("incorrect data type")

    new_family = family[start:end]

    try:
        old_shape = _get2Dshape(family)
        new_shape = _get2Dshape(new_family)
    except AssertionError:
        raise

    print("My shape is :", old_shape)
    print("My new shape is :", new_shape)

    return new_family


def _get2Dshape(family: list) -> tuple[int, int]:
    """Find the shape of nested family list in 2D"""
    if len(family) == 0:
        return (0, 0)

    length0 = len(family[0])

    for item in family:
        if len(item) != length0:
            raise AssertionError("uneven list sizes in family")

    return (len(family), length0)
