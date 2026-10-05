from lib.make_snippet import *
import pytest

def test_snippet_over_5():
    result = make_snippet("testing whether this actually works at all")
    assert result == "testing whether this actually works ..."

def test_snippet_under_5():
    result = make_snippet("testing whether this works")
    assert result == "testing whether this works"

def test_snippet_exactly_5():
    result = make_snippet("test whether this actually works")
    assert result == "test whether this actually works"

#****************************
#these are tests i have added after watching the video

def test_empty_string():
    result = make_snippet("")
    assert result == ""
