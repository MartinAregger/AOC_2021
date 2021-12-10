from statistics import median
k_dict = {"(": ")", "[": "]", "{": "}", "<": ">"}
points_dict_corrupted = {")": 3,"]": 57,"}":1197, ">":25137}
points_dict_misses = {")": 1, "]":2, "}":3,">":4}

corrupted_list = []
miss_list = []
for line in open("Data/aoc_10.txt").read().splitlines():
    r_list = []
    for c in line:
        if c in k_dict:
            r_list.insert(0,k_dict[c])
        elif c == r_list[0]:
            r_list.pop(0)
        else:
            corrupted_list.append(c)
            r_list=[]
            break
    if r_list: 
        points = 0
        for c in [points_dict_misses[c] for c in r_list]:
            points = points*5 + c
        miss_list.append(points)

print(f"Answer 1: {sum(points_dict_corrupted[c] for c in corrupted_list)}")
print(f"Answer 2: {median(miss_list)}")