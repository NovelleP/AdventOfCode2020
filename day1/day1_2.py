def search_target_by_3numsum(nums, target):
    for idx1 in range(len(nums)):
        diff = set()
        for idx2 in range(idx1 + 1, len(nums)):
            if (target - nums[idx1] - nums[idx2]) in diff:
                return nums[idx1], nums[idx2], (target - nums[idx1] - nums[idx2])
            diff.add(nums[idx1])
            diff.add(nums[idx2])
    return float('nan'), float('nan'), float('nan')


if __name__ == '__main__':
    with open('input', 'r') as f:
        nums = [int(num) for num in f.readlines()]
    target = 2020
    num1, num2, num3 = search_target_by_3numsum(nums, target)
    print(num1, num2, num3, num1*num2*num3)
