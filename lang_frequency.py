
import re
import os
import sys
from collections import Counter


def load_data(file_path):
    try:
        with open(file_path, 'r', encoding='cp1251') as file_reader:
            text = file_reader.read()
        return text
    except (FileNotFoundError, IndexError, UnicodeError):
        return None
        # sys.exit('Please, use correct filepath.')


def get_most_frequent_words(text, top_lenght):
    words = re.findall(r'\w+', text)
    top_freq_words = Counter(
            [word.lower().strip() for word in words]
            ).most_common(top_lenght)
    return top_freq_words


if __name__ == '__main__':
    if load_data(sys.argv[1]) is None:
        sys.exit('Please, check your file')
    else:
        text_file = load_data(sys.argv[1])
    try:
        top_lenght = int(input('How many most frequent words you need? '))
        words = get_most_frequent_words(text_file, top_lenght)
        print('That is your TOP {} list of words: '.format(top_lenght))
    except (TypeError, ValueError):
        sys.exit('Please, use only digits.')
    for word in words:
        print('Word: {}, count of reiterative: {}'
              .format(word[0], word[1]))
