class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        out = 0
        pre = 0
        for i, v in enumerate(nums):
            if v == 0:
                if i - pre > out:
                    out = i - pre
                pre = i + 1
            elif i == len(nums) - 1:
                if i + 1 - pre >= out:
                    out = i + 1 - pre
        return out

if __name__ == '__main__':
    s = Solution
    nums = [1]
    print(s.findMaxConsecutiveOnes(s, nums))