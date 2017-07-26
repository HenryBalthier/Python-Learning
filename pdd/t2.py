def Solution(x):
    """
    :param x: str
    :return: bool
    """
    lst = []
    s = ['(', ')', '[', ']', '{', '}']
    d = {
        ')': 0,
        ']': 0
    }
    for i in x:
        if i in s:
            if i == '(':
                if i in lst:
                    return False
                elif len(lst) > 0:
                    if lst[-1] != '[':
                        return False
                lst.append(i)
                d[')'] = d[']'] = 0

            elif i == '[':
                if i in lst:
                    return False
                elif len(lst) > 0:
                    if lst[-1] != '{':
                        return False
                lst.append(i)
                d[')'] = d[']'] = 0

            elif i == "{":
                if len(lst) > 0:
                    if lst[-1] != '{':
                        return False
                lst.append(i)
                d[')'] = d[']'] = 0

            elif i == ')':
                if len(lst) == 0:
                    return False
                elif lst[-1] != '(':
                    return False
                lst.pop()
                d[i] += 1

            elif i == ']':
                if len(lst) == 0:
                    return False
                elif lst[-1] != '[':
                    return False
                elif d[')'] == 0:
                    return False
                lst.pop()
                d[i] += 1

            elif i == '}':
                if len(lst) == 0:
                    return False
                elif lst[-1] != '{':
                    return False
                elif d[')'] == 0 or d[']'] == 0:
                    return False
                lst.pop()

    return len(lst) == 0

# x = '{[(2+3)*(1-3)] + 4}*(14-3)'
x = '[()()]()[]()[()]{{[()]}}'
print(Solution(x))
