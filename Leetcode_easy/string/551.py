class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        A = 0
        L = 0
        M = 0
        for i in s:
            if i == 'A':
                A += 1
                L = 0
            elif i == 'L':
                L += 1
            else:
                L = 0
            M = max(M, L)

        return A <= 1 and M <= 2

if __name__ == '__main__':
    s = Solution()
    x = "PPALLLP"
    print(s.checkRecord(x))