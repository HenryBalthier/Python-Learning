class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """

        l = [(x, y) for x in nums1 for y in nums2]
        l.sort(key=sum)
        return l[:k]




if __name__ == '__main__':
    s = Solution()
    nums1 = [1, 1, 2]
    nums2 = [1, 2, 3]
    k = 3
    print(s.kSmallestPairs(nums1, nums2, k))