class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        def F(S, lst):

            if len(lst) == 4:
                if len(S) == 0:
                    res.append('.'.join(lst))
                else:
                    return
            if len(S) == 0:return
            for i in range(3):
                if len(S) < i+1:break
                if int(S[0:i+1]) < 256:
                    F(S[i+1:], lst + [S[0:i+1]])
                if i == 0 and S[0] == '0':break
        F(s, [])
        #return res

        ans = []
        def G(S,record):
            """record:List of strings"""
            if len(record)==4:
                if len(S)==0:
                    ans.append('.'.join(record))

            if len(S)==0:return
            for i in range(3):
                if len(S)<i+1:break
                if int(S[0:i+1])<256:
                    G(S[i+1:],record+[S[0:i+1]])
                if i==0 and S[0]=='0':break
        G(s,[])
        return ans

s = Solution()
x = "11055"
print(s.restoreIpAddresses(x))