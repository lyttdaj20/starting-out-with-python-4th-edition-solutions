
# 3.5 Mass and Weight

mass = float(input('Enter Mass in kg: '))

weight = round(mass * 9.8, 2)
print('Weight (N):', weight)

if weight > 500:
    print('Object is too heavy')
elif weight < 100:
    print('Object is too light')
    