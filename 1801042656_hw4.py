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


# class Q2:
    
        


if __name__ == "__main__":
    print("Welcome to the homework 4. \nPress 1 to test part1\nPress 2 to test part2\nPress 3 to test part3")
    # inp = take_input("Enter your choice: ")
    inp = "2"
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
        # Q2()
    elif inp == "3":
        print("Question 3:")
        # Q3()
    else:
        print("Error! Wrong input.")
