fishies = [int(fish) for fish in open("Data/aoc_06.txt").read().split(",")]
fishies_by_type = [fishies.count(type) for type in range(9)]

for day in range(256):
    if day == 80:
        print(f"Answer 1: {sum(fishies_by_type)}")
    
    new_fishies = fishies_by_type[0]
    
    for type in range(8):
        fishies_by_type[type] = fishies_by_type[type + 1]
    
    fishies_by_type[6], fishies_by_type[8] = (
        fishies_by_type[6] + new_fishies,
        new_fishies,
    )


print(f"Answer 2: {sum(fishies_by_type)}")
