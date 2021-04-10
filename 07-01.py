
# 7.1 Total Sales

def main():
    
    total_sales = 0

    sales = []

    for day in range(1, 8):

        sales.append(float(input('Enter Sales for Day ' + str(day) + ': ')))
        
    for i in sales:
        
        total_sales += i
    
    print('Total Sales:', total_sales)
    
main()