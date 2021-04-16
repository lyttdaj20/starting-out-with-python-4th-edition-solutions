
# 5.2 Sales Tax Program Refactoring

def main():

    STATE_SALES_TAX = .05
    
    COUNTY_SALES_TAX = .025
    
    subtotal = float(input('Enter Purchase Amount (in Dollars): '))
    
    print('Subtotal:', subtotal)
    print('State Sales Tax:', state_tax(subtotal))
    print('County Sales Tax:', county_tax(subtotal))
    print('Total Sales Tax:', total_tax(subtotal))
    print('Total:', total(subtotal))
    
def state_tax(subtotal):
    return round(subtotal * .05, 2)
    
def county_tax(subtotal):
    return round(subtotal * .025, 2)

def total_tax(subtotal):
    return state_tax(subtotal) + county_tax(subtotal)

def total(subtotal):
    return subtotal + total_tax(subtotal)

    
    
    
main()

