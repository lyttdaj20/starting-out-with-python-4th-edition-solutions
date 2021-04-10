
# 6.7 Random Number File Writer

import random

def main():
    no_of_values = int(input('Enter number of values: '))

    number = 0
    
    file = open('numbers.txt', 'w')
    
    for i in range(0, no_of_values):
        
        number = str(random.randint(1, 500))
        
        file.write(number + '\n')
    
    file.close()
    
main()