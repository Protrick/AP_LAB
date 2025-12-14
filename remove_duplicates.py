text = input("Enter a string: ")
unique_chars = ""
for char in text:
    if char not in unique_chars:
        unique_chars += char

print(f"String without duplicates: {unique_chars}")
