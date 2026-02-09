"""
04_collections_and_unpacking.py

Purpose:
Explain nested lists and unpacking in a practical way.
"""

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
numbers = [even, odd]

print("numbers (nested list):", numbers)

for number_list in numbers:
    print("Inner list:", number_list)

# Tuple unpacking example:
point = (10, 25)
x, y = point
print("Tuple unpacking:", point, "-> x =", x, ", y =", y)

# Unpacking in a loop
pairs = [("a", 1), ("b", 2), ("c", 3)]
for letter, num in pairs:
    print(f"letter={letter}, num={num}")
