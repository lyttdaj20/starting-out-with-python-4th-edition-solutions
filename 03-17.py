
# 3-17 Wi-Fi Diagnostic Tree

print('Reboot the computer and try to connect.')

fixed = input('Did that fix the problem? ')

if fixed == 'no':
    
    print('Reboot the router and try to connect.')
    
    fixed = input('Did that fix the problem? ')
    
    if fixed == 'no':
        
        print('Make sure the cables between the router & modem are plugged in firmly.')
        
        fixed = input('Did that fix the problem? ')
        
        if fixed == 'no':
            
            print('Move the router to a new location and try to connect.')
            
            fixed = input('Did that fix the problem? ')
            
            if fixed == 'no':
                
                print('Get a new router.')