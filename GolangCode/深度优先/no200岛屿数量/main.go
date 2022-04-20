package main

func numIslands(grid [][]byte) int {
	if len(grid) == 0 {
		return 0
	}
	island := byte(1)
	count := 0
	for y, _ := range grid {
		for x, _ := range grid[0] {
			if grid[y][x] == island {
				count += 1
			}
			dfs(grid, y, x)
		}
	}
	return count
}

func dfs(grid [][]byte, row int, column int) {
	var island byte
	island = 1
	if row < 0 || row >= len(grid) || column < 0 || column >= len(grid[0]) {
		return
	}
	if grid[row][column] != island {
		return
	}
	grid[row][column] = 2
	dfs(grid, row-1, column)
	dfs(grid, row+1, column)
	dfs(grid, row, column+1)
	dfs(grid, row, column-1)
}
