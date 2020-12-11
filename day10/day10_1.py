def counting_sort(joltages):
    min_joltage, max_joltage = min(joltages), max(joltages)
    available_joltages = [False for _ in range(min_joltage, max_joltage + 1)]
    offset = min_joltage
    for joltage in joltages:
        available_joltages[joltage - offset] = True
    return [(idx + offset) for idx, is_available in enumerate(available_joltages) if is_available]

if __name__ == '__main__':
    with open('input', 'r') as f:
        joltages = [int(joltage) for joltage in f.readlines()]

    joltages.extend((0, max(joltages) + 3))
    sorted_joltages = counting_sort(joltages)

    offset = sorted_joltages[0]
    joltdiff_1, joltdiff_3 = 0, 0
    prev_joltage = sorted_joltages[0]
    for joltage in sorted_joltages:
        if (joltage - prev_joltage) == 1:
            joltdiff_1 += 1
        elif (joltage - prev_joltage) == 3:
            joltdiff_3 += 1
        prev_joltage = joltage
    print(joltdiff_1, joltdiff_3, joltdiff_1 * joltdiff_3)
