# Day 4: Printing Department

NEIGHBORS = [
    (-1, -1), (0, -1), (1, -1),
    (-1,  0),          (1,  0),
    (-1,  1), (0,  1), (1,  1),
]

def load_grid():
    grid = []
    with open("day_4/input.csv") as f:
        for row in f:
            grid.append(list(row.strip()))
    return grid

def count_adjacent_rolls(grid, y0, x0):
    height = len(grid)
    width = len(grid[0])
    count = 0

    for dx, dy in NEIGHBORS:
        x1 = x0 + dx
        y1 = y0 + dy
        if 0 <= x1 < width and 0 <= y1 < height:
            if grid[y1][x1] == "@":
                count += 1

    return count

def part1():
    grid = load_grid()
    height = len(grid)
    width = len(grid[0])

    total = 0
    for y in range(height):
        for x in range(width):
            if grid[y][x] == "@":
                if count_adjacent_rolls(grid, y, x) < 4:
                    total += 1

    print(total)

def part2():
    grid = load_grid()
    height = len(grid)
    width = len(grid[0])
    total_removed = 0

    while True:
        # Find all rolls that can be removed this round
        to_remove = []
        for y in range(height):
            for x in range(width):
                if grid[y][x] == "@":
                    if count_adjacent_rolls(grid, y, x) < 4:
                        to_remove.append((y,x))

        if not to_remove:
            break

        for y, x in to_remove:
            grid[y][x] = "x"
            total_removed += 1

    print(total_removed)

part1()
part2()
