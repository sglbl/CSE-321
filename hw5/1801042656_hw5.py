# Suleyman Golbol
# 1801042656
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
 
 
class Q1:
    
    def get_half(self, string):
        size_half = len(string) // 2
        return size_half
    
    def get_left_array(self, string_array, size_half):
        return string_array[:size_half]
    
    def get_right_array(self, string_array, size_half):
        return string_array[size_half:]
    
    def longest_common_str(self, string_array, length):
        if length == 1:
            return string_array[-1]
        else:
            middle_size = self.get_half(string_array)
            left_array = self.get_left_array(string_array, middle_size)
            right_array = self.get_right_array(string_array, middle_size)
            return self.longest_common_str_between_2(
                self.longest_common_str(left_array, len(left_array)), 
                self.longest_common_str(right_array, len(right_array))
                )
        
    def get_smallest_string(self, string1, string2):
        if len(string1) < len(string2):
            return string1
        else:
            return string2
        
    def longest_common_str_between_2(self, string1, string2):
        smallest_string = self.get_smallest_string(string1, string2)
        for i in range(len(smallest_string)):
            if string1[i] != string2[i]:
                return string1[:i]
        return smallest_string  
      

class Q2:
    array = []
    max = -1
    min = 1000
    max_index = -1
    min_index = -1
    
    def create_random_array(self, size):
        self.size = size
        for i in range(size):
            self.array.append(random.randint(1, 40))   
    
    def print_array(self): 
        print(self.array)
    
    def get_half(self, array):
        size_half = len(array) // 2
        return size_half
    
    def get_left_array(self, array, size_half):
        return array[:size_half]
    
    def get_right_array(self, array, size_half):
        return array[size_half:]
    
    def last_occurrence(self, array, value):
        index = -1
        while True:
            try:
                index = array.index(value, index+1)
            except ValueError:
                return index
        
    # find the biggest difference between two elements in array with recursion
    def a_divide_and_conquer_solver(self, array, length, index):
        # base case
        if length == 1:
            return 0
        else:
            middle_size = self.get_half(array)
            left_array = self.get_left_array(array, middle_size)
            right_array = self.get_right_array(array, middle_size)
            # conquer
            left_solved = self.a_divide_and_conquer_solver(left_array, len(left_array), self.array.index(left_array[0]))
            right_solved = self.a_divide_and_conquer_solver(right_array, len(right_array),  self.array.index(right_array[0]))
            max_min_dif = max(right_array) - min(left_array)
            
            # print("left array is ", left_array, " and right array is ", right_array)
            arr = [left_solved, right_solved, max_min_dif]
            ind = arr.index(max(arr)) # which has the highest value
            
            if ind == 2:
                self.max = max(right_array)
                self.min = min(left_array)
                self.sell_index = self.last_occurrence(self.array, self.max)
                self.buy_index = self.array.index(min(left_array))
            elif ind == 0: # left_solved has the max
                self.max = max(left_array)
                self.min = min(left_array)
                self.sell_index = self.last_occurrence(self.array, self.max)
                self.buy_index = self.array.index(min(left_array))
            else: # right_solved has the max
                self.min = min(right_array)
                self.max = max(right_array)
                self.buy_index = self.array.index(self.min)
                self.sell_index = self.last_occurrence(self.array, self.max)
                
            return max(left_solved, right_solved, max_min_dif)
    
    # b
    def is_next_smaller(self, array, index):
        if array[index+1] > array[index]:
            return False
        else:
            return True
    
    def b_solve_normal(self, array):
        profit = 0
        minimum = array[0]
        
        for i in range(len(array)):
            # update minimum
            minimum = min(array[i], minimum)
            difference_with_min = array[i] - minimum
            # if difference with min is bigger than profit, update profit
            profit = max(profit, difference_with_min)
    
        print(f"2b: Buy on Day{q2.buy_index} for {q2.min} TL and sell on Day{q2.sell_index} for {q2.max}. Profit is {profit} TL")


# Dynamic programming
class Q3:
    array = []
    length_storer_array = []
    
    def create_random_array(self, size):
        self.size = size
        for i in range(size):
            self.array.append(random.randint(1, 40))   
    
    def print_array(self): 
        print(self.array)
    
    # Solving with dynamic programming by dividing the problem into subproblems
    def longest_increasing_subarray(self, array, length):
        self.length_storer_array = [0] * length
        # For ex for array with size 10; it will be [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.length_storer_array[0] = 1
        
        for i, element in enumerate(array):
            if i == 0:
                continue
            # element = array[i] and previous_element = array[i-1]
            previous_element = array[i-1]
            
            # compare with previous element
            if element > previous_element:  
                if self.length_storer_array[i] < self.length_storer_array[i-1]:
                    # this is for not to compute the same subproblem again
                    self.length_storer_array[i] = self.length_storer_array[i-1]
            # adding current element to the sequence length
            self.length_storer_array[i] = self.length_storer_array[i] + 1
        
        max_length = max(self.length_storer_array)
        max_len_index = self.length_storer_array.index(max_length)
        print("The longest increasing subarray is: ", self.array[max_len_index - max_length + 1: max_len_index+1])
        return max_length    
            
        
class Q4:
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
   
   
    def route_printer(self, route):
        route_str = ""
        for i in range(len(route)):
            route_str += ("A" + str(route[i][0]+1) + "B" + str(route[i][1]+1))
            if i != len(route)-1:
                route_str += " -> "
        return route_str
    
    def point_printer(self, points):
        points_str = ""
        for i in range(len(points)):
            points_str += str(points[i])
            if i != len(points)-1:
                points_str += " + "
        return points_str
   
    def get_path_and_score(self, T):
        # start from the end and backtrace to find biggest path
        i = self.n-1
        j = self.m-1
        path = [[i,j]]
        total_points = [T[i][j]]

        while i > 0 and j > 0:
            if T[i-1][j] >= T[i][j-1]:
                i -= 1
            else:
                j -= 1
            path.append([i, j])
            total_points.append(T[i][j])
        
        # Reversing the path
        path.append([0, 0])
        path.reverse()
        
        # Extracting points from total points and Reversing the points
        for i in range(len(total_points)-1):
            total_points[i] = total_points[i] - total_points[i+1]
        total_points.append(T[0][0])
        total_points[-2] = total_points[-2] - total_points[-1]
        total_points.reverse()
        return path, total_points

    def dp_find_highest_points(self):
        route = []
        points = []
        T = []
        
        # Initialize 2d array with 0s except the first element of the array
        for i in range(self.n):
            T.append([])
            for j in range(self.m):
                if i == 0 and j == 0:
                    T[i].append(self.array[i][j])
                else:
                    T[i].append(0)
        
        # initializing all first columns
        for i in range(1, self.n):
            T[i][0] = self.array[i][0] + T[i-1][0]
        # initializing all first rows
        for j in range(1, self.m):
            T[0][j] = self.array[0][j] + T[0][j-1]
            
        # adding all the elements so that we can find the max 
        # and we don't need to compute the same subproblem again
        for i in range(self.n):
            for j in range(self.m):
                if i == 0 or j == 0:
                    continue
                else:
                    max_val = max(T[i-1][j], T[i][j-1])
                    T[i][j] = self.array[i][j] + max_val
                    route.append([i, j])
                    points.append(self.array[i][j])

        # print("T is ", T)
        route, points = self.get_path_and_score(T)
        print("Route: ", self.route_printer(route))
        print("points is ", self.point_printer(points) + " = " + str(T[self.n-1][self.m-1]))
        return T[self.n-1][self.m-1]

    # Greedy solution
    def gr_find_highest_points(self):
        route = []
        points = []
        
        route.append([0, 0])
        points.append(self.array[0][0])
        
        i = 0
        j = 0
        while i < self.n-1 and j < self.m-1:
            if self.array[i+1][j] <= self.array[i][j+1]:
                j = j + 1
            else:
                i = i + 1
            points.append(self.array[i][j])
            route.append([i, j])
        points.append(self.array[self.n-1][self.m-1])
        print("Route: ", self.route_printer(route))
        print("points is ", self.point_printer(points) + " = " + str(sum(points)))
        return sum(points)
        

    
   
if __name__ == "__main__":
    print("Welcome to the homework 5. \nPress 1 to test part1\nPress 2 to test part2\nPress 3 to test part3\nPress 4 to test part4")
    inp = take_input("Enter your choice: ")
    if inp == "1":
        print("Question 1:")
        # string_array = ["try1", "trying2", "trytotest", "trytotestclass", "try_div_and_conq"]
        n = take_input("Enter number of strings: ")
        string_array = []
        for i in range(int(n)):
            string_array.append(take_input("Enter string: "))

        length = len(string_array)
        q1 = Q1()
        val = q1.longest_common_str(string_array, length)
        print("Answer:", val)
        
    elif inp.startswith("2"):   
        print("Question 2:")
        q2 = Q2()
        size = int(take_input("Enter # of elements: "))
        q2.create_random_array(size)
        q2.print_array()
        
        print("Solving 2a:")
        profit= q2.a_divide_and_conquer_solver(q2.array, size, 0)
        print(f"2a: Buy on Day{q2.buy_index} for {q2.min} TL and sell on Day{q2.sell_index} for {q2.max}. Profit is {profit} TL")
        
        print("Solving 2b:")
        q2.b_solve_normal(q2.array)   # Linear time
        
    elif inp == "3":
        print("Question 3:")
        q3 = Q3()
        n = take_input("Enter n: ")
        q3.create_random_array(int(n))
        q3.print_array()
        answer = q3.longest_increasing_subarray(q3.array, len(q3.array))
        print("Biggest subarray size: " , answer)
    
    elif inp.startswith("4"):   
        print("Question 4:")
        q4 = Q4()
        n = take_input("Enter n: ")
        m = take_input("Enter m: ")
        q4.create_random_array(int(n), int(m))
        # q4.n = 4
        # q4.m = 3
        # q4.array = [
        #     [25,30,25],
        #     [45,15,11],
        #     [1,88,15],
        #     [9,4,23]
        # ]
        q4.print_array()
        print("Dynamic approach: ")
        max_score = q4.dp_find_highest_points()
        print("Max score of dynamic approach: ", max_score)
        
        print("Greedy approach: ")
        max_score = q4.gr_find_highest_points()
        print("Max score of greedy approach: ", max_score)
        
    else:
        print("Error! Wrong input.")
        
        
        
    