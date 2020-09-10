# given a M*N grid, 1 means balloon, 0 means shooting spot.
# You can shoot in up, down, left, and right direction, and one shoot will clear all
# balloons in that direction.

# Whats tha max number of balloons you can clear?

# example:
# [
# [1,0,0,1,0],
# [0,0,1,1,1],
# [0,1,1,0,1],
# [1,1,1,1,0]
# ]
# max number is at grid[4][4], shoot left 4 balloons


def max_balloons(grid):
	if not grid or not grid[0]:
		return -1
	
	res = 0
	rows = len(grid)
	cols = len(grid[0])
	moves = [(1, 0), (0, -1), (-1, 0), (0, 1)]
	max_case = max(rows-1, cols-1)


	for i in range(rows):
		for j in range(cols):
			if not grid[i][j]:
				for x, y in moves:
					res = max(res, dfs(grid, i, j, x, y, max_case))
	
	return res


def dfs(grid, x, y, next_x, next_y, max_case):
	x+=next_x
	y+=next_y
	res = 0

	while 0<=x<len(grid) and 0<=y<len(grid[0]):
		if grid[x][y]:
			res+=1
		
		# if we get the max case just return
		if res == max_case:
			return res

		x+=next_x
		y+=next_y

	return res