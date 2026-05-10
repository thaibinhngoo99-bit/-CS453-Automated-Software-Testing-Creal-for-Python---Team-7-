#!/usr/bin/env python3

UNKNOWN = -1

def read_val():
    return int(input())

def read_row():
    return list(map(int, input().split()))

def read_grid():
    return [read_row() for _ in range(read_val())]

def make_blank_row(i):
    return [UNKNOWN] * i

def make_blank_grid(n):
    return [make_blank_row(i) for i in range(1, n + 1)]

def compute_max_path_sum(grid):
    memo = make_blank_grid(len(grid))
    
    def dfs(i, j):
        if i == len(grid):
            return 0
        
        if memo[i][j] == UNKNOWN:
            memo[i][j] = grid[i][j] + max(dfs(i + 1, j), dfs(i + 1, j + 1))
        
        return memo[i][j]
    
    return dfs(0, 0)

for t in range(read_val()):
    print(compute_max_path_sum(read_grid()))
