import re


def count_node_childrens_with_weight(node_name, prev_weight, visited_nodes, graph, result):
    pass

if __name__ == '__main__':
    graph = {}
    with open('test_input', 'r') as f:
        for line in f.readlines():
            container_info, content_info = line.split('contain')
            if content_info.strip() == 'no other bags.':
                continue
            container_color = re.search('.+?(?= bags)', container_info).group()
            if container_color not in graph:
                graph[container_color] = []
            for inner_bag_info in content_info.split(','):
                match = re.search('([0-9]+)(?: )([a-z][a-z ]*(?= bags?))', inner_bag_info)
                amount, color = int(match.group(1)), match.group(2)
                graph[container_color].append((color, amount))
    import pprint
    pprint.pprint(graph)
    result = [0]
    print(count_node_childrens_with_weight('shiny gold', 1, set('shiny gold'), graph, result))
    print(result)