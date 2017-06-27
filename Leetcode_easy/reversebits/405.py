class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        d = {
            0: '0',
            1: '1',
            2: '2',
            3: '3',
            4: '4',
            5: '5',
            6: '6',
            7: '7',
            8: '8',
            9: '9',
            10: 'a',
            11: 'b',
            12: 'c',
            13: 'd',
            14: 'e',
            15: 'f'
        }
        res = ''
        if num < 0:
            #num = num + 2**32
            num = (-num ^ 0xffffffff) + 1
        if num > 0:
            while num > 0:
                res += d[num % 16]
                num = int(num / 16)
            return res[::-1]
        elif num == 0:
            return '0'

s = Solution()
x = -16
print(s.toHex(x))
