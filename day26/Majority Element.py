#  Problem 1: Majority Element
# Description:
# Given a list of integers, find the element that appears more than n/2 times.
# If no such element exists, return "None".

# Example:
# Input: [3, 3, 4, 2, 3, 3, 5]
# Output: 3
# Input: [1, 2, 3, 4]
# Output: None
def majority_element(n):
    a=len(n)/2
    b={}
    for i in n:
        if i not in b:
            b[i]=1
        else:
            b[i]+=1
    for i,v in b.items():
        if v>a:
            print(i)
    return "None"
majority_element([3, 3, 4, 2, 3, 3, 5])
majority_element([1, 2, 3, 4])