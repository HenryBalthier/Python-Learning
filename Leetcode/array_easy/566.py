class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        lst = []
        r0 = len(nums)
        c0 = len(nums[0])
        if c * r != c0 * r0:
            return nums
        for i in nums:
            for j in i:
                lst.append(j)
        output = []
        for i in range(r):
            l = i * c
            output.append(lst[l:l+c])
        return output

if __name__ == '__main__':
    s = Solution
    nums = [[1, 2], [3, 4]]
    r = 2
    c = 4
    print(s.matrixReshape(s, nums, r, c))