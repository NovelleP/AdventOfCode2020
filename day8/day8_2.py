def parse_instruction(line):
    op, arg = line.strip().split(' ')
    return op, int(arg)


def acc(arg, accumulator):
    return accumulator + arg


def jmp(arg, pc):
    return pc + arg


def change_instruction(instruction, instruction_mapping):
    return instruction_mapping[instruction[0]], instruction[1]


def execute_without_loops(instructions, accumulator, pc, executed):
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
    return pc, accumulator


if __name__ == '__main__':
    with open('input', 'r') as f:
        instructions = [parse_instruction(line) for line in f.readlines()]

    instruction_ampping = {
        'jmp': 'nop',
        'nop': 'jmp'
    }
    instructions_to_change_idx = (idx for idx, (op, _) in enumerate(instructions) if op in instruction_ampping)
    for idx in instructions_to_change_idx:
        new_instruction = change_instruction(instructions[idx], instruction_ampping)
        tmp_instructions = [*instructions[:idx], new_instruction, *instructions[idx + 1:]]
        pc, accumulator = execute_without_loops(tmp_instructions, 0, 0, [False for _ in instructions])
        if pc == len(instructions):
            print(accumulator)
            break

