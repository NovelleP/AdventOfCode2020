import re


def parse_line(line, parser):
    match = parser.search(line)
    return int(match.group(1)), int(match.group(2)), match.group(3), match.group(4)


def check_range_rule(password, letter, lowerlimit, upperlimit):
    return lowerlimit <= password.count(letter) <= upperlimit


if __name__ == '__main__':

    parser = re.compile('([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)')
    valid_passwords = 0
    with open('input', 'r') as f:
        for line in f.readlines():
            lowerlimit, upperlimit, letter, password = parse_line(line, parser)
            if check_range_rule(password, letter, lowerlimit, upperlimit):
                valid_passwords += 1
    print(valid_passwords)
