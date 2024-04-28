import sys
from ft_filter import filter as ft


def main():
    """Receive a string and a number and print words longer than the number"""
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")
        content = sys.argv[1].split()
        try:
            number = int(sys.argv[2])
        except ValueError:
            raise AssertionError("the arguments are bad")
    except AssertionError as e:
        print("AssertionError:", e)
        return

    longs = ft(lambda x: len(x) > number, content)
    print(longs)


if __name__ == '__main__':
    main()
