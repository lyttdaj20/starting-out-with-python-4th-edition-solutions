
#2.4 Total Purchase

SALES_TAX = .07

item1 = float(input('Enter the price of the first item: '))
item2 = float(input('Enter the price of the second item: '))
item3 = float(input('Enter the price of the third item: '))
item4 = float(input('Enter the price of the fourth item: '))
item5 = float(input('Enter the price of the fifth item: '))

subtotal = item1 + item2 + item3 + item4 + item5
sales_tax = round(subtotal * SALES_TAX, 2)
total =  round(subtotal * (1 + SALES_TAX), 2)

print()
print('Subtotal:', subtotal)
print('Sales Tax:', sales_tax)
print('Total:', total)