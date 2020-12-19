import re


def is_int(val):
    try:
        int(val)
        return True
    except:
        return False


def parse_child(child):
    splitted_child = child.strip().split(' ')
    return tuple(int(c) if is_int(c) else c[1:-1] for c in splitted_child)


def parse_grammar(raw_grammar):
    grammar = {}
    for line in raw_grammar.strip().splitlines():
        token, childs = line.split(':')
        grammar[int(token)] = [parse_child(child) for child in childs.split('|')]
    return grammar


def make_regex(grammar):
    r = ''.join(f'{{s{val}}}' for suc in grammar[0] for val in suc)
    while (vals := re.findall('s\d+', r)):
        d = {val: '' for val in vals}
        for val in vals:
            tmp = '('
            for idx, s in enumerate(grammar.get(int(val[1:]), [])):
                rep = ''
                tmp += '('
                for v in s:
                    if is_int(v):
                        tmp += f'({{s{v}}})'
                    else:
                        tmp += f'({v})'
                tmp += ')'
                if idx < len(grammar.get(int(val[1:]), [])) - 1:
                    tmp += '|'
            d[val] = tmp + ')'
        r = r.format(**d)
    return r


if __name__ == '__main__':
    with open('input_1', 'r') as f:
        raw_grammar, words = f.read().strip().split('\n\n')
        grammar = parse_grammar(raw_grammar)

    grammar_regex = make_regex(grammar)
    print(grammar_regex)

    res = 0
    for word in words.strip().splitlines():
        if re.fullmatch(grammar_regex, word):
            res += 1
    print(res)