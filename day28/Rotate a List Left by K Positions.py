# Problem 3: Rotate a List Left by K Positions
# Description:
# Rotate a list to the left by k positions without using built-in slicing.

# Example:
# Input: nums = [1, 2, 3, 4, 5], k = 2
# Output: [3, 4, 5, 1, 2]
def lis_lef_pos_(nums,k):
    a=[]
    for i in range(k,len(nums)):
        a.append(nums[i])
    for i in range(0,k):
        a.append(nums[i])
    return a
lis_lef_pos_([1, 2, 3, 4, 5],2)