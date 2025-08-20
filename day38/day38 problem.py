# You are given a number.
# Find the sum of its digits raised to the power of their position (from left to right), and check if it equals the original number.

# This is somewhat like a special number check (not a direct Armstrong number).

# Example:

# Input: a = 3435

# Calculation:

# 3¹ + 4² + 3³ + 5⁴ = 3 + 16 + 27 + 625 = 671 (not equal → False)

# Input: a = 89

# 8¹ + 9² = 8 + 81 = 89 (equal → True ✅)
a = int(input("Enter a number: "))

b = str(a)   
c = 0        #
d = 1      

for digit in b:
    c += int(digit) ** d
    d += 1

print("Special Number?" , c == a)
