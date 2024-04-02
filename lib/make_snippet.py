def make_snippet(string):
    if len(string.split(' ')) > 5:
        words_list = string.split(' ')[:5]
        merged_words = ' '.join(words_list)
        return merged_words + "..."
    else:
        return string

    