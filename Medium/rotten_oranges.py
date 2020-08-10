"""
In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

"""

#use BFS to traverse through the graph, and find each rotten orange to infect the fresh ones
def orangesRotting(self, grid):
    row = len(grid)
    timestep = 0
    col = len(grid[0])
    queue = []
    num_fresh = 0
    #record the number of fresh oranges, and add the positions of rotten oranges into the queue
    for r in range(row):
        for c in range(col):
            if grid[r][c] == 2:
                queue.append([r, c])
            elif grid[r][c] == 1:
                num_fresh +=1
    #check the corner cases intially
    if num_fresh == 0:
        return 0
    if len(queue) == 0:
        return -1
    #after finding the number of new rotten oranges infected in each round, add a delimeter to the queue so that we know each timestep is done
    queue.append(None)
    prev_num_fresh = num_fresh
    while queue:
        cell = queue.pop(0)
        if cell is None: #cell = None means that we're at the end of one timestep
            #if no new oranges is rotten, and the number of fresh oranges is still positive, return -1 (they will never be rotten)
            if prev_num_fresh == num_fresh and num_fresh != 0:
                return -1
            if len(queue) > 0:
                prev_num_fresh = num_fresh
                timestep+=1 #do not add another timestep if the queue is about to be empty
                queue.append(None)
        else:
            #check if each valid neighbor is a fresh orange, infect it and add it to the queue
            if cell[0] > 0 and grid[cell[0] -1][cell[1]] == 1:
                    grid[cell[0] -1][cell[1]] = 2
                    num_fresh -=1
                    queue.append([cell[0] -1, cell[1]])
            if cell[0] < len(grid)-1 and grid[cell[0] +1][cell[1]] == 1:
                    grid[cell[0] +1][cell[1]] = 2
                    num_fresh -=1
                    queue.append([cell[0] +1, cell[1]])
            if cell[1] > 0 and grid[cell[0]][cell[1] -1] == 1:
                    grid[cell[0]][cell[1] -1] = 2
                    num_fresh -=1
                    queue.append([cell[0], cell[1] -1])
            if cell[1] < len(grid[0])-1 and grid[cell[0]][cell[1]+1] == 1:
                    grid[cell[0]][cell[1] +1] = 2
                    num_fresh -=1
                    queue.append([cell[0], cell[1] +1])
    return timestep