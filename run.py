import sys
from morseovka import MorseToText, TextToMorse

if len(sys.argv) == 1:
    print("usage: morse [M|T]", file=sys.stderr)
    print("Pro překlad Morseovky na text napiš 'M'", file=sys.stderr)
    print("Pro překlad textu do morseovky napiš 'T'", file=sys.stderr)
    exit(1)
else:
    co = sys.argv[1].upper()

def JakyPreklad(co):
    if co == 'M':
        return MorseToText(zprava)
    elif co == 'T':
        return TextToMorse(zprava)
    else:
        pass

zprava = sys.stdin.read()

print(JakyPreklad(co))
