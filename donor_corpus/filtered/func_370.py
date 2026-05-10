def step(grid):
    grid += 1
    flash = np.zeros_like(grid, dtype=bool)
    while np.any(grid[~flash] > 9):
        new_flash = (grid > 9) ^ flash
        grid[:-1, :-1] += new_flash[1:, 1:]
        grid[:-1, :] += new_flash[1:, :]
        grid[:-1, 1:] += new_flash[1:, :-1]
        grid[:, :-1] += new_flash[:, 1:]
        grid[:, 1:] += new_flash[:, :-1]
        grid[1:, :-1] += new_flash[:-1, 1:]
        grid[1:, :] += new_flash[:-1, :]
        grid[1:, 1:] += new_flash[:-1, :-1]
        flash |= new_flash
    grid[flash] = 0
    return flash