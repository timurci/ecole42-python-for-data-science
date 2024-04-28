import sys


def main():
    try:
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")

        try:
            number = int(sys.argv[1])
        except ValueError:
            raise AssertionError("argument is not an integer")

    except AssertionError as e:
        print('AssertionError:', e)
        return

    if number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


if __name__ == "__main__":
    main()
