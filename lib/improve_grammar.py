'''
As a user
So that I can improve my grammar
I want to verify that a text starts with 
a capital letter and ends
with a suitable sentence-ending punctuation mark.

'''
def is_grammar_correct(text):
    if text == '':
        raise Exception("I cannot check an empty text.")
    suitable_punctuation = ['!', '?', '.']
    if all([text[0] == text[0].upper(), text[0].isalpha(), text[-1] in suitable_punctuation]):
        return True
    else:
        return False