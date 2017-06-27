class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        s = bin(n)[2:]
        n = 32 - len(s)
        ss = '0' * n + s
        res = '0b' + ss[::-1]
        return int(res, 2)

s = Solution()
n = 9
print(s.reverseBits(n))