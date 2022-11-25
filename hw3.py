# Directed acyclic graph (DAG) class

class DAG:
    def __init__(self, filename):
        self.filename = filename
        self.graph = {}
        self.read_graph()
        self.topological_order = []
        self.topological_sort()
        self.longest_path = []
        self.find_longest_path()

    def read_graph(self):
        with open(self.filename) as f:
            for line in f:
                line = line.strip()
                if line:
                    node, children = line.split(':')
                    self.graph[node] = children.split()

    def topological_sort(self):
        visited = set()
        for node in self.graph:
            if node not in visited:
                self.topological_sort_helper(node, visited)

    def topological_sort_helper(self, node, visited):
        visited.add(node)
        for child in self.graph[node]:
            if child not in visited:
                self.topological_sort_helper(child, visited)
        self.topological_order.append(node)
        
    def find_longest_path(self):
        self.longest_path = []
        self.longest_path_helper(self.topological_order[-1], [])
    
    def longest_path_helper(self, node, path):
        path.append(node)
        if len(path) > len(self.longest_path):
            self.longest_path = path[:]
        for child in self.graph[node]:
            self.longest_path_helper(child, path)
        path.pop()
    
    def __str__(self):
        return 'Graph: ' + str(self.graph)
    
DAG('graph.txt')
