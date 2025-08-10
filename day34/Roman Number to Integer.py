#Roman Number to Integer
def f(a):
    b = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    c = 0
    d = 0
    for e in a[::-1]:
        f = b[e]
        if f < d:
            c -= f
        else:
            c += f
        d = f
    return c

print(f("IX"))
print(f("XL"))
print(f("MCMIV"))
