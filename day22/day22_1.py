import re


if __name__ == '__main__':
    with open('input', 'r') as f:
        player1, player2 = f.read().strip().split('\n\n')

    player1 = list(map(int, re.findall('(?<=\n)[0-9]+(?=\n|$)', player1)))
    player2 = list(map(int, re.findall('(?<=\n)[0-9]+(?=\n|$)', player2)))

    while player1 and player2:
        p1, p2 = player1.pop(0), player2.pop(0)
        if p1 > p2:
            player1.extend((p1, p2))
        elif p2 > p1:
            player2.extend((p2, p1))
        else:
            print(p1, p2)
    print(sum(c * (idx + 1) for idx, c in enumerate((player1 or player2)[::-1])))
