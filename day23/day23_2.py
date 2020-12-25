class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

    def __str__(self):
        return str(self.val)


class CircularList:
    def __init__(self, node=None):
        self.first_node = node
        if node:
            self.first_node.next = self.first_node
        self.last_node = None

    def add(self, node):
        if not self.first_node:
            self.first_node = node
            self.first_node.next = self.first_node
        elif not self.last_node:
            self.first_node.next = node
            self.last_node = node
            self.last_node.next = self.first_node
        else:
            self.last_node.next = node
            self.last_node = node
            self.last_node.next = self.first_node

    def add_next_to_node(self, base_node, next_node):
        next_node.next = base_node.next
        base_node.next = next_node

    def pop_next(self, node):
        next_node = node.next
        node.next = next_node.next
        next_node.next = None
        return next_node

    def __str__(self):
        s = ''
        if self.first_node:
            s = str(self.first_node.val)
            curr_node = self.first_node.next
            while curr_node != self.first_node:
                s += str(curr_node.val)
                curr_node = curr_node.next
        return s


def calc_curr_min(removed_cups, abs_min):
    curr_min = abs_min
    while curr_min in removed_cups:
        curr_min += 1
    return curr_min


def calc_curr_max(removed_cups, abs_max):
    curr_max = abs_max
    while curr_max in removed_cups:
        curr_max -= 1
    return curr_max


def calc_target_cup(curr_cup, curr_min, curr_max, removed_cups):
    target_cup = curr_cup - 1
    while target_cup in removed_cups and target_cup >= curr_min:
        target_cup -= 1
    if target_cup < curr_min:
        target_cup = curr_max
    return target_cup


def insert_removed_cups(removed_nodes, base_node, c_list):
    curr_node = base_node
    for removed_node in removed_nodes:
        c_list.add_next_to_node(curr_node, removed_node)
        curr_node = removed_node


if __name__ == '__main__':
    cup_to_node = {}
    c_list = CircularList()
    with open('input', 'r') as f:
        for cup in f.readline():
            node = Node(int(cup))
            c_list.add(node)
            cup_to_node[int(cup)] = node
    for cup in range(len(cup_to_node) + 1, 1000001):
        node = Node(int(cup))
        c_list.add(node)
        cup_to_node[int(cup)] = node

    curr_node = c_list.first_node
    abs_min, abs_max = 1, len(cup_to_node)
    for i in range(10000000):
        removed_nodes = [c_list.pop_next(curr_node) for _ in range(3)]
        removed_cups = {removed_node.val for removed_node in removed_nodes}
        curr_min, curr_max = calc_curr_min(removed_cups, abs_min), calc_curr_max(removed_cups, abs_max)
        target_cup = calc_target_cup(curr_node.val, curr_min, curr_max, removed_cups)
        insert_removed_cups(removed_nodes, cup_to_node[target_cup], c_list)
        curr_node = curr_node.next
    node1, node2 = cup_to_node[1].next, cup_to_node[1].next.next
    print(node1, node2, node1.val * node2.val)
