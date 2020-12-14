import re


def apply_mask(mask, val):
    return ''.join(m if m in {'0', '1'} else v for m, v in zip(mask, val))


if __name__ == '__main__':

    size = 36
    mem = {}
    mask = 'X' * size

    with open('input', 'r') as f:
        for line in f.readlines():
            if (match := re.search('(?<=mask = )[0-9X]+', line)):
                mask = match.group().zfill(size)
            else:
                dir, val = re.search('mem\[([0-9]+)\] = ([0-9]+)', line).groups()
                mem[dir] = apply_mask(mask, bin(int(val))[2:].zfill(size))

    print(sum(int(val, 2) for val in mem.values()))
