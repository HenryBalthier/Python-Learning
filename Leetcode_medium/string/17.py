class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        d = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }
        l = len(digits)
        if l == 0:
            return []
        elif l == 1:
            return d[digits[-1]]
        else:
            pre = self.letterCombinations(digits[:-1])
            res = d[digits[-1]]
            return [x + y for x in pre for y in res]



s = Solution()
x = '22'
print(s.letterCombinations(x))