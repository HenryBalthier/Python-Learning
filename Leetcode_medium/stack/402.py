class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        out = []
        for d in num:
            while k and out and out[-1] > d:
                print(out)
                out.pop()
                k -= 1
            out.append(d)
            print(out)
        return ''.join(out[:-k or None]).lstrip('0') or '0'


if __name__ == '__main__':
    s = Solution()
    x = "321987"
    k = 4
    print(s.removeKdigits(x, k))