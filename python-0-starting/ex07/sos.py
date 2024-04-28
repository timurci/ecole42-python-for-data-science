import sys


def main():
    """Print a message in morse code"""

    MORSE = {
        ' ': '/',
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
    }

    try:
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")

        message = sys.argv[1].upper()
        code = []

        for letter in message:
            if letter in MORSE:
                code.append(MORSE[letter])
            else:
                raise AssertionError("the arguments are bad")

    except AssertionError as e:
        print("AssertionError:", e)
        return

    print(" ".join(code))


if __name__ == '__main__':
    main()
