class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lst = sorted(nums)
        l = int(len(nums) / 2) +1
        return lst[l]


if __name__ == '__main__':
    s = Solution
    nums = [1,2,2,2,3]
    print(s.majorityElement(s, nums))