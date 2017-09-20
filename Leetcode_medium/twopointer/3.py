class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        r = 0
        length = len(s)
        Max = 0
        while r < length:
            while s[r] in s[l:r]:
                l += 1
            r += 1
            Max = max(Max, r-l)
        return Max

if __name__ == '__main__':
    s = Solution()
    x = 'abcabcbb'
    print(s.lengthOfLongestSubstring(x))
