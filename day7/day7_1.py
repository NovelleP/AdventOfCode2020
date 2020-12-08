import re


def count_node_parents(node_name, graph):
    stack = [node for node in graph.get(node_name, [])]
    visited_nodes = {node_name, *stack}
    parents_count = 0
    while stack:
        curr_node = stack.pop()
        parents_count += 1
        for node in graph.get(curr_node, []):
            if node not in visited_nodes:
                stack.append(node)
                visited_nodes.add(node)
    return parents_count


def count_node_parents_v2(node_name, visited_nodes, graph):
    acc = 0
    for parent_node in graph.get(node_name, []):
        if parent_node not in visited_nodes:
            visited_nodes.add(parent_node)
            acc += 1 + count_node_parents_v2(parent_node, visited_nodes, graph)
    return acc


if __name__ == '__main__':
    graph = {}
    with open('input', 'r') as f:
        for line in f.readlines():
            container_info, content_info = line.split('contain')
            if content_info.strip() == 'no other bags.':
                continue
            container_color = re.search('.+?(?= bags)', container_info).group()
            for inner_bag_info in content_info.split(','):
                inner_bag_color = re.search('[a-z][a-z ]*(?= bags?)', inner_bag_info).group()
                if inner_bag_color not in graph:
                    graph[inner_bag_color] = []
                graph[inner_bag_color].append(container_color)
    print(count_node_parents('shiny gold', graph))
    print(count_node_parents_v2('shiny gold', {'shiny gold'}, graph))