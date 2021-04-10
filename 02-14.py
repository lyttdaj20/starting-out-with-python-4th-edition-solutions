
# 2.14 Compound Interest

# The formula is The formula for compound interest is P (1 + r/n)^(nt)

principal = float(input('Principal Deposited: '))
interest = float(input('Interest Rate: ')) / 100
number_of_times = float(input('# of time Compounded Annually: '))
years = float(input('Number of Years: '))

balance = round(principal * pow(1 + (interest / number_of_times), number_of_times * years), 2)

print('Balance: ', balance)