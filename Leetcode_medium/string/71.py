class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        l = path.split('/')
        st = []
        for p in l:
            if p == "..":
                try:
                    st.pop()
                except:
                    pass
            elif p == "." or p == '':
                pass
            else:
                st.append(p)
        print('/'.join(st))

        return '/' + '/'.join(st)

s = Solution()
x = "/a/./b/v"
print(s.simplifyPath(x))