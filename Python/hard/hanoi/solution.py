#!/usr/bin/env python3

from os import system
import time
import sys

def solve(towers, a, b, c, i):
	if i == 0:
		return

	solve(towers, a, c, b, i - 1)

	towers[c].append(towers[a].pop())
	display(towers)

	solve(towers, b, a, c, i - 1)

def floor_string(tower, width, pos):
	if len(tower) <= pos:
		return " " * width

	buf = "▄" * tower[pos]
	rem = width - tower[pos]
	if rem % 2 == 1:
		buf = '▗' + buf[1:] + "▖"

	cushion = " " * int(rem / 2)
	return cushion + buf + cushion

def display(towers, max_width = None):
	if max_width is None:
		# the biggest disc must be at the bottom
		bottom_widths = [
			tower[0] if len(tower) > 0 else 0
			for tower in towers
		]

		max_width = max(*bottom_widths)

	print()
	for f in range(max_width - 1, -1, -1):
		floors = [floor_string(towers[t], max_width, f) for t in range(3)]
		print(" ".join(floors))

	print("▇" * (max_width * 3 + 2))
	time.sleep(0.5)

if __name__ == '__main__':
	towers = [[],[],[]]

	discs = 5
	if len(sys.argv) > 1:
		discs = int(sys.argv[1])

	assert discs < 20, "disc count must be below 20"

	# initialize towerz
	for i in range(discs, 0, -1):
		towers[0].append(i)

	display(towers)

	solve(towers, 0, 1, 2, discs)
