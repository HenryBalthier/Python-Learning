class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        flag = 0
        for i in findNums:
            for j in nums:
                print(i, j, flag)
                if i == j:
                    flag = 1
                    m = -1
                if flag:
                    if j > i:
                        m = j
                        flag = 0
                        break
            res.append(m)
            flag = 0
        return res

s = Solution()
nums1 = [1,3,5,2,4]
nums2 = [5,4,3,2,1]

print(s.nextGreaterElement(nums1, nums2))
