def count_words(string):
    if type(string) == str:
        string_split = string.split(' ')
        filtered_list = [word for word in string_split if word != '']
        return len(filtered_list)
    else:
        return "Please enter a valid string."