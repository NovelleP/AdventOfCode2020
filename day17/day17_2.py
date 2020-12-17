def get_activate_neighs(x, y, z, w, coords):
    pos = (x, y, z, w)
    activate_neighs = 0
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            for k in range(z - 1, z + 2):
                for l in range(w - 1, w + 2):
                    curr_pos = (i, j, k, l)
                    if curr_pos in coords and pos != curr_pos:
                        activate_neighs += 1
    return activate_neighs


def exec_round(coords):
    t = list(zip(*coords))
    tmp = {coord for coord in coords}
    for i in range(min(t[0]) - 1, max(t[0]) + 2):
        for j in range(min(t[1]) - 1, max(t[1]) + 2):
            for k in range(min(t[2]) - 1, max(t[2]) + 2):
                for l in range(min(t[3]) - 1, max(t[3]) + 2):
                    activate_neighs = get_activate_neighs(i, j, k, l, coords)
                    if (i, j, k, l) in coords and activate_neighs not in range(2, 4):
                        tmp.remove((i, j, k, l))
                    elif (i, j, k, l) not in coords and activate_neighs == 3:
                        tmp.add((i, j, k, l))
    return tmp


if __name__ == '__main__':
    with open('input', 'r') as f:
        coords = {(i, j, 0, 0) for i, row in enumerate(f.readlines()) for j, val in enumerate(row.strip()) if val == '#'}

    for _ in range(6):
        coords = exec_round(coords)
    print(len(coords))
