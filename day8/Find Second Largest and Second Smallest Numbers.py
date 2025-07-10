# Problem 14: Find Second Largest and Second Smallest Numbers
# 🧠 Problem A: Find Second Largest Number
# Description:
# Write a Python function that returns the second largest number in a list.

# Input:
# [4, 1, 7, 9, 3]
# Expected Output:
# 7
def sec_lar_sma(n):
    a=sorted(n)
    print(f'largest number was {a[-2]} and smallest number was {a[1]}')
sec_lar_sma([4, 1, 7, 9, 3])