    match (np.where(np.sum(grid, axis=0)>grid.shape[0]/2, True, False)[i]):
#         case True:
#             grid = np.where(grid[i],1,0) * grid
# print(grid)