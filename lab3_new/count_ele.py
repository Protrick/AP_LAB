def count_element(lst, elem):
    return sum(1 for x in lst if x == elem)

# Input
n = int(input("Enter list size: "))
lst = list(map(int, input("Enter numbers: ").split()))
elem = int(input("Enter element to count: "))

count = count_element(lst, elem)
print(f"List: {lst}")
print(f"Count of {elem}: {count}")
