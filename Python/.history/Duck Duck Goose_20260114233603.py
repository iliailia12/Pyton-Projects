def solution(lst):
    x = lst[0]
    y = 1

    while x != y:
        if x > y:
            x = x - y
        else:
            y = y - x

    return x
