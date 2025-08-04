# Problem: Find All Duplicates in a List
# 📝 Description:
# Given a list of integers, write a Python program to find all the elements that appear more than once and return them in a new list.

# 📥 Input:
# nums = [4, 3, 2, 7, 8, 2, 3, 1]
# 📤 Expected Output:
# [2, 3]
# The duplicates should be listed once, even if they appear more than twice.

# ✅ Bonus:
# Try solving it without using any libraries like collections.Counter.
def fin_all_dup(nums):
    a=[]
    for i in nums:
        if i not in a:
            if nums.count(i)>1:
                a.append(i)
    return a
print(fin_all_dup([4, 3, 2, 7, 8, 2, 3, 1]))
#method2
def find_all_duplicates(nums):
    f= {}
    r= []

    for i in nums:
        if i in f:
            f[i] += 1
        else:
            f[i] = 1

    for j in f:
        if f[j] > 1:
            r.append(j)

    return r

print(find_all_duplicates([4, 3, 2, 7, 8, 2, 3, 1]))  