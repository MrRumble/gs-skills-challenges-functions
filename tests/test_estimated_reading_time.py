from lib.estimated_reading_time import *
import pytest

def test_empty_text_returns_error():
    with pytest.raises(Exception) as e:
        estimated_reading_time('')
    error_message = str(e.value)
    assert error_message == "Cant estimate a time for an empty string"
#RAISE AN ERROR PLUS REDO EVERYTHING WITH FLOAT RETURN
    
def test_text_with_200_words():
    long_text = " ".join(['RUMBLE' for x in range(200)])
    result = estimated_reading_time(long_text)
    assert result == 1.0

def test_text_with_1000_words():
    long_text = " ".join(['RUMBLE' for x in range(1000)])
    result = estimated_reading_time(long_text)
    assert result == 5.0

def test_text_with_not_many_words():
    result= estimated_reading_time('X')
    assert result == 0.005




