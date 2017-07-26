def Solution(x):
    """"
    :param x: List[List[int]]
    :return: List[int]
    """
    if x is None:
        return []

    left = x[0][0]
    right = x[0][-1]

    for i in x:
        if left > i[0]:
            left = i[0]
        if right < i[-1]:
            right = i[-1]

    print([left, right])

    def check(left, right):
        flag = 0
        for i in x:
            for j in i:
                if left <= j <= right:
                    flag = 1
                    break
            if flag != 1:
                return False
            flag = 0
        return True

    def search(left, right):
        if not check(left,right):
            return 0, 99999
        if left <= right:
            l1, r1 = search(left+1, right)
            l2, r2 = search(left, right-1)
            if r1 - l1 < right - left:
                right, left = r1, l1
            if r2 - l2 < right - left:
                right, left = r2, l2
        return left, right

    l, r = search(left,right)
    print(l, r)



x = [
    [1, 3, 5],
    [4, 8],
    [2, 5]
]
print(Solution(x))