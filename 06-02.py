
# 6.2 File Head Display

def main():
    
    file_name = input('Enter File Name: ')

    file = open(file_name, 'r')
    
    line_number = 1
    
    for line in file:
        
        if line_number <= 5:
            
            print(line.rstrip('\n'))
            
            line_number += 1
    
    file.close()
    
main()