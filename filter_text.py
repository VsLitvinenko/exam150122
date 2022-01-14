import string
import re


def remove_punctuation(text):
    return "".join([ch if ch not in (string.punctuation + '—«»”') else ' ' for ch in text])


def remove_numbers(text):
    return ''.join([i if not i.isdigit() else ' ' for i in text])


def remove_multiple_spaces(text):
    return re.sub(r'\s+', ' ', text, flags=re.I)


def remove_symbols(text):
    return remove_multiple_spaces(
        remove_numbers(
            remove_punctuation(text.lower())
        )
    )
