# Majd Hamdan, Danzan Achit-Erdene
# Python program to find Minimum Spanning
# Tree of a given connected, undirected
# and weighted graph using Kruskal algorithm

class Graph:
### Creating a graph
    # n is the number of vertices and m is the number of edges
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.edges = []
        
    
    # add an edge between u and v with weight w
    def add_edge(self, v, u, w):
        self.edges.append([u, v, w])
        
### checking for a cycle
        
# we use unin-find algorithm optemized by rank

    # find the set containing element i
    def find(self, i, parent):
        if parent[i] == i:
            return i
        else:
            return self.find(parent[i], parent)
        
    def union(self, parent, rank, set1, set2):
        if rank[set1] < rank[set2]:
            parent[set1] = set2
        elif rank[set1] > rank[set2]:
            parent[set2] = set1
        else:
            parent[set2] = set1
            rank[set1] += 1

### finding MST
    def kruskal(self):
        MST = [] # store edges of MST
        cost = 0
        
        # Sort edges in increasing order by cost so that
        sorted_edges = sorted(self.edges, key=lambda indix:indix[2]) # sort the edges list by w (w index is 2)
        
        # Create the union-find data structure
        parent = []
        rank = []
        for v in range(self.n):
            parent.append(v)
            rank.append(0)
        # loop through the edges starting from smallest edge
        for e in sorted_edges:
            # If this edge doesn't form a cycle, include it the MST and update union-find structure
            set1 = self.find(e[0], parent)
            set2 = self.find(e[1], parent)
            if  set1 != set2:
                self.union(parent, rank, set1, set2)
                MST.append(e)
                cost += e[2]
        return cost, MST

