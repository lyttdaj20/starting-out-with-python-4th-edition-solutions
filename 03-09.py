
# 3.9 Roulette Wheel Colors

pocket = int(input('Enter pocket number: '))

color = ''

if pocket == 0:
    color = 'green'
elif (pocket >= 1 and pocket <= 10) or (pocket >= 19 and pocket <= 86):
    if (pocket % 2 == 1):
        color = 'red'
    else:
        color = 'black'

elif (pocket >= 11 and pocket <= 18) or (pocket >= 29 and pocket <= 36):
    if (pocket % 2 == 1):
        color = 'black'
    else:
        color = 'red'
        
if pocket > 36 or pocket < 0:
    print('Error - Number out of range')
else:
    print('Color:', color)