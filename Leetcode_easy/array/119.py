class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        res = [[1]]
        for i in range(numRows):
            a = res[-1] + [0]
            b = [0] + res[-1]
            c = []
            for j in range(i+2):
                c += [a[j] + b[j]]
            res.append(c)
        return res[-1]



if __name__ == '__main__':
    s = Solution
    n = 3
    print(s.generate(s, n))