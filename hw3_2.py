# Author : Suleyman Golbol

class DAG:
    is_dag = True
    
    def __init__(self) -> None:
        self.graph = {}        
        
    # Taking input from user properly
    def take_input(self, string, int_type=False):
        wrong_input = True
        while wrong_input == True:
            try:
                inp_value = input(string)
                if int_type == True and inp_value.isdigit() == False:
                    raise TypeError 
                wrong_input = False
            # value or type error
            except ValueError:
                print("Wrong input. Please try again.")
            except TypeError:
                print("Wrong input. Please try again.")
        return inp_value
        
    def take_graph(self):
        num_of_nodes = int(self.take_input("Enter the number of nodes you want on the graph: ", int_type=True))
            
        for i in range(num_of_nodes):
            node = self.take_input("Enter the node" + str(i+1) + ": ")
            if node not in self.graph:
                self.graph[node] = []
            num_of_children = int(self.take_input("Enter the number of children: ", int_type=True))
            if num_of_children == 0:
                pass
            for j in range(num_of_children):
                child = self.take_input("Enter the child" + str(j+1) + ": ")
                self.graph[node].append(child)
        
    def visualize(self):
        # Visualize the graph using dict values
        print("Graph: {")
        for i in self.graph:
            if self.graph[i] != []:
                print(i, " -> ", self.graph[i])
        print("}")
        
    def dfs_topological_sort(self):
        visited = set()
        stack = []
        for _i, iter in enumerate(self.graph):
            if iter not in visited:
                self.dfs_topological_sort_recursive(iter, visited, stack)
        print("Dfs Topological sort: ", stack)
    
    def dfs_topological_sort_recursive(self, node, visited, stack):
        visited.add(node)
        try:
            for child in self.graph[node]:
                if child not in visited:
                    self.dfs_topological_sort_recursive(child, visited, stack)
        except KeyError:
            pass
        stack.insert(0, node)
        
    # If there exists vertex with in-degree 0 and vertex with out-degree 0, then it is a DAG
    # because if there was a edge goes back to a node already visited, that shows the existence of a cycle.
    def non_dfs_topological_sort(self):
        # kahn's algorithm
        in_degree = self.in_degree_finder()
        queue_of_in_degrees = []
        for i in self.graph:
            if in_degree[i] == 0:
                queue_of_in_degrees.append(i)
        counter = 0
        topological_order = []
        while(queue_of_in_degrees != []):
            node = queue_of_in_degrees.pop(0)
            topological_order.append(node)
            for child in self.graph[node]:
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    queue_of_in_degrees.append(child)
            counter += 1
        length = len(self.graph)
        if counter == length:
            print("Non-Dfs Topological sort: ", topological_order)
        else:
            print("Graph is not a DAG.")
        
    def in_degree_finder(self):
        in_degree = {}
        for i in self.graph:
            in_degree[i] = 0
        for i in self.graph:
            for j in self.graph[i]:
                in_degree[j] += 1
        return in_degree    
        
    def check_in_out_degrees(self):
        in_degree = {}
        out_degree = {}
        for i in self.graph:
            in_degree[i] = 0
            out_degree[i] = 0
        for i in self.graph:
            for j in self.graph[i]:
                print(i, " -> ", j)
                in_degree[j] += 1
                out_degree[i] += 1
        for i in self.graph:
            if in_degree[i] == 0:
                print("In-degree of ", i, " is 0")
                for j in self.graph:
                    if out_degree[j] == 0:
                        print("Out-degree of ", j, " is 0")
                        return

def q1():    
    dag = DAG()
    dag.take_graph()
    dag.visualize()
    dag.dfs_topological_sort()
    dag.non_dfs_topological_sort()
    

if __name__ == "__main__":
    q1()
