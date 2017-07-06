class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0 or n == 0:
            return 0
        paths = [[1]*n for _ in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                paths[i][j] = paths[i-1][j] + paths[i][j-1]
        return paths[-1][-1]

s = Solution()
m = 3
n = 3
print(s.uniquePaths(m,n))