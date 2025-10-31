#Reverse words in a sentence without using split()

a="raja rajesh rakesh"
b=[]
c=""
for i in range(len(a)):
    if a[i].isalpha():
        c=a[i]+c
    else:
        b.append(c+" ")
        c=""
b.append(c)   
print(" ".join(b))