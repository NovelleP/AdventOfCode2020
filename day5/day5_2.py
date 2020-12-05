def lower_half(start, end):
    return start, ((end + start - 1) // 2)


def upper_half(start, end):
    return ((end + start + 1) // 2), end


def calc_seatid(row, col):
    return row * 8 + col


def find_seat(instructions, row_range, col_range):
    for inst in instructions:
        if inst in row_instructions:
            row_range = instruction_to_fun[inst](*row_range)
        elif inst in col_instructions:
            col_range = instruction_to_fun[inst](*col_range)
    return row_range[0], col_range[0]


if __name__ == '__main__':

    row_instructions = {'F', 'B'}
    col_instructions = {'L', 'R'}
    instruction_to_fun = {
        'F': lower_half,
        'B': upper_half,
        'L': lower_half,
        'R': upper_half
    }

    row_range = (0, 127)
    col_range = (0, 7)
    seat_ids = []
    with open('input', 'r') as f:
        for line in f.readlines():
            row, col = find_seat(line, row_range, col_range)
            seat_ids.append(calc_seatid(row, col))
    seat_ids.sort()
    print(seat_ids)

    for seat_id in range(seat_ids[0], seat_ids[-1]+1):
        if seat_id not in seat_ids:
            print(seat_id)
