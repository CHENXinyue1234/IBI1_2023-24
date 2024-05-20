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
    
#example
example_born_year=1977
print('Example: Assume the year you were born is 1977.')
print('Your favourite Bond is:', favourite_actor(example_born_year))

#call the function
born_year=int(input('Please enter the year you were born:'))
print('Your favourite Bond is:', favourite_actor(born_year))


