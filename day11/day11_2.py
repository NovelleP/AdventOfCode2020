def get_first_visible_values(row, col, values, grid):
    visible_values = []

    # rows
    for curr_row in range(row-1, -1, -1):
        if (val := grid[curr_row][col]) in values:
            visible_values.append(val)
            break
    for curr_row in range(row+1, len(grid)):
        if (val := grid[curr_row][col]) in values:
            visible_values.append(val)
            break

    # cols
    for curr_col in range(col-1, -1, -1):
        if (val := grid[row][curr_col]) in values:
            visible_values.append(val)
            break
    for curr_col in range(col+1, len(grid[row])):
        if (val := grid[row][curr_col]) in values:
            visible_values.append(val)
            break

    # diagonals
    curr_row, curr_col = row-1, col-1
    while (curr_row >= 0) and (curr_col >= 0):
        if (val := grid[curr_row][curr_col]) in values:
            visible_values.append(val)
            break
        curr_row, curr_col = curr_row - 1, curr_col - 1
    curr_row, curr_col = row + 1, col + 1
    while (curr_row < len(grid)) and (curr_col < len(grid[curr_row])):
        if (val := grid[curr_row][curr_col]) in values:
            visible_values.append(val)
            break
        curr_row, curr_col = curr_row + 1, curr_col + 1
    curr_row, curr_col = row - 1, col + 1
    while (curr_row >= 0) and (curr_col < len(grid[curr_row])):
        if (val := grid[curr_row][curr_col]) in values:
            visible_values.append(val)
            break
        curr_row, curr_col = curr_row - 1, curr_col + 1
    curr_row, curr_col = row + 1, col - 1
    while (curr_row < len(grid)) and (curr_col >= 0):
        if (val := grid[curr_row][curr_col]) in values:
            visible_values.append(val)
            break
        curr_row, curr_col = curr_row + 1, curr_col - 1

    return visible_values


def transform_grid(grid):
    values = {'L', '#'}
    tmp_grid = [[v for v in row] for row in grid]
    changes = 0
    for idx_row, row in enumerate(grid):
        for idx_col, val in enumerate(row):
            if val == 'L' and all(v == 'L' for v in get_first_visible_values(idx_row, idx_col, values, grid)):
                tmp_grid[idx_row][idx_col] = '#'
                changes += 1
            elif val == '#' and sum(v == '#' for v in get_first_visible_values(idx_row, idx_col, values, grid)) >= 5:
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

