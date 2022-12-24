# Author : Suleyman Golbol
import random 


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


# Iterative brute-force highest point finder 
class Q1:
    array = []
    n = 1
    m = 1
        
    def create_random_array(self, n, m):
        self.n = n
        self.m = m
        
        for i in range(n):
            self.array.append([])
            for _j in range(m):
                self.array[i].append(random.randint(0, 40))         
        
        
    def print_array(self): 
        # print outer contraints   
        print("   |", end="\t")
        for i in range(self.m):
            print("B"+str(i+1), end="\t")
        print(" ")
        for j in range(self.n):
            print("-------", end="")
        print(" ")
        
        # print numbers
        for i in range(self.n):
            print("A" + str(i+1) + " |", end="\t")
            for j in range(self.m):
                print(self.array[i][j], end="\t")
            print(" ")
    
    
    def find_highest_points(self, all_points, all_paths):
        # Brute force algorithm to get the highest points using stack
        sums = []
        for i in range(len(all_points)):
            sum = 0
            for j in range(len(all_points[i])):
                sum += all_points[i][j]
            sums.append(sum)
        return sums.index(max(sums)), max(sums)

    
    # Returns the value of the current position inside brackets (to store the every point in the path)
    def get_value(self, y, x):
        return [self.array[y][x]]


    # Returns the current position inside brackets (to store the every point in the path)
    def get_path(self, y, x):
        return [(y, x)]

    
    def check_y_valid(self, val):
        if val[0] + 1 < self.n:
            return True
        return False
    
    
    def check_x_valid(self, val):
        if val[1] + 1 < self.m:
            return True
        return False
    
    
    def route_printer(self, route):
        route_str = ""
        for i in range(len(route)):
            route_str += ("A" + str(route[i][0]+1) + "B" + str(route[i][1]+1))
            if i != len(route)-1:
                route_str += " -> "
        return route_str


    # Finds all paths and returns the paths
    def path_generator(self):
        points = []
        path_routes = []
        stack = []
        stack.append(((0,0), self.get_value(0,0), self.get_path(0,0)))
        
        while len(stack) > 0:
            current_position, point, path = stack.pop()
            # print("Current position: ", current_position, " and point: ", point)
            # base case: we have reached the end position
            if current_position == (self.n-1, self.m-1):
                # add the current path to the list of paths
                points.append(point)
                path_routes.append(path)
                continue
            
            # checking moves in the y direction
            if(self.check_y_valid(current_position) == True):
                # print("YCurrent position: ", current_position, " and valid position: ", (current_position[0]+1, current_position[1]))
                stack.append(((current_position[0]+1, current_position[1]), 
                              point + self.get_value(current_position[0]+1, current_position[1]),
                              path + self.get_path(current_position[0]+1, current_position[1])))   
                
            # checking moves in the x direction
            if(self.check_x_valid(current_position) == True):
                # print("XCurrent position: ", current_position, " and valid position: ", (current_position[0], current_position[1]+1))
                stack.append(((current_position[0], current_position[1]+1), 
                              point + self.get_value(current_position[0], current_position[1]+1),
                              path + self.get_path(current_position[0], current_position[1]+1)))
        return points, path_routes


# Decrease and Conquer algorithm to find the median of unsorted array
class Q2:
    array = []
    size = 0
    
    def median_finder(self, median_index):
        left = 0
        right = len(q2.array)-1
        if len(self.array) % 2 == 1:
            median = self.find_kth_smallest(median_index, left, right)
        else:
            median = (self.find_kth_smallest(median_index, left, right) + 
                      self.find_kth_smallest(median_index-1, left, right)) / 2
        
        return median
    
    def median_index_finder(self):
        median_index = len(self.array)//2
        return median_index
    
    
    def create_random_array(self, size):
        self.size = size
        for i in range(size):
            self.array.append(random.randint(0, 40))     
        
        
    def print_array(self): 
        print(self.array)
    
    
    def swapper(self, a, b):
        a, b = b, a
        return a, b
    
    
    def lomuto_partition(self, s, left_index, right_index):
        pivot = self.array[s]  # pivot element 
        self.array[s], self.array[right_index] = self.swapper(self.array[s], self.array[right_index])

        iter_index_left = left_index 
        for i in range(left_index, right_index+1):
            if self.array[i] < pivot:
                self.array[i], self.array[iter_index_left] = self.swapper(self.array[i], self.array[iter_index_left])
                iter_index_left = iter_index_left + 1
            
        self.array[iter_index_left], self.array[right_index] = self.swapper(self.array[iter_index_left], self.array[right_index])    
        return iter_index_left
        
        
    def find_kth_smallest(self, k, left_index, right_index):
        # QUICK SELECT (Finding the kth smallest element which is the median)
        if left_index == right_index:
            return self.array[left_index] # base case
        
        s = left_index # pivot index
        s = self.lomuto_partition(s, left_index, right_index)
        if s == k:
            return self.array[s]
        if s > k:
            return self.find_kth_smallest(k, left_index, s-1)
        return self.find_kth_smallest(k, s+1, right_index)
        
