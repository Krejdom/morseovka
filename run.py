import sys
#print(sys.argv[1])

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

def UpravaZpravy(zprava):
	zprava = zprava.lower()
	zprava = zprava.replace("ě","e")
	zprava = zprava.replace("š", "s")
	zprava = zprava.replace("č", "c")
	zprava = zprava.replace("ř", "r")
	zprava = zprava.replace("ž", "z")
	zprava = zprava.replace("ý", "y")
	zprava = zprava.replace("á", "a")
	zprava = zprava.replace("í", "i")
	zprava = zprava.replace("é", "e")
	zprava = zprava.replace("ů", "u")
	zprava = zprava.replace("ú", "u")
	zprava = zprava.replace("ó", "o")
	return zprava

zprava = UpravaZpravy(input())

slovnik = {'.-' : 'a', '-...' : 'b', '-.-.' : 'c', '-..' : 'd', '.' : 'e', '..-.' : 'f', '--.' : 'g', '....' : 'h', '----' : 'ch', '..' : 'i', '.---' : 'j', '-.-' : 'k', '.-..' : 'l', '--' : 'm', '-.' : 'n', '---' : 'o', '.--.' : 'p', '--.-' : 'q', '.-.': 'r', '...' : 's', '-' : 't', '..-' : 'u', '...-' : 'v', '.--' : 'w', '-..-' : 'x', '-.--' : 'y', '--..' : 'z',  '.-.-.-' : '. ',  '' : ' ', '--..--' : ',', '..--..' : '?'}

slovnik2 = {}
for k, v in slovnik.items():
	slovnik2[v] = k

slovnik2 = {v:k for k, v in slovnik.items()}


# z morseovky na text
def MorseToText(zprava):
	zprava = zprava.replace('///', '/.-.-.-/')
	zprava = zprava.replace('//', '//')
	zprava = zprava.split("/")

	morse = []
	for i,znak in enumerate(zprava):
		pismeno = slovnik.get(znak)
		morse.append(pismeno)
	if morse[-1] == None:
		morse.pop(-1)
	morse = ''.join(morse)

	return morse

# z textu na morseovku
def TextToMorse(zprava):
	text = ""
	for znak in zprava:
		text += slovnik2.get(znak)
		text += "/"
	while text[-3:] != "///":
		text += "/"

	return text

print()
print(JakyPreklad(co))