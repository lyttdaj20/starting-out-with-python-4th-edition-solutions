
# 7.4 Number Analysis Program

def main():

    numbers = []
    
    for i in range(20):
        
        numbers.append(float(input('Enter Number ' + str(i + 1) + ': ')))
    
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
    
    print('Low:', low)
    print('High:', high)
    print('Total:', total)
    print('Average:', average)
    
main()