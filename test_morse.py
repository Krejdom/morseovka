import morseovka

def test_Atext():
	assert morseovka.TextToMorse("A") == ".-///"

def test_Amorse():
	assert morseovka.MorseToText(".-") == "a"

def test_veta():
	assert morseovka.TextToMorse("Tohle je věta") == "-/---/..../.-.././/.---/.//...-/./-/.-///"
