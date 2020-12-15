if __name__ == '__main__':
    with open('input', 'r') as f:
        input = list(map(int, f.read().split(',')))

    game_state = {num: (idx + 1) for idx, num in enumerate(input[:-1])}
    prev_num = act_num = input[-1]
    for prev_idx in range(len(input), 2020):
        act_num = prev_idx - game_state[prev_num] if prev_num in game_state else 0
        game_state[prev_num] = prev_idx
        prev_num = act_num
    print(act_num)
