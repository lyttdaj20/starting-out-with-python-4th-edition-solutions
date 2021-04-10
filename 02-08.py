
# 2.8 Tip, Tax, and Total

TIP = .18

SALES_TAX = .07

subtotal = float(input('Enter Total Amount Spent: '))

tip = round(subtotal * TIP, 2)

sales_tax = round(subtotal * SALES_TAX, 2)

total = round(subtotal + sales_tax + tip, 2)

print('Subtotal:', subtotal)
print('Tip:', tip)
print('Sales Tax:', sales_tax)
print('Total:', total)