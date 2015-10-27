dictionary = {
    '.-': 'a',
    '-...': 'b',
    '-.-.': 'c',
    '-..': 'd',
    '.': 'e',
    '..-.': 'f',
    '--.': 'g',
    '....': 'h',
    '----': 'ch',
    '..': 'i',
    '.---': 'j',
    '-.-': 'k',
    '.-..': 'l',
    '--': 'm',
    '-.': 'n',
    '---': 'o',
    '.--.': 'p',
    '--.-': 'q',
    '.-.': 'r',
    '...': 's',
    '-': 't',
    '..-': 'u',
    '...-': 'v',
    '.--': 'w',
    '-..-': 'x',
    '-.--': 'y',
    '--..': 'z', 
    '.-.-.-': '.', 
    '': ' ',
    '--..--': ',',
    '..--..': '?',
    '--...-': '!',
    '\n': '\n',
    '.----': '1',
    '..---': '2',
    '...--': '3',
    '....-': '4',
    '.....': '5',
    '-....': '6',
    '--...': '7',
    '---..': '8',
    '----.': '9',
    '-----': '0',
}

dictionary2 = {v:k for k, v in dictionary.items()}
dictionary2["χ"] = "----"

def message_modification(message):
    message = message.lower()
    message = message.strip()
    message = message.replace("ě","e")
    message = message.replace("š", "s")
    message = message.replace("č", "c")
    message = message.replace("ř", "r")
    message = message.replace("ž", "z")
    message = message.replace("ý", "y")
    message = message.replace("á", "a")
    message = message.replace("í", "i")
    message = message.replace("é", "e")
    message = message.replace("ů", "u")
    message = message.replace("ú", "u")
    message = message.replace("ó", "o")
    message = message.replace("ch", "χ")
    message = message.replace("ď", "d")
    message = message.replace("ť", "t")
    message = message.replace("ň", "n")
    message = message.replace("ľ", "l")
    message = message.replace("ä", "e")
    message = message.replace("ô", "o")
    message = message.replace("ŕ", "r")
    message = message.replace("ĺ", "l")

    return message


def morse_to_text(message):
    message = message.replace('\n', '\n/')
    message = message.replace('///', '/.-.-.-/')
    message = message.replace('//', '//')
    message = message.split("/")

    morse = []
    for i,symbol in enumerate(message):
        letter = dictionary[symbol]
        morse.append(letter)
    if morse[-1] == None:
        morse.pop(-1)
    morse = ''.join(morse)

    return morse


def text_to_morse(message):
    message = message_modification(message)
    text = ""
    for symbol in message:
        if symbol == "\n":
            text += "/"
        text += dictionary2[symbol]
        if symbol != "\n":
            text += "/"
    while text[-3:] != "///":
        text += "/"

    return text
