def number_of_islands(grid):

    def bfs(i, j):
        queue = deque([(i, j)])
        grid[i][j] = '0'
        while queue:
            row, col = queue.popleft()
            for x, y in get_neighbors(row, col):
                if grid[x][y] == '0':
                    continue
                queue.append(row, col)
                grid[x][y] = '0'
    count = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '0':
                continue
            bfs(i, j)
            count += 1
    return count
