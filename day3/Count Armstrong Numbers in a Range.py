# Problem 4: Count Armstrong Numbers in a Range
# Write a program to count how many Armstrong numbers are there between two given numbers.
# Input: 1 to 1000
# Output: Number of Armstrong numbers = 10
def count_armstrong_numbers_in_a_range(n):
    c=0
    for i in range(n):
           a=str(i)
           b=0
           for j in a:
              b+=int(j)**len(a)
           if i==b:
              c+=1
    print(c)
count_armstrong_numbers_in_a_range(10000)