
# 5.4 Automobile Costs

loan_payment = 0
insurance = 0
gas = 0
oil = 0
tires = 0
maintenance = 0

def main():
    
    global loan_payment
    global insurance
    global gas
    global oil
    global tires
    global maintenance
    
    print('Enter the Amount Spent on')
    loan_payment = float(input('Loan Payment: '))
    insurance = float(input('Insurance: '))
    gas = float(input('Gas: '))
    oil = float(input('Oil: '))
    tires = float(input('Tires: '))
    maintenance = float(input('Maintenance: '))
    
    monthly_cost = calculate_monthly_cost()
    annual_cost = calculate_annual_cost()
    
    print('Total Monthly Cost:', monthly_cost)
    print('Total Annual Cost:', annual_cost)
    
def calculate_monthly_cost():
    cost = loan_payment + insurance + gas + oil + tires + maintenance
    return cost

def calculate_annual_cost():
    cost = 12 * calculate_monthly_cost()
    return cost

main()
