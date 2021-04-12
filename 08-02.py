
# 8.2 Sum of Digits in a String

def main():
    
    numbers = input('Enter String: ')
    
    sum = 0
    
    for ch in numbers:    
        
        sum += int(ch)

    print('Sum:', sum)
    
main()
