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


def get_adj_positions(position):
    return [tuple(map(lambda x, y: x + y, position, distance)) for distance in [(-2, 0), (2, 0),
                                                                                 (-1, 1), (1, 1),
                                                                                 (-1, -1), (1, -1)]]


def count_adj_blacks(position, position_to_color):
    blacks = 0
    for adj_pos in get_adj_positions(position):
        # print(position_to_color.get(adj_pos))
        if position_to_color.get(adj_pos, 'white') == 'black':
            blacks += 1
    return blacks


def flip_tiles(position_to_color):
    tmp = {k: v for k, v in position_to_color.items()}
    for position, color in position_to_color.items():
        adj_blacks = count_adj_blacks(position, position_to_color)
        if color == 'white' and adj_blacks == 2:
            tmp[position] = 'black'
        elif color == 'black' and adj_blacks not in (1, 2):
            tmp[position] = 'white'
    return tmp


if __name__ == '__main__':
    parser = re.compile('nw|ne|sw|se|w|e')
    with open('input', 'r') as f:
        routes = [parser.findall(route) for route in f.readlines()]
    position_to_visits = {}
    for route in routes:
        position = calc_position(route)
        position_to_visits[position] = position_to_visits.get(position, 0) + 1
    position_to_color = {k: ('white' if (v % 2 == 0) else 'black') for k, v in position_to_visits.items()}
    for _ in range(100):
        position_to_color = {
            **position_to_color,
            **{adj_pos: 'white' for pos in position_to_color for adj_pos in get_adj_positions(pos)
               if adj_pos not in position_to_color}
        }
        position_to_color = flip_tiles(position_to_color)
    print(sum(map(lambda color: color == 'black', position_to_color.values())))
