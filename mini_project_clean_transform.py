"""
mini_project_clean_transform.py

Purpose:
Given a messy list of strings representing a large number with spaces,
clean it and convert it to an integer.

Example:
['9', ' ', '2', '2', '3', ' ', ...] -> 9223...
"""

def chars_to_int(char_list: list[str]) -> int:
    """Convert a list of digit/space characters into an integer."""
    digits = []
    for ch in char_list:
        if ch.isdigit():
            digits.append(ch)

    number_str = "".join(digits)
    return int(number_str)

generated_list = [
    '9', ' ',
    '2', '2', '3', ' ',
    '3', '7', '2', ' ',
    '0', '3', '6', ' ',
    '8', '5', '4', ' ',
    '7', '7', '5', ' ',
    '8', '0', '7'
]

print("Original:", generated_list)
print("As int:", chars_to_int(generated_list))