# Problem 4: Sum of Digits in Factorial
# Compute n!, then return the sum of its digits.
# Example: 5! = 120 ⇒ 1+2+0 = 3
def factori_iterata(n):
    a=1
    for i in range(1,n+1):
        a*=i
    c=str(a)
    b=0
    for i in c:
        b+=int(i)
    print(b)
                
    
factori_iterata(5)