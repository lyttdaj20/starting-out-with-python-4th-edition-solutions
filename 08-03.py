
# 8.3 Date Printer

def main():

    date = input('Enter Date (mm/dd/yyyy): ')
    
    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
                   'September', 'October', 'November', 'December' ]
    
    month = month_names[int(date[0:2]) - 1]
 
    day = int(date[3:5])
    
    year = int(date[6:10])
    
    print(month, str(day) + ',', year)
    
main()