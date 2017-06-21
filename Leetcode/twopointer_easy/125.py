class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        l = len(s)
        if not s:
            return True
        left = 0
        right = l-1
        while left < right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

if __name__ == '__main__':
    s = Solution()
    x = "A man, a 1plan, a canal: P1anama"
    print(s.isPalindrome(x))