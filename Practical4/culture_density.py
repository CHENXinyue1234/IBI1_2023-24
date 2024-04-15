# The initial density is 5%
density = 5
# Begin with day 1
day = 0
#
while density <= 90:
    # density double in a day
    density = 2*density
    # if doubled density smaller than or equal to 90%
    if density <= 90:
        # all the cells to grow for one more day
        day += 1
    # if doubled density bigger than 90%
    else:
        # stop the cells from growing
        break
print ("It takes", day+1, "days for the density to go over 90%")
print ("The maximum number of days I can have a holiday from lab is", day)
