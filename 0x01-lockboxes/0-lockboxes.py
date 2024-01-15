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
    current_position = 0
    unlocked_boxes = {}

    for box in boxes:
        if len(box) == 0 or current_position == 0:
            unlocked_boxes[current_position] = "always_unlocked"
        for key in box:
            if key < len(boxes) and key != current_position:
                unlocked_boxes[key] = key
        if len(unlocked_boxes) == len(boxes):
            return True
        current_position += 1
    return False
