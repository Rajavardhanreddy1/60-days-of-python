# Problem 5: Is Factorial?
# Check if a given number is a factorial of any number.
#  Example: 120 → True (5!), 150 → False
def gactorial(n):
    a=1
    for i in range(1,n+1):
        a*=i
        if a>=n:
            break
    if a==n:
        return True
    else:
        return False
gactorial(150)