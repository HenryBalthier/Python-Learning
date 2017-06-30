class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        res = -9999
        MAX = []
        MIN = []

        for i in arrays:
            MAX.append(i[-1])
            MIN.append(i[0])
        MAXX = sorted(MAX)
        MINN = sorted(MIN)
        print(MAX, MIN, MAXX, MINN)
        m1 = MAXX[-1]
        m2 = MAXX[-2]
        n1 = MINN[0]
        n2 = MINN[1]

        for i, v in enumerate(MAX):
            if v == m1 and (n1 in (MIN[:i] + MIN[i+1:])):
                print(v)
                return m1 - n1
        return max(m1 - n2, m2 - n1)





s = Solution()
x = [[1,4], [0, 5]]
print(s.maxDistance(x))