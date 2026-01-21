def rotate_left(lst, k):
    if not lst: return []
    k = k % len(lst)
    return lst[k:] + lst[:k]

def rotate_right(lst, k):
    if not lst: return []
    k = k % len(lst)
    return lst[-k:] + lst[:-k]

# Input
n = int(input("Enter list size: "))
lst = list(map(int, input("Enter numbers: ").split()))
k = int(input("Enter rotation positions: "))

left = rotate_left(lst, k)
right = rotate_right(lst, k)

print(f"Original: {lst}")
print(f"Left {k}: {left}")
print(f"Right {k}: {right}")
