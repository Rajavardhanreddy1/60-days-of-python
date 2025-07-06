# Problem 3: Count Strong Numbers in a Given Range
# Input: L = 1, R = 1000
# Output: 3
# Explanation: There are 3 strong numbers: 1, 2, 145
import math
def str_num(n):
    b=0
    for i in range(n+1):
        a=0
        for j in str(i):
            a+=math.factorial(int(j))
        if a==i:                 
            b+=1
        else:
            pass
    print(b)
str_num(1000)