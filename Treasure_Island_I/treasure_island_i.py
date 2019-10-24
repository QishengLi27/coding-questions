# You have a map that marks the location of a treasure island. Some of the map area has jagged rocks and dangerous reefs. Other areas are safe to sail in.
# There are other explorers trying to find the treasure. So you must figure out a shortest route to the treasure island.
# Assume the map area is a two dimensional grid, represented by a matrix of characters.
# You must start from the top-left corner of the map and can move one block up, down, left or right at a time.
# The treasure island is marked as ‘X’ in a block of the matrix. ‘X’ will not be at the top-left corner.
# Any block with dangerous rocks or reefs will be marked as ‘D’. You must not enter dangerous blocks. You cannot leave the map area.
# Other areas ‘O’ are safe to sail in. The top-left corner is always safe.
# Output the minimum number of steps to get to the treasure.
# e.g.
# Input
# [
# [‘S’, ‘O’, ‘O’, ‘O’],
# [‘D’, ‘O’, ‘D’, ‘O’],
# [‘O’, ‘O’, ‘O’, ‘O’],
# [‘X’, ‘D’, ‘D’, ‘O’],
# ]

# Output from aonecode.com
# Route is (0, 0), (0, 1), (1, 1), (2, 1), (2, 0), (3, 0) The minimum route takes 5 steps.

from collections import deque

def shortestDistance(matrix, start_x, start_y):
	queue = deque()
	queue.append((start_x, start_y, 0))
	directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    distance_map = {(start_x, start_y): 0}
    while queue:
        x, y, distance = queue.popleft()
        
        if targetMap[x][y] == 2:
            return distance_map[x, y]
            
        for dirs in directions:
            next_x = x + dirs[0]
            next_y = y + dirs[1]
            
            if (next_x, next_y) in distance_map:
                continue
            
            if 0 <= next_x < len(targetMap) and 0 <= next_y < len(targetMap[0]) and targetMap[next_x][next_y] != 1:
                queue.append((next_x, next_y, distance + 1))
                distance_map[next_x, next_y] = distance + 1
    return -1


# For treasure island ii, the input becomes:
# [['S', 'O', 'O', 'S', 'S'],
#  ['D', 'O', 'D', 'O', 'D'],
#  ['O', 'O', 'O', 'O', 'X'],
#  ['X', 'D', 'D', 'O', 'O'],
#  ['X', 'D', 'D', 'D', 'O']]

#  Start from any S, find the shortest X

def treasure_ii(matrix):
    res = sys.maxsize
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 'S':
                temp = bfs(matrix, i, j)
                res = min(res, temp)
    return res