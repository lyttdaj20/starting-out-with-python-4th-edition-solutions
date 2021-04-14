
# 3.2 Areas of Rectangles

length1 = float(input('Enter the length of Rectangle 1: '))
width1 = float(input('Enter the width of Rectangle 1: '))
area1 = length1 * width1

length2 = float(input('Enter the length of Rectangle 2: '))
width2 = float(input('Enter the width of Rectangle 2: '))
area2 = length2 * width2

if area1 > area2:
    print('Rectangle 1 is larger')
elif area2 > area1:
    print('Rectangle 2 is larger')
else:
    print('Both rectangles are the same size')