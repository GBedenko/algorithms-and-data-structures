'''BinaryTree data structure, includes in order and post order traversals and the tree sort algorithm'''


class BinaryTreeNode():
    """BinaryTree is represented as BinaryTreeNodes linked together. No object for the entire
       tree, but works as a collection of nodes linked in a tree structure"""

    def __init__(self, value):
        '''BinaryTree works as a node which has a value,
           and can have a left child or right child or both'''

        self.value=value
        self.left=None
        self.right=None


def tree_insert(tree, item):
    '''Tree insert is a function that inserts a node at the correct position for the
       given binary tree'''

    # If the tree has no node, enter the item here
    if tree==None:
        tree=BinaryTreeNode(item)

    # Otherwise, look at child nodes
    else:

        # If the item is smaller than the node's value, go to the left subtree
        if item < tree.value:

            # If left child is empty, enter the item here
            if tree.left==None:
                tree.left=BinaryTreeNode(item)

            # Otherwise, run the insert function again with the left subtree being the root node
            else:
                tree_insert(tree.left,item)

        # If the item is larger than the node's value, go to the right subtree
        else:

            # If left child is empty, enter the item here
            if tree.right==None:
                tree.right=BinaryTreeNode(item)

            # Otherwise, run the insert function again with the right subtree being the root node
            else:
                tree_insert(tree.right,item)

    return tree


def output_post_order(tree):
    '''Displays the tree in order of following the left child, following the right child,
       then displaying the node'''

    # If there is a node on the left subtree, run the function for the left child
    if tree.left != None:
        output_post_order(tree.left)

    # If there is a node on the right subtree, run the function for the right child
    if tree.right != None:
        output_post_order(tree.right)

    # Once there is no child to display, output the node itself
    print(tree.value)


def output_in_order(tree):
    '''Displays the tree in order of left child, the node itself, then the right child
       When following the left or right child, follow the same instruction
       Function is done iteratively as per requirement'''

    stack = [] # Create a stack to add values to

    traversed = False

    # While the tree has not been completely traversed
    while traversed == False:

      # If current node has a value
      if tree != None:

        stack.append(tree) # Add the value to the stack
        tree = tree.left # Next iteration will use left child as the current node

      # If the node doesn't have a value, it has reached the end
      else:

        # If the stack has a value
        if len(stack) > 0:

          tree = stack.pop() # Go back to the last value
          print(tree.value) # Print out the value

          tree = tree.right # Next tree node is the right child

        # If the stack doesnt have anything in it
        else:
          traversed = True


def tree_sort(values_list):
    '''Builds a binary search tree from a given list of values
       Then traverses the binary tree to display the values in order'''

    # Creates the tree with the first value as the first node
    tree = tree_insert(None,values_list[0])

    # For each value in the list, insert it to the binary tree
    for i in range(1, len(values_list)):
        tree_insert(tree, values_list[i])

    # Traverse and output the tree using output_in_order
    output_in_order(tree)


if __name__ == '__main__':

    t = tree_insert(None,6)
    tree_insert(t,10)
    tree_insert(t,5)
    tree_insert(t,2)
    tree_insert(t,3)
    tree_insert(t,4)
    tree_insert(t,11)

    print("The first tree displayed in order is:")
    output_in_order(t)
    print(" ")

    print("The first tree displayed postorder is:")
    output_post_order(t)
    print(" ")

    print("The tree_sort tree displayed is:")
    random_list = [5,2,4,3,9,8,11,12,20,1]
    tree_sort(random_list)
