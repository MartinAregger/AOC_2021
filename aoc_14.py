def dijkstra(grid):
    dist={}
    points={}
    ind = [(x,y) for x in range(len(grid[0])) for y in range(len(grid))]
    for x,y in ind:
        dist[(x,y)] = 0 if x == y == 0 else float("inf")
        points[(x,y)] = grid[x][y]

    while ind:
        left_over_distances = {k: dist[k] for k in ind}
        x,y = min(left_over_distances, key=left_over_distances.get)
        ind.remove((x,y))
        neighbors = [i for i in[(x-1,y),(x+1, y),(x,y-1),(x,y+1)] if i[0]>=0 and i[1]>=0 and i[0] < len(grid) and i[1] < len(grid[0])]
        for p in neighbors:  
            temp_dist = dist.get((x,y)) + (points.get(p))
            if temp_dist < dist.get(p):
                dist[p] = temp_dist
    return dist

grid = [list(line.replace("\n","")) for line in open("Data/aoc_14.txt")]
ext_grid = grid = [[int(i) for i in j] for j in grid]
print(f"Answer 1: {dijkstra(grid)[(len(grid[0])-1,len(grid[0])-1)]}")

for _ in range(2):
    ext_grid = [[line,list(map(lambda x: (x%9+1) ,line)),list(map(lambda x: (x+1)%9+1 ,line)),list(map(lambda x: (x+2)%9+1 ,line)),list(map(lambda x: (x+3)%9+1 ,line))] for line in ext_grid]
    ext_grid = list(map(list,zip(*[[val for sublist in g for val in sublist] for g in ext_grid])))

print(f"Answer 2: {dijkstra(ext_grid)[(len(ext_grid[0])-1,len(ext_grid[0])-1)]}")