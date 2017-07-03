class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if candidates == []:
            return []
        cand = sorted(candidates, reverse=True)
        result = []
        lenth = len(cand)
        def helper(res, index):
            if index >= lenth:
                return
            s = sum(res)
            for i, v in enumerate(cand[index:]):
                if s + v < target:
                    helper(res+[v], index+i)
                elif s + v > target:
                    continue
                else:
                    result.append(res + [v])
        helper([], 0)
        return result


s = Solution()
x = [2,3,4,1]
t = 7
print(s.combinationSum(x, t))