class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        s = len(set(nums))
        return n-s>0


if __name__ == '__main__':
    s = Solution
    nums = [1, 2, 3, 4, 5, 1]
    print(s.containsDuplicate(s, nums))