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
			'.-.-.-' : '. ', 
			'' : ' ',
			'--..--' : ',',
			'..--..' : '?'
			}

slovnik2 = {v:k for k, v in slovnik.items()}
slovnik2["χ"] = "----"

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
	zprava = zprava.replace("ch", "χ")
	return zprava

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

def TextToMorse(zprava):
	zprava = UpravaZpravy(zprava)
	text = ""
	for znak in zprava:
		text += slovnik2.get(znak)
		text += "/"
	while text[-3:] != "///":
		text += "/"

	return text
