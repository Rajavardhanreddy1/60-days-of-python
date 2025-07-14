#worked on hacker rank problem ginortS
s=sorted(input())
d={'lower':'','upper':'','odd':'','even':''}
for i in s:
    if i.islower():
        d['lower']+=i
    elif i.isupper():
        d['upper']+=i
    elif i.isdigit:
        if int(i)%2!=0:
            d['odd']+=i
        else:
            d['even']+=i
print(''.join(d.values()))
