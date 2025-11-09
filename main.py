from stats import get_num_words, get_chars_dict#, sort_word_list


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words") 
    print("--------- Character Count -------")
    print(f"{chars_dict}")
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
