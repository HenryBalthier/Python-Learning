class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        T = nums[0]
        maxsub = T
        for i in nums[1:]:
            T += i
            if i > T:
                T = i
            if T > maxsub:
                maxsub = T
        return maxsub


if __name__ == '__main__':
    s = Solution
    n = [-2,1,-3,4,-1,2,1,-5,4]
    print(s.maxSubArray(s,n))