class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        def helper(m, res):
            n = []
            if m == [[]] or m == []:
                return res
            res += m[0]
            n[:] = m[1:]
            n = list(map(list, zip(*n)))[::-1]
            return helper(n, res)
        return helper(matrix, [])


s = Solution()
x = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
print(s.spiralOrder(x))