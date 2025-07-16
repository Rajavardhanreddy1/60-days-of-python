#Pythagorean Triplet
#Given an array arr[], return true if there is a triplet (a, b, c) from the array (where a, b, and c are on different indexes) that satisfies a2 + b2 = c2, otherwise return false.
#Input: arr[] = [3, 2, 4, 6, 5]
#Output: true
#Explanation: a=3, b=4, and c=5 forms a pythagorean triplet.
class Solution:
	def pythagoreanTriplet(self, arr):
    	# code here
    	a=[i**2 for i in arr]
    	b=set(a)
    	c=len(a)
    	for i in range(c) :
    	    for j in range(i+1,c):
    	        if a[i]+a[j] in b:
    	            return True
    	        
    	else:
    	    return False