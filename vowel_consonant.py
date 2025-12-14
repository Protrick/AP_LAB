text = input("Enter a string: ").lower()
vowels = "aeiou"
vowel_count = 0
consonant_count = 0
digit_count = 0
space_count = 0

for char in text:
    if char in vowels:
        vowel_count += 1
    elif char.isalpha():
        consonant_count += 1
    elif char.isdigit():
        digit_count += 1
    elif char == " ":
        space_count += 1

print(f"Vowels: {vowel_count}")
print(f"Consonants: {consonant_count}")
print(f"Digits: {digit_count}")
print(f"Spaces: {space_count}")
