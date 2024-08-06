#!/usr/bin/python3


def canUnlockAll(boxes):
    '''
    This function can determine if all the boxes can be opened
    '''
    Unlocked = [0]
    for id_box in Unlocked:
        for b in boxes[id_box]:
            if b not in Unlocked:
                Unlocked.append(b)
    for i in range(len(boxes)):
        if i not in Unlocked:
            return False
    return True