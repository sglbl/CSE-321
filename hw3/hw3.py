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
        try:
            in_degree = {}
            for i in self.graph:
                in_degree[i] = 0
            for i in self.graph:
                for j in self.graph[i]:
                    in_degree[j] += 1
            return in_degree    
        except KeyError:
            print("KeyError detected. Make sure you entered the graph correctly. (For Ex. Enter the node even doesn't have any children)")
            exit()
        
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

def q1_user():    
    dag = DAG()
    dag.take_graph()
    dag.visualize()
    dag.dfs_topological_sort()
    dag.non_dfs_topological_sort()

def q1_auto():    
    dag = DAG()
    # dag.take_graph()
    dag.graph = {
        "CSE102": ["CSE241"],
        "CSE241": ["CSE222"],
        "CSE222": ["CSE321", "CSE422"],
        "CSE211": ["CSE321"],
        "CSE321": ["CSE422"],
        "CSE422": []
    }
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


def q2_user():
    a = int(input("Enter the base: "))
    n = int(input("Enter the exponent: "))
    res = exponentiation(a, n)
    print("Result: ", res)

def q2_auto():
    a = 2
    n = 10
    res = exponentiation(a, n)
    print("Result of 2^10: ", res)
    n = 11
    res = exponentiation(a, n)
    print("Result of 2^11: ", res)

# QUESTION 3    
class Sudoku:    
    # constructor
    def __init__(self):
        self.sudoku = []
        
            
    def get_sudoku_input(self):
        print("Note: To remain an empty cell, write '0' as input")
    
        for i in range(9):  
            row = []
            print(f"Enter the row {i+1} (9 numbers separating with enter): ")
            for j in range(9):
                row.append(int(take_input(str(j+1) + ": ")))
            self.sudoku.append(row)
    
    
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
        # if it's legal to put, return True
        
         # if the cell is not empty, it is not legal
        if self.get_value(row, col) != 0:
            return False
        
        for i in range(9):
            # if value is already in the row, it is not legal
            if self.get_value(row, i) == value:
                return False
            # if value is already in the column, it is not legal
            if self.get_value(i, col) == value:
                return False
        
        # if value is already in the 3x3 box, it is not legal
        row_start = (row // 3) * 3
        col_start = (col // 3) * 3
        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                if self.get_value(i, j) == value:
                    return False
        return True
    
    def end_of_row(self, column):
        if column == 9:
            column = 0
            return True
        return False
    
    def solver(self, row, column):
        if (row == 8):
            if (column == 9):
                return True # we are done
        
        # Change row number to next and reset the column
        if self.end_of_row(column):
            column = 0
            row = row + 1
    
        # If already filled, skip to next column
        if self.sudoku[row][column] != 0:
            return self.solver(row, column + 1)
        for num in range(1, 10):
            if self.is_legal(row, column, num):
                self.sudoku[row][column] = num
                # control next
                if self.solver(row, column + 1):
                    return True
            # If not solved return back to 0
            self.sudoku[row][column] = 0
        return False
    
    
def q3_auto():
    sudoku_object = Sudoku()
    sudoku_object.sudoku = [[1, 0, 0, 0, 0, 7, 0, 9, 0],
                            [0, 3, 0, 0, 2, 0, 0, 0, 8],
                            [0, 0, 9, 6, 0, 0, 5, 0, 0],
                            [0, 0, 5, 3, 0, 0, 9, 0, 0],
                            [0, 1, 0, 0, 8, 0, 0, 0, 2],
                            [6, 0, 0, 0, 0, 4, 0, 0, 0],
                            [3, 0, 0, 0, 0, 0, 0, 1, 0],
                            [0, 4, 0, 0, 0, 0, 0, 0, 7],
                            [0, 0, 7, 0, 0, 0, 3, 0, 0]]
    
    print("Unsolved sudoku: ")    
    sudoku_object.print_sudoku()
    sudoku_object.solver(0, 0)
    print("Solved sudoku: ")
    sudoku_object.print_sudoku()

def q3_user():
    sudoku_object = Sudoku()
    sudoku_object.get_sudoku_input()
    
    print("Unsolved sudoku: ")    
    sudoku_object.print_sudoku()
    sudoku_object.solver(0, 0)
    print("Solved sudoku: ")
    sudoku_object.print_sudoku()


if __name__ == "__main__":
    print("Welcome to the homework 3. \nPress 1 for test every part automatically\nPress 2 for test by user input")
    inp = take_input("Enter your choice: ")
    if inp == "1":
        print("Question 1:")
        q1_auto()
        print("Question 2:")
        q2_auto()
        print("Question 3:")
        q3_auto()
    elif inp == "2":
        print("Enter the question no you want to test: ")
        inp = take_input("Enter your choice: ")
        if inp == "1":
            print("Question 1:")
            q1_user()
        elif inp == "2":
            print("Question 2:")
            q2_user()
        elif inp == "3":
            print("Question 3:")
            q3_user()
        else:
            print("Error! Wrong input.")
