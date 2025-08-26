class Solution:
    def minMaxCandy(self, a, b):
        a.sort()
        n = len(a)
        
        x = 0
        i, j = 0, n - 1
        while i <= j:
            x += a[i]
            i += 1
            j -= b
        
        y = 0
        i, j = 0, n - 1
        while i <= j:
            y += a[j]
            j -= 1
            i += b
        
        return [x, y]
