from lib.diaryentry import *
import pytest

def test_diary_entry_formt():
    diary_entry = DiaryEntry('Diary Entry', 'Contents of the entry.')
    result = diary_entry.format()
    assert result == 'Diary Entry: Contents of the entry.'

def test_diary_count_words():
    diary_entry = DiaryEntry('Entry', 'count the words in this.')
    result = diary_entry.count_words()
    assert result == 5

def test_reading_time_wpm_entry_is_int():
    diary_entry = DiaryEntry('Entry', 'How long does it take to read this?')
    with pytest.raises(Exception) as e:
        diary_entry.reading_time('a string')
    error_message = str(e.value)
    assert error_message == 'Please enter an integer'

def test_reading_time():
    diary_entry = DiaryEntry('Entry', 'How long does it take to read this?')
    result = diary_entry.reading_time(1)
    assert result == 8

def test_reading_time_is_not_float():
    diary_entry = DiaryEntry('Entry', 'How long does it take')
    result = diary_entry.reading_time(2)
    assert result == 3

def test_reading_chunk_wpm_and_minutes_are_ints():
    diary_entry = DiaryEntry('Entry', 'This is the contents')
    with pytest.raises(Exception) as e:
        diary_entry.reading_chunk('string', 0.5)
    error_message = str(e.value)
    assert error_message == 'reading_chunk only accepts ints as parameters'

def test_reading_chunk_wpm_and_minutes_are_ints():
    diary_entry = DiaryEntry('Entry', 'This is the contents')
    with pytest.raises(Exception) as e:
        diary_entry.reading_chunk('', 0)
    error_message = str(e.value)
    assert error_message == 'reading_chunk only accepts ints as parameters'

def test_reading_chunk_returns_correct_string():
    diary_entry = DiaryEntry('Entry', 'This is the contents')
    result = diary_entry.reading_chunk(1, 3)
    assert result == 'This is the'


def test_reading_chunk_returns_correct_string():
    diary_entry = DiaryEntry('Entry', 'This is the contents how much to read here')
    result = diary_entry.reading_chunk(2, 3)
    assert result == 'This is the contents how much'

def test_reading_chunk_returns_next_chunk():
    diary_entry = DiaryEntry('Entry', 'This is the contents to slice into chunks to read')
    diary_entry.reading_chunk(1, 3)
    result = diary_entry.reading_chunk(1, 3)
    assert result == 'contents to slice'

def test_reading_chunk_returns_next_chunk():
    diary_entry = DiaryEntry('Entry', 'This is the contents to slice into chunks to read')
    diary_entry.reading_chunk(1, 3)
    result = diary_entry.reading_chunk(2, 2)
    assert result == 'contents to slice into'

def test_reading_chunk_returns_to_the_beggining():
    diary_entry = DiaryEntry('Entry', 'This is the contents to slice into chunks to read')
    diary_entry.reading_chunk(1, 3)
    diary_entry.reading_chunk(2, 2)
    result = diary_entry.reading_chunk(1, 4)
    assert result == 'This is the contents'