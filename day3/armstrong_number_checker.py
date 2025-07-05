# Armstrong Number Problems
#  Problem 1: Check Armstrong Number (3-digit)
# Write a program to check whether a 3-digit number is an Armstrong number or not.
# An Armstrong number is a number such that:
# abc = a³ + b³ + c³
# Input: 153
# Output: Yes, it is an Armstrong number
def armstrong_number_checker(n):
    a=str(n)
    b=0
    if len(a)==3:
        for i in a:
            b+=int(i)**len(a)
        if n==b:
            print("Yes, it is an Armstrong number")
        else:
            print("No, it is not Armstrong number")
    else:
        print("expecting 3 digit number only")
armstrong_number_checker(153)