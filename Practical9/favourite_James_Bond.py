born_year=int(input('Please enter the year you were born:'))
def favourite_actor(born):
    eighteen=born+18
    if eighteen >= 1973 and eighteen <= 1986:
        your_actor= "Roger Moore"
    elif eighteen >= 1987 and eighteen <= 1994:
        your_actor="Timothy Dalton"
    elif eighteen >= 1995 and eighteen <= 2005:
        your_actor="Pierce Brosnan"
    elif eighteen >= 2006 and eighteen <= 2021:
        your_actor="Daniel Craig"
    else:
        your_actor="None"
    return your_actor
print('Your favourite Bond is:', favourite_actor(born_year))
        