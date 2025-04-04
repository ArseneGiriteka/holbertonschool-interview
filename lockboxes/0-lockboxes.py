#!/usr/bin/python3
from collections import OrderedDict
"""
Lockboxes:
You have n number of locked boxes in front of you. Each box is numbered
sequentially from 0 to n - 1 and each box may contain keys to the other
boxes.
"""


def canUnlockAll(boxes):
    """
    This function will return True if all boxes can be open
    and False oteherwise.
    """
    unlocked_box = [0]
    for box in boxes:
        if len(box) == 0:
            break
        for key in box:
            unlocked_box += [key]
    unlocked_box = sorted(list(OrderedDict.fromkeys(unlocked_box)))
    print(unlocked_box)
    return len(unlocked_box) == len(boxes)
