def stockBuySell(price, n):
 
    # Prices must be given for at least two days
    if (n == 1):
        return
 
    # Traverse through given price array
    i = 0
    while (i < (n - 1)):
 
        # Find Local Minima
        # Note that the limit is (n-2) as we are
        # comparing present element to the next element
        while ((i < (n - 1)) and
                (price[i + 1] <= price[i])):
            i += 1
 
        # If we reached the end, break
        # as no further solution possible
        if (i == n - 1):
            break
 
        # Store the index of minima
        buy = i
        i += 1
 
        # Find Local Maxima
        # Note that the limit is (n-1) as we are
        # comparing to previous element
        while ((i < n) and (price[i] >= price[i - 1])):
            i += 1
 
        # Store the index of maxima
        sell = i - 1
 
        print("Buy on day: ", buy, "\t",
              "Sell on day: ", sell)
        print("Profit is: ", price[sell] - price[buy])
 
# Driver code
def best_trade(prices) -> int:
    """
    Single scan in O(n).
    """
    if not prices:
        return 0
    lowest = prices[0]
    best = 0
    for p in prices:
        lowest = min(p, lowest)
        best = max(best, p - lowest)
    return best

# Stock prices on consecutive days
price = [3, 22, 23, 4, 29, 20, 16, 7, 30, 40]
n = len(price)
 
# Function call
# stockBuySell(price, n)
print(best_trade(price))
 

###############

# def get_path_and_score(T):
#     n = len(T)
#     m = len(T[0])

#     # start from the end and backtrace to find biggest path
#     i = n-1
#     j = m-1
#     path = [[i,j]]
#     total_points = [T[i][j]]

#     while i > 0 and j > 0:
#         if T[i-1][j] >= T[i][j-1]:
#             i -= 1
#         else:
#             j -= 1
#         path.append([i, j])
#         total_points.append(T[i][j])
    
#     # Reversing the path
#     path.append([0, 0])
#     path.reverse()
    
#     # Reversing the points
#     for i in range(len(total_points)-1):
#         total_points[i] = total_points[i] - total_points[i+1]
#     total_points.append(T[0][0])
#     total_points[-2] = total_points[-2] - total_points[-1]
#     total_points.reverse()
#     return path, total_points

# def maximum_score(scores):
#   path = []
#   points = []
#   n = len(scores)
#   m = len(scores[0])
#   T = [[0] * m for _ in range(n)]
#   T[0][0] = scores[0][0]
#   for i in range(1, n):
#     T[i][0] = T[i-1][0] + scores[i][0]
#   for j in range(1, m):
#     T[0][j] = T[0][j-1] + scores[0][j]
#   for i in range(1, n):
#     for j in range(1, m):
#       T[i][j] = max(T[i-1][j], T[i][j-1]) + scores[i][j]
#       path.append([i, j])
#       points.append(scores[i][j])

#   print("T is ", T)
#   path, points = get_path_and_score(T, scores)
#   print("path is ", path)
#   print("points is ", points)
#   return T[n-1][m-1]

# q4_array = [[25,30,25],
#             [45,15,11],
#             [1,88,15],
#             [9,4,23]]

# print(maximum_score(q4_array))


############################

# # Iterative function to find the longest increasing subsequence of a given list
# def findLIS(arr):
 
#     # base case
#     if not arr:
#         return []
 
#     # LIS[i] stores the longest increasing subsequence of sublist
#     # `arr[0…i]` that ends with `arr[i]`
#     LIS = [[] for _ in range(len(arr))]
 
#     # LIS[0] denotes the longest increasing subsequence ending at `arr[0]`
#     LIS[0].append(arr[0])
 
#     # start from the second element in the list
#     for i in range(1, len(arr)):
 
#         # do for each element in sublist `arr[0…i-1]`
#         for j in range(i-1,i):
 
#             # find the longest increasing subsequence that ends with `arr[j]`
#             # where `arr[j]` is less than the current element `arr[i]`
 
#             if arr[j] < arr[i] and len(LIS[j]) > len(LIS[i]):
#                 LIS[i] = LIS[j].copy()
 
#         # include `arr[i]` in `LIS[i]`
#         LIS[i].append(arr[i])
 
#     # `j` will store the index of LIS
#     j = 0
#     for i in range(len(arr)):
#         if len(LIS[j]) < len(LIS[i]):
#             j = i
 
#     # print LIS
#     print(LIS[j])
 
 
# if __name__ == '__main__':
 
#     arr = [1, 4, 5, 2, 4, 3, 6, 7, 1, 2, 3, 4, 7]
#     findLIS(arr)