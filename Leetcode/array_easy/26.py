class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums[:] = sorted(list(set(nums)))
        return len(nums)


if __name__ == '__main__':
    s = Solution
    n = [1,2,2,2,2]
    print(s.removeDuplicates(s,n))