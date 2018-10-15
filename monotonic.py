class Solution:
    def isMonotonic(A):
        B = A
        C = A[::-1]
        if B == sorted(A):
            return True
        elif C == sorted(A):
            return True
        else:
            return False




c = [1,2,2,3]
sol1 = Solution.isMonotonic(c)
print(sol1)
