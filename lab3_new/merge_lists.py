# Input
n1 = int(input("Enter size of list1: "))
list1 = list(map(int, input("Enter list1: ").split()))
n2 = int(input("Enter size of list2: "))
list2 = list(map(int, input("Enter list2: ").split()))

merged = list1[:] + list2[:]
print(f"List1: {list1}")
print(f"List2: {list2}")
print(f"Merged: {merged}")
