class Solution():

    def URLify(self,l,true_length):
        space_count = 0

        for idx in range(true_length):
            if l[idx] == ' ':
                space_count += 1


        actual_length = true_length + (space_count*2) - 1

        l = l[:actual_length+1]

        for idx in range(true_length-1,-1,-1):
            if l[idx] == ' ':
                l[actual_length] = '0'
                l[actual_length-1] = '2'
                l[actual_length-2] = '%'
                actual_length -= 3
            else:
                l[actual_length] = l[idx]
                actual_length -= 1
        return l



print(Solution().URLify(list("Mr John Smith         "),13))