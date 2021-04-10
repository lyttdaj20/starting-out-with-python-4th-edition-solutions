
# 6.5 Sum of Numbers

def main():
    
    file = open('numbers.txt', 'r')
    
    sum = 0
    
    for line in file:
        
        sum += int(line)
        
    print('Sum of Numbers:', sum)
    
    file.close()
    
main()