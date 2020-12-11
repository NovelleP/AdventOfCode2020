def two_sum(target, nums):
    diff = set()
    for num in nums:
        if (target - num) in diff:
            return True
        diff.add(num)
    return False


if __name__ == '__main__':
    with open('input', 'r') as f:
        nums = [int(num) for num in f.readlines()]

    start = 25
    for idx in range(start, len(nums)):
        if not two_sum(nums[idx], nums[idx-25: idx]):
            print(nums[idx])

