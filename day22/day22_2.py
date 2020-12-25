import re
from collections import deque


def choose_winner(player1, player2, p1, p2):
    if p1 > p2:
        player1.extend((p1, p2))
    elif p2 > p1:
        player2.extend((p2, p1))
    else:
        print(p1, p2)


def solve(player1, player2):
    prev_p1, prev_p2 = set(), set()
    while player1 and player2:
        prev_p1.add(tuple(player1))
        prev_p2.add(tuple(player2))
        p1, p2 = player1.popleft(), player2.popleft()
        if p1 > len(player1) or p2 > len(player2):
            choose_winner(player1, player2, p1, p2)
        else:
            winner, _, _ = solve(deque(list(player1)[:p1]), deque(list(player2)[:p2]))
            if winner == 1:
                player1.extend((p1, p2))
            elif winner == 2:
                player2.extend((p2, p1))
            else:
                print(winner)
        if tuple(player1) in prev_p1 and tuple(player2) in prev_p2:
            return 1, player1, player2
    return (1 if player1 else 2), player1, player2


if __name__ == '__main__':
    with open('input', 'r') as f:
        player1, player2 = f.read().strip().split('\n\n')

    player1 = deque(map(int, re.findall('(?<=\n)[0-9]+(?=\n|$)', player1)))
    player2 = deque(map(int, re.findall('(?<=\n)[0-9]+(?=\n|$)', player2)))


    winner, player1, player2 = solve(player1, player2)
    print(sum(c * (idx + 1) for idx, c in enumerate(list((player1 if winner == 1 else player2))[::-1])))
