class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for i, v in enumerate(nums):
            d[v] = d.get(v, 0) + 1
        res = 0
        for i in d:
            if i+1 in d:
                m = d[i] + d[i+1]
                if m > res:
                    res = m
        return res

if __name__ == '__main__':
    s = Solution
    n = [1,3,2,2,5,2,3,7]
    print(s.findLHS(s,n))