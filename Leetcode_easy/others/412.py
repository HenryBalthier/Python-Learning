class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        for i in range(n):
            m = i+1
            if m % 3 == 0 and m % 5 == 0:
                res.append('FizzBuzz')
            elif m % 3 == 0:
                res.append('Fizz')
            elif m % 5 == 0:
                res.append('Buzz')
            else:
                res.append(str(m))
        return res

s = Solution()
x = 15
print(s.fizzBuzz(x))