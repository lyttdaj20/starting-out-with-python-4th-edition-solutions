
# 7.12 Prime Number Generation

def main():
    
    number = int(input('Enter Number: '))

    number_list = []
    
    for i in range(2, number + 1):
        
        number_list.append(i)
    
    for i in number_list:
        
        is_prime(i)
    

def is_prime(number):
    
    prime = True
    
    for i in range(2, number):
        
        if number % i == 0:
            
            prime = False
        
    if prime:
        
        print(number)
        
    


main()