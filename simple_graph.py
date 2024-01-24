import networkx as nx
import matplotlib.pyplot as plt


def generate_graph():
    people_names = ['Alice', 'Bob', 'Charlie', 'David', 'Eva']

    graph = nx.cycle_graph(people_names)

    weights = {'Alice': 1, 'Bob': 2, 'Charlie': 3, 'David': 4, 'Eva': 5}
    for edge in graph.edges():
        graph[edge[0]][edge[1]]['weight'] = weights[edge[0]]

    new_people = ['Frank', 'Grace', 'Hank']
    for person in new_people:
        graph.add_node(person)
        graph.add_edge(person, people_names[0], weight=9)

    new_people2 = ['Ian', 'Karen']
    for person in new_people2:
        graph.add_node(person)
        graph.add_edge(person, new_people[0], weight=8)

    return graph;


if __name__ == "__main__":
    graph = generate_graph()

    # pos = nx.spring_layout(graph)
    # nx.draw_networkx_nodes(graph, pos, node_size=700, node_color='skyblue')
    # nx.draw_networkx_edges(graph, pos)
    # nx.draw_networkx_labels(graph, pos)
    #
    # plt.title("Циклічний граф соціальної мережі")
    # plt.show()

    # Візуалізація графа
    pos = nx.spring_layout(graph, seed=42)
    nx.draw(graph, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=15, width=2)
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)

    plt.show()
