def compute_max_path_sum(grid):
    memo = make_blank_grid(len(grid))

    def dfs(i, j):
        if i == len(grid):
            return 0
        if memo[i][j] == UNKNOWN:
            memo[i][j] = grid[i][j] + max(dfs(i + 1, j), dfs(i + 1, j + 1))
        return memo[i][j]
    return dfs(0, 0)