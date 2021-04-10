
# 5.16 Odd/Even Counter

import random

odd = 0
even = 0
 
def main():
    
    global odd
    global even
    
    number = 0
    
    for i in range(1,101):
        number = random.randint(0, 9)
        
        if is_even(number):
            even += 1
        else:
            odd += 1
      
    print('Odd:', odd)
    print('Even:', even)
        
def is_even(number):
    return number % 2 == 0
    
main()    
