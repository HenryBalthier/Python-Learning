from math import factorial

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        ans = []
        def f(k, res):
            if k < 0:
                return k
            lst = [str(i+1) for i in range(n) if str(i+1) not in res]
            if len(lst) == 0:
                k -= 1
                if k == 0:
                    ans.append(''.join(res))
                    return k - 1
                return k
            for i in lst:
                k = f(k, res + [i])
                if k < 0:
                    break
            return k
        _ = f(k, [])
        return ans[-1]

    def getPermutation2(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        def f(lst, k, pre):
            length = len(lst)
            if length == 1:
                return pre + str(lst[0])
            fact = factorial(length-1)
            idx = (k-1) // fact
            cur = lst[idx]
            return f(lst[:idx]+lst[idx+1:], (k-1)%fact + 1, pre + str(cur))
        l = []
        ans = f(range(1, n+1), k, '')
        return ans


s = Solution()
n = 9
k = 94494
# print(s.getPermutation(n, k))
print(s.getPermutation2(n, k))