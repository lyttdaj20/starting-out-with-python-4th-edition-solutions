
# 3.4 Roman Numerals

number = int(input('Enter Number Between 1-10: '))

if number == 1:
    roman = 'I'
elif number == 2:
    roman = 'II'
elif number == 3:
    roman = 'III'
elif number == 4:
    roman = 'IV'
elif number == 5:
    roman = 'V'
elif number == 6:
    roman = 'VI'
elif number == 7:
    roman = 'VII'
elif number == 8:
    roman = 'VIII'
elif number == 9:
    roman = 'IX'
elif number == 10:
    roman = 'X'
else:
    roman = 'Error - Number must be between 1-10'
    
print(roman)