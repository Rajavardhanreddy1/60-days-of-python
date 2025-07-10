# Problem 16: Find the Most Repeated Number in a List
# 🧠 Problem:
# Write a Python program to find the number that appears most frequently in a list.

# Input Example:
# Edit
# [1, 3, 1, 7, 3, 3, 1, 2]
# Expected Output:

# 1  → 3 times
def rep(n):
    a={}
    for i in n:
        if i not in a:
            a[i]=1
        else:
            a[i]+=1
    b,c=0,0
    for i,v in a.items():
        if v>b:
            b=v
            c=i
    print(c)
rep([1, 3, 1, 7, 3, 3, 1, 2])