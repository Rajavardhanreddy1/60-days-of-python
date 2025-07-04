# Problem 1: Print First N Fibonacci Numbers
# Write a program to print the first N numbers of the Fibonacci series.
# Input: N = 7
# Output: 0 1 1 2 3 5 8
def fibonacci_numbers(N):
    a=[]
    for i in range(0,N):
        if len(a)<2:
            a.append(i)
        elif len(a)>=2:
            b=a[-1]+a[-2]
            a.append(b)
    print(a)
fibonacci_numbers(20)