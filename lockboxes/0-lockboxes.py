#!/usr/bin/python3
from collections import OrderedDict
"""
Lockboxes
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
