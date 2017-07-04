class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        if length == 0:
            return ""
        maxlen = 1
        start = 0
        res = ''
        for i in range(length):
            if i - maxlen >= 1 and s[i-maxlen-1:i+1] == s[i-maxlen-1:i+1][::-1]:
                start = i-maxlen-1
                maxlen += 2
            elif i - maxlen >= 0 and s[i-maxlen:i+1] == s[i-maxlen:i+1][::-1]:
                start = i-maxlen
                maxlen += 1
        return s[start:start+maxlen]

s = Solution()
x = "babadada"
print(s.longestPalindrome(x))