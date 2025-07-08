# Problem 8: Count Letter Frequency in a String
# Problem Statement:
# Write a Python function that takes a string as input and returns a dictionary with the frequency of each letter (ignore spaces and make it case-insensitive).
# Example Input:
# "Hello World"
# Expected Output:
# {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}
def count_letter_frequency(n):
    d={}
    for i in n:
        if i.isalpha():
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
    print(d)
count_letter_frequency("Hello World")