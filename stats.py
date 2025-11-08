def count_words(input):
    counter = 0
    new_list = input.split()
    for word in new_list:
        counter += 1
    return counter

def count_letters(input):
    set_of_letters = set()
    for letter in input:
        set_of_letters.add(letter.lower())
    for word in set_of_letters:
        
    return set_of_letters