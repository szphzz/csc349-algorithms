import sys
from graph import *


def read_data():
    graph = []
    v_count = 0

    file = open(sys.argv[1], "r")
    content = file.readlines()
    for i in range(len(content)):
        line = content[i].split()
        graph.append([int(line[0]), int(line[1]), int(line[2])])
        v_count = max(v_count, int(line[0]), int(line[1]), int(line[2]))

    return graph, v_count


def kruskal(graph, v_count):
    res = []
    i = 0
    e = 0
    graph = sorted(graph, key=lambda item: item[2])
    parent = []
    rank = []

    for node in range(v_count + 1):
        parent.append(node)
        rank.append(0)

    while e < v_count - 1 and i < len(graph):
        u, v, w = graph[i]
        i += 1

        x = find(parent, u)
        y = find(parent, v)
        
        if x != y:
            e += 1
            res.append([u, v, w])
            union(parent, rank, x, y)

    return res


def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])


def union(parent, rank, x, y): 
    xroot = find(parent, x) 
    yroot = find(parent, y) 
  
    if rank[xroot] < rank[yroot]: 
        parent[xroot] = yroot 
    elif rank[xroot] > rank[yroot]: 
        parent[yroot] = xroot 
    else:
        parent[yroot] = xroot 
        rank[xroot] += 1


def double(mst): # need this for correct order
    res = []
    for i in range(len(mst)):
        res.append(mst[i])
        res.append([mst[i][1],
                    mst[i][0],
                    mst[i][2]])
    res.sort()
    return res


def explore(doubled_graph, vertex, visited, dfs_res):
    visited[vertex] = True
    dfs_res.append(vertex)
    
    adj_list = doubled_graph[vertex]
    for k in adj_list.keys():
        if visited[k] == False:
            explore(doubled_graph, k, visited, dfs_res)


def dfs(doubled_graph, v_count):
    visited = [False] * (v_count + 1)
    dfs_res = []

    for vertex in range(1, v_count):
        if visited[vertex] == False:
            explore(doubled_graph, vertex, visited, dfs_res)
    return dfs_res


def get_graph(graph): # undirected edges
    graph_res = Graph()
    for i in range(len(graph)):
        graph_res.add_edge(graph[i][0],
                           graph[i][1],
                           graph[i][2])
    return graph_res


def tot_weight(graph, res):
    weight = 0
    
    graph1 = [] # deepcopy takes too long
    [graph1.append(x[:-1]) for x in graph[0]]
    
    res_graph = []
    for i in range(len(res) - 1):
        if res[i] < res[i + 1]:
            res_graph.append([res[i], res[i + 1]])
        else:
            res_graph.append([res[i + 1], res[i]])

    for e in res_graph:
        i = graph1.index(e)
        weight += graph[0][graph1.index(e)][2]
        
    return weight


graph = read_data()
mst = kruskal(graph[0], graph[1])
doubled_mst = double(mst)
doubled_graph = get_graph(doubled_mst)
dfs_res = dfs(doubled_graph, max(doubled_graph.keys()))

res = []
[res.append(x) for x in dfs_res if x not in res]
res.append(res[0])

weight = tot_weight(graph, res)

print("Hamiltonian cycle of weight {}:".format(weight))
output = []
for i in res:
    output.append(str(i))
print(", ".join(output))
