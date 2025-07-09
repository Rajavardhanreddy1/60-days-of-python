# Problem 3: Large Factorial
# Find the last non-zero digit of the factorial of n.
def factor_iterat(n):
    a=1
    for i in range(1,n+1):
        a*=i
    c=str(a)
    for i in range(1,len(c)):
        if c[-i]=='0':
           pass
        else:
            print(c[-i])
            break        
    
factor_iterat(5)