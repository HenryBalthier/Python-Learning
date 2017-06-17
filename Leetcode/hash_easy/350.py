class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d = {}
        res = []
        for i in nums1:
            d[i] = 1 + d.get(i, 0)
        for i in nums2:
            if d.get(i, False):
                d[i] -= 1
                res.append(i)
        return res


if __name__ == '__main__':
    s = Solution()
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    print(s.intersect(nums1, nums2))