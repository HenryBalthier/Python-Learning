class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        m = int(area ** 0.5)
        while m >= 1:
            if area % m == 0:
                return [area//m, m]
            m -= 1

s = Solution()
x = 7
print(s.constructRectangle(x))