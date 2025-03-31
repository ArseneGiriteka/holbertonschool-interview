#!/usr/bin/python3
"""
Lockboxes
"""


def canUnlockAll(boxes):
    unlocked_box = []
    for box in boxes:
        if isinstance(box, int) and 0 <= box and box >= (len(boxes) - 1)\
                and box not in unlocked_box:
            unlocked_box += [box]
        else:
            return False
    return True
