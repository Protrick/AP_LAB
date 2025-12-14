rows = int(input("Enter number of rows: "))
n = rows // 2

# Upper half (including middle)
for i in range(n + 1):
    spaces = " " * (n - i)
    stars = "*" * (2 * i + 1)
    print(spaces + stars)

# Lower half
for i in range(n - 1, -1, -1):
    spaces = " " * (n - i)
    stars = "*" * (2 * i + 1)
    print(spaces + stars)
