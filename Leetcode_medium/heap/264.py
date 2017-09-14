class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return

        s = {2, 3, 5}
        n -= 1
        Min = 1
        while n:
            Min = min(s)
            s.remove(Min)
            s.add(Min*2)
            s.add(Min*3)
            s.add(Min*5)
            n -= 1
        return Min

if __name__ == '__main__':
    s = Solution()
    n = 206
    print(s.nthUglyNumber(n))