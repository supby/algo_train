'''
2. You have a map of the monitor's pixels (of width W and height H) where good pixels are marked with zeros and dead pixels are marked with ones. Write a code that returns the number of dead pixel groups. If two pixels are adjacent to each other vertically or horizontally, they are considered a part of one group.

1 <= W <= 7680

1 <= H <= 4320

Example 1: input - [1,0,1], output - 4
				   [0,0,0],
				   [1,0,1]
				   
Example 2: input - [1,1,1], output - 2
				   [1,0,0],
				   [1,0,1]
'''

def count_groups(mat:[]) -> int:

    if not mat: return 0

    height = len(mat)
    width = len(mat[0])

    visited = set()
    group_count = 0

    for i in range(height):
        for j in range(width):
            cell = (i,j)
            if cell not in visited and mat[cell[0]][cell[1]] == 1:
                visited.add(cell)
                group_count += 1
                mark_group(mat, cell, visited, height, width)

    return group_count

def mark_group(mat:[], cell: (), visited: {}, height: int, width: int) -> int:
    for d in [[0,1],[1,0],[0,-1],[-1,0]]:        
        next_cell = (cell[0]+d[0], cell[1]+d[1])        
        if next_cell[0] > height - 1 or \
            next_cell[0] < 0 or \
            next_cell[1] > width - 1 or \
            next_cell[1] < 0:
            continue
        
        if next_cell not in visited and mat[next_cell[0]][next_cell[1]] == 1:
            visited.add(next_cell)
            mark_group(mat, next_cell, visited, height, width)

print(count_groups([[1,0,1],
				   [0,0,0],
				   [1,0,1]])) # res: 4

print(count_groups([[1,1,1],
				   [1,0,0],
				   [1,0,1]])) # res: 2

print(count_groups([])) # res: 0

print(count_groups(None)) # res: 0

print(count_groups([[1],[1]])) # res: 1




