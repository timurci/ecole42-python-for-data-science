from PIL import Image
from numpy import array, ndarray


def ft_load(path: str) -> ndarray:
    """Load an image from path"""
    if not isinstance(path, str):
        raise AssertionError("path is not an object of type 'str'")

    try:
        img = Image.open(path)
    except FileNotFoundError:
        raise
    except Image.UnidentifiedImageError:
        raise
    except OSError:  # If the file cannot be opened
        raise

    width, height = img.size

    img_array = array(img.getdata())
    img_array = img_array.reshape((height, width, img_array.shape[1]))

    print("The shape of image is:", img_array.shape)

    return img_array
