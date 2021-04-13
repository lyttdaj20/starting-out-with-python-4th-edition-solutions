
# 4.3 Budget Analysis

budget = float(input('Enter Monthly Budget: '))

total_expenses = 0

expense = 0

i = 1

while expense >= 0:
    
    total_expenses += expense
    
    expense = float(input('Enter Individual Expense ' + str(i) + ': '))
    
    i += 1
    
difference = budget - total_expenses

print('You are', '$' + str(difference), 'under budget')