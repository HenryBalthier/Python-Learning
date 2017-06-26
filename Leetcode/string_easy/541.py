class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if not s:
            return ''
        return s[:k][::-1] + s[k:k*2] + self.reverseStr(s[k*2:], k)



if __name__ == '__main__':
    s = Solution()
    x = 'abcdefghijklmn'
    k = 3
    print(s.reverseStr(x, k))