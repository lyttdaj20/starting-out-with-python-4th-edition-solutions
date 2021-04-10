
#2.6 Sales Tax

STATE_SALES_TAX = .05

COUNTY_SALES_TAX = .025

subtotal = float(input('Enter Purchase Amount (in Dollars): '))

state_sales_tax = round(subtotal * STATE_SALES_TAX, 2)
county_sales_tax = round(subtotal * COUNTY_SALES_TAX, 2)
total_tax = round(state_sales_tax + county_sales_tax, 2)
total = round(subtotal + total_tax, 2)

print('Subtotal:', subtotal)
print('State Sales Tax:', state_sales_tax)
print('County Sales Tax:', county_sales_tax)
print('Total Sales Tax:', total_tax)
print('Total:', total)