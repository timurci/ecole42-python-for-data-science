from load_image import ft_load
from matplotlib import pyplot as plt
from numpy import vstack


def main():
    """Show square cut and rotated version of an image"""
    path = "animal.jpeg"

    try:
        img = ft_load(path)
        print(img)
    except Exception as e:
        print(e)
        return

    try:
        sliced = img[100:600, 100:600, 0]

        transposed = sliced[:, 0]

        for i in range(1, sliced.shape[1]):
            transposed = vstack([transposed, sliced[:, i]])

        print("New shape after Transpose:", transposed.shape)
        print(transposed)
    except ValueError as e:
        print(e)
        return

    plt.imshow(transposed, cmap='gray', vmin=0, vmax=255)
    plt.show()


if __name__ == "__main__":
    main()
