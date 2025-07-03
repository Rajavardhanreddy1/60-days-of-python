# 2. Palindrome String (String Way)
# Problem Statement:
# Write a Python function to check if a given string is a palindrome.
# A string is a palindrome if it reads the same backward as forward.
# Example:
# vbnet
# Copy
# Edit
# Input: "madam"
# Output: True
# Input: "hello"
# Output: False
# Input: "A man, a plan, a canal: Panama"
# Output: True  (Ignore cases, spaces, punctuation)
# Optional Challenge:
# Ignore non-alphanumeric characters and consider case-insensitivity.
def palindrome_string_checker(word):
    a=''
    b=''
    c=len(word)
    for i in range(0,len(word)):
        if word[i].isalpha():
            a+=word[i]
        if word[c-1].isalpha():
            b+=word[c-1]
        c-=1
            
    return a.lower()==b.lower()
palindrome_string_checker("A man, a plan, a canal: Panama")