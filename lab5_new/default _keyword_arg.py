def calculate_bill(amount, tax=5, discount=0):
    tax_amount = amount * tax / 100
    discount_amount = amount * discount / 100
    final_amount = amount + tax_amount - discount_amount
    return final_amount


print(calculate_bill(1000))
print(calculate_bill(amount=1000, tax=12, discount=10))