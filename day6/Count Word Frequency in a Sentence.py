# Problem 9: Count Word Frequency in a Sentence
# Problem Statement:
# Write a Python function that takes a sentence as input and returns the frequency of each word (case-insensitive, ignore punctuation).

# Example Input:
# "Hello hello world, hello again world"
# Expected Output:
# {'hello': 3, 'world': 2, 'again': 1}
def count_word_frequency(n):
    d={}
    a=n.lower().split()
    for i in a:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    print(d)
count_word_frequency("Hello hello world, hello again world")
    