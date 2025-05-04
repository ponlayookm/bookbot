from stats import get_num_words, count_characters
import sys


# def get_book_text(file_path):
#     with open(file_path) as f:
#         file_contents = f.read()
#     return file_contents


def main():
    if len(sys.argv) < 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)

    book_path = sys.argv[1]
    with open(book_path) as f:
        book_contents = f.read()

    # contents = get_book_text("books/frankenstein.txt")
    total_words = get_num_words(book_contents)
    char_count = count_characters(book_contents)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")


    for char, count in sorted(char_count.items(), key=lambda item: item[1], reverse=True):
        print(f"{char}: {count}")

main()
