import re
import argparse
from collections import Counter


def load_data(filepath):
    with open(filepath, encoding='utf-8') as input_file:
        input_data = input_file.read()
    return input_data


def get_most_frequent_words(text):
    top_count = 10
    text = text.lower()
    clear_words = re.findall("([^\W\d]+)", text)
    word_counts = Counter(clear_words)
    return word_counts.most_common(top_count)


def create_parser():
    parser = argparse.ArgumentParser(description='Frequency Analysis of Words')
    parser.add_argument("path", help="path to input text")
    return parser


def print_top_words(word_counts):
    for number, (word, count) in enumerate(word_counts, start=1):
        print(number, word)


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    word_counts = get_most_frequent_words(load_data(args.path))
    print_top_words(word_counts)
