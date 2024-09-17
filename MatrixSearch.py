Problem Description
 
 

Given a matrix of integers A of size N x M and an integer B. Write an efficient algorithm that searches for integer B in matrix A. 

This matrix A has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than or equal to the last integer of the previous row.
Return 1 if B is present in A, else return 0.

NOTE: Rows are numbered from top to bottom, and columns are from left to right.

class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, B):
        row_selected = 0
        
        #Number of rows and columns
        N = len(A)
        M = len(A[0])
        
        #Finding the maximum first element of a row that is lower than B
        start,end = 0, N-1
        while start <= end: 
            mid = start + (end - start)//2
            if A[mid][0] == B:
                return 1
            elif A[mid][0] < B: 
                start = mid + 1
            else: 
                end = mid - 1
        
        row_selected = end
        
        #Finding the element inside of the selected row
        start,end = 0, M-1
        while start <= end: 
            mid = start + (end - start)//2
            if A[row_selected][mid] == B:
                return 1
            elif A[row_selected][mid] < B: 
                start = mid + 1
            else: 
                end = mid - 1
        
        return 0
