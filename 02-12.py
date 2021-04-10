
# 2.12 Stock Transaction Program

shares = 2000
stock_buy = 40.00
stock_sell = 42.75
commission_rate = 0.03

spent_on_stock = round(shares * stock_buy, 2)
spent_commission = round(spent_on_stock * commission_rate, 2)
spent = round(spent_on_stock + spent_commission)

made_on_stock = round(shares * stock_sell, 2)
made_commission = round(made_on_stock *  commission_rate, 2)
made = round(spent_on_stock - spent_commission)

profit = made - spent

print('Spent Buying Stock:', spent_on_stock)
print('Commission From Buying:', spent_commission)
print('Made Selling Stock:', made_on_stock)
print('Commission From Selling:', made_commission)
print('Profit:', profit)
