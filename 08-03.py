
# 8.3 Date Printer

def main():

    date = input('Enter Date (mm/dd/yyyy): ')
    
    month = int(date[0:2])
    
    if month == 1:
        month = 'January'
    elif month == 2:
        month = 'February'
    elif month == 3:
        month = 'March'
    elif month == 4:
        month = 'April'
    elif month == 5:
        month = 'May'
    elif month == 6:
        month = 'June'
    elif month == 7:
        month = 'July'
    elif month == 8:
        month = 'August'
    elif month == 9:
        month = 'September'
    elif month == 10:
        month = 'October'
    elif month == 11:
        month = 'November'
    else:
        month = 'December'
        
    day = int(date[3:5])
    
    year = int(date[6:10])
    
    print(month, str(day) + ',', year)
    
main()