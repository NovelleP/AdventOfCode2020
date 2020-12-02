import re


def parse_line(line, parser):
    match = parser.search(line)
    return int(match.group(1)), int(match.group(2)), match.group(3), match.group(4)


def check_positions_rule(password, letter, pos1, pos2):
    return (password[pos1-1] == letter) ^ (password[pos2-1] == letter)


if __name__ == '__main__':

    parser = re.compile('([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)')
    valid_passwords = 0
    with open('input', 'r') as f:
        for line in f.readlines():
            pos1, pos2, letter, password = parse_line(line, parser)
            if check_positions_rule(password, letter, pos1, pos2):
                valid_passwords += 1
    print(valid_passwords)
