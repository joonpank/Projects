"""
Game of Life. The simulation is based on following rules:

1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
2. Any live cell with two or three live neighbours lives on to the next generation.
3. Any live cell with more than three live neighbours dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

White Cells indicate living cell and black dead one.
"""
import numpy as np
import cv2
import random

# Give height and width as parameters
height = 200
width = 200
seed = None

def create_random_binary_array(n) -> list():
    # Create random array of zeros and ones with array being length of n.
    # Probability for 1 or 0 are equally 50/50.
    binary_array = []
    for i in range(n):
        if random.random() < 0.50:
            binary_array.append(0)
        else:
            binary_array.append(1)

    return binary_array

# Create random binary arrays to make random grid of ones and zeros
def random_seed() -> list():
    # Create a grid if it does not exists
    if not seed:
        # create 2D grid of arrays
        grid = []
        for i in range(height):
            row = create_random_binary_array(width)
            grid.append(row)

        grid = np.array(grid)
        return grid


def update_frame(grid) -> list():
    new_array = []
    for i in range(height):
        row = []
        for j in range(width):
            updated_cell = check_cell(grid, i, j)
            row.append(updated_cell)
        new_array.append(row)

    new_array = np.array(new_array, dtype= "uint16")
    return new_array


def check_cell(grid, i, j) -> int():
    # Check if grid cell element (i,j) dies, comes to life or stays the same.
    # Check all surrounding neigbour status, living neigbour has status of 1.
    # Iterate from i-1 to i+1 and from j-1 to j+1.
    living_neigbours = 0
    for k in range(3):
        for l in range(3):
            try:
                if grid[i-1 + k, j-1 + l] == 1:
                    living_neigbours += 1
            except:
                pass

    if living_neigbours == 3 and grid[i,j] == 0:
        return 1
    elif living_neigbours > 2:
        if living_neigbours > 3:
            return 0
        else:
            return 1

    elif living_neigbours < 2:
        return 0
    else:
        return 0


def scale_frame(grid):
    # Scales frame with desired multiplier
    scale_percent = 500 # percent of original size
    w = int(grid.shape[1] * scale_percent / 100)
    h = int(grid.shape[0] * scale_percent / 100)
    dim = (w, h)
    resized = cv2.resize(grid, dim, interpolation = cv2.INTER_AREA)
    return resized

def main():
    grid = random_seed()
    while True:
        # Get a numpy array to display from the simulation
        grid = update_frame(grid)
        resized = scale_frame(grid)
        cv2.imshow('image', resized.astype(np.float32))
        cv2.waitKey(1)

if __name__ == "__main__":
    main()
