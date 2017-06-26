class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        ss = s.split(' ')
        res = ''
        for i, v in enumerate(ss):
            ss[i] = ss[i][::-1]
            res = res + ss[i] + ' '
        return res[:-1]

if __name__ == '__main__':
    s = Solution()
    x = "Let's  take LeetCode contest"
    print(s.reverseWords(x))