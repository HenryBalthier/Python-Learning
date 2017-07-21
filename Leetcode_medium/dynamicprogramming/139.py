class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if len(s) == 0:
            return True
        for i in wordDict:
            if i in s:
                res = s.split(i)
                tmp = 1
                for j in res:
                    tmp *= self.wordBreak(j, wordDict)
                if tmp == 1:
                    return True
        return False

s = Solution()
x = "ABC"
dict = ['AB',"A", "BC"]
print(s.wordBreak(x, dict))