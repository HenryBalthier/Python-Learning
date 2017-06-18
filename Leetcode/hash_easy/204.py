class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        res = [1] * n
        res[0] = res[1] = 0
        for i in range(int(n ** 0.5)+1):
            if res[i]:
                res[i*i:n:i] = [0] * len(res[i*i:n:i])
        return sum(res)


if __name__ == '__main__':
    s = Solution()
    n = 100
    print(s.countPrimes(n))