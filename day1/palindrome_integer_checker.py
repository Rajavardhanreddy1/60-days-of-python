# Problem Statement:

# Write a Python program to check whether a given integer is a palindrome.
# An integer is called a palindrome when it reads the same backward as forward.
# Example:
# vbnet
# Copy
# Edit
# Input: 121
# Output: True
# Input: -121
# Output: False  (reads 121- backward)
# Input: 123
# Output: False
# Constraints:
# Do not convert the number to a string.
# Try solving using mathematical operations

def palindrome_checker(num):
    c=num
    r=str(num)
    a=0
    for i in range(len(r)):
        b=c%10
        a=a*10+b
        c//=10
    return str(num)==str(a)
palindrome_checker(123)