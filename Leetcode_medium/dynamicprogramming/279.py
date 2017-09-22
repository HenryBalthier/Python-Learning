class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """

        def func(n, count):
            print(n, count, res)

            if n == 0:
                res.append(count)
                return

            if count >= res[-1] - 1:
                return

            m = int(n ** 0.5)
            for i in range(m, 0, -1):
                func(n - i ** 2, count + 1)

        res = [999999]
        if n == 1:
            return 1

        m = int(n ** 0.5)
        for i in range(m, 0, -1):
            func(n - i ** 2, 1)
        return min(res)


if __name__ == '__main__':
    s = Solution()
    x = 7168
    print(s.numSquares(x))