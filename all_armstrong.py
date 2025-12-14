start = int(input("Enter start range: "))
end = int(input("Enter end range: "))

print(f"Armstrong numbers between {start} and {end}:")
for num in range(start, end + 1):
    order = len(str(num))
    sum_digits = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum_digits += digit ** order
        temp //= 10
    if sum_digits == num:
        print(num)
