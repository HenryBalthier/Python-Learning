class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False
        for i in range(m):
            if target < matrix[i][0]:
                break
            elif target > matrix[i][-1]:
                continue
            for j in range(n):
                if target < matrix[i][j]:
                    break
                elif target > matrix[i][j]:
                    continue
                else:
                    return True
        return False


s = Solution()
x = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
t = 35
print(s.searchMatrix(x, t))