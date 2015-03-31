import sys

from morseovka import morse_to_text, text_to_morse

if len(sys.argv) == 1:
    print("usage: morse [M|T]", file=sys.stderr)
    print("For Morse to text translation type 'M'", file=sys.stderr)
    print("For text to Morse translation type 'T'", file=sys.stderr)
    exit(1)
else:
    argument = sys.argv[1].upper()

def which_translation(argument):
    if argument == 'M':
        return morse_to_text(message)
    elif argument == 'T':
        return text_to_morse(message)
    else:
        pass

message = sys.stdin.read()

print(which_translation(argument))
