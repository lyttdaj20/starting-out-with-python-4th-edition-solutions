
# 7-01 Lottery Number Generator

import random

def main():
    
    number_list = []
    lottery_number = ''
    
    for i in range(1,8):
        
        number_list.append(random.randint(0,9))
    
    for i in number_list:
        lottery_number += str(i)
    
    print('Lottery Number:', lottery_number)
    
main()