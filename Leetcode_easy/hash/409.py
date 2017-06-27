class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        c = 0
        n = 0
        for item in s:
            d[item] = 1 + d.get(item, 0)
        print(d)
        for key, item in d.items():
            print(item)
            if item % 2 == 1:
                c = 1
                n += item - 1
            if item % 2 == 0:
                n += item
        return n + c

if __name__ == '__main__':
    s = Solution()
    n = "abccccdd"
    print(s.longestPalindrome(n))