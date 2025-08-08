# Problem:
# You are given a list of integers. Write a Python program to find all pairs of numbers in the list that sum up to a target value.

# Example 1:
# Input: nums = [2, 4, 3, 7, 5, 1,3], target = 6  
# Output: [(2, 4), (5, 1), (3, 3)]  # order inside the pair doesn’t matter
# Example 2:
# Input: nums = [1, 2, 3, 4, 5], target = 10  
# Output: []
# Constraints:

# Each number can be used only once in a pair.

# The output can be in any order.
def pair_nums(a, b):
    c = set()
    d = []
    for e in a:
        f = b - e
        if f in c:
            d.append((f, e))
        c.add(e)
    print(d)

pair_nums([2, 4, 3, 7, 5, 1,3], 6)
pair_nums([1, 2, 3, 4, 5],10)