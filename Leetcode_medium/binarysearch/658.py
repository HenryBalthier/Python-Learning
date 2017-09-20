class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        import operator
        lst = []
        for i in arr:
            lst.append([i, abs(x - i)])
        lst = sorted(lst, key=operator.itemgetter(1, 0))
        res = []
        for i in range(k):
            res.append(lst[i][0])
        res = sorted(res)
        return res


if __name__ == '__main__':
    s = Solution()
    t = [1,2,3,4,5]
    k = 4
    x = 3
    print(s.findClosestElements(t, k, x))