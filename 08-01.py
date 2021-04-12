
# 8.1 Initials

def main():
    
    full_name = input('Enter Full Name: ')
    
    index = 0
    
    initials = ''
    
    for name in range(3):    
    
        current_name = ''
    
        for i in range(index, len(full_name)):
            
            current_char = full_name[index]
            
            index += 1
            
            if current_char != ' ':
                
                current_name += current_char
                
            else:
            
                break
    
        initials += current_name[0] + '. '
    
    
    print('Initials:', initials)
    
main()
