def search_target_by_2numsum(nums, target):
    diff = set()
    for num in nums:
        if (target - num) in diff:
            return (target - num), num
        diff.add(num)
    return float('nan'), float('nan')


if __name__ == '__main__':
    with open('input', 'r') as f:
        nums = [int(num) for num in f.readlines()]
    target = 2020
    num1, num2 = search_target_by_2numsum(nums, target)
    print(num1, num2, num1*num2)
