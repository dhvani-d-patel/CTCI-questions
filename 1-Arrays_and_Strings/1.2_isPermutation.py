class Solution:

    def isPermutation(self,s1,s2):
        # # Using sorting string, time complexity -> O(N log N)
        # if len(s1) != len(s2):
        #     return False
        #
        # s1 = sorted(s1)
        # s2 = sorted(s2)
        # return s1==s2

        # Using hashtable, time complexity -> O(N)
        if len(s1) != len(s2):
            return False

        hash_table_s1 = {}
        hash_table_s2 = {}

        for idx in range(len(s1)):
            ch_1 = s1[idx]
            ch_2 = s2[idx]

            if ch_1 in hash_table_s1:
                hash_table_s1[ch_1] += 1
            else:
                hash_table_s1[ch_1] = 1

            if ch_2 in hash_table_s2:
                hash_table_s2[ch_2] += 1
            else:
                hash_table_s2[ch_2] = 1

        return hash_table_s1 == hash_table_s2


print(Solution().isPermutation('abd', 'cba'))