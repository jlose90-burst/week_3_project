from lib.count_words import *
import pytest 

def test_count_is_correct():
    result = count_words("how many words are in here")
    assert result == 6

def test_empty_string():
    result = count_words("")
    assert result == 0

def test_separated_by_commas():
    result = count_words("test,with,commas")
    assert result == 3

def test_space():
    result = count_words(" ")
    assert result == 0

def test_integer():
    with pytest.raises(TypeError) as e:
        count_words(2)
    error = str(e.value)
    assert error == "must put in a string"

def test_not_string():
    with pytest.raises(TypeError) as e:
        count_words([2,3,4,'hello'])
    error = str(e.value)
    assert error == "must put in a string"


