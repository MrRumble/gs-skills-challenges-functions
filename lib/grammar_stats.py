import math

class GrammarStats:
    def __init__(self):
        self.correct_grammar = 0
        self.total = 0

    def check(self, text):
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
        
        if text == '':
            raise Exception("I cannot check an empty text.")
        suitable_punctuation = ['!', '?', '.']
        if all([text[0] == text[0].upper(), text[0].isalpha(), text[-1] in suitable_punctuation]):
            self.correct_grammar += 1
            self.total += 1
            return True
        else:
            self.total += 1
            return False

    def percentage_good(self):
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.

        return int(round(self.correct_grammar / self.total * 100))