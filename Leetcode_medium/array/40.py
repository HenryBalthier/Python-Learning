class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if candidates == []:
            return []
        candidates = sorted(candidates, reverse=True)
        results = []
        lenth =  len(candidates)
        def helper(res, idx):
            if idx >= lenth:
                return

            s = sum(res)
            for i, v in enumerate(candidates[idx:]):
                ss = s + v
                if ss < target:
                    helper(res + [v], i + idx + 1)
                elif ss > target:
                    continue
                else:       # ss == target
                    lst = res + [v]
                    if lst not in results:
                        results.append(lst)

        helper([], 0)
        return results

s = Solution()
x = [10, 1, 2, 7, 6, 1, 5]
t = 8
print(s.combinationSum2(x,t))