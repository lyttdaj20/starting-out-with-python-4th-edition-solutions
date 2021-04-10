
# 2.11 Male and Female Percentages

males = int(input('Enter # of Males: '))
females = int(input('Enter # of Females: '))

total = males + females

male_percentage = round(males / total, 3)
female_percentage = round(females / total, 3)

print('Male Proportion:', male_percentage)
print('Female Proportion:', female_percentage)