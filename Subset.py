Example Input
A = [1, 2, 3]


Example Output
[
 [],
 [1],
 [1, 2],
 [1, 2, 3],
 [1, 3],
 [2],
 [2, 3],
 [3],
]

class Solution:
	# @param A : list of integers
	# @return a list of list of integers          
	def subsets(self, A):
        def backtrack (start, curr): 
            ans.append(curr[:])
            for i in range(start, len(A)): 
                curr.append(A[i])
                backtrack(i+1,curr)
                curr.pop()
        A.sort()
        ans = []
        curr = []
        backtrack (0, curr)      
        return ans
