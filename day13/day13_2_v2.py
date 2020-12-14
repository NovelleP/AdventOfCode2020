import itertools
from sympy import Matrix
from diophantine import solve


if __name__ == '__main__':
    with open('input', 'r') as f:
        time = int(f.readline())
        pos_bus_ids = [(idx, int(bus_id)) for idx, bus_id in enumerate(f.readline().split(',')) if bus_id != 'x']

    combs = itertools.combinations(pos_bus_ids, 2)
    matrix = []
    sols = []
    for comb1, comb2 in combs:
        row = [0 for _ in pos_bus_ids]
        row[pos_bus_ids.index(comb1)] = comb1[1]
        row[pos_bus_ids.index(comb2)] = -comb2[1]
        matrix.append(row)
        sols.append(comb1[0] - comb2[0])
    M = Matrix(matrix)
    s = Matrix(sols)
    r = solve(M, s)
    print(r[0][0] * pos_bus_ids[0][1])
