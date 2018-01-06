
import re
import os
import sys
from collections import Counter


def load_data(file_path):
    with open(file_path, 'r', encoding='cp1251') as file_reader:
        text = file_reader.read()
    return text


def get_most_frequent_words(text, top_lenght):
    words = re.findall(r'\w+', text)
    top_freq_words = Counter(
            [word.lower().strip() for word in words]
            ).most_common(top_lenght)
    return top_freq_words

if __name__ == '__main__':
    try:
        text_file = load_data(sys.argv[1])
    except (FileNotFoundError, IndexError):
        sys.exit('Please, use correct filepath.')
    except UnicodeError:
        sys.exit('Please, check your file encoding')
    try:
        top_lenght = int(input('How many most frequent words you need? '))
        print('That is TOP {} list of words - (word, count of repetition):'
              .format(top_lenght))
        print(get_most_frequent_words(text_file, top_lenght))

    except (TypeError, ValueError):
        sys.exit('Please, use only digits.')
