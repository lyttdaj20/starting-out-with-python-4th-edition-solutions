
# 3.16 February Days

year = int(input('Enter Year: '))

days = 0

if year % 100 == 0:
    
    if year % 400 == 0:
        
        days = 29
    
    else:
        
        days = 28

else:
    
    if year % 4 == 0:
        
        days = 29
        
    else:
        
        days = 28
        
print('In', year, 'February has', days, 'days')