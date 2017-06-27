class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        if a == 0:
            return b
        elif b == 0:
            return a

        mask = 0xffffffff

        # positive's two's complement is itself.
        # so we only need to convert negative
        print(bin(a))
        print(bin(b))


        if a < 0:
            a = ~(a ^ mask)
        if b < 0:
            b = ~(b ^ mask)
        print(bin(a))
        print(bin(b))

        # result stores in a.
        # result is in two's complement format
        while b != 0:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask

            print(bin(a))
            print(bin(b))

        # a is negative if the first bit is 1
        if (a >> 31) & 1:
            return ~(a ^ mask)
        else:
            return a

s = Solution()
a = 3
b = -2
print(s.getSum(a, b))