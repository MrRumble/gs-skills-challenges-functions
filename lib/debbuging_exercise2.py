def get_most_common_letter(text):
    counter = {}
    text = text.replace(" ", "")
    print(f'text to count is: {text}')
    for char in text:
        print(char)
        counter[char] = counter.get(char, 0) + 1
        print(counter.get(char, 0) + 1)
    letter = sorted(counter.items(), key=lambda item: item[1])[-1][0]
    print(sorted(counter.items(), key=lambda item: item[1]))
    print('List below')
    
    print(letter)
    return letter


print(f"""
Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
Expected: o
Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
""")
