class Solution():

    def isOneEditAway(self,s1,s2):
        if len(s1) < len(s2):
            s1,s2 = s2,s1

        if len(s1)-len(s2) > 1:
             return False

        idx1 = idx2 = 0
        count_diff = 0

        while idx1 < len(s1) and idx2 < len(s2):
            if s1[idx1] != s2[idx2]:
                count_diff += 1
                if count_diff > 1:
                    return False

                if len(s1) == len(s2):  # Replace check
                    idx1 += 1
                    idx2 += 1
                else:                   # Remove/insert check
                    idx1 += 1
            else:
                idx1 += 1
                idx2 += 1
        return count_diff <= 1



print(Solution().isOneEditAway('a',''))