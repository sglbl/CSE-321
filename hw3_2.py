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
            for j in range(num_of_children):
                child = self.take_input("Enter the child" + str(j+1) + ": ")
                self.graph[node].append(child)
    
    def check_if_dag(self):
        visited = set()
        for node in self.graph:
            if node not in visited:
                self.check_if_dag_helper(node, visited)
        print("Graph: ", visited)
        return self.is_dag
    
    def check_if_dag_helper(self, node, visited):
        visited.add(node)
        try:
            for child in self.graph[node]:
                if child not in visited:
                    self.check_if_dag_helper(child, visited)
                else:
                    self.is_dag = False
                    return    
        except KeyError:
            pass

    def visualize(self):
        # Visualize the graph using dict values
        print("Graph: ", self.graph)
        

def q1():    
    dag = DAG() 
    dag.take_graph()
    if dag.check_if_dag() == False:
        print("The graph that you entered is not a DAG!")
        return
    dag.visualize()
    # print("DFS BASED SOLUTION")
    # print("The longest path is: ", end = "")
    # dag.find_longest_path()
    
    

    
    

if __name__ == "__main__":
    q1()
