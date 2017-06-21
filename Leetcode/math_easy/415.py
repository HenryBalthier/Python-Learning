class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        d = {str(x): x for x in range(10)}
        n1 = n2 = 0
        for i in num1:
            n1 = n1*10 + d[i]
        for i in num2:
            n2 = n2*10 + d[i]
        res = n1 + n2
        s = {x: str(x) for x in range(10)}
        out = '' if res > 0 else '0'
        while res:
            out+=(s[res%10])
            res = res // 10
        return out[::-1]

if __name__ == '__main__':
    s = Solution()
    n1 = '7234'
    n2 = '321'
    print(s.addStrings(n1, n2))