# Problem 2: Check Armstrong Number (n-digit)
# Write a program to check whether an n-digit number is an Armstrong number.
# Input: 9474 (4-digit)
# Output: Yes (since 9⁴ + 4⁴ + 7⁴ + 4⁴ = 9474)
def armstrong_number_checker(n):
    a=str(n)
    b=0
    for i in a:
        b+=int(i)**len(a)
    if n==b:
        print("Yes, it is an Armstrong number")
    else:
        print("No, it is not Armstrong number")
armstrong_number_checker(9474)