
# 7.3 Rainfall Statistics

def main():

    numbers = []
    
    for i in range(12):
        
        numbers.append(float(input('Enter Rainfall in Month ' + str(i + 1) + ': ')))
    
    low = numbers[0]
    high = numbers[0]
    total = 0
    
    for i in numbers:
        
        if i < low:
            
            low = i
            
        if i > high:
            
            high = i
        
        total += i
    
    average = round(total / 20, 1)
    
    print('Total:', total)
    print('Average:', average)
    print('Low:', low)
    print('High:', high)
    
    
main()