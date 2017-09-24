class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        nums = []
        strings = [[]]
        preisnum = 0
        for i in s:
            if '0' <= i <= '9':
                if preisnum:
                    nums[-1] = nums[-1] * 10 + int(i)
                else:
                    preisnum = 1
                    nums.append(int(i))
            elif i == '[':
                strings.append([])
                preisnum = 0
            elif i == ']':
                tmp = strings[-1] * nums[-1]
                strings.pop()
                nums.pop()
                strings[-1] += tmp
                preisnum = 0
            else:
                strings[-1].append(i)
                preisnum = 0
            print(strings, nums)
        return ''.join(strings[0])

if __name__ == '__main__':
    s = Solution()
    x = "2[abc]3[cd]ef"
    print(s.decodeString(x))