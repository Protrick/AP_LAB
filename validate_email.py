import re

email = input("Enter email address: ")

pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

if re.match(pattern, email):
    print(f"{email} is a VALID email address")
else:
    print(f"{email} is an INVALID email address")
