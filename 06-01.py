
# 6.1 File Display

def main():
    
    file = open('numbers.txt', 'r')
    
    for line in file:
        
        number = int(line)
        
        print(number)
    
    file.close()
    
main()