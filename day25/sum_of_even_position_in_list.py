# Problem: Sum of Numbers at Even Indices
# 📝 Description:
# Write a Python program that takes a list of integers and returns the sum of the numbers at even indices (i.e., index 0, 2, 4, ...).

# 📥 Example Input:
# numbers = [10, 5, 20, 15, 30, 25]
# 📤 Expected Output:
# Sum of numbers at even indices: 60
# Explanation: Elements at indices 0, 2, and 4 → 10 + 20 + 30 = 60
def sum_num(n):
    a=0
    b=0
    for i in range(len(n)//2):
        b+=n[a]
        a+=2
    return b
sum_num([10, 5, 20, 15, 30, 25])