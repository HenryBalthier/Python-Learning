class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        ss = s.split(' ')
        n = len(ss)
        for i in ss:
            if len(i) == 0:
                n -= 1
        return n
if __name__ == '__main__':
    s = Solution()
    x = "Hello,   my name is John  "
    print(s.countSegments(x))