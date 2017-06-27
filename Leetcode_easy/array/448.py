class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        m = set(nums)
        n = []
        for i in range(len(nums)+1):
            if i not in m and i > 0:
                n.append(i)
        return n


if __name__ == '__main__':
    s = Solution
    nums = [4,3,2,7,8,2,3,1]
    print(s.findDisappearedNumbers(s, nums))
