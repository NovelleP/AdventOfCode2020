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
    row_step = 1
    col_step = 3
    print(count_trees(input_map, tree_symbol, start_row, row_step, col_step))
