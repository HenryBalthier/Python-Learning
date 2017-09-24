class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        lst = []
        for i in logs:
            lst.append(i.split(':'))
        res = [0] * n
        pre = []
        for log in lst:
            print('log = ', log)

            if log[1] == 'start':
                if pre != []:
                    res[pre[0]] += int(log[2]) - pre[1]
                pre = ([int(log[0]), int(log[2]), log[1]])

            else:
                w = 0 if pre[2] == 'end' else 1
                res[int(log[0])] += int(log[2]) - pre[1] + w
                pre = [int(log[0]), int(log[2]), log[1]]
            print('pre = ', pre)
            print('res = ', res)
        return res


if __name__ == '__main__':
    n = 8
    logs = ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]
    logs = ["0:start:0","1:start:5","2:start:6","3:start:9","4:start:11","5:start:12","6:start:14","7:start:15","1:start:24","1:end:29","7:end:34","6:end:37","5:end:39","4:end:40","3:end:45","0:start:49","0:end:54","5:start:55","5:end:59","4:start:63","4:end:66","2:start:69","2:end:70","2:start:74","6:start:78","0:start:79","0:end:80","6:end:85","1:start:89","1:end:93","2:end:96","2:end:100","1:end:102","2:start:105","2:end:109","0:end:114"]
    s = Solution()
    print(s.exclusiveTime(n, logs))