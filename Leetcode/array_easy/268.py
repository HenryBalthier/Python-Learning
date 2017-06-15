class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        n = int((1 + l) * l / 2)
        sum = 0
        for i in nums:
            sum += i
        return n - sum

if __name__ == '__main__':
    s = Solution
    nums = [0, 1, 3]
    print(s.missingNumber(s, nums))