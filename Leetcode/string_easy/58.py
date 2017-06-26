class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = 0
        ss = s[::-1]
        for i in ss:
            if n > 0 and i == ' ':
                return n
            elif i != ' ':
                n += 1
        return n

if __name__ == '__main__':
    s = Solution()
    x =  "aa"
    print(s.lengthOfLastWord(x))