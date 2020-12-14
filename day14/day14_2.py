import re
import itertools


def apply_mask(mask, val):
    return ''.join(v if m == '0' else '1' if m == '1' else '{}' for m, v in zip(mask, val))


if __name__ == '__main__':

    size = 36
    mem = {}
    mask = 'X' * size
    variable_positions = mask.count('X')

    with open('input', 'r') as f:
        for line in f.readlines():
            if (match := re.search('(?<=mask = )[0-9X]+', line)):
                mask = match.group().zfill(size)
                variable_positions = mask.count('X')
            else:
                dir, val = re.search('mem\[([0-9]+)\] = ([0-9]+)', line).groups()
                dir_template = apply_mask(mask, bin(int(dir))[2:].zfill(size))
                for c in itertools.product('01', repeat=variable_positions):
                    mem[dir_template.format(*c)] = val

    print(sum(int(val) for val in mem.values()))