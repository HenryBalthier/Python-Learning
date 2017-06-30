class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g = sorted(g, reverse=True)
        s = sorted(s, reverse=True)
        res = 0
        l1 = len(g)
        l2 = len(s)
        p = 0
        q = 0
        while p < l1 and q < l2 :
            if g[p] <= s[q]:
                p += 1
                q += 1
                res += 1
            else:
                p += 1
        return res


s = Solution()
x = [1,2,3,3,3,4]
y = [1,2,3,1]
print(s.findContentChildren(x,y))