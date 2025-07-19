# Problem 2: Trailing Zeros
# Write a function that returns the number of trailing zeros in the factorial of a number.
#  Hint: Count factors of 5
def facto_itera(n):
    a=1
    for i in range(1,n+1):
        a*=i
    b=0
    c=str(a)
    for i in range(1,len(c)):
        if c[-i]=='0':
           b+=1
        else:
            break
    print(b)          
    
facto_itera(100)