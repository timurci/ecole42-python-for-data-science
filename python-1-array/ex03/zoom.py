from load_image import ft_load
from matplotlib import pyplot as plt


def main():
    """Show zoomed version of an image"""
    path = "animal.jpeg"

    try:
        img = ft_load(path)
        print(img)
    except Exception as e:
        print(e)
        return

    try:
        sliced = img[100:600, 100:600, :]
        print("New shape after slicing:", sliced.shape)
        print(sliced)
    except ValueError as e:
        print(e)
        return

    if len(sliced.shape) == 2:
        plt.imshow(sliced, cmap='gray', vmin=0, vmax=255)
    else:
        plt.imshow(sliced)
    plt.show()


if __name__ == "__main__":
    main()
