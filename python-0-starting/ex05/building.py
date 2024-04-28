"""Display string information

string_evaluator: Print the number of characters by type
"""
import sys
import string


def string_evaluator(content: str):
    """Print the number of characters by type in content string"""
    if not isinstance(content, str):
        raise AssertionError("content is not an object of type 'str'")

    print("The text contains", str(len(content)), "characters:")

    uppercase = 0
    lowercase = 0
    punctcase = 0
    spacecase = 0
    digitcase = 0

    for upper in string.ascii_uppercase:
        uppercase += content.count(upper)
    for lower in string.ascii_lowercase:
        lowercase += content.count(lower)
    for punct in string.punctuation:
        punctcase += content.count(punct)
    for space in string.whitespace:
        spacecase += content.count(space)
    for digit in string.digits:
        digitcase += content.count(digit)

    print(uppercase, "upper letters")
    print(lowercase, "lower letters")
    print(punctcase, "punctuation marks")
    print(spacecase, "spaces")
    print(digitcase, "digits")


def main():
    """Print the number of characters by type from the input

    Receive an argument from the command line or from stdin and print the
    number of characters by their type

    Usage: building.py <content>
    """
    try:
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is passed")
    except AssertionError as e:
        print("AssertionError:", e)
        return

    if len(sys.argv) < 2:
        content = None
    else:
        content = sys.argv[1]

    while content is None or len(content) == 0:
        content = input("What is the text to count?\n")

    try:
        string_evaluator(content)
    except AssertionError as e:
        print("AssertionError:", e)


if __name__ == "__main__":
    main()
