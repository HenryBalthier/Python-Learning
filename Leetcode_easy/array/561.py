class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lst = sorted(nums)
        sum = 0
        for i, v in enumerate(lst):
            if i % 2 == 0:
                sum += v
        return sum

if __name__ == '__main__':
    s = Solution
    nums = [1, 4, 3, -2]
    print(s.arrayPairSum(s, nums))
