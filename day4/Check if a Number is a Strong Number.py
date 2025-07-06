# Problem 1: Check if a Number is a Strong Number
# Input: n = 145
# Output: Yes
# Explanation: 1! + 4! + 5! = 145
def strong_number(n):
    a=0
    for i in str(n):
        b=int(i)
        def fact(b):
            if b==1 or b==0:
                return 1
            else:
                return b*fact(b-1)
        a+=fact(b)
    if a==n:
        print("yes")
    else:
        print("no")
strong_number(145)