import statistics

def solution_1(input_list: list) -> int:
    return sum(a<b for a,b in zip(input_list,input_list[1:]))


if __name__ == "__main__":
    with open("/mnt/z/vscode_wsl_data/aoc_2021/Data/aoc_01a.txt", "r") as aoc_01_data:
        lines = [int(n) for n in aoc_01_data.readlines()]
        
    # Part 1
    print(solution_1(lines))
    
    # Part 2
    print(solution_1([statistics.mean([a,b,c]) for a,b,c in zip(lines,lines[1:],lines[2:])]))
    