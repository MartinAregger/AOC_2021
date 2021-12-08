
output_codes = []

for line in open("Data/aoc_08.txt").read().splitlines():
    input, output = [list(filter(None, codes.split(" "))) for codes in line.split("|")]
    input = ["".join(sorted(code)) for code in input]
    output = ["".join(sorted(code)) for code in output]

    lengths = dict([(len(code), code) for code in set(input + output)])
    t_dict = {}
    t_dict[1], t_dict[4], t_dict[7], t_dict[8] = lengths[2], lengths[4], lengths[3], lengths[7]

    for code in set(output+input):
        if len(code) == 5:
            if len((set(code) & set(t_dict[1]))) == 2: t_dict[3] = code 
            elif len((set(code) & set(t_dict[4]))) == 2: t_dict[2] = code 
            else: t_dict[5] = code 
        if len(code) == 6:
            if len((set(code) & set(t_dict[1]))) == 1: t_dict[6] = code
            elif len((set(code) & set(t_dict[4]))) == 4: t_dict[9] = code 
            else: t_dict[0] = code
    
    t_dict_inv = {v: k for k, v in t_dict.items()}
    output_codes.append([t_dict_inv[code] for code in output])

print(f"Answer 1: {len([f for sublist in output_codes for f in sublist if f in [1,4,7,8]])}")
print(f'Answer 2: {sum(int("".join([str(code) for code in sublist]))for sublist in output_codes)}')