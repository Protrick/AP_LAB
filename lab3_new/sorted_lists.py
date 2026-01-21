n = int(input("Enter list size: "))
lst = list(map(int, input("Enter numbers: ").split()))
asc = sorted(lst)
desc = sorted(lst, reverse=True)

print(f"Original: {lst}")
print(f"Ascending: {asc}")
print(f"Descending: {desc}")
