def get_adjacent_values(row, col, grid):
    adjacent_values = []
    for curr_row in range(max(0, row-1), min(row+2, len(grid))):
        for curr_col in range(max(0, col-1), min(col+2, len(grid[curr_row]))):
            if (row, col) != (curr_row, curr_col):
                adjacent_values.append(grid[curr_row][curr_col])
    return adjacent_values


def transform_grid(grid):
    tmp_grid = [[v for v in row] for row in grid]
    changes = 0
    for idx_row, row in enumerate(grid):
        for idx_col, val in enumerate(row):
            if val == 'L' and all(v in ('L', '.') for v in get_adjacent_values(idx_row, idx_col, grid)):
                tmp_grid[idx_row][idx_col] = '#'
                changes += 1
            elif val == '#' and sum(v == '#' for v in get_adjacent_values(idx_row, idx_col, grid)) >= 4:
                tmp_grid[idx_row][idx_col] = 'L'
                changes += 1

    return changes, tmp_grid


if __name__ == '__main__':
    with open('input', 'r') as f:
        grid = [list(line.strip()) for line in f.readlines()]

    while t := transform_grid(grid):
        changes, grid = t
        if not changes:
            break
    print(len([v for row in grid for v in row if v == '#']))

