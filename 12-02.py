
# 12.2 Recursive Multiplication

def main():
    print('Product:', product(12, 12))

def product(x, y):
    
    sum = 0
    
    if y > 0:

        sum = x + product(x, y - 1)

    return sum

main()