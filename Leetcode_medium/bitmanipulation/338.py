class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = []
        for i in range(num+1):
            s = str(bin(i))[2:]
            res.append(s.count('1'))
        return res


s = Solution()
x = 5
print(s.countBits(x))