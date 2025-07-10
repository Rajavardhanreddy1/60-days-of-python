# Problem 13: Find the Maximum Number in a List
# 🧠 Problem:
# Write a Python function to find the maximum number in a given list without using the built-in max() function.

# Input Example:
# [2, 45, 7, 23, 89, 12]
# Expected Output:
# 89
def max_num(n):
    a=1
    for i in n:
        if i>a:
            a=i
    print(a)
max_num([2, 45, 7, 23, 89, 12])