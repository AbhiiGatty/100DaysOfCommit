# Problem Statememt: https://projecteuler.net/problem=11


def greatest_product(grid):
    adjacent_nums = 4
    grid_size = len(grid)
    max_product = 0
    curr_product = 0
    # For left and right direction
    for i in range(grid_size):
        for j in range(grid_size - adjacent_nums):
            curr_product = grid[i][j] * grid[i][j+1] * grid[i][j+2] * grid[i][j+3]
            if curr_product > max_product: max_product = curr_product
    # For up and down direction
    for i in range(grid_size - adjacent_nums):
        for j in range(grid_size):
            curr_product = grid[i][j] * grid[i+1][j] * grid[i+2][j] * grid[i+3][j]
            if curr_product > max_product: max_product = curr_product
    # For diagonal direction
    for i in range(grid_size - adjacent_nums): # Diagonal from top left to bottom right
        for j in range(grid_size - adjacent_nums):
            curr_product = grid[i][j] * grid[i+1][j+1] * grid[i+2][j+2] * grid[i+3][j+3]
            if curr_product > max_product: max_product = curr_product
                
    for i in range(-1, -1 * (grid_size - adjacent_nums + 1), -1):
        for j in range(grid_size - adjacent_nums): # Diagonal from the bottom left to top right
            curr_product = grid[i][j] * grid[i-1][j+1] * grid[i-2][j+2] * grid[i-3][j+3]
            if curr_product > max_product: max_product = curr_product
    
    return max_product

if __name__ == "__main__":
    grid = [ list(map(int,i.split())) for i in open('problem_11_input.txt').read().splitlines() ]
    answer = greatest_product(grid)
    print("The greatest product in the grid is: {}".format(answer))




