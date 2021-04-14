
# 3.3 Age Classifier

age = int(input('Enter Age: '))

age_class = ''

if age <= 1:
    age_class = 'infant'
elif age > 1 and age < 13:
    age_class = 'child'
elif age >= 13 and age < 20:
    age_class = 'teenager'
else:
    age_class = 'adult'

print('This person is a(n)', age_class)
    
    