from lib.count_words import *
import pytest

# A function called count_words that takes a string 
# as an argument and returns the number of words 
# in that string.


def test_count_string_when_string_length_zero():
    result = count_words("")
    assert result == 0

def test_count_string_when_word_count_one():
    result = count_words('One')
    assert result == 1

def test_count_string_when_word_count_two():
    result = count_words("One Two")
    assert result == 2

def test_count_string_if_words_seperated_by_two_spaces():
    result = count_words("One  Two Three")
    assert result == 3

def test_count_string_if_words_seperated_by_large_spaces():
    result = count_words("      One      Two Three  Four    Five   ")
    assert result == 5

def test_count_valid_string_entered():
    result = count_words(0)
    assert result == "Please enter a valid string."

def test_string_with_only_spaces():
    result = count_words("    ")
    assert result == 0