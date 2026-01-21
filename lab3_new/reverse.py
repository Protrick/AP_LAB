n = int(input("Enter list size: "))
lst = list(map(int, input("Enter numbers: ").split()))
reversed_lst = lst[::-1]

print(f"Original: {lst}")
print(f"Reversed: {reversed_lst}")
