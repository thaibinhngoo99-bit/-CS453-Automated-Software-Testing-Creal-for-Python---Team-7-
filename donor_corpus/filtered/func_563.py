@utils.part1
def part1(puzzleInput: str):
    coordList = [[tuple((int(coord) for coord in pair.split(','))) for pair in line.split(' -> ')] for line in puzzleInput.strip().splitlines()]
    part1Grid: dict[tuple[int, int], int] = {}
    part2Grid: dict[tuple[int, int], int] = {}
    for (startX, startY), (endX, endY) in coordList:
        xMod = -1 if endX < startX else 1
        xRange = range(startX, endX + xMod, xMod)
        yMod = -1 if endY < startY else 1
        yRange = range(startY, endY + yMod, yMod)
        if startX == endX or startY == endY:
            for x in xRange:
                for y in yRange:
                    part1Grid[x, y] = part1Grid.get((x, y), 0) + 1
                    part2Grid[x, y] = part2Grid.get((x, y), 0) + 1
        else:
            for i, x in enumerate(xRange):
                y = yRange[i]
                part2Grid[x, y] = part2Grid.get((x, y), 0) + 1
    if utils.getOption('draw'):
        from PIL import Image
        maxX, maxY = (0, 0)
        for (startX, startY), (endX, endY) in coordList:
            maxX = max(startX, endX, maxX)
            maxY = max(startY, endY, maxY)
        for i, grid in enumerate([part1Grid, part2Grid]):
            canvas = Image.new('RGB', (maxX + 1, maxY + 1))
            for coord, count in grid.items():
                canvas.putpixel(coord, (255, 0, 0) if count > 1 else (255, 255, 255))
            canvas.save(pathlib.Path.cwd() / f'day05.part{i + 1}.png')
    utils.printAnswer(len([item for item in part1Grid.items() if item[1] > 1]))
    return len([item for item in part2Grid.items() if item[1] > 1])