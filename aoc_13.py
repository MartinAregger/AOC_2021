import matplotlib.pyplot as plt

input_data = [line.replace("\n", "") for line in open("Data/aoc_13.txt")]
dots = [(int(point[0]),int(point[1])) for point in [(line.split(",")) for line in input_data if "," in line]]
folds = [(direction[0],int(direction[1])) for direction in [line.replace("fold along ", "").split("=") for line in input_data if "=" in line]]


def fold_paper(fold, dot):
        if (fold[0] == "x") & (dot[0] > fold[1]): return (fold[1]-(dot[0]-fold[1]),dot[1])
        elif (fold[0] == "y") & (dot[1] > fold[1]): return (dot[0],fold[1]-(dot[1]-fold[1]))
        else: return dot

for nr_fold,fold in enumerate(folds):
    dots = [fold_paper(fold, dot) for dot in dots]
    dots = list(set(dots))
    if nr_fold == 0: print(f"Answer 1: {len(dots)}")
    
plt.scatter(*zip(*dots))
plt.savefig("aoc_13.png")