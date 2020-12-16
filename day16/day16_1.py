import re


def make_range_checker(min_num, max_num):
    return lambda num: num in range(min_num, max_num + 1)


def parse_rules(raw_rules):
    return [make_range_checker(*map(int, vals.split('-'))) for vals in re.findall('[0-9]+-[0-9]+', raw_rules)]


def parse_tickets(raw_tickets):
    return [int(num) for num in re.findall('[0-9]+', raw_tickets)]


if __name__ == '__main__':
    with open('input', 'r') as f:
        raw_rules, raw_ticket, raw_nearby_tickets = re.search('(.+)(your ticket:.+)(nearby tickets:.+)', f.read(), re.DOTALL).groups()

    rules = parse_rules(raw_rules)
    nearby_tickets = parse_tickets(raw_nearby_tickets)
    res = sum(filter(lambda val: not any(rule(val) for rule in rules), nearby_tickets))
    print(res)
