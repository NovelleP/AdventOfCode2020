def windowing_subset_sum(target, start_idx, min_subset_size, nums):
    idx1, idx2 = start_idx, start_idx + 1
    sum = (nums[idx1] + nums[idx2])
    idx2 += 1
    while (idx2 < len(nums)) and (sum < target):
        sum += nums[idx2]
        idx2 += 1
        while sum > target and idx1 <= idx2:
            sum -= nums[idx1]
            idx1 += 1
    return (idx1, idx2-1) if ((sum == target) and (idx2 - idx1) >= min_subset_size) else (None, None)


if __name__ == '__main__':
    with open('input', 'r') as f:
        nums = [int(num) for num in f.readlines()]

    target = 375054920
    idx1, idx2 = windowing_subset_sum(target, 0, 2, nums)
    subset = nums[idx1: idx2+1]
    smallest, largest = min(subset), max(subset)
    print(smallest + largest)

