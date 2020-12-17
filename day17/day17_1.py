def get_activate_neighs(x, y, z, m):
    pos = (x, y, z)
    activate_neighs = 0
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            for k in range(z - 1, z + 2):
                curr_pos = (i, j, k)
                if m.get(curr_pos, '.') == '#' and pos != curr_pos:
                    activate_neighs += 1
    return activate_neighs


def exec_round(m):
    t = list(zip(*m))
    tmp = {k: v for k, v in m.items()}
    for i in range(min(t[0]) - 1, max(t[0]) + 2):
        for j in range(min(t[1]) - 1, max(t[1]) + 2):
            for k in range(min(t[2]) - 1, max(t[2]) + 2):
                activate_neighs = get_activate_neighs(i, j, k, m)
                if m.get((i, j, k), '.') == '#' and activate_neighs not in range(2, 4):
                    del tmp[(i, j, k)]
                elif m.get((i, j, k), '.') == '.' and activate_neighs == 3:
                    tmp[(i, j, k)] = '#'
    return tmp


if __name__ == '__main__':
    with open('input', 'r') as f:
        m = {(i, j, 0): val for i, row in enumerate(f.readlines()) for j, val in enumerate(row.strip()) if val == '#'}

    for _ in range(6):
        m = exec_round(m)
    print(len(m))