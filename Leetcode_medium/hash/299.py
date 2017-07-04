class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        d = {}
        for i in secret:
            d[i] = d.get(i, 0) + 1
        bull = cow = 0
        lst = []
        for i, v in enumerate(guess):
            if v == secret[i]:
                bull += 1
                d[v] -= 1
                lst.append(i)
        for i, v in enumerate(guess):
            if i not in lst and v in d.keys():
                if d[v] > 0:
                    d[v] -= 1
                    cow += 1
        return str(bull) + 'A' + str(cow) + 'B'

s = Solution()
x = '1122'
y = '1222'
print(s.getHint(x, y))
