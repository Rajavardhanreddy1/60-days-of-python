# 2. Reverse Each Word in a Sentence
# Let’s take:
# Input: "Hello world this is GPT"
# Expected Output: "olleH dlrow siht si TPG"
def rev_wor(n):
    a=n.split()
    b=[]
    for i in a:
        b.append(i[::-1])
    
    print(' '.join(b))
rev_wor("Hello world this is GPT")