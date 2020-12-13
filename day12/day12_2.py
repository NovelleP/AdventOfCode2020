import re
import math


def rotate(x, y, degrees):
    return round(x * math.cos(math.radians(degrees)) - y * math.sin(math.radians(degrees)), 10), \
           round(x * math.sin(math.radians(degrees)) + y * math.cos(math.radians(degrees)), 10)


if __name__ == '__main__':

    actions = {
        'N': lambda px, py, dx, dy, v: ((px, py), (dx, dy + v)),
        'S': lambda px, py, dx, dy, v: ((px, py), (dx, dy - v)),
        'E': lambda px, py, dx, dy, v: ((px, py), (dx + v, dy)),
        'W': lambda px, py, dx, dy, v: ((px, py), (dx - v, dy)),
        'R': lambda px, py, dx, dy, v: ((px, py), rotate(dx, dy, v)),
        'L': lambda px, py, dx, dy, v: ((px, py), rotate(dx, dy, v)),
        'F': lambda px, py, dx, dy, v: ((px + dx * v, py + dy * v), (dx, dy))
    }

    position = (0, 0)
    direction = (10, 1)
    parser = re.compile('([NSEWRLF])([0-9]+)')
    with open('input', 'r') as f:
        for line in f.readlines():
            action, value = (v for v in parser.search(line).groups())
            position, direction = actions[action](*position, *direction, -int(value) if action == 'R' else int(value))
    print(sum(abs(val) for val in position))
