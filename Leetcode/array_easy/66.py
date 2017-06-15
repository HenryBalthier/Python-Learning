class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        sum = 0
        for i in range(len(digits)):
            sum += digits[-(i + 1)] * (10 ** i)
        sum += 1
        return [int(i) for i in str(sum)]



if __name__ == '__main__':
    s = Solution
    d = [9,9,9]
    print(s.plusOne(s,d))