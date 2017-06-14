class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = sorted(list(set(nums)))
        return s[-1] if len(s) < 3 else s[-3]



if __name__ == '__main__':
    s = Solution
    nums = [3, 2, 1]
    print(s.thirdMax(s, nums))
