# Problem:
# Given a string, find the length of the longest substring without repeating characters.
def f(a):
    b = set()
    c = 0
    d = 0
    e = 0
    while d < len(a):
        if a[d] not in b:
            b.add(a[d])
            d += 1
            c = max(c, d - e)
        else:
            b.remove(a[e])
            e += 1
    return c

print(f("abcabcbb"))
print(f("bbbbb"))
print(f("pwwkew"))