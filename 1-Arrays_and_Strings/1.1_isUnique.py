class Solution:

    def is_unique(self,s):
        # # Using arrays
        # occurence = [False] * 128
        # for ch in s:
        #     if occurence[ord(ch)]:
        #         return False
        #     else:
        #         occurence[ord(ch)] = True
        # return True

        # Using bit manipulation
        checker = 0
        for ch in s:
            value = 128 - ord(ch)
            if ((checker & (1 << value)) > 0):
                return False
            checker = checker | (1 << value)
        return True

print(Solution().is_unique('a%$bcsf!Ad#@$'))