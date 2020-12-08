def parse_instruction(line):
    op, arg = line.strip().split(' ')
    return op, int(arg)


def acc(arg, accumulator):
    return accumulator + arg


def jmp(arg, pc):
    return pc + arg


def change_instruction(instruction, instruction_mapping):
    return instruction_mapping.get(instruction[0], instruction[0]), instruction[1]


def exec_instruction(op, arg, accumulator, pc):
    if op == 'acc':
        accumulator = acc(arg, accumulator)
        pc += 1
    elif op == 'jmp':
        pc = jmp(arg, pc)
    else:
        pc += 1
    return pc, accumulator


def run_without_loops(instructions, accumulator, pc, executed):
    while (pc < len(instructions)) and (not executed[pc]):
        executed[pc] = True
        op, arg = instructions[pc]
        pc, accumulator = exec_instruction(op, arg, accumulator, pc)
    return pc, accumulator


def run_without_loops_v2(instructions, accumulator, pc, executed, flag, instruction_ampping):
    if pc == len(instructions):
        print(accumulator)
        flag[0] = True
        return

    if not flag[0]:
        if not executed[pc]:
            executed[pc] = True
            op, arg = instructions[pc]
            tmp_pc, tmp_accumulator = exec_instruction(op, arg, accumulator, pc)
            run_without_loops_v2(instructions, tmp_accumulator, tmp_pc, executed, flag, instruction_ampping)
            if op in instruction_ampping and not flag[0]:
                op, arg = change_instruction(instructions[pc], instruction_ampping)
                tmp_pc, tmp_accumulator = exec_instruction(op, arg, accumulator, pc)
                run_without_loops_v2(instructions, tmp_accumulator, tmp_pc, executed, flag, instruction_ampping)



if __name__ == '__main__':
    with open('input', 'r') as f:
        instructions = [parse_instruction(line) for line in f.readlines()]

    instruction_ampping = {
        'jmp': 'nop',
        'nop': 'jmp'
    }
    import time
    start = time.perf_counter_ns()
    instructions_to_change_idx = (idx for idx, (op, _) in enumerate(instructions) if op in instruction_ampping)
    for idx in instructions_to_change_idx:
        new_instruction = change_instruction(instructions[idx], instruction_ampping)
        tmp_instructions = [*instructions[:idx], new_instruction, *instructions[idx + 1:]]
        pc, accumulator = run_without_loops(tmp_instructions, 0, 0, [False for _ in instructions])
        if pc == len(instructions):
            print(accumulator)
            break
    print(f'Tiempo (ns) solucion iterativa: {time.perf_counter_ns() - start}')

    start = time.perf_counter_ns()
    run_without_loops_v2(instructions, 0, 0, [False for _ in instructions], [False], instruction_ampping)
    print(f'Tiempo (ns) solucion recursiva: {time.perf_counter_ns() - start}')

