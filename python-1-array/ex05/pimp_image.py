from numpy import array


def ft_invert(array) -> array:
    """Invert the color of the image received as a numpy array"""
    array[:, :, 0] = 255 - array[:, :, 0]
    array[:, :, 1] = 255 - array[:, :, 1]
    array[:, :, 2] = 255 - array[:, :, 2]


def ft_red(array) -> array:
    """Convert the color of the image received to red"""
    array[:, :, 1:] *= 0
    return array


def ft_green(array) -> array:
    """Convert the color of the image received to green"""
    array[:, :, 0:3:2] *= 0
    return array


def ft_blue(array) -> array:
    """Convert the color of the image received to blue"""
    array[:, :, :2] *= 0
    return array


def ft_grey(array) -> array:
    """Convert the image to grayscale"""
    maxed = array.max(axis=2)
    array[:, :, 0] = maxed
    array[:, :, 1] = maxed
    array[:, :, 2] = maxed
    return array
