class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        if k > 9 or k < 1:
            return []
        MIN = sum(i for i in range(k+1))
        MAX = sum(i for i in range(9, 9-k, -1))

        if n > MAX or n < MIN:
            return []

        res = []

        def func(k, n, idx, lst):
            if k == 1:
                if 10 > n > idx:
                    res.append(lst + [n])
                return

            for i in range(idx+1, 10):
                func(k-1, n-i, i, lst + [i])

        func(k, n, 0, [])

        return res



if __name__ == '__main__':
    k = 3
    n = 9
    s = Solution()
    print(s.combinationSum3(k, n))
