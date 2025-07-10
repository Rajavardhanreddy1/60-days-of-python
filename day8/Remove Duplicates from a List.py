# Problem 5: Remove Duplicates from a List
# Problem:
# Write a Python function to remove duplicates from a list and return a list with only unique values (keep the original order).

# Input Example:
# [4, 5, 4, 6, 5, 7]
# Expected Output:
# [4, 5, 6, 7]
def dup(n):
    a=set(n)
    print(list(a))
dup([4, 5, 4, 6, 5, 7])