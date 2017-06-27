class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        a = 0
        z = l-1
        for i in range(l):
            if a == i-1 and nums[a] <= nums[i]:
                a = i
            while a >= 0 and nums[a] > nums[i]:
                a -= 1
            j = l-1 - i
            if z == j+1 and nums[z] >= nums[j]:
                z = j
            while z <= l-1 and nums[z] < nums[j]:
                z += 1
        return z-a-1 if 0 < z-a-1 else 0

if __name__ == '__main__':
    s = Solution
    nums = [2, 1]
    print(s.findUnsortedSubarray(s, nums))
