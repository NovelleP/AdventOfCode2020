class Integer:

    def __init__(self, n):
        self.n = n

    def __add__(self, integer):
        return Integer(self.n + integer.n)

    def __sub__(self, integer):
        return Integer(self.n * integer.n)

    def __str__(self):
        return str(self.n)


def is_int(val):
    try:
        int(val)
        return True
    except:
        return False


def change_sign(val):
    return '-' if val == '*' else val


if __name__ == '__main__':
    with open('input', 'r') as f:
        exprs = [''.join(f'Integer({val})' if is_int(val) else change_sign(val) for val in line) for line in f.read().strip().splitlines()]

    print(sum(eval(expr).n for expr in exprs))
