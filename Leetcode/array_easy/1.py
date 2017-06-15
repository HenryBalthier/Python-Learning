class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, v in enumerate(nums):
            if target - v in nums:
                if target - v != v:
                    return [i, nums.index(target - v)]
                elif nums.count(v) > 1:
                    nums.pop(i)
                    return [i, nums.index(target - v)+1]

if __name__ == '__main__':
    s = Solution
    nums = [3, 3]
    t = 6
    print(s.twoSum(s, nums, t))