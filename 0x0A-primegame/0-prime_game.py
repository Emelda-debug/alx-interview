#!/usr/bin/python3
""" Determines if all boxes can be opened """


def can_open_all_boxes(boxes: list[list[int]]) -> bool:
    """
    Checks if all boxes in the list can be opened.

    Args:
        boxes: The list of lists representing the boxes and their keys.

    Returns:
        True if all boxes can be opened, else False.
    """

    num_boxes = len(boxes)
    opened_boxes = set([0])  # Start with the first box open
    unopened_boxes = set(boxes[0]).difference(set([0]))

    while unopened_boxes:
        box_index = unopened_boxes.pop()

        if box_index < 0 or box_index >= num_boxes:
            continue

        if box_index not in opened_boxes:
            unopened_boxes.update(boxes[box_index])
            opened_boxes.add(box_index)

    return num_boxes == len(opened_boxes)