
# 5.1 Kilometer Converter

def main():
    kilometers = float((input('Enter Distance in Kilometers: ')))
    miles = convert_to_miles(kilometers)
    print('Distance in Miles:', miles)

def convert_to_miles(kilometers):
    miles = round(kilometers * 0.6214, 1)
    return miles

main()