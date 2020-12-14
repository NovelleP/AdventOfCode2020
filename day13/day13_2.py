import math


def lcm(nums):
    lcm = 1
    for num in nums:
        lcm = lcm * num // math.gcd(lcm, num)
    return lcm


def solve(idx, bus_ids, timestamps, diffs):
    if idx >= len(bus_ids):
       return idx
    elif (timestamp := timestamps[idx - 1] + diffs[idx - 1]) % bus_ids[idx] == 0:
            timestamps[idx] = timestamp
            return solve(idx + 1, bus_ids, timestamps, diffs)
    else:
        return idx


if __name__ == '__main__':
    with open('input', 'r') as f:
        time = int(f.readline())
        pos_bus_ids = [(idx, int(bus_id)) for idx, bus_id in enumerate(f.readline().split(',')) if bus_id != 'x']

    bus_ids = [bus_id for _, bus_id in pos_bus_ids]
    pos = [pos for pos, _ in pos_bus_ids]
    diffs = [b - a for a, b in zip(pos[:-1], pos[1:])]
    timestamps = [0] * len(bus_ids)
    first_idx_to_check = 1
    step = bus_ids[0]
    while first_idx_to_check < len(bus_ids):
        timestamps[0] += step
        new_first_idx_to_check = solve(1, bus_ids, timestamps, diffs)
        if new_first_idx_to_check > first_idx_to_check:
            first_idx_to_check = new_first_idx_to_check
            step = lcm(bus_ids[:first_idx_to_check])
    print(timestamps[0])