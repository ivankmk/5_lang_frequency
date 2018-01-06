
import re
import os
import sys
from collections import Counter


def load_data(file_path):
    try:
        with open(file_path, 'r', encoding="utf-8") as file_reader:
            text = file_reader.read().lower()
        return text
    except (FileNotFoundError, UnicodeError):
        return None


def get_most_frequent_words(text):
    words = re.findall(r'\b\w+\b', text)
    cnt_of_words = 10
    top_freq_words = Counter(
            [word.strip() for word in words]
            ).most_common(cnt_of_words)
    return dict(top_freq_words)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('No file provided')
    else:
        text_file = load_data(sys.argv[1])
        if text_file is None:
            sys.exit('Please check your text file')
    words = get_most_frequent_words(text_file)
    print('That is your Top-10 list of words:\n')
    for word, count in words.items():
        print('Word: {}, count of reiterative: {}'.format(word, count))
