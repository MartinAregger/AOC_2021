with open("Data/aoc_02.txt", "r") as input_file:
    lines = [(line.split(" ")) for line in input_file.read().splitlines()]

depth = distance = aim = 0

for direction, steps in lines:
    steps = int(steps)
    match direction:
        case "down":
            aim += steps
        case "forward":
            distance += steps
            depth += aim*steps
        case  "up":
            aim -= steps
            
        
print(f"Answer 1: {aim*distance}")
print(f"Answer 2: {depth*distance}")
