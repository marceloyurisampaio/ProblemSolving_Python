Example Input
A: [2, 7, 11, 15]
B: 9


Example Output
[1, 2]

class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return a list of integers
	def twoSum(self, A, B):
        hmap = {}
        for i in range(0,len(A)): 
            target = B - A[i]
            if target in hmap: 
                return [hmap[target]+1, i+1]
            if A[i] not in hmap: 
                hmap[A[i]] = i
        return []
