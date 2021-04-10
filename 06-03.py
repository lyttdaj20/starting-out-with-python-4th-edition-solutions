
# 6.3 Line Numbers

def main():
    
    file_name = input('Enter File Name: ')

    file = open(file_name, 'r')
    
    line_number = 1
    
    for line in file:
        
        line = line.rstrip('\n')
        
        print(str(line_number) + ':', line)
        
        line_number += 1
        
    file.close()
    
main()