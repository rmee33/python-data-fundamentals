"""
02_string_cleaning.py

Purpose:
Demonstrate cleaning strings and extracting only alphanumeric characters.
"""

def keep_alnum(text: str) -> str:
    """Return a version of text containing only letters and digits."""
    return "".join(ch for ch in text if ch.isalnum())

def is_sentence_palindrome(text: str) -> bool:
    """Check if text is a palindrome, ignoring punctuation/spaces/case."""
    cleaned = keep_alnum(text).casefold()
    return cleaned == cleaned[::-1]

samples = [
    "A man, a plan, a canal: Panama!",
    "Was it a car or a cat I saw?",
    "hello world",
]

for s in samples:
    print(s, "-> cleaned:", keep_alnum(s), "| palindrome:", is_sentence_palindrome(s))