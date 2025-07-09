# Problem 6: Factorial Series
# Generate a list of factorials for numbers from 1 to N.
def factorial_series(n):
    if n==0:
        return 1
    else:
        a=1
        for i in range(1,n+1):
            a*=i
            print(a)
factorial_series(25)