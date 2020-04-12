# Description
# 中文
# English
# Given a boolean 2D matrix, 0 is represented as the sea, 1 is represented as the island. If two 1 is adjacent, we consider them in the same island. We only consider up/down/left/right adjacent.

# Find the number of islands.

# Input:
# [
#   [1,1,0,0,0],
#   [0,1,0,0,1],
#   [0,0,0,1,1],
#   [0,0,0,0,0],
#   [0,0,0,0,1]
# ]
# Output:
# 3

# https://www.lintcode.com/problem/number-of-islands/description


# bfs
from collections import deque
def numIslands_bfs(grid):
    if not grid or not grid[0]:
        return 0
    
    rows = len(grid)
    cols = len(grid[0])
    
    visited_points = set()
    result = 0
    
    for i in range(rows):
        for j in range(cols):
            point_value = grid[i][j]
            if point_value and (i, j) not in visited_points:
                bfs(grid, i, j, visited_points)
                result += 1
    
    return result
    
def bfs(grid, x, y, visited_points):
    queue = deque([(x, y)])
    visited_points.add((x, y))
    moves = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    
    while queue:
        current_point = queue.popleft()
        
        for next_x, next_y in  moves:
            next_x = current_point[0] + next_x
            next_y = current_point[1] + next_y
            
            if (not ( 0 <= next_x < len(grid) and 0 <= next_y < len(grid[0]))) \
                or grid[next_x][next_y] != 1 \
                or (next_x, next_y) in visited_points:
                    continue
            queue.append((next_x, next_y))
            visited_points.add((next_x, next_y))


# dfs
def numIslands_dfs(grid):
    if not grid or not grid[0]:
        return 0
    
    rows = len(grid)
    cols = len(grid[0])
    
    visited_points = set()
    result = 0
    
    for i in range(rows):
        for j in range(cols):
            point_value = grid[i][j]
            if point_value and (i, j) not in visited_points:
                dfs(grid, i, j, visited_points)
                result += 1
    
    return result
    
def dfs(self, grid, x, y, visited_points):
    visited_points.add((x, y))
    moves = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        
    for next_x, next_y in  moves:
        next_x = x + next_x
        next_y = y + next_y
            
        if (not ( 0 <= next_x < len(grid) and 0 <= next_y < len(grid[0]))) \
            or grid[next_x][next_y] != 1 \
            or (next_x, next_y) in visited_points:
                continue
        visited_points.add((next_x, next_y))
        self.dfs(grid, next_x, next_y, visited_points)