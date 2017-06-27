class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        d = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        pre = res = 0
        for i in range(l - 1, -1, -1):
            cur = d[s[i]]
            print(cur)
            if cur < pre:
                res -= cur
            else:
                res += cur
            pre = cur
            print(res)
        return res


if __name__ == '__main__':
    s = Solution()
    x = 'IIVXX'
    print(s.romanToInt(x))