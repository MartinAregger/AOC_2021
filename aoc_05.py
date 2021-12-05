# input
lines = [
    (line.replace(" -> ", ",").split(","))
    for line in open("Data/aoc_05.txt").read().split("\n")
]
lines = [[int(value) for value in coord] for coord in lines]
lines = [[(p[0], p[1]), (p[2], p[3])] for p in lines]



def find_line_points(p1,p2):
    if p1[0]==p2[0]:
        x_values = [p1[0] for _ in range(abs(p1[1]-p2[1])+1)]
    elif (p1[0]<p2[0]):
        x_values = [x for x in range(p1[0],p2[0]+1)]
    elif (p1[0]>p2[0]):
        x_values = [x for x in range(p1[0],p2[0]-1,-1)]
        
    if p1[1]==p2[1]:
        y_values = [p1[1] for _ in range(abs(p1[0]-p2[0])+1)]
    elif (p1[1]<p2[1]):
        y_values = [y for y in range(p1[1],p2[1]+1)]
    elif (p1[1]>p2[1]):
        y_values = [y for y in range(p1[1],p2[1]-1,-1)]

    if "x_values" in locals():
        return zip(x_values,y_values)
    
# board
board = [[0] * 1000 for _ in range(1000)]

#A1
orthogonal_lines = [point for point in lines if (point[0][0]==point[1][0]) or (point[0][1]==point[1][1])]
points_hit = [find_line_points(p1, p2) for p1, p2 in orthogonal_lines]
for p in [item for sublist in points_hit for item in sublist]:
    board[p[0]][p[1]] += 1
print(f"Answer 1: {sum(len([x for x in line if x > 1]) for line in board)}")

#A2
diagonal_lines = [point for point in lines if (point[0][0]!=point[1][0]) and (point[0][1]!=point[1][1])]
points_hit = [find_line_points(p1, p2) for p1, p2 in diagonal_lines]
for p in [item for sublist in points_hit for item in sublist]:
    board[p[0]][p[1]] += 1
print(f"Answer 2: {sum(len([x for x in line if x > 1]) for line in board)}")


