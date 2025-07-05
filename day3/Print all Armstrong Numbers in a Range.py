# Problem 3: Print all Armstrong Numbers in a Range
# Write a program that prints all Armstrong numbers between 1 and 10000.
# Output:
# 1 2 3 4 5 6 7 8 9 153 370 371 407 1634 8208 9474
def print_n_armstrong_number(n):
    for i in range(n):
        a=str(i)
        b=0
        for j in a:
            b+=int(j)**len(a)
        if i==b:
            print(b,end=' ')
print_n_armstrong_number(10000)