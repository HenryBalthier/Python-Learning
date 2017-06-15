class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        nums1[:] = sorted(nums1[:m] + nums2[:n])
        print(nums1)


if __name__ == '__main__':
    s = Solution
    n1 = [1,2,3,4,5]
    n2 = [-4,5,6,7]
    m1 = 0
    m2 = 4
    s.merge(s, n1, m1, n2, m2)