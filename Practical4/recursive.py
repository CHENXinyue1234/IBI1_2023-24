# generate a recursive sequence called a(n)
# define a(n):
# if n = 1, then return a(1)
# if not, then return 2*a(n-1) + 3
def a(n):
     if n == 1:
         return 4
     else:
         return 2*a(n-1) + 3
# to have only the first five values
# from n=1 to n=5 
#      give me a(n) as I defined
for n in range (1,6):
    print (a(n))
