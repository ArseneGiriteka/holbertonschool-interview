#!/usr/bin/python3
"""
Lockboxes:
You have n number of locked boxes in front of you. Each box is numbered
sequentially from 0 to n - 1 and each box may contain keys to the other
boxes.
"""


def canUnlockAll(boxes):
    """
    Returns True if all boxes can be opened, otherwise False.
    """
    n = len(boxes)
    visited = set()
    stack = [0]  # Start with box 0

    while stack:
        box = stack.pop()
        if box not in visited:
            visited.add(box)
            # Add keys to stack only if they're valid and not visited
            for key in boxes[box]:
                if 0 <= key < n and key not in visited:
                    stack.append(key)

    return len(visited) == n
