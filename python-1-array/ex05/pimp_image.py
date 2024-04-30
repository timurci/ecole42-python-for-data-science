from numpy import ndarray


def ft_invert(image) -> ndarray:
    """Invert the color of the image received as a numpy array"""
    try:
        _validate_image(image)
    except AssertionError:
        raise

    image[:, :, 0] = 255 - image[:, :, 0]
    image[:, :, 1] = 255 - image[:, :, 1]
    image[:, :, 2] = 255 - image[:, :, 2]
    return image


def ft_red(image) -> ndarray:
    """Convert the color of the image received to red"""
    try:
        _validate_image(image)
    except AssertionError:
        raise

    image[:, :, 1:] *= 0
    return image


def ft_green(image) -> ndarray:
    """Convert the color of the image received to green"""
    try:
        _validate_image(image)
    except AssertionError:
        raise

    image[:, :, 0:3:2] *= 0
    return image


def ft_blue(image) -> ndarray:
    """Convert the color of the image received to blue"""
    try:
        _validate_image(image)
    except AssertionError:
        raise

    image[:, :, :2] *= 0
    return image


def ft_grey(image) -> ndarray:
    """Convert the image to grayscale"""
    try:
        _validate_image(image)
    except AssertionError:
        raise

    maxed = image.max(axis=2)
    image[:, :, 0] = maxed
    image[:, :, 1] = maxed
    image[:, :, 2] = maxed
    return image


def _validate_image(image):
    """Check if image object is of correct data type and format"""
    if not isinstance(image, ndarray):
        raise AssertionError("the image object is not of type 'ndarray'")
    if not len(image.shape) == 3:
        raise AssertionError("the image is not 3D")
