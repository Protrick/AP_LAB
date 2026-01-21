nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list = list(filter(lambda x: x%2 == 0, nums))

print(f"original list: {nums}")
print(f"filtered even list: {even_list}")