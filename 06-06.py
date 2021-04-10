
# 6.6 Average of Numbers

def main():
    
    file = open('numbers.txt', 'r')
    
    sum = 0
    total = 0
    
    for line in file:
        
        sum += int(line)
        total += 1
        
    average = round(sum/total, 2)
    
    print('Average of Numbers:', average)
    
    file.close()
    
main()