class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        l = len(triangle)
        if l == 1:
            return triangle[0][0]
        i = l-2

        while i >= 0:
            tmp = []
            for j in range(i+1):
                tmp.append(triangle[i][j] + min(triangle[i+1][j], triangle[i+1][j+1]))
            triangle[i] = tmp
            i -= 1

        return triangle[0][0]

s = Solution()
x = [
     [2],
    [3,4]
]

print(s.minimumTotal(x))