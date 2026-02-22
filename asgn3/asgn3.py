# Kosaraju's algorithm to find strongly connected components

import sys
from collections import defaultdict

class DirectedGraph:

    def __init__(self, vertex):
        self.V = vertex # number of vertices
        self.graph = defaultdict(list)
        self.list = []

    def add_edge(self, s, d):
        self.graph[s].append(d)

    def dfs(self, d, visited, scc):
        visited[d] = True
        scc.append(d)
        for i in self.graph[d]:
            if not visited[i]:
                self.dfs(i, visited, scc)

    def fill_order(self, d, visited, stack):
        visited[d] = True
        for i in self.graph[d]:
            if not visited[i]:
                self.fill_order(i, visited, stack)
        stack = stack.append(d)

    # reverse original graph
    def reverse(self):
        g = DirectedGraph(self.V)

        for i in self.graph:
            for j in self.graph[i]:
                g.add_edge(j, i)
        return g

    def print_scc(self):
        # perform dfs
        stack = []
        visited = [False] * (self.V + 1)

        for i in range(1, self.V + 1):
            if not visited[i]:
                self.fill_order(i, visited, stack)

        gr = self.reverse()

        visited = [False] * (self.V + 1)

        while stack:
            i = stack.pop()
            scc = []
            if not visited[i]:
                gr.dfs(i, visited, scc)
                g.list.append(scc)

        print(len(g.list), "Strongly Connected Component(s):")
        for l in g.list:
            print(*l, sep=", ")
                

file = open(sys.argv[1], "r")
contents = file.readlines()
contents = [line.replace("\n", "") for line in contents]
int_list = []
for i in range(0, len(contents)):
    int_list.append(int(contents[i].split(" ")[0]))
    int_list.append(int(contents[i].split(" ")[1]))


g = DirectedGraph(max(int_list))
i = 0
curr = 0
while i < (len(int_list) / 2):
    g.add_edge(int_list[curr], int_list[curr + 1])
    curr += 2
    i += 1

g.print_scc()
