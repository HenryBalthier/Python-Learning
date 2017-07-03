class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        low = n*n+1
        while low > 1:
            high, low = low, low - len(res)
            lst = [[i for i in range(low, high)]]

            res = lst + list(map(list, zip(*res[::-1])))
        return res


s = Solution()
x = 3
print(s.generateMatrix(x))