#!/usr/bin/python3
"""
Lockboxes:
You have n number of locked boxes in front of you. Each box is numbered
sequentially from 0 to n - 1 and each box may contain keys to the other
boxes.
"""
from collections import OrderedDict


def canUnlockAll(boxes):
    """
    This function will return True if all boxes can be open
    and False oteherwise.
    """
    unlocked_boxes = [0]
    for box in boxes:
        if len(box) == 0:
            break
        for key in box:
            unlocked_boxes += [key]
    unlocked_boxes = sorted(list(OrderedDict.fromkeys(unlocked_boxes)))

    return len(unlocked_boxes) == len(boxes)
