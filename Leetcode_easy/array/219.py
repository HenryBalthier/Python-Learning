class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dct = dict()
        for i, v in enumerate(nums):
            if v in dct and i - dct[v] <= k:
                return True
            else:
                dct[v] = i
        return False


if __name__ == '__main__':
    s = Solution
    nums = [1, 2, 3, 4, 5, 6, 7, 1]
    k = 8
    print(s.containsNearbyDuplicate(s, nums, k))