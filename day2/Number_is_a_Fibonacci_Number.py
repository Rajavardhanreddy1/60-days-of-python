# Problem 3: Check if a Number is a Fibonacci Number
# Write a function to check whether a given number is a Fibonacci number or not.
# Input: 21
# Output: Yes
def Fib_num(n):
    a=[0,1]
    while a[-1]<n:
        b=a[-1]+a[-2]
        a.append(b)
    if a[-1]==n or n==0:
        return 'yes'
    else:
        return 'no'
Fib_num(0)