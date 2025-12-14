text = input("Enter text: ")
shift = int(input("Enter shift: "))

encrypted = ""
for char in text:
    if 'A' <= char <= 'Z':
        encrypted += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
    elif 'a' <= char <= 'z':
        encrypted += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
    else:
        encrypted += char

print(f"Encrypted: {encrypted}")
