import re


def make_range_checker(min_num, max_num):
    return lambda num: num in range(min_num, max_num + 1)


def parse_rules(raw_rules):
    return {rule[0]: [make_range_checker(*map(int, vals.split('-'))) for vals in rule[1:]] for rule in re.findall('(.+?): ([0-9]+-[0-9]+).+?([0-9]+-[0-9]+)', raw_rules)}


def parse_tickets(raw_tickets):
    return [[int(num) for num in raw_ticket.split(',')] for raw_ticket in raw_tickets.strip().split('\n')[1:]]


def is_valid(ticket, rules):
    for val in ticket:
        l = [rule(val) for rule in rules]
        if not any(rule(val) for rule in rules):
            return False
    return True


def filter_tickets(nearby_tickets, rules):
    return [ticket for ticket in nearby_tickets if is_valid(ticket, rules)]


def solve(idx, rule_names, graph, rulename_to_col):
    if idx >= len(rule_names):
        return rulename_to_col
    for col in graph[rule_names[idx]]:
        if col not in rulename_to_col.values():
            rulename_to_col[rule_names[idx]] = col
            return solve(idx + 1, rule_names, graph, rulename_to_col)


def make_graph(rules, tickets):
    graph = {}
    for name, checkers in rules.items():
        for idx, col in enumerate(zip(*tickets)):
            if all(any(checker(val) for checker in checkers) for val in col):
                if name in graph:
                    graph[name].add(idx)
                else:
                    graph[name] = {idx}
    return graph


if __name__ == '__main__':
    with open('input', 'r') as f:
        raw_rules, raw_ticket, raw_nearby_tickets = re.search('(.+)(your ticket:.+)(nearby tickets:.+)', f.read(), re.DOTALL).groups()

    rules = parse_rules(raw_rules)
    ticket = parse_tickets(raw_ticket)
    nearby_tickets = parse_tickets(raw_nearby_tickets)
    valid_tickets = filter_tickets(nearby_tickets, [subrule for rule in rules.values() for subrule in rule])
    graph = make_graph(rules, [*ticket, *valid_tickets])

    rulename_to_col = solve(0, sorted(graph, key=lambda k: len(graph[k])), graph, {})
    res = 1
    for name, col in rulename_to_col.items():
        if name.startswith('departure'):
            res *= ticket[0][col]
    print(res)
