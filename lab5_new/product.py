from functools import reduce

lst = [1, 2, 3, 4, 5]

product = reduce(lambda a, b: a * b, lst)

print(product)