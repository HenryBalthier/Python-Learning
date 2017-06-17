
class Solution(object):
    def findAnagrams(self, s, p):
        lp = len(p)
        ls = len(s)
        dp = self.count(st=p)
        lst = []
        print(dp)
        ds = self.count(s[0:lp])
        print(ds)
        if ds == dp:
            lst.append(0)
        for i in range(ls - lp):
            ds[s[i]] -= 1
            if ds[s[i]] == 0:
                ds.pop(s[i])
            ds[s[i+lp]] = 1 + ds.get(s[i+lp], 0)
            print(ds)
            if ds == dp:
                lst.append(i+1)
        return lst

    def count(self, st):
        d = {}
        for i in st:
            d[i] = 1 + d.get(i, 0)
        return d

if __name__ == '__main__':
    s = Solution()
    ss = "ababababab"
    p = "aab"
    print(s.findAnagrams(ss ,p))