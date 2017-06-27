class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        sum = 0
        for index, i in enumerate(points):
            d = {}
            for j in points:
                m = i[0] - j[0]
                n = i[1] - j[1]
                mn = m * m + n * n
                d[mn] = 1 + d.get(mn, 0)
            print(d)
            for ii in d:
                sum += d[ii] * (d[ii] - 1)
        return sum




if __name__ == '__main__':
    s = Solution
    p = [[0,0],[1,0],[-1,0],[0,1],[0,-1]]
    print(s.numberOfBoomerangs(s, p))