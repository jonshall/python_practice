"""reverse_words.py

reverse the words of a given string
"""
def RevWord(string: str) -> str:
    reverse = string.split()[::-1]

    return f"' '.join(reverse)"
