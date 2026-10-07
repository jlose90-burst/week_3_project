from lib.time_remaining import *
import pytest

def test_200_word_lenght():
    result = time_remaining("")
    assert result == 'you have approximatly 1 minutes estimated left'  