
# 3.1 Day of the Week

number = int(input('Enter a number between 1 and 7: '))

DAY_CONSTANT = 'day'

day = DAY_CONSTANT

if number == 1:
    day = 'Monday'
elif number == 2:
    day = 'Tuesday'
elif number == 3:
    day = 'Wednesday'
elif number == 4:
    day = 'Thursday'
elif number == 5:
    day = 'Friday'
elif number == 6:
    day = 'Saturday'
elif number == 7:
    day = 'Sunday'

if day != DAY_CONSTANT:
    print(day)
else:
    print('Error - Number must be between 1 and 7')
    