from collections import Counter


def get_num_words(contents):
    words = contents.split()
    num_words = len(words)
    return num_words


def count_characters(file_contents):
    char_count = {}
    for char in file_contents.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count