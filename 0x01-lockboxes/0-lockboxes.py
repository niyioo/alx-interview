#!/usr/bin/python3
"""
Lockboxes module
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list): A list of lists where each list represents a box.

    Returns:
        bool: True if all boxes can be opened, else False.
    """
    if not boxes or not boxes[0]:
        return False

    num_boxes = len(boxes)
    keys = set(boxes[0])
    opened_boxes = {0}

    while opened_boxes:
        box_to_open = opened_boxes.pop()
        for key in boxes[box_to_open]:
            if key < num_boxes and key not in keys:
                keys.add(key)
                opened_boxes.add(key)

    return len(keys) == num_boxes
