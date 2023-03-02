#!/usr/bin/python3
"""
SE: Ikary Ryann
BY: ALX
INTERVIEW: Lockboxes
"""


def canUnlockAll(boxes):
    """check if boxes can opened"""
    n = len(boxes)
    keys = boxes[0]
    locked = []
    print(boxes[0][0])
    for i in range(n):
        if i > 0:
            locked.append(i)
    print(locked)
    for x in range(n):
        if len(boxes[x]) == 1:
            if boxes[x][0] in locked:
                result = locked.index(boxes[x][0])
                locked.pop(result)
                locked.insert(result, None)
        else:
            for y in range(len(boxes[x])):
                if boxes[x][y] in locked:
                    result = locked.index(boxes[x][y])
                    locked.pop(result)
                    locked.insert(result, None)
            print(locked)
    return locked == []
