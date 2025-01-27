import copy

def spread_fire(grid):
    """Update the forest grid based on fire spreading rules.

    - 0: Empty cell
    - 1: Tree
    - 2: Burning tree
    """
    grid_size = len(grid)
    update_grid = copy.deepcopy(grid)
    for i in range(grid_size):
        for j in range(grid_size):
            if grid[i][j] == 1:
                neighbors = []
                # Check boundaries
                if i > 0: 
                    neighbors.append(grid[i-1][j])  # Top
                if i < grid_size - 1:
                    neighbors.append(grid[i+1][j])  # Bottom
                if j > 0:
                    neighbors.append(grid[i][j-1])  # Left
                if j < grid_size - 1:
                    neighbors.append(grid[i][j+1])  # Right
                # If any neighbor is burning, this tree catches fire
                if 2 in neighbors:
                    update_grid[i][j] = 2
    return update_grid

def print_grid(grid):
    """Helper function to print the grid."""
    for row in grid:
        print(" ".join(str(cell) for cell in row))
    print()

# Test case
grid = [
    [1, 1, 1, 0],
    [1, 2, 1, 0],
    [1, 1, 1, 0],
    [0, 0, 0, 0],
]

print("Before spreading fire:")
print_grid(grid)

updated_grid = spread_fire(grid)

print("After spreading fire:")
print_grid(updated_grid)
