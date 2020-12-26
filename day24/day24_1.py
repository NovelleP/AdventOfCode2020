import re


# position: (x, y)
# X axis for North and South
# Y axis for West enad East
# w: x - 2
# e: x + 2
# nw: x - 1, y + 1
# ne: x + 1, y + 1
# sw: x - 1, y - 1
# se: x + 1, y - 1


def calc_position(route, x=0, y=0):
    for direction in route:
        if direction == 'w': x -= 2
        if direction == 'e': x += 2
        if direction == 'nw': x, y = x - 1, y + 1
        if direction == 'ne': x, y = x + 1, y + 1
        if direction == 'sw': x, y = x - 1, y - 1
        if direction == 'se': x, y = x + 1, y - 1
    return x, y


if __name__ == '__main__':
    parser = re.compile('nw|ne|sw|se|w|e')
    with open('input', 'r') as f:
        routes = [parser.findall(route) for route in f.readlines()]

    position_to_visits = {}
    for route in routes:
        position = calc_position(route)
        position_to_visits[position] = position_to_visits.get(position, 0) + 1
    print(sum(map(lambda val: val % 2 != 0, position_to_visits.values())))
