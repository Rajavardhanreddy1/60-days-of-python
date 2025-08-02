# Problem 2: Count Characters Between Matching Pairs
# Description:
# Given a string, count the number of characters between the first and last occurrence of a given character.

# Example:
# Input: s = "abXcdXeXfXgh", char = "X"
# Output: 8  # characters between the first X and last X
# If the character occurs less than 2 times, return 0.
#method1
def count_char(s,char):
    a=s.count(char)
    b=s.index(char)
    c=1
    d=0
    for i in range(b,len(s)+1):
        if s[i]==char:
            d+=1
        if d==a:
            break
        c+=1
    print(c)
count_char("abXcdXeXfXgh","X")
#method2
def count_chars(s, char):
    first = s.index(char)
    last = s.rindex(char)
    count = last - first + 1
    print(count)

count_chars("abXcdXeXfXgh", "X")