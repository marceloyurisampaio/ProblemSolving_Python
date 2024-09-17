Example Input
Input 1:

 A = [cat, dog, god, tca]
Input 2:

 A = [rat, tar, art]


Example Output
Output 1:

 [ [1, 4],
   [2, 3] ]
Output 2:

 [ [1, 2, 3] ]

class Solution:
	# @param A : tuple of strings
	# @return a list of list of integers
	def anagrams(self, A):
        res = {}
        
        for i in range(0,len(A)):
            s = A[i]
            count = [0]*26
            for c in s:
                count[ord(c) - ord("a")] += 1
            count_tuple = tuple(count)
            if count_tuple not in res: 
                res[count_tuple] = []
            res[count_tuple].append(i+1)
        
        return list(res.values())
