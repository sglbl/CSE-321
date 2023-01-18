@SuppressWarnings("unchecked")
public class BTtoBST<E extends Comparable<E>> {

    /**
     * To traverse the array items
     */
    private static int index = 0;

    /**
     * The method should build a binary search tree of n nodes
     * @param bt The structure of the binary search tree should be same as the structure of the binary tree
     * @param items The binary search tree should contain the items
     * @return binary search tree (BST) as output
     */
    public BinaryTree<E> generateBST(BinaryTree<E> bt, E [] items){

        if(bt != null) {
            BinaryTree.Node<E> temp = bt.root;
            sortArray(items);
            sortedArrayToBST(items, temp);
            temp = bt.root;
            System.out.println("\n\n----------After converting from binary tree to binary search tree(inorder traversal)---------\n");
            printInorder(temp);
            System.out.println("\n");
        }
        else
            System.out.println("\nThere is no structure to put elements...\n");

        return bt;
    }

    /**
     * Given a binary tree, print its nodes in inorder
     * @param node root node
     */
    public void printInorder(BinaryTree.Node<E> node) {
        if (node == null) return;

        /* first recur on left child */
        printInorder(node.left);

        /* then print the data of node */
        System.out.print(node.data + " ");

        /* now recur on right child */
        printInorder(node.right);
    }

    /**
     * sorts array
     * @param items array that will sorted
     */
    private void sortArray(E [] items){

        E temp;
        for (int i = 1; i < items.length; i++) {
            for (int j = i; j > 0; j--) {
                if (items[j].compareTo(items [j-1]) < 0) {
                    temp = items[j];
                    items[j] = items[j - 1];
                    items[j - 1] = temp;
                }
            }
        }
    }

    /**
     * inorder traversing
     * @param items items array
     * @param root root of binary tree
     */
    private void sortedArrayToBST(E [] items, BinaryTree.Node<E> root) {

        if(root == null) return;

        sortedArrayToBST(items, root.left);
        putTree(root, items);
        sortedArrayToBST(items, root.right);
    }

    /**
     * Puts array elements into binary search tree by inorder traversing
     * @param root root node
     * @param items items array
     */
    private void putTree(BinaryTree.Node<E> root, E [] items){

        root.data = items[index];
        index++;
    }
}