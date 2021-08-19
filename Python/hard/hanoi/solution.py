#!/usr/bin/env python3

from os import system
import time
import sys

def solve(towers, first, second, third, count):
    '''Moves the first count discs from the first to the third tower by
    termporarily moving count - 1 discs to the second tower, then moving the
    biggest disc to the third, and, finally, moving the count - 1 discs from the
    second tower to the third tower as well'''
    if count == 0:
        return

    solve(towers, first, third, second, count - 1)

    towers[third].append(towers[first].pop())
    display(towers)

    solve(towers, second, first, third, count - 1)

def floor_string(tower, width, floor):
    '''Returns a string that is width long and contains a centered visualization
    of the disc on the given floor'''
    if len(tower) <= floor:
        return " " * width

    buf = "▄" * tower[floor]
    rem = width - tower[floor]
    if rem % 2 == 1:
        buf = '▗' + buf[1:] + "▖"

    cushion = " " * int(rem / 2)
    return cushion + buf + cushion

def display(towers, max_width = None):
    '''Show the current state of the towers on STDOUT'''
    if max_width is None:
        # the biggest disc must be at the bottom
        bottom_widths = [
            tower[0]
            for tower in towers
            if len(tower) > 0
        ]

        max_width = max(bottom_widths)

    print()
    for f in range(max_width - 1, -1, -1):
        floors = [
            floor_string(towers[t], max_width, f)
            for t in range(3)
        ]
        print(" ".join(floors))

    print("▇" * (max_width * 3 + 2))
    time.sleep(0.5)

if __name__ == '__main__':
    towers = [[],[],[]]

    discs = 5
    if len(sys.argv) > 1:
        discs = int(sys.argv[1])

    assert discs < 20, "disc count must be below 20"

    # initialize the left-most tower by piling the discs bottom-up
    for i in range(discs, 0, -1):
        towers[0].append(i)

    display(towers, discs)

    solve(towers, 0, 1, 2, discs)
