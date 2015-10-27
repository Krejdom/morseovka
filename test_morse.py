import pytest

import morseovka

def test_atext():
    assert morseovka.text_to_morse("A") == ".-///"


def test_amorse():
    assert morseovka.morse_to_text(".-") == "a"


def test_veta():
    assert morseovka.text_to_morse("Tohle je věta") == "-/---/..../.-.././/.---/.//...-/./-/.-///"


def test_veta_slovak():
    assert morseovka.text_to_morse("Ľubozvučné slovenské slová sú guľôčka, stĺp, pŕŕ!") == ".-../..-/-.../---/--../...-/..-/-.-./-././/.../.-../---/...-/./-./.../-.-/.//.../.-../---/...-/.-//.../..-//--./..-/.-../---/-.-./-.-/.-/--..--//.../-/.-../.--./--..--//.--./.-./.-./--...-///"


def test_smichu():
    assert morseovka.text_to_morse("cha cha cha") == "----/.-//----/.-//----/.-///"


def test_smichu_naopak():
    assert morseovka.morse_to_text("----/.-//----/.-//----/.-") == "cha cha cha"


def test_spatneho_znaku():
    with pytest.raises(KeyError):
        morseovka.text_to_morse("螭")


def test_na_vice_radku():
    assert morseovka.text_to_morse("Ahoj\nheslo je KORÝŠ\n") == ".-/..../---/.---//\n...././.../.-../---//.---/.//-.-/---/.-./-.--/...///"


def test_vice_radku_naopak():
    assert morseovka.morse_to_text(".-/..../---/.---//\n...././.../.-../---//.---/.//-.-/---/.-./-.--/...///") == ("ahoj \nheslo je korys. ")


def test_cisla_a_dalsi():
    assert morseovka.text_to_morse("42!") == ("....-/..---/--..--///")
