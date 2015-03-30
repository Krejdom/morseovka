import morseovka

def test_Atext():
	assert morseovka.TextToMorse("A") == ".-///"

def test_Amorse():
	assert morseovka.MorseToText(".-") == "a"