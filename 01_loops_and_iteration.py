
#`01_loops_and_iteration.py`

"""
01_loops_and_iteration.py

Purpose:
Demonstrate common loop patterns used in data work:
- iterating over values
- iterating with index using enumerate
- filtering with a loop vs a list comprehension
"""

data = [4, 5, 104, 105, 110, 120, 130, 130, 150, 160, 170, 183, 185, 187, 191, 350, 360]
min_valid = 100

print("Original:", data)

# Example 1: build a new list (like a SQL WHERE clause)
filtered = []
for value in data:
    if value >= min_valid:
        filtered.append(value)

print("Filtered (loop):", filtered)

# Equivalent list comprehension
filtered_comp = [value for value in data if value >= min_valid]
print("Filtered (comprehension):", filtered_comp)

# Example 2: enumerate gives (index, value)
for index, value in enumerate(data):
    if value >= min_valid:
        print(f"First value >= {min_valid} occurs at index {index} (value={value})")
        break
