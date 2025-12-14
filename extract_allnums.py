import re

text = input("Enter a string: ")
numbers = re.findall(r'\d+', text)

print(f"Extracted numbers: {numbers}")
print(f"Total numbers found: {len(numbers)}")
