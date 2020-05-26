class Solution():

    def zeroMatrix(self,matrix):

        # # O(M + N) space complexity
        # rows = set()
        # cols = set()
        #
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if matrix[i][j] == 0:
        #             rows.add(i)
        #             cols.add(j)
        #
        # for row in rows:
        #     for col in range(len(matrix[0])):
        #         matrix[row][col] = 0
        #
        # for col in cols:
        #     for row in range(len(matrix)):
        #         matrix[row][col] = 0
        #
        # return matrix


        # O(1) space complexity

        firstRow = False
        firstCol = False

        # First check the first row and column
        for col in range(len(matrix[0])):
            if matrix[0][col] == 0:
                firstRow = True
                break

        for row in range(len(matrix)):
            if matrix[row][0] == 0:
                firstCol = True
                break

        # Check for 0 in matrix expect firstRow and firstCol
        for row in range(1,len(matrix)):
            for col in range(1,len(matrix[0])):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0

        # Update zeros for inner layer matrix rows and col
        for row in range(1,len(matrix)):
            if matrix[row][0] == 0:
                for col in range(len(matrix[0])):
                    matrix[row][col] = 0

        for col in range(1,len(matrix[0])):
            if matrix[0][col] == 0:
                for row in range(len(matrix)):
                    matrix[row][col] = 0

        # Update zeros for first row and column
        if firstRow:
            for col in range(len(matrix[0])):
                matrix[0][col] = 0

        if firstCol:
            for row in range(len(matrix)):
                matrix[row][0] = 0

        return matrix


print(Solution().zeroMatrix([[1,0]]))