
import re
import argparse
from collections import Counter


def load_data(filepath):
    with open(filepath, encoding='utf-8') as input_file:
        input_data = input_file.read()
    return input_data


def get_most_frequent_words(text):
    clear_words = []
    text = text.lower().split()
    regex = re.compile("(?P<clear_word>\w+).*")
    for word in text:
        try:
            clear_word = re.match(regex, word).group('clear_word')
            clear_word = re.match('\D+', clear_word).group()
            clear_words.append(clear_word)
        except:
            pass
    word_counts = Counter(clear_words)
    for number, word in enumerate(word_counts):
        if number < 10:
            print(number+1, word)
        else:
            break


def create_parser():
    parser = argparse.ArgumentParser(description='Frequency Analysis of Words')
    parser.add_argument("path", help="path to input text")
    return parser


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    if args.path:
        get_most_frequent_words(load_data(args.path))
