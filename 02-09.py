
# 2.9 Celsius to Fahrenheit Temperature Converter

# The book may mistaken list 9/5 (or 1.8 as I used) as 95 in the formula

celcius = float(input('Enter Temperature in Degrees Celsius: '))

fahrenheit = round((1.8 * celcius) + 32, 0)

print('Temperature in Degrees Fahrenheit:', fahrenheit)