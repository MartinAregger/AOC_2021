
with open("Data/aoc_01a.txt", "r") as aoc_01_data:
    lines = [int(n) for n in aoc_01_data.readlines()]
    
# Part 1
print(sum(a<b for a,b in zip(lines,lines[1:]))

)

# Part 2
print(sum(a<b for a,b in zip(lines,lines[3:])))