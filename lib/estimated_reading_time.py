'''
The signature of a function includes:

The name of the function.
What parameters it takes, their names and data types.
What it returns and the data type of that value.
Any other side effects it might have.
'''

'''
As a user
So that I can manage my time
I want to see an estimate of reading time for a text, 
assuming that I can read 200 words a minute.

Parameters:
    input: text: in the form of a string
    output: float: representing an estimated reading time
'''

def estimated_reading_time(text):
    if text == '':
        raise Exception("Cant estimate a time for an empty string")
    
    words = text.split()
    word_count = len(words)
    return word_count / 200
