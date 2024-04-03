from lib.grammar_stats import *
import pytest

def test_one_word_correct_already():
    grammar = GrammarStats()
    result = grammar.check('Hi.')
    assert result == True

def test_one_word_with_punctuation_no_capital():
    grammar = GrammarStats()
    result = grammar.check('hi.')
    assert result == False

def test_one_word_with_capital_no_punctuation():
    grammar = GrammarStats()
    result = grammar.check('Hi')
    assert result == False

def test_full_sentece_with_correct_grammar():
    grammar = GrammarStats()
    result = grammar.check('This sentence has correct grammar.')
    assert result == True

def test_full_sentece_with_wrong_grammar():
    grammar = GrammarStats()
    result = grammar.check('this sentence has incorrect grammar.')
    assert result == False

def test_full_sentece_with_wrong_grammar():
    grammar = GrammarStats()
    result = grammar.check('This sentence does not have a full stop')
    assert result == False

def test_a_sentece_with_no_entry():
    grammar = GrammarStats()
    with pytest.raises(Exception) as e:
        grammar.check('')
    error_message = str(e.value)
    assert error_message == 'I cannot check an empty text.'

def test_a_sentence_not_starting_with_char():
    grammar = GrammarStats()
    result = grammar.check('4This begins with a number.')
    assert result == False

def test_percentage_good_check_one_entry():
    grammar = GrammarStats()
    grammar.check("This is correct grammar.")
    result = grammar.percentage_good()
    assert result == 100

def test_percentage_good_check_one_correct_entry_one_wrong_entry():
    grammar = GrammarStats()
    grammar.check("This is correct grammar.")
    grammar.check("This is wrong")
    result = grammar.percentage_good()
    assert result == 50

def test_percentage_good_check_one_correct_entry_two_wrong_entry():
    grammar = GrammarStats()
    grammar.check("This is correct grammar.")
    grammar.check("This is wrong")
    grammar.check("This is wrong")
    result = grammar.percentage_good()
    assert result == 33

def test_percentage_good_check_two_correct_entry_one_wrong_entry():
    grammar = GrammarStats()
    grammar.check("This is correct grammar.")
    grammar.check("This is correct grammar.")
    grammar.check("This is wrong")
    result = grammar.percentage_good()
    assert result == 67