######### QUESTION 3 ##############
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedListCircular:
    
    def __init__(self) -> None:
        self.head = None
        self.size = 0
        self.current = None
        
    def add(self, element):
        if self.head == None:
            self.head = Node(element)
            self.head.next = self.head
            return
        element_node = Node(element)
        element_node.next = self.head
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = element_node      
        
        
    # Remove which also returns next element
    def remove(self, element):
        if self.head != None:
            temp = self.head
            while temp.next != self.head:
                if temp.next.data == element:
                    temp.next = temp.next.next
                    return temp.next
                else:
                    temp = temp.next
            # if that data is in the head
            if temp.next.data == element:
                temp.next = temp.next.next
                self.head = temp.next
                return temp.next
        return None
    
    def remove_next(self):
        # Using current, removes next
        if self.current != None:
            self.current.next = self.current.next.next
            return self.current.next

    def print_list(self):
        print("Elements: ", end="")
        temp = self.head
        while temp is not None:
            if temp.next == self.head:
                print(temp.data)
            else:
                print(temp.data, end=" -> ")
            temp = temp.next  
            if temp == self.head:
                break    
        print("")

        
class Q3a:
    linked_list = LinkedListCircular()
    
    def create_elements(self, size):
        self.linked_list.size = size
        for i in range(size):
            self.linked_list.add("P"+str(i+1))     
        
    def print_elements(self): 
        self.linked_list.print_list()
            
    def kill_next(self):
        # current = self.linked_list.remove(self.linked_list.current.next.data)
        # Remove next using current data
        current = self.linked_list.remove_next()
        # Update current
        self.linked_list.current = current
        # Update size
        self.linked_list.size = self.linked_list.size - 1

    def winner(self):
        self.linked_list.current = self.linked_list.head
        
        while self.linked_list.size > 1:
            self.kill_next()
            
        return self.linked_list.current.data

        
class Q3b:
    
    def print_elements(self, n): 
        for i in range(n):
            if i == n-1:
                print("P"+str(i+1))
            else:
                print("P"+str(i+1), end=" -> ")
    
    def log_finder(self, n):
        # Find the log base 2 of n
        log = 0
        while n > 1:
            n = n/2
            log = log + 1
        return log
    
    def winner(self, n):
        # Check report 3b for explanation
        two_to_x = 1
        while two_to_x <= n/2:
            if two_to_x*2 > n:
                break
            two_to_x = two_to_x*2
        x = self.log_finder(two_to_x)
        print(f"Biggest 2^x = {two_to_x} which is smaller than n = {n}. So x = {x}. \nWinner = 2*({n} - 2^{x}) + 1 = 2*({n} - {two_to_x}) + 1")
        return 2*(n-two_to_x) + 1            

if __name__ == "__main__":
    print("Welcome to the homework 4. \nPress 1 to test part1\nPress 2 to test part2\nPress 3a to test part3a\nPress 3b to test part3b")
    inp = take_input("Enter your choice: ")
    # inp = "3b"
    if inp == "1":
        print("Question 1:")
        q1 = Q1()
        n = take_input("Enter n: ")
        m = take_input("Enter m: ")
        q1.create_random_array(int(n), int(m))
        # q1.n = 4
        # q1.m = 3
        # q1.array = [
        #     [25,30,25],
        #     [45,15,11],
        #     [1,88,15],
        #     [9,4,23]
        # ]
        q1.print_array()
        points, paths = q1.path_generator()
        max_index, sum = q1.find_highest_points(points, paths)
        
        print("Points: ", points[max_index], " | Sum = ", sum)
        print("Route: ", q1.route_printer(paths[max_index]))
        
    elif inp == "2":
        print("Question 2:")
        q2 = Q2()
        size = int(take_input("Enter # of elements: "))
        q2.create_random_array(size)
        q2.print_array()
        median_index = q2.median_index_finder()
        median = q2.median_finder(median_index)
        print("Median value: ", median)
        
    elif inp == "3a":
        print("Question 3:")
        q3a = Q3a()
        n = take_input("Enter n: ")
        q3a.create_elements(int(n))
        q3a.print_elements()
        
        print("Winner: " , q3a.winner())
        
    elif inp == "3b":
        print("Question 3b:")
        q3b = Q3b()
        n = take_input("Enter n: ")
        q3b.print_elements(int(n))
        
        print("Winner: " , "P" + str(q3b.winner(int(n))))
        
    else:
        print("Error! Wrong input.")
