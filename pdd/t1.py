def Solution(x):
    """
    :param x: List[List[int]]
    :return: List[List[int]]
    """
    if x is None:
        return
    lst = []
    r = [0, 0]
    for i, s in enumerate(x):
        SUM = sum(s)
        if SUM > r[1]:
            lst.clear()
            r[0] = i+1
            r[1] = SUM
            lst.append(r[:])
        elif SUM == r[1]:
            r[0] = i + 1
            lst.append(r[:])
    return lst

if  __name__ == '__main__':
    x = [
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0 ,0, 0, 0, 1 ,1, 1, 1 ,1 ,1],
        [0, 0, 0, 0 ,0, 0, 0, 0, 0 ,1 ,1, 1],
        [0, 0 ,0, 0, 0, 0 ,0, 1 ,1, 1, 1 ,1],
        [0, 0, 0, 0, 1 ,1, 1, 1, 1 ,1 ,1 ,1]
    ]
    print(Solution(x))