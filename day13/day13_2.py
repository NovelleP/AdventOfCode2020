def solve(idx, bus_ids, timestamps, diffs, solved):
    if idx >= len(bus_ids):
       return True
    elif (timestamp := timestamps[idx - 1] + diffs[idx - 1]) % bus_ids[idx] == 0:
            timestamps[idx] = timestamp
            return solve(idx + 1, bus_ids, timestamps, diffs, solved)
    else:
        return False


if __name__ == '__main__':
    with open('input', 'r') as f:
        time = int(f.readline())
        pos_bus_ids = [(idx, int(bus_id)) for idx, bus_id in enumerate(f.readline().split(',')) if bus_id != 'x']

    bus_ids = [bus_id for _, bus_id in pos_bus_ids]
    pos = [pos for pos, _ in pos_bus_ids]
    diffs = [b - a for a, b in zip(pos[:-1], pos[1:])]
    timestamps = [0] * len(bus_ids)
    solved = False
    while not solved:
        timestamps[0] += bus_ids[0]
        solved = solve(1, bus_ids, timestamps, diffs, solved)
    print(solved, timestamps)
