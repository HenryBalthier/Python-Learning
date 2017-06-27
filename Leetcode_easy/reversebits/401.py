class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        assert 0 <= x <= 10
        res = []
        for h in range(12):
            for m in range(60):
                if bin(h).count('1') + bin(m).count('1') == num:
                    s = [str(h) + ':' + str(m)] if len(str(m)) == 2 else [str(h) + ':0' + str(m)]
                    res += s
        return res


s = Solution()
x = 1
print(s.readBinaryWatch(x))