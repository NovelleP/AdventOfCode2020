def counting_sort(joltages):
    min_joltage, max_joltage = min(joltages), max(joltages)
    available_joltages = [False for _ in range(min_joltage, max_joltage + 1)]
    offset = min_joltage
    for joltage in joltages:
        available_joltages[joltage - offset] = True
    return [(idx + offset) for idx, is_available in enumerate(available_joltages) if is_available]

# recursive solution: slow solution for large inputs
def solve(idx, sorted_joltages, ans):
    if idx + 1 == len(sorted_joltages):
        ans[0] += 1
        return
    val = sorted_joltages[idx]
    for curr_idx in range(idx + 1, len(sorted_joltages)):
        curr_val = sorted_joltages[curr_idx]
        if (curr_val - val) > 3:
            break
        solve(curr_idx, sorted_joltages, ans)


def dp_solve(sorted_joltages):
    dp = [0 for _ in sorted_joltages]
    dp[-1] = 1
    for idx in range(len(dp) - 2, -1, -1):
        dp[idx] = sum(dp[i] for i in range(idx+1, idx+4)
                      if (i < len(dp))
                        and ((sorted_joltages[i] - sorted_joltages[idx]) <= 3))
    return dp[0]


if __name__ == '__main__':
    with open('input', 'r') as f:
        joltages = [int(joltage) for joltage in f.readlines()]

    joltages.extend((0, max(joltages) + 3))
    sorted_joltages = counting_sort(joltages)
    '''ans = [0]
    solve(0, sorted_joltages, ans)
    print(ans)'''
    print(dp_solve(sorted_joltages))
