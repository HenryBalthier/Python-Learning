class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = str(bin(n))[2:]
        return s.count('1')

s = Solution()
x = 11
print(s.hammingWeight(x))