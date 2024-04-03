import math

class DiaryEntry:
    def __init__(self, title, contents):
        # self.:
        #   title: string
        #   contents: string
        self.title = title
        self.contents = contents
        self.chunk_count = 0
        

    def format(self):
        return f'{self.title}: {self.contents}'

    def count_words(self):
        if type(self.contents) == str:
            string_split = self.contents.split(' ')
            filtered_list = [word for word in string_split if word != '']
            return len(filtered_list)
        else:
            return "Please enter a valid string."

    def reading_time(self, wpm):
        if type(wpm) != int:
            raise Exception('Please enter an integer')
        return math.ceil(self.count_words() / wpm)
        
    def reading_chunk(self, wpm, minutes):
        if type(wpm) != int or type(minutes) != int:
            raise Exception('reading_chunk only accepts ints as parameters')
        
        string_split = self.contents.split(' ')
        filtered_list = [word for word in string_split if word != '']
        words_to_count = wpm * minutes
        if (words_to_count + self.chunk_count) > len(filtered_list):
            self.chunk_count = 0
        final_words_list = [word for word in filtered_list[self.chunk_count: self.chunk_count + words_to_count]]
        self.chunk_count += words_to_count
        return ' '.join(final_words_list)
        



