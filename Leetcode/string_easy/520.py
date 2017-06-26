class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if not word:
            return False
        if len(word) == 1:
            return True
        f = 0
        for i, v in enumerate(word):
            if i == 0:
                if not v.isupper():
                    f = -1
            else:
                if v.isupper():
                    if f != 0 and f != 1:
                        return False
                    else:
                        f = 1
                else:
                    if f != 0 and f != -1:
                        return False
                    else:
                        f = -1

        return True



if __name__ == '__main__':
    s = Solution()
    x = 'aa'
    print(s.detectCapitalUse(x))