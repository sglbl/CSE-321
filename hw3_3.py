# Author : Suleyman Golbol

    
# Taking input from user properly
def take_input(string, int_type=False):
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
        

class DAG:
    is_dag = True
    
    def __init__(self) -> None:
        self.graph = {}        
    
    def take_graph(self):
        num_of_nodes = int(take_input("Enter the number of nodes you want on the graph: ", int_type=True))
            
        for i in range(num_of_nodes):
            node = take_input("Enter the node" + str(i+1) + ": ")
            if node not in self.graph:
                self.graph[node] = []
            num_of_children = int(take_input("Enter the number of children: ", int_type=True))
            if num_of_children == 0:
                pass
            for j in range(num_of_children):
                child = take_input("Enter the child" + str(j+1) + ": ")
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
        counter = 0
        topological_order = []
        queue_of_in_degrees = []        
        in_degree = self.in_degree_finder()

        for i in self.graph:
            if in_degree[i] == 0:
                queue_of_in_degrees.append(i)
        
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
        
    # def check_in_out_degrees(self):
    #     in_degree = {}
    #     out_degree = {}
    #     for i in self.graph:
    #         in_degree[i] = 0
    #         out_degree[i] = 0
    #     for i in self.graph:
    #         for j in self.graph[i]:
    #             print(i, " -> ", j)
    #             in_degree[j] += 1
    #             out_degree[i] += 1
    #     for i in self.graph:
    #         if in_degree[i] == 0:
    #             print("In-degree of ", i, " is 0")
    #             for j in self.graph:
    #                 if out_degree[j] == 0:
    #                     print("Out-degree of ", j, " is 0")
    #                     return

def q1():    
    dag = DAG()
    dag.take_graph()
    dag.visualize()
    dag.dfs_topological_sort()
    dag.non_dfs_topological_sort()


# QUESTION 2
def exponentiation(a, n):
    # check if a is integer 
    if isinstance(a, int) == False \
        or isinstance(n, int) == False \
            or n < 0:
        print("Error! A or n is not an integer or n is negative.")
        
    result = 1
    while(n >= 1):
        if n % 2 == 1:
            result *= a
        a = a*a
        n //= 2
    return result


def q2():
    a = int(input("Enter the base: "))
    n = int(input("Enter the exponent: "))
    res = exponentiation(a, n)
    print("Result: ", res)

# QUESTION 3    
class Sudoku:    
    # constructor
    def __init__(self):
        self.sudoku = []
        
            
    def get_sudoku_input(self):
        print("Enter the first row (9 numbers separating with enter): ")
        row = []
    
        for i in range(3):  
            for j in range(3):
                row.append(int(take_input(str(j) + ": ")))
            self.sudoku.append(row)
        self.print_sudoku(self.sudoku)
    
    
    def print_sudoku(self):
        for i in range(9):
            if i % 3 == 0:
                print("-------------------------")
            for j in range(9):
                if j % 3 == 0:
                    print("| ", end="")
                print(self.sudoku[i][j], end=" ")
            print("|")
        print("-------------------------")
    
    
    def set_value(self, row, col, value):
        self.sudoku[row][col] = value
    
    
    def get_value(self, row, col):
        return self.sudoku[row][col]
    
    
    def is_legal(self, row, col, value):
        if self.get_value(row, col) != 0:
            return False
        for i in range(9):
            if self.get_value(row, i) == value:
                return False
            if self.get_value(i, col) == value:
                return False
        row_start = (row // 3) * 3
        col_start = (col // 3) * 3
        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                if self.get_value(i, j) == value:
                    return False
        return True
    
    def is_solution(self):
        for i in range(9):
            for j in range(9):
                if self.get_value(i, j) == 0:
                    return False
        return True           
    
    def iterative_solver(self):
        # iterative sudoku solver using stack
        stack = []
        for i in range(9):
            for j in range(9):
                if self.get_value(i, j) == 0:
                    stack.append((i, j))
        while(stack != []):
            row, col = stack.pop()
            value = self.get_value(row, col)
            while(value < 9):
                value += 1
                if self.is_legal(row, col, value):
                    print("Old: ", self.sudoku[row][col])
                    self.set_value(row, col, value)
                    print("New: ", self.sudoku[row][col], " at ", row, col)
                    stack.append((row, col))
                    break
            if value == 9:
                # because 
                self.set_value(row, col, 0)       
        print("Self.sudoku[0][1]: ", self.sudoku[0][1])
    
    
def q3():
    sudoku_object = Sudoku()
    # sudoku.get_sudoku_input()
    sudoku_object.sudoku = [[1, 0, 0, 0, 0, 7, 0, 9, 0],
                            [0, 3, 0, 0, 2, 0, 0, 0, 8],
                            [0, 0, 9, 6, 0, 0, 5, 0, 0],
                            [0, 0, 5, 3, 0, 0, 9, 0, 0],
                            [0, 1, 0, 0, 8, 0, 0, 0, 2],
                            [6, 0, 0, 0, 0, 4, 0, 0, 0],
                            [3, 0, 0, 0, 0, 0, 0, 1, 0],
                            [0, 4, 0, 0, 0, 0, 0, 0, 7],
                            [0, 0, 7, 0, 0, 0, 3, 0, 0]]
                
    sudoku_object.print_sudoku()
    sudoku_object.iterative_solver()
    sudoku_object.print_sudoku()


if __name__ == "__main__":
    # q1()
    # q2()
    q3()
