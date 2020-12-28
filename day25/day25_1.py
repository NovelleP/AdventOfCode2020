if __name__ == '__main__':
    with open('input', 'r') as f:
        card_publickey, door_publickey = map(int, f.read().strip().split('\n'))

    subject_number = 7
    value = 1
    loop_size = 1
    while (value := (value * subject_number) % 20201227) != card_publickey:
        loop_size += 1
    print(value, loop_size)

    privatekey = 1
    for _ in range(loop_size):
        privatekey = (privatekey * door_publickey) % 20201227
    print(privatekey)

    value = 1
    loop_size = 1
    while (value := (value * subject_number) % 20201227) != door_publickey:
        loop_size += 1
    print(value, loop_size)

    privatekey = 1
    for _ in range(loop_size):
        privatekey = (privatekey * card_publickey) % 20201227
    print(privatekey)