
# 4.12 Calculating the Factorial of a Number

number = int(input('Enter Number: '))
factorial = 1

for i in range(1, number+1):
    factorial *= i
    
print('Factorial: ', factorial)
