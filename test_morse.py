import pytest

import morseovka

def test_Atext():
	assert morseovka.TextToMorse("A") == ".-///"


def test_Amorse():
	assert morseovka.MorseToText(".-") == "a"


def test_veta():
	assert morseovka.TextToMorse("Tohle je věta") == "-/---/..../.-.././/.---/.//...-/./-/.-///"


def test_smichu():
	assert morseovka.TextToMorse("cha cha cha") == "----/.-//----/.-//----/.-///"


def test_smichu_naopak():
	assert morseovka.MorseToText("----/.-//----/.-//----/.-") == "cha cha cha"


def test_spatneho_znaku():
	with pytest.raises(KeyError):
		morseovka.TextToMorse("螭")
