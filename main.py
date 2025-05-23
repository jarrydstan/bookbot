from stats import count_words, count_chars, sort_char_counts
import sys

def get_book_text(file):
    with open(file) as f:
        text = f.read()
    return text
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    num_words = count_words(book_text)
    num_chars = count_chars(book_text)
    sorted_list = sort_char_counts(num_chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['num']}")

main()
