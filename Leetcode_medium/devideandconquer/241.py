class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        lst = list(input)
        nums = []
        op = []
        for i in lst:
            if '0' <= i <= '9':
                nums.append(int(i))
            else:
                op.append(i)
        if op == []:
            return nums
        print(nums, op)
        res = []

        mark = []

        def operater(a, b, op):
            if op == "+":
                return a + b
            if op == '-':
                return a - b
            if op == '*':
                return a * b
            return False

        def func(nums, op):
            if op == []:
                res.append(nums[0])
                return
            length = len(op)
            for i in range(length):
                tmp = [operater(nums[i], nums[i+1], op[i])]
                if i > 0:
                    tmp = nums[:i] + tmp
                if i < length-1:
                    tmp = tmp + nums[i+2:]
                ops = op[:i] + op[i+1:]
                print(tmp, ops)
                func(tmp, ops)

        func(nums, op)
        return res

if __name__ == '__main__':
    s = Solution()
    x = "2*3-4*5"
    print(s.diffWaysToCompute(x))
