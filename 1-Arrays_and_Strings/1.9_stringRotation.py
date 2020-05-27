class Solution():

    def stringRotation(self,A,B):
        if A == B:
            return True
        for i in range(len(A) - 1, -1, -1):
            if A[i:] + A[:i] == B:
                return True
        return False

print(Solution().stringRotation('waterbottle','erbottlewat'))