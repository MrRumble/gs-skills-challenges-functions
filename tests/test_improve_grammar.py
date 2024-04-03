from lib.improve_grammar import *
import pytest

def test_one_word_correct_already():
    result = is_grammar_correct('Hi.')
    assert result == True

def test_one_word_with_punctuation_no_capital():
    result = is_grammar_correct('hi.')
    assert result == False

def test_one_word_with_capital_no_punctuation():
    result = is_grammar_correct('Hi')
    assert result == False

def test_full_sentece_with_correct_grammar():
    result = is_grammar_correct('This sentence has correct grammar.')
    assert result == True

def test_full_sentece_with_wrong_grammar():
    result = is_grammar_correct('this sentence has incorrect grammar.')
    assert result == False

def test_full_sentece_with_wrong_grammar():
    result = is_grammar_correct('This sentence does not have a full stop')
    assert result == False

def test_a_sentece_with_no_entry():
    with pytest.raises(Exception) as e:
        is_grammar_correct('')
    error_message = str(e.value)
    assert error_message == 'I cannot check an empty text.'

def test_a_sentence_not_starting_with_char():
    result = is_grammar_correct('4This begins with a number.')
    assert result == False