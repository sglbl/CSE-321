# Author : Suleyman Golbol
import random 


class Q1:
    array = []
    n = 1
    m = 1
    def __init__(self):
        print("Question 1")

        
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
    
    
    # def find_highest_points(self):
    #     # Brute force algorithm to get the highest points using stack
    #     stack = []
    #     max_sum = 0
    #     max_path = []
    #     start_point = (0,0)
    #     stack.append(start_point)
        
    #     visited = []
        
    #     sum = self.array[0][0]
    #     while len(stack) > 0:
    #         current_val = stack.pop()
    #         if current_val == (self.n-1, self.m-1):
    #             if sum > max_sum:
    #                 max_sum = sum
    #                 max_path = visited
    #                 # sum = 0
    #                 # path = []
    #             print("Path: ", visited)
    #             print("Sum: ", sum)
            
    #         elif (current_val[0], current_val[1]+1) not in visited and self.check_validity(current_val[0], current_val[1]+1):
    #             current_val = (current_val[0], current_val[1]+1)
    #             stack.append(current_val)
    #             print("Adding to stack: ", self.array[current_val[0]][current_val[1]])
    #             sum += self.array[current_val[0]][current_val[1]]
    #             visited.append(current_val)
    #         elif (current_val[0]+1, current_val[1]) not in visited and self.check_validity(current_val[0]+1, current_val[1]):
    #             current_val = (current_val[0]+1, current_val[1])
    #             stack.append(current_val)
    #             print("Adding to stack: ", self.array[current_val[0]][current_val[1]])
    #             sum += self.array[current_val[0]][current_val[1]]
    #             visited.append(current_val)            
    #     return stack  



    # def find_highest_points(self, max_sum, max_path, sum=0, visited=[], start_point=(0,0)):
    #     # Brute force algorithm to get the highest points using stack
    #     finished = False
    #     stack = []
    #     stack.append(start_point)
        
    #     sum = self.array[0][0]
    #     while len(stack) > 0:
    #         current_val = stack.pop()
    #         if (current_val[0], current_val[1]+1) not in visited and self.check_validity(current_val[0], current_val[1]+1):
    #             current_val = (current_val[0], current_val[1]+1)
    #             stack.append(current_val)
    #             print("Adding to stack: ", self.array[current_val[0]][current_val[1]])
    #             sum += self.array[current_val[0]][current_val[1]]
    #             visited.append(current_val)
    #         if (current_val[0]+1, current_val[1]) not in visited and self.check_validity(current_val[0]+1, current_val[1]):
    #             current_val = (current_val[0]+1, current_val[1])
    #             stack.append(current_val)
    #             print("Adding to stack: ", self.array[current_val[0]][current_val[1]])
    #             sum += self.array[current_val[0]][current_val[1]]
    #             visited.append(current_val)         
    #         if current_val == (self.n-1, self.m-1):
    #             if sum > max_sum:
    #                 max_sum = sum
    #                 max_path = visited
    #                 print("Path: ", visited)
    #                 print("Sum: ", sum)
    #                 print("Popping: ", visited.pop())
    #                 sum = sum - self.array[current_val[0]][current_val[1]]
    #                 current_val = visited.pop()
    #                 self.find_highest_points(max_sum, max_path, sum, visited, stack.pop())
    #                 # self.find_highest_points(max_sum, max_path, sum, visited, current_val)
    #             finished = True   
        
    #     if finished == False:
    #         # no successful path found, pop the last element and try again
    #         visited.pop()
    #         self.find_highest_points(max_sum, max_path, visited)            
    #     return stack  
            
    
    def find_highest_points(self, max_sum, max_path, sum=0, visited=[], start_point=(0,0)):
        # Brute force algorithm to get the highest points using stack
        finished = False
        stack = []
        stack.append(start_point)
        
        sum = self.array[0][0]
        while len(stack) > 0:
            current_val = stack.pop()
            if (current_val[0], current_val[1]+1) not in visited and self.check_validity(current_val[0], current_val[1]+1):
                current_val = (current_val[0], current_val[1]+1)
                stack.append(current_val)
                print("Adding to stack: ", self.array[current_val[0]][current_val[1]])
                sum += self.array[current_val[0]][current_val[1]]
                visited.append(current_val)
            if (current_val[0]+1, current_val[1]) not in visited and self.check_validity(current_val[0]+1, current_val[1]):
                current_val = (current_val[0]+1, current_val[1])
                stack.append(current_val)
                print("Adding to stack: ", self.array[current_val[0]][current_val[1]])
                sum += self.array[current_val[0]][current_val[1]]
                visited.append(current_val)         
            if current_val == (self.n-1, self.m-1):
                if sum > max_sum:
                    max_sum = sum
                    max_path = visited
                    print("Path: ", visited)
                    print("Sum: ", sum)
                    print("Popping: ", visited.pop())
                    sum = sum - self.array[current_val[0]][current_val[1]]
                    current_val = visited.pop()
                    self.find_highest_points(max_sum, max_path, sum, visited, stack.pop())
                    # self.find_highest_points(max_sum, max_path, sum, visited, current_val)
                finished = True   
        
        if finished == False:
            # no successful path found, pop the last element and try again
            visited.pop()
            self.find_highest_points(max_sum, max_path, visited)            
        return stack  
    
    
    
    def path_generator(self):
        paths = []
        stack = []
        stack.append((0,0))
                
        while len(stack) > 0:
            current_position = stack.pop()
            # base case: we have reached the end position
            if current_position == (self.n-1, self.m-1):
                # add the current path to the list of paths
                # stack.append(current_position)
                print("Path: ", stack)
                paths.append(stack.copy())
                continue
            
            current_position_temp = current_position
            if(self.check_y_valid(current_position) == True):
                print("YCurrent position: ", current_position, " and valid position: ", (current_position[0]+1, current_position[1]))
                stack.append((current_position[0]+1, current_position[1]))   
                current_position = (current_position[0]+1, current_position[1])             
                # print("Path: ", stack)
            current_position = current_position_temp
            if(self.check_x_valid(current_position) == True):
                print("XCurrent position: ", current_position, " and valid position: ", (current_position[0], current_position[1]+1))
                stack.append((current_position[0], current_position[1]+1))
                current_position = (current_position[0], current_position[1]+1)
                # print("Path: ", stack)
        return paths
    
    
    
    def check_y_valid(self, val):
        if val[0] + 1 < self.n:
            return True
        return False
    
    def check_x_valid(self, val):
        if val[1] + 1 < self.m:
            return True
        return False
        
    def check_validity(self, val1, val2):
        if val1 >= self.n or val2 >= self.m:
            return False
        return True
    
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
        


if __name__ == "__main__":
    print("Welcome to the homework 4. \nPress 1 to test part1\nPress 2 to test part2\nPress 3 to test part3")
    # inp = take_input("Enter your choice: ")
    inp = "1"
    if inp == "1":
        print("Question 1:")
        q1 = Q1()
        # q1.create_random_array(4, 3)
        q1.n = 4
        q1.m = 3
        q1.array = [
            [25,30,25],
            [45,15,11],
            [1,88,15],
            [9,4,23]
        ]
        q1.print_array()
        max_sum = 0
        max_path = []
        paths = q1.path_generator()
        # print paths properly
        for path in paths:
            print("[", path, "]\n")
            
        
        # print("Highest points are: ", q1.find_highest_points(max_sum, max_path))
    elif inp == "2":
        print("Question 2:")
        # Q2()
    elif inp == "3":
        print("Question 3:")
        # Q3()
    else:
        print("Error! Wrong input.")
