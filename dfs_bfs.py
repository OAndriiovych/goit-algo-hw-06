from simple_graph import generate_graph
import networkx as nx

graph = generate_graph()

dfs_nodes = list(nx.dfs_preorder_nodes(graph, source='Frank'))

print("DFS обхід графа починаючи з вершини", 'Frank', ":", dfs_nodes)




bfs_nodes = list(nx.bfs_edges(graph, source='Frank'))

print("BFS обхід графа починаючи з вершини", 'Frank', ":", bfs_nodes)


