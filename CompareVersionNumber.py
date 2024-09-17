Problem Description
 
 

Compare two version numbers version1 and version2.
If version1 > version2 return 1,
If version1 < version2 return -1,
otherwise return 0.
You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences. For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Note: Here is an example of version numbers ordering:
0.1 < 1.1 < 1.2 < 1.13 < 1.13.4

class Solution:
	# @param A : string
	# @param B : string
	# @return an integer
	def compareVersion(self, A, B):
        v1 = A.split(".")
        v2= B.split(".")
        N1 = len(v1)
        N2 = len(v2)
        
        for i in range(max(N1,N2)):
            n1 = 0 if i >= N1 else int(v1[i])
            n2 = 0 if i >= N2 else int(v2[i])    
            
            if n1 > n2: 
                return 1
            elif n1 < n2: 
                return -1
        
        return 0     
