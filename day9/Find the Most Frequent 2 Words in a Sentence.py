# Problem 17: Find the Most Frequent 2 Words in a Sentence
# 🧠 Problem:
# Write a Python program to find the top 2 most frequent words in a given sentence. Ignore case and punctuation.

# Input Example:
# "The sun shines over the lake. The sun is bright and the lake is calm."
# Expected Output:

# 'the' → 4 times  
# 'lake' → 2 times
def most_freq(n):
    a=n.replace('.','').lower().split()
    b={}
    for i in a:
        if i not in b:
            b[i]=1
        else:
            b[i]+=1
    word=sorted(b.items(),key=lambda x:x[1],reverse=True)
    for i in word[:2]:
        print(i)
most_freq("the sun shines over  the lake. the sun is bright and the lake is calm.")