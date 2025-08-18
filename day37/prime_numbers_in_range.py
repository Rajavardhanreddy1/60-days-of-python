def f(a, b):
    c = []
    for d in range(a, b + 1):
        if d > 1:
            e = True
            for g in range(2, int(d**0.5) + 1):
                if d % g == 0:
                    e = False
                    break
            if e:
                c.append(d)
    return c

print(f(2, 10))
print(f(14, 16))
