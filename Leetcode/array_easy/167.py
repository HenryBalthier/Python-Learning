class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = dict()
        for i, v in enumerate(numbers):
            if v in d:
                return[d[v]+1, i+1]
            else:
                d[target - v] = i

if __name__ == '__main__':
    s = Solution
    nums = [0,0,0,0,0,0,1,2,3,4,5]
    t = 4
    print(s.twoSum(s, nums, t))