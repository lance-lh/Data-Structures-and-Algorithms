# illustration can be found here:
# https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/

# time complexity: O(n^2)
# where, n equals nums of vertices

# Given a graph and a source vertex in the graph,
# find shortest paths from source to all vertices in the given graph.

# adjacency matrix representation of the graph

# Library for INT_MAX
import sys
# note: python2 -> sys.maxint
#       python3 -> sys.maxsize

# Graph class has the following method:
# 1. initialize vertices ranging from 0 - 9 and adjacency matrix
# 2. print final shortest paths
# 3. compute min distance
class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def printSolution(self, dist):
        print("Vertex  Distance from Source")
        for node in range(self.V):
            print(' ',node, '\t\t\t',dist[node])

    def minDistance(self, dist, sptSet):

        # min = sys.maxint
        min = sys.maxsize

        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v

        return min_index

    def dijkstra(self, src):
        # dist saves the shortest distance
        # sptSet saves True (for min distance) or False
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for cout in range(self.V):

            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # u is always equal to src in first iteration
            u = self.minDistance(dist, sptSet)

            # Put the minimum distance vertex in the
            # shotest path tree
            sptSet[u] = True

            # Update dist value of the adjacent vertices of the picked vertex
            for v in range(self.V):
                # self.graph[u][v] > 0, this line cancel the drawback of dijkstra
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]

        self.printSolution(dist)


# test
# vertex is 0 to 9
g = Graph(9)
# distance values
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ]

g.dijkstra(0)