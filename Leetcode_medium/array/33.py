class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums == []:
            return -1
        n = sorted(nums)
        l = len(n)
        def find(t, num):
            for i, v in enumerate(num):
                if v == t:
                    return i
            return -1

        def find2(t, num):
            l = 0
            r = len(num) - 1
            while l < r:
                mid = (r - l) // 2
                print('mid = %d' % mid)
                if num[l + mid] < t:
                    l = mid+ l
                elif num[l + mid] > t:
                    r = mid + l
                else:
                    return l+mid
                if mid == 0:
                    break
            if num[l] == t:
                return l
            elif num[r] == t:
                return r
            else:
                return -1


        x = find2(nums[0], n)
        print(x)
        y = find2(target, n)
        if y == -1:
            return -1
        print(y)
        res = y - x
        print(res)
        if res < 0:
            res += l
        if res > l:
            res -= l

        return res

s = Solution()
x = [1, 3]
#x = [4, 5, 6, 7, 0, 1, 2]
#   [0, 1, 2, 4, 5, 6, 7]
t = 3
print(s.search(x, t))