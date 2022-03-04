from függvények_tesztelésre import is_ascending, word_concat


def test_is_ascending():
    assert is_ascending(1, 6, 9) == True
    assert is_ascending(3, 2, 1) == False
    assert is_ascending(1, 1, 1) == False

# ez abban rossz, hogy 3 assert van egymás alatt. Inkább írj egy külön függvényt, természetesen az új függvényeknek legyen eltérő nevük

def test_word_concat_first_shorter():
    assert word_concat("alma", "körte") == "almakörte"

def test_word_concat_first_longer():
    assert word_concat("cseresznye", "meggy") == "meggycseresznye"

def test_word_concat_both_equal():
    assert word_concat("cseresznye", "meggy") == "meggycseresznye"




    # assert word_concat("körte", "meggy") == "körtemeggy"
    # assert word_concat("cseresznye", "meggy") == "meggycseresznye"