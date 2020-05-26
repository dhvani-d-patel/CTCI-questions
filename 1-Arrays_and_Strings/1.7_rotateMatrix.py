class Solution:

    def rotateMatrix(self,matrix):
        new_matrix = [[0]*len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix[0])):

            new = []
            for j in range(len(matrix)):
                new.append(matrix[j][i])
            new_matrix.append(new[::-1])
        return new_matrix[len(matrix):]

print(Solution().rotateMatrix([[1,2,3,10],[4,5,6,11],[7,8,9,12]]))