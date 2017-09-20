class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        length = len(nums)
        if len(nums) < 4:
            return []

        def threeSum(nums, target):
            """
            :type nums: List[int]
            :rtype: List[List[int]]
            """
            res = []
            for i in range(len(nums) - 2):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                l, r = i + 1, len(nums) - 1
                while l < r:
                    s = nums[i] + nums[l] + nums[r]
                    if s < target:
                        l += 1
                    elif s > target:
                        r -= 1
                    else:
                        res.append([nums[i], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                        l += 1
                        r -= 1
            return res

        res = []
        for i in range(length - 3):
            lst = threeSum(nums[i+1:], target-nums[i])
            if lst is not None:
                for j in lst:
                    j.append(nums[i])
                    t = sorted(j)
                    if t not in res:
                        res.append(t)
        return res

    def fourSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def NSum(nums, target, N, result, results):
            if len(nums) < N or N < 2 or target < nums[0] * N or target > nums[-1] * N:
                return
            if N == 2:
                l, r = 0, len(nums) - 1
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
            else:
                for i in range(len(nums) - N + 1):
                    if i == 0 or (i > 0 and nums[i-1] != nums[i]):
                        NSum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results)
        results = []
        nums.sort()
        NSum(nums, target, 4, [], results)
        return results


if __name__ == '__main__':
    s = Solution()
    x = [-1,-5,-5,-3,2,5,0,4]

    t = -7
    print(s.fourSum(x, t))
