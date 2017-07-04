class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0
        length = len(s)
        l = 0
        r = 1
        res = r - l
        while r < length:
            while s[r] in s[l:r]:
                l += 1
            r += 1
            res = max(res, r-l)
        return res

s = Solution()
x = "abcabcbb"
print(s.lengthOfLongestSubstring(x))