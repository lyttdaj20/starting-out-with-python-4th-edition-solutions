
# 12.6 Sum of Numbers

def main():
    
    print('Sum:', sum(int(input('Enter Number: '))))
    
def sum(n):
    
    if n > 0:
    
        return n + sum(n - 1)

    else:
    
        return n
main()