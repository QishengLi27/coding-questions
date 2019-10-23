# There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

# Given the ball's start position, the destination and the maze, find the shortest distance for the ball to stop at the destination. The distance is defined by the number of empty spaces traveled by the ball from the start position (excluded) to the destination (included). If the ball cannot stop at the destination, return -1.

# The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.

# Input:  
# 	(rowStart, colStart) = (0,4)
# 	(rowDest, colDest)= (4,4)
# 	0 0 1 0 0
# 	0 0 0 0 0
# 	0 0 0 1 0
# 	1 1 0 1 1
# 	0 0 0 0 0

# 	Output:  12
	
# 	Explanation:
# 	(0,4)->(0,3)->(1,3)->(1,2)->(1,1)->(1,0)->(2,0)->(2,1)->(2,2)->(3,2)->(4,2)->(4,3)->(4,4)

# https://www.lintcode.com/problem/the-maze-ii/description

# Note: the difference between this maze problem and treasure island is that in maze you
# 		you won't stop rolling until hitting a wall

from collections import deque

def shortestDistance(maze, start, destination):
    # write your code here
    rows = len(maze)
    cols = len(maze[0])
    if rows == 0 or cols == 0:
        return -1
    
    queue = deque([[start[0],start[1],0]])
    moves = [(1,0),(-1,0),(0,1),(0,-1)]
    
    while queue:
        node = queue.popleft()
        row = node[0]
        col = node[1]
        l = node[2]
        
        maze[row][col] = -1
        if row == destination[0] and col == destination[1]:
            return l
        
        for y, x  in moves:
            new_row = row + y
            new_column = col + x
            new_l = l + 1 
            while 0 <= new_row < rows and 0 <= new_column < cols and maze[new_row][new_column] != 1:
                new_row += y
                new_column += x
                new_l += 1
            new_row -= y
            new_column -= x
            new_l -= 1
            
            if maze[new_row][new_column] == 0:
                queue.append([new_row,new_column,new_l])
    return -1