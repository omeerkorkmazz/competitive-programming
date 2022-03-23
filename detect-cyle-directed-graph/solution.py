class Solution:
    has_cycle = False
    # Function to detect cycle in a directed graph.

    def visit_and_check_cycle(self, node, adj, visited, neighbour_visited):
        visited[node] = True
        neighbour_visited[node] = True

        for neighbour in adj[node]:
            if visited[neighbour] == False:
                if self.visit_and_check_cycle(neighbour, adj, visited, neighbour_visited) == True:
                    return True
            elif neighbour_visited[neighbour] == True:
                return True

        neighbour_visited[node] = False
        return False

    def isCyclic(self, V, adj):
        visited = [False] * (V + 1)
        neighbour_visited = [False] * (V + 1)

        for node in range(V):
            if visited[node] == False:
                if self.visit_and_check_cycle(node, adj, visited, neighbour_visited) == True:
                    return True
        return False
