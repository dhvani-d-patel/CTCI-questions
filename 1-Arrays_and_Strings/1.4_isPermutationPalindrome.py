class Solution():

    def isPermutationPalindrome(self,s):
        # # Hashtable, time complexity -> O(N)
        # hashmap = {}
        # odd_count = 0
        # for ch in s:
        #     if ch != ' ':
        #         if ch not in hashmap:
        #             hashmap[ch] = 1
        #             odd_count += 1
        #         else:
        #             if hashmap[ch]%2 == 0:
        #                 odd_count += 1
        #             else:
        #                 odd_count -= 1
        #             hashmap[ch] += 1
        # return odd_count <= 1

        # # 26 length array, time complexity -> O(N)
        # char_array = [0]*26
        # odd_count = 0
        # for ch in s:
        #     if ch != ' ':
        #         index = ord(ch) - 97
        #         if char_array[index] % 2 == 0:
        #             odd_count += 1
        #         else:
        #             odd_count -= 1
        #         char_array[index] += 1
        # return odd_count <= 1


        # Bit manipulation, saves space complexity
        bit_vector = 0
        for ch in s:
            if ch != ' ':
                index = ord(ch) - 97 + 1
                mask = 1 << index

                if (bit_vector & mask) == 0:
                    bit_vector |= mask
                else:
                    bit_vector &= ~mask

        return bit_vector == 0 or (bit_vector & (bit_vector-1)) == 0




print(Solution().isPermutationPalindrome('taco catod'))