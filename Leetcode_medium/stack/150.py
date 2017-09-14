class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        s = ['+', '-', '*', '/']
        def oprator(a, b, op):
            if op == '+':
                return a + b
            if op == '-':
                return a - b
            if op == '*':
                return a * b
            if op == '/':
                return int(a / b)
            return
        lst = []
        for i in tokens:
            if i in s:
                tmp = oprator(lst[-2], lst[-1], i)
                lst = lst[:-2] + [tmp]
            else:
                lst.append(int(i))
            print(lst)
        return lst[0]

if __name__ == '__main__':
    s = Solution()
    t = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(s.evalRPN(t))