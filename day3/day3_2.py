def count_trees(input_map, tree_symbol, start_row, row_step, col_step):
    trees_count = 0
    col_idx = 0
    for row_idx in range(start_row, len(input_map), row_step):
        if input_map[row_idx][col_idx] == tree_symbol:
            trees_count += 1
        col_idx = (col_idx + col_step) % len(input_map[row_idx])
    return trees_count


if __name__ == '__main__':
    with open('input', 'r') as f:
        input_map = [list(line.strip()) for line in f.readlines()]
    tree_symbol = '#'
    start_row = 0
    steps = ((1, 1), (1, 3), (1, 5), (1, 7), (2, 1))
    result = 1
    for row_step, col_step in steps:
        result *= count_trees(input_map, tree_symbol, start_row, row_step, col_step)
    print(result)
