
# 3.6 Magic Dates

month = int(input('Enter Month in (Numerical): '))
day = int(input('Enter Day: '))
year = int(input('Enter Year (Two-digit): '))

if month * day == year:
    print('This is a magic date')
else:
    print('This is not a magic date')