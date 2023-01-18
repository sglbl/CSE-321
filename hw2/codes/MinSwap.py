# Python3 program for Minimum swap required
# to convert binary tree to binary search tree
 
# Inorder Traversal of Binary Tree
def inorder(a, n, index):
     
    global v
     
    # If index is greater or equal to
    # vector size
    if (index >= n):
        return
     
    inorder(a, n, 2 * index + 1)
 
    # Push elements in vector
    v.append(a[index])
    inorder(a, n, 2 * index + 2)
 
# Function to find minimum swaps
# to sort an array
def minSwaps():
     
    global v
    t = [[0, 0] for i in range(len(v))]
    ans = -2
 
    for i in range(len(v)):
        t[i][0], t[i][1] = v[i], i
 
    t, i = sorted(t), 0
 
    while i < len(t):
         
        # break
        # second element is equal to i
        if (i == t[i][1]):
            i += 1
            continue
        else:
             
            # Swapping of elements
            t[i][0], t[t[i][1]][0] = t[t[i][1]][0], t[i][0]
            t[i][1], t[t[i][1]][1] = t[t[i][1]][1], t[i][1]
 
        # Second is not equal to i
        if (i == t[i][1]):
            i -= 1
 
        i += 1
 
        ans += 1
 
    return ans


# Print the inorder traversal of the tree
def printInorder(root):
    if root is None:
        return
    printInorder(root.left)
    print (root.data, end=" ")
    printInorder(root.right)
 
# Driver Code
if __name__ == '__main__':
     
    v = []
    a = [ 5, 6, 7, 8, 9, 10, 11 ]
    n = len(a)
    inorder(a, n, 0)
 
    print(minSwaps())
    # print(a)
    printInorder(a)
 
# This code is contributed by mohit kumar 29