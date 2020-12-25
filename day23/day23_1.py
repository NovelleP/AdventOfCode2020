if __name__ == '__main__':
    with open('input', 'r') as f:
        cups = list(map(int, f.readline()))

    size = len(cups)
    idx = 0
    for _ in range(100):
        curr = cups[idx]
        removed_cups = [cups[(idx+1) % size], cups[(idx+2) % size], cups[(idx+3) % size]]
        active_cups = cups[::]
        for cup in removed_cups:
            active_cups.remove(cup)
        target = curr - 1
        min_cup, max_cup = min(active_cups), max(active_cups)
        while target in set(removed_cups) and target >= min_cup:
            target -= 1
        if target < min_cup:
            target = max_cup
        target_idx = active_cups.index(target)
        cups = active_cups[:target_idx+1] + removed_cups + active_cups[target_idx+1:]
        idx = (cups.index(curr) + 1) % size
    index_1 = cups.index(1)
    print(''.join(map(str, [*cups[(index_1+1) % size:], *cups[:index_1]])))