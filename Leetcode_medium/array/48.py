class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n//2):
            for j in range(n-n//2):
                matrix[~j][i], matrix[~i][~j], matrix[j][~i], matrix[i][j]= \
                    matrix[i][j], matrix[~j][i], matrix[~i][~j], matrix[j][~i]
        return matrix

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
x = [1,2,3]
y = [4,5,6]
z = [7,8,9]
x2 = list(map(list,zip(*a[::-1])))
print(x2)
print(~3)
s = Solution()
print(s.rotate(a))