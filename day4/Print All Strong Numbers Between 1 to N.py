# Problem 2: Print All Strong Numbers Between 1 to N
# Input: N = 1000
# Output: 1 2 145
import math
def str_num(n):
    for i in range(n+1):
        a=0
        for j in str(i):
            
            a+=math.factorial(int(j))
        if a==i:
                             
            print(i,end=' ')
        else:
            pass
str_num(1000)