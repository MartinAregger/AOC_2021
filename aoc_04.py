import numpy as np

with open("Data/aoc_04.txt", "r") as input_file:
    lines = [(line.split()) for line in input_file.read().splitlines()]

picked_numbers = [int(value) for value in lines.pop(0)[0].split(",")]

board_list_list = []
board_array_list = []

for line in lines[1:]:
    line = [int(element) for element in line]
    if bool(line):
        board_list_list.append(line)
    else:
        board_array_list.append(np.array(board_list_list))
        board_list_list = []

# bingo
def check_for_bingo(board):
    return (np.any(np.all((board == 0), axis=1))) | (
        np.any(np.all((board == 0), axis=0))
    )

bingo_counter = 0
last_bingo_board_sum = np.nan
for called_number in picked_numbers:
    board_array_list = [
        np.where(board == called_number, 0, board) for board in board_array_list
    ]
    for board_id, board  in enumerate(board_array_list):
        if check_for_bingo(board):
            last_bingo_board_sum = np.sum(board) * called_number
            if bingo_counter == 0:
                print(f"Answer 1:{last_bingo_board_sum}")
            bingo_counter += 1
            board_array_list.pop(board_id)
            
print(f"Answer 2: {last_bingo_board_sum}")
