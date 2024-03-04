# generate a recursive sequence called a(n)
def a(n):
     if n == 1:
         return 4
     else:
         return 2*a(n-1) + 3
# to have the first five values
for n in range (1,6):
    print (a(n))
