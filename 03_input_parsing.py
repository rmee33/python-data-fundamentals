"""
03_input_parsing.py

Purpose:
Parse user input like "a,b,c" and compute a + b - c with validation.
"""

def parse_three_ints(csv_text: str) -> tuple[int, int, int]:
    """
    Parse input of the form 'a,b,c' into three integers.
    Raises ValueError if parsing fails.
    """
    parts = csv_text.split(",")
    if len(parts) != 3:
        raise ValueError("Input must contain exactly three values separated by commas.")

    a_str, b_str, c_str = (p.strip() for p in parts)
    return int(a_str), int(b_str), int(c_str)

user_input = input("Enter three integers separated by commas (a,b,c): ")

try:
    a, b, c = parse_three_ints(user_input)
    result = a + b - c
    print(f"{a} + {b} - {c} = {result}")
except ValueError as e:
    print("Invalid input:", e)