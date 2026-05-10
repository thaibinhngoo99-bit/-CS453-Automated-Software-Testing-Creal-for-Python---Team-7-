def main():
    data = '5483143223\n2745854711\n5264556173\n6141336146\n6357385478\n4167524645\n2176841721\n6882881134\n4846848554\n5283751526'
    data = aocd.get_data(day=DAY, year=YEAR)
    inlist = np.array([list(map(int, l)) for l in data.split('\n')])
    print(inlist)
    grid = inlist.copy()
    num_flashes = 0
    for i in range(100):
        num_flashes += np.sum(step(grid))
    print(num_flashes)
    answer = num_flashes
    aocd.submit(answer, part='a', day=DAY, year=YEAR)
    grid = inlist.copy()
    for i in itertools.count(1):
        flash = step(grid)
        if np.all(flash):
            answer = i
            break
    print(answer)
    aocd.submit(answer, part='b', day=DAY, year=YEAR)