class Solution:

    def stringCompression(self,s):
        new_string = []
        count = 0
        for idx in range(len(s)):
            count += 1
            if idx != len(s) - 1 and s[idx] != s[idx+1]:
                new_string.append(s[idx])
                new_string.append(str(count))
                count = 0
        new_string.append(s[-1])
        new_string.append(str(count))
        if len(new_string) <= len(s):
            return ''.join(new_string)
        else:
            return s

print(Solution().stringCompression('abbbaa'))