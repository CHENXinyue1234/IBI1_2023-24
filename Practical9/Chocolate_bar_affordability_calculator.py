total_money=int(input('How much money do you have?'))
price=int(input('What is the price of one chocolate bar?'))
def affordability(money, price):
    number=money//price
    return(number)
def change(money, price):
    change=money%price
    return(change)
print('The number of bars you can buy is',affordability(total_money,price))
print("You remaining change is",change(total_money,price))