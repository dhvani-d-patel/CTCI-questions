class Solution:

    def rotateMatrix(self,matrix):

        # Transpose and then reverse each row of matrix
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i < j:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for row in range(len(matrix)):
            matrix[row]= matrix[row][::-1]
        return matrix


print(Solution().rotateMatrix([[1,2,3],[4,5,6],[7,8,9]]))