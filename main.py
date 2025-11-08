from stats import count_words

def main():
    output = count_words(get_book_text("books/frankenstein.txt"))
    print(f"Found {output} total words")
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents
main()

