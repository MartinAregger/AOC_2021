import numpy as np


lines = [[int(c) for c in list(code.rstrip("\n"))] for code in open("Data/aoc_03.txt")]
grid = np.array(lines)

# 1
gamma = np.where(np.sum(grid, axis=0)>grid.shape[0]/2, 1, 0)
gamma = int(str.join('',map(str, gamma)),2)

print(f"Answer 1: {gamma*(~gamma&0xFFF)}") 


# 2
def get_rating(input_grid, rating):
    i = 0
    while input_grid.shape[0] > 1:    
        more_ones = (np.where(np.sum(input_grid, axis=0)>=input_grid.shape[0]/2, True, False)[i])
        if (more_ones & (rating == "O2")) or ((not more_ones) & (rating == "CO2")):
            input_grid = input_grid[input_grid[:,i] == 1]
        else:
            input_grid = input_grid[input_grid[:,i] == 0]
        i += 1

    return int(str.join('',map(str, input_grid[0])),2)

print(f"Answer 2: {get_rating(grid, 'O2') * get_rating(grid, 'CO2')}")