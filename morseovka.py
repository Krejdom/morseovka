slovnik = {
			'.-' : 'a',
			'-...' : 'b',
			'-.-.' : 'c',
			'-..' : 'd',
			'.' : 'e',
			'..-.' : 'f',
			'--.' : 'g',
			'....' : 'h',
			'----' : 'ch',
			'..' : 'i',
			'.---' : 'j',
			'-.-' : 'k',
			'.-..' : 'l',
			'--' : 'm',
			'-.' : 'n',
			'---' : 'o',
			'.--.' : 'p',
			'--.-' : 'q',
			'.-.': 'r',
			'...' : 's',
			'-' : 't',
			'..-' : 'u',
			'...-' : 'v',
			'.--' : 'w',
			'-..-' : 'x',
			'-.--' : 'y',
			'--..' : 'z', 
			'.-.-.-' : '.', 
			'' : ' ',
			'--..--' : ',',
			'..--..' : '?',
			'--..--' : '!',
			'\n' : '\n',
			'.----' : '1',
			'..---' : '2',
			'...--' : '3',
			'....-' : '4',
			'.....' : '5',
			'-....' : '6',
			'--...' : '7',
			'---..' : '8',
			'----.' : '9',
			'-----' : '0',
			}

slovnik2 = {v:k for k, v in slovnik.items()}
slovnik2["χ"] = "----"

def UpravaZpravy(zprava):
	zprava = zprava.lower()
	zprava = zprava.strip()
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
	zprava = zprava.replace("ch", "χ")
	return zprava

def MorseToText(zprava):
	zprava = zprava.replace('\n', '\n/')
	zprava = zprava.replace('///', '/.-.-.-/')
	zprava = zprava.replace('//', '//')
	zprava = zprava.split("/")

	morse = []
	for i,znak in enumerate(zprava):
		pismeno = slovnik[znak]
		morse.append(pismeno)
	if morse[-1] == None:
		morse.pop(-1)
	morse = ''.join(morse)

	return morse

def TextToMorse(zprava):
	zprava = UpravaZpravy(zprava)
	text = ""
	for znak in zprava:
		if znak == "\n":
			text += "/"
		text += slovnik2[znak]
		if znak != "\n":
			text += "/"
	while text[-3:] != "///":
		text += "/"

	return text
