
# 12.7 Recursive Power Method

def main():
    print('Power:', power(4, 3))

def power(x, y):
    
    product = 1
    
    if y > 0:

        product = x * power(x, y - 1)

    return product

main()