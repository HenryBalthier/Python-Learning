class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = int(n / 2) + 1
        lst = []
        for i in range(2, l+1):
            m = n
            j = i
            tmp = []
            while m % j != 0:
                tmp.append(int(m / j))
                m -= int(m / j)
                j -= 1
            t = [int(m / j)] * j
            tmp += t
            if len(tmp) > 1:
                lst.append(tmp)
        if lst == []:
            return 1
        res = []
        for i in lst:
            tmp = 1
            for j in i:
                tmp *= j
            res.append(tmp)
        #print(res)
        return max(res)

if __name__ == '__main__':
    s = Solution()
    n = 50
    print(s.integerBreak(n))