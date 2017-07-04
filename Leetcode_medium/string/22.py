class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []
        if n == 1:
            return ['()']

        res = []

        def helper(l, r, sum, str):
            if l == r == n:
                res.append(str)
                return
            elif sum == 0:
                helper(l+1, r, sum+1, str+'(')
            else:
                if l < n:
                    helper(l+1, r, sum+1, str+'(')
                helper(l, r+1, sum-1, str+')')

        l = r = 0
        helper(l, r, 0, '')
        return res

s = Solution()
x = 3
print(s.generateParenthesis(x))