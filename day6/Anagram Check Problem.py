# Anagram Check Problem
# Problem Statement:
# Write a Python function that checks if two given strings are anagrams of each other (ignore spaces and case).

# Example Input:
# str1 = "Listen"
# str2 = "Silent"
# Expected Output:
# True
def anagram(str1,str2):
    str1=str1.lower().replace(" ",'')
    str2=str2.lower().replace(" ",'')
    if len(str1)!=len(str2):
        return False
    return sorted(str1)==sorted(str2)
anagram("Listen","Silent")