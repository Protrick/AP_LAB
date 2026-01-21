def remove_duplicates(lst):
    seen = []
    for item in lst:
        if item not in seen:
            seen.append(item)
    return seen

# Input
n = int(input("Enter list size: "))
lst = list(map(int, input("Enter numbers: ").split()))
unique = remove_duplicates(lst)

print(f"Original: {lst}")
print(f"Without duplicates: {unique}")
