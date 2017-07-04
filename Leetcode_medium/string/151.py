class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        lst = s.split(' ')
        return ' '.join(lst[::-1])

s = Solution()
x = "the sky is blue"
print(s.reverseWords(x))