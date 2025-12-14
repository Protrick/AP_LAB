def is_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

number = int(input("Enter a number: "))
result = is_even_odd(number)
print(f"{number} is {result}")
