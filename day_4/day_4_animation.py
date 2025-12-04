import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.colors as mcolors 
import numpy as np

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

# Convert grid to numeric matrix for plotting
def grid_to_array(grid):
    arr = np.zeros((len(grid), len(grid[0])), dtype=int)
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "@":
                arr[y, x] = 1
            elif grid[y][x] == "x":
                arr[y, x] = 2
            # '.' stays 0
    return arr

# Create all frames of the animation
def generate_frames(grid):
    frames = []
    height = len(grid)
    width = len(grid[0])
    while True:
        to_remove = []
        for y in range(height):
            for x in range(width):
                if grid[y][x] == "@":
                    if count_adjacent_rolls(grid, y, x) < 4:
                        to_remove.append((y, x))
        if not to_remove:
            break
        for y, x in to_remove:
            grid[y][x] = "x"
        frames.append(grid_to_array(grid))
    return frames

grid = load_grid()
frames = generate_frames(grid)

fig, ax = plt.subplots()
cmap = mcolors.ListedColormap(['grey', 'black', 'grey'])
im = ax.imshow(frames[0], cmap=cmap)

def update(frame):
    im.set_data(frame)
    return [im]

ani = FuncAnimation(fig, update, frames=frames, interval=50, blit=True)
plt.xticks([])
plt.yticks([])
plt.show()
