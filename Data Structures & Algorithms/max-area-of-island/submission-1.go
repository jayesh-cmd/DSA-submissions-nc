func maxAreaOfIsland(grid [][]int) int {
    row := len(grid)
    col := len(grid[0])

    var dfs func(r, c int) int

    dfs = func(r, c int)int{
        if r < 0 || r >= row || c < 0 || c >= col || grid[r][c] != 1{
            return 0
        }

        grid[r][c] = 0

        return 1 + dfs(r, c+1) + dfs(r+1, c) + dfs(r, c-1) + dfs(r-1, c)
    }

    maxarea := 0
    for i := 0; i < row; i++{
        for j := 0; j < col; j++{
            if grid[i][j] == 1{
                cur_area := dfs(i, j)
                if cur_area > maxarea{
                    maxarea = cur_area
                }
            }
        }
    }

    return maxarea
}
