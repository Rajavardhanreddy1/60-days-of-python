# Problem 2: Find Nth Fibonacci Number
# Write a function that returns the Nth Fibonacci number using recursion or iteration.
# Input: N = 6
# Output: 8
def fibonaacci_number_recursion(N):
    if N==1:
        return 0
    elif N==2:
        return 1
    else:
        return fibonaacci_number_recursion(N-1)+fibonaacci_number_recursion(N-2)
fibonaacci_number_recursion(20)