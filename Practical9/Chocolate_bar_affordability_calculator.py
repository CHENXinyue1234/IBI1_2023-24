#function
def affordability(money, price):
    number=money//price
    change=money%price

    return number,change
#example to call the function
total_money=100
price=7
number,change=affordability(total_money,price)
print('The number of bars you can buy is',number)
print('The change that will be left over is',change)
