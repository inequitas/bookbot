def count_words(input):
    counter = 0
    new_list = input.split()
    for word in new_list:
        counter += 1
    return counter