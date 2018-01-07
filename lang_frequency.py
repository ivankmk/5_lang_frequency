
import re
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
    frequent_words = 10
    top_freq_words = Counter(
        [word.strip() for word in words]
    ).most_common(frequent_words)
    return dict(top_freq_words)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('No file provided')
    else:
        text = load_data(sys.argv[1])
        if text is None:
            sys.exit('Please check your text file')
    words = get_most_frequent_words(text)
    print('That is your Top-10 list of words:\n')
    for word, count in words.items():
        print('{}:  {}'.format(word, count))
    print('\n')
