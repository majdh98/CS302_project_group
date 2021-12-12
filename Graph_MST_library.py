# Majd Hamdan, Danzan Achit-Erdene
# Python program to find Minimum Spanning
# Tree of a given connected, undirected
# and weighted graph using Kruskal algorithm

import math

class Graph_kruskal:
### Creating a graph
    # n is the number of vertices and m is the number of edges
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.edges = []
        
    
    # e = [v, u, w], an edge between u and v with weight w
    def add_edge(self, e):
        self.edges.append(e)
        
### checking for a cycle
        
# we use unin-find algorithm optemized by rank

    # find the set containing element i
    def find(self, i, parent):
        while parent[i] != i:
            i = parent[i]
        return i
        
    def union(self, parent, rank, set1, set2):
        if rank[set1] == rank[set2]:
            parent[set2] = set1
            rank[set1] += 1
        # attach the set with less rank to the set
        # with larger rank to compress the path
        elif rank[set1] > rank[set2]:
            parent[set2] = set1
        else:
            parent[set1] = set2
            

### finding MST
    def kruskal(self):
        MST = [] # store edges of MST
        cost = 0
        
        # Sort edges in increasing order by cost so that
        sorted_edges = sorted(self.edges, key=lambda indix:indix[2]) # sort the edges list by w (w index is 2)
        
        # Create the union-find data structure
        parent = [v for v in range(self.n)]
        rank = [0 for v in range(self.n)]

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
    
        
    
class Graph_prim:
### Creating a graph
    # n is the number of vertices and m is the number of edges
    def __init__(self, n, m):
        self.n = n
        self.m = m
        # we need to update the possible vertices that can be
        # reached from the small MST everytime we add a vertex
        # to it to find the minimum edge to all the other
        # vertices not in the partial MST yet. An adjacency list
        # representation allow to reduce the cost of updating the
        # possible vertices from O(m) to O(n)
        self.edges = [[math.inf for v in range(n)] for v in range(n)]
    
    # e = [v, u, w] where v and u are vertices and w is the weight of the edge
    # connecting them
    def add_edge(self, e):
        self.edges[e[0]][e[1]] = e[2]
        # because graph is undirected, edges must
        # be symmetric about its diameter
        self.edges[e[1]][e[0]] = e[2]
    
    
### Finding MST
        
    def find_min(self, possible_vertices):
        min_edge = math.inf
        min_u = 0
        
        # we don't have to worry about vertices that are
        # already in the MST because the weight of every
        # edge connecting to them is set to inf when they are
        # added to the partial MST
        for u in range(self.n):
            if possible_vertices[u] != -math.inf and possible_vertices[u] < min_edge:
                min_edge = possible_vertices[u]
                min_u = u
        return min_u
    
    # include the cost of the edges leading to the vertices that
    # can be reached from the partial MST
    def update_possible_vertices(self, possible_vertices, u):
        for v in range(self.n):
            if(possible_vertices[v] > self.edges[u][v] and possible_vertices[v] != -math.inf):
                possible_vertices[v] = self.edges[u][v]
        
    def prim(self):
        
        MST = []
        cost = 0
        # we always start from vertex 0
        possible_vertices = self.edges[0]
        possible_vertices[0] = -math.inf
        
        # there are n-1 edges in an MST
        for r in range(self.n-1):
            
            u = self.find_min(possible_vertices) # min-cost edge such that u is in V’ and v is in V-V'
            if u == 0:
                continue
            cost += possible_vertices[u]
            possible_vertices[u] = -math.inf # Mark u as visited
            self.update_possible_vertices(possible_vertices, u) # For all (v,w) update data structure for finding edges
            
        return cost, MST
            
            
            
            
        
        
    


# g = Graph_kruskal(5, 7)
# g.add_edge([0, 1, 10])
# g.add_edge([0, 2, 6])
# g.add_edge([0, 3, 5])
# g.add_edge([1, 3, 15])
# g.add_edge([3, 4, 1])
#  
# # Function call
# print(g.kruskal())


# g = Graph_prim(5, 7)
# g.add_edge([0, 1, 10])
# g.add_edge([0, 2, 6])
# g.add_edge([0, 3, 5])
# g.add_edge([1, 3, 15])
# g.add_edge([3, 4, 1])
#  
# # Function call
# print(g.prim())
