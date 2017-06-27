class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = []
        num = n
        while num > 0:
            result.append(chr((num - 1) % 26 + ord('A')))
            num = (num - 1) // 26
        result.reverse()
        return ''.join(result)

if __name__ == '__main__':
    s = Solution()
    x = 27
    print(s.convertToTitle(x))