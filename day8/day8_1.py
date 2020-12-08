def parse_instruction(line):
    op, arg = line.strip().split(' ')
    return op, int(arg)


def acc(arg, accumulator):
    return accumulator + arg


def jmp(arg, pc):
    return pc + arg


def run_without_loops(instructions, accumulator, pc, executed):
    while (pc < len(instructions)) and (not executed[pc]):
        executed[pc] = True
        op, arg = instructions[pc]
        if op == 'acc':
            accumulator = acc(arg, accumulator)
            pc += 1
        elif op == 'jmp':
            pc = jmp(arg, pc)
        else:
            pc += 1
    return accumulator


if __name__ == '__main__':
    with open('input', 'r') as f:
        instructions = [parse_instruction(line) for line in f.readlines()]

    print(run_without_loops(instructions, 0, 0, [False for _ in instructions]))

