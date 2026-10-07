price = float(input("Enter the price with cents: "))
price_with_tax = price * 1.20
print("price with tax:", price_with_tax)
payment = float(input("Enter the amount paid: "))
print("Your change:", payment-price_with_tax)