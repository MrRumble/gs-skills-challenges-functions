from lib.make_snippet import *
# A function called make_snippet that takes a string as 
# an argument 
# and returns the first five words and then a '...' if there are more 
# than that.


def test_make_snippet_string_more_than_5_words():
    result = make_snippet("this is a test string longer than five words.")
    assert result == "this is a test string..."

def test_make_snippet_string_less_than_five_words():
    result = make_snippet("This is a short string.")
    assert result == "This is a short string."