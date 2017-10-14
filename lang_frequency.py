import re
import argparse
from collections import Counter


def load_data(filepath):
    with open(filepath, encoding='utf-8') as input_file:
        input_data = input_file.read()
    return input_data


def get_most_frequent_words(text):
    text = text.lower()
    regex = re.compile("(?P<clear_word>[^\W\d]+)")
    clear_words = regex.findall(text)
    print(clear_words)
    word_counts = Counter(clear_words)
    return word_counts


def create_parser():
    parser = argparse.ArgumentParser(description='Frequency Analysis of Words')
    parser.add_argument("path", help="path to input text")
    return parser


def print_top_words(word_counts, quantity):
    for number, word in enumerate(word_counts.most_common(quantity)):
        print(number + 1, word[0])


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    if args.path:
        word_counts = get_most_frequent_words(load_data(args.path))
        print_top_words(word_counts, 10)
