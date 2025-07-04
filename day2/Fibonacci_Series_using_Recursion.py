# Problem 4: Fibonacci Series using Recursion
# Write a recursive function to print the Fibonacci series up to N terms.
# Input: N = 5
# Output: 0 1 1 2 3
def fib_using_recursion(n):
    if n<=1:
        return n
    else:
        return fib_using_recursion(n-1)+fib_using_recursion(n-2)
def print_fib_series(n):
    for i in range(n):
        print(fib_using_recursion(i),end=' ')
print_fib_series(10)