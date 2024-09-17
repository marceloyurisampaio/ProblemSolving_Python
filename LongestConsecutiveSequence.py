Example: 

Given [100, 4, 200, 1, 3, 2],

The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.

class Solution:
	# @param A : tuple of integers
	# @return an integer
	def longestConsecutive(self, A):
        hmap = {}
        for c in A:
            if c not in hmap:
                hmap[c] = 1
            else: 
                hmap[c] += 1
        
        max_len, curr_len = 0,0
        for i in range(0,len(A)):
            elem = A[i]
            prev_e = elem - 1
            next_e = elem + 1
            if prev_e not in hmap:
                curr_len += 1
                while next_e in hmap: 
                    curr_len += 1
                    next_e += 1
                max_len = max(max_len, curr_len)
            curr_len = 0
        return max_len
