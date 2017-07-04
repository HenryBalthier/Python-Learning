class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'
        if num1 == '' or num2 == '':
            return ''

        def addstr(n1, n2):
            if n1 == '0':
                return n2
            elif n2 == '0':
                return n1
            c = 0
            Nsum = ''
            l1 = len(n1)
            l2 = len(n2)
            # assum l2 <= l1
            if l1 < l2:
                n1, n2 = n2, n1
                l1, l2 = l2, l1
            n2 = '0'*(l1-l2) + n2
            def add(x, y, c):
                res = int(x) + int(y) + c
                if res >= 10:
                    c = 1
                    res = res % 10
                else:
                    c = 0
                return str(res), c

            for i in range(l1-1, -1, -1):
                N, c = add(n1[i], n2[i], c)
                Nsum = N + Nsum

            if c == 1:
                Nsum = '1' + Nsum

            return Nsum
        result = '0'
        for i in num2[::-1]:
            res = '0'
            for j in range(int(i)):
                res = addstr(res, num1)
            result = addstr(result, res)
            num1 = num1 + '0'
        return result



s = Solution()
x1 = '99'
x2 = '199999'
print(s.multiply(x1,x2))