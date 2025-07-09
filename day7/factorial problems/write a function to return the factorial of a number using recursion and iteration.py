# Problem 1: Basic
# Write a function to return the factorial of a number using recursion and iteration.
def fact_rec(n):
    if n==0 or n==1:
        return 1
    elif n==2:
        return 2
    else:
        return n*fact_rec(n-1)
fact_rec(9)


def fact_iter(n):
    a=1
    for i in range(1,n+1):
        a*=i
    if n==0 or n==1:
        print(1)
    else:
        print(a)
fact_iter(5)