"""
Week Binary search tree 5 warm up
"""
"""
*** Objective 1 Challenge ***
-----------------
- Calculate how many levels a perfect binary tree has given that the total 

number of nodes is 127.
log2(n + 1) = h
# log2 is 2**(? + 1) = h
log2(128) = h
2**7 = 128
7 <~~ answer

- Calculate the total number of nodes on a perfect binary tree, given that 
  the height of the tree is 8.
  
n = 2h - 1
n = 2**8 - 1
n = 256 - 1
n = 255 <~~ answer
"""

"""
*** Objective 2 Challenge *** 
-----------------------------
- In your own words, explain why an unbalanced binary search tree's 
performance becomes degraded.
The worst case performance is linear because each node would potentially need to be traversed
"""

"""
Challenge
To implement a delete operation on our BST and BSTNode classes, we must consider three cases:

If the BSTNode to be deleted is a leaf (has no children), we can remove that node from the tree.
If the BSTNode to be deleted has only one child, we copy the child node to be deleted and delete it.
If the BSTNode to be deleted has two children, we have to find the "in-order successor". The "in-order successor" is the next highest value, the node that has the minimum value in the right subtree.
Given the above information, can you write pseudocode for a method that can find the minimum value of all the nodes within a tree or subtree?

- search for the node to find its place in the tree and make sure it exists
- set the parents pointer to it to None if it has no children and set the 
root to none if it is the root node
- if the node has 1 child set the value to its child value and set its 
pointer to none
- find successor or predecessor and copy the value of it to the 
node to be deleted and then we can delete the successor or predecessor
"""


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    def search(self, target):
        if self.value == target:
            return self.value
        elif target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.search(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.search(target)


class BST:
    def __init__(self, value):
        self.root = BSTNode(value)

    def insert(self, value):
        self.root.insert(value)

    def search(self, target):
        self.root.search(target)


"""
*** Binary Search Tree Guided ***
---------------------------------
"""

"""
*** Demo 1 ***
--------------
You are given a binary tree.
Write a function that can find the **maximum depth** of the binary tree. The
maximum depth can be defined as the number of nodes found along the longest
path from the root down to the furthest leaf node. Remember, a leaf node is a
node that has no children.
Example:
Given the following binary tree
    5
   / \
  12  32
     /  \
    8    4
your function should return the depth = 3.
"""


class BinaryTreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def maxDepth(self, root):
    # if root is None return 0
    if root is None:
        return 0
    # if root exists get the left depth and the right depth by recursively
    # calling maxDepth on each side of the subtree
    left_depth = self.maxDepth(root.left)
    right_depth = self.maxDepth(root.right)
    # if the left depth is greater than the right depth return the left depth
    # plus 1
    if left_depth > right_depth:
        return left_depth + 1
    else:
        # else return right depth plus 1
        return right_depth + 1


"""
*** Demo 2 ***
--------------

You are given a binary tree. You need to write a function that can determine if
it is a valid binary search tree.
The rules for a valid binary search tree are:
- The node's left subtree only contains nodes with values less than the node's
value.
- The node's right subtree only contains nodes with values greater than the
node's value.
- Both the left and right subtrees must also be valid binary search trees.
Example 1:
Input:
    5
   / \
  3   7
Output: True
Example 2:
Input:
    10
   / \
  2   8
     / \
    6  12
Output: False
Explanation: The root node's value is 10 but its right child's value is 8.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def is_valid_BST(self, root):
    # if there is no root return False
    if root is None:
        return True
    # traverse the tree to make sure it is valid
    else:
        if root.left is None and root.right is None:
            return True
        elif root.left is None:
            if root.right > root:
                self.is_valid_BST(self, root.right)
            else:
                # if a right node is greater than a parent return false
                return False
        # if the left child is less than parent traverse that subtree
        elif root.right is None:
            if root.left < root:
                self.is_valid_BST(self, root.left)
            else:
                # if a left node is greater than parent return false
                return False
        # if the right child is greater than parent traverse the right subtree

    # if we never get a false condition the tree is valid so return true
    return True


"""
*** Codesignal Project ***
--------------------------
"""

"""
You are given a binary tree and you need to write a function that can determine if it is height-balanced.

A height-balanced tree can be defined as a binary tree in which the left and right subtrees of every node differ in height by a maximum of 1.

Example 1:
Given the following tree [5,10,25,None,None,12,3]:

    5
   / \
 10  25
    /  \
   12   3
return True.

Example 2:
Given the following tree [5,6,6,7,7,None,None,8,8]:

       5
      / \
     6   6
    / \
   7   7
  / \
 8   8
return False.

[execution time limit] 4 seconds (py3)

[input] tree.integer root

[output] boolean
"""


#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def balancedBinaryTree(root):
    # define method to get the height of the tree
    def get_height(root):
        if root is None:
            return 0
        return max(get_height(root.left), get_height(root.right)) + 1

    # if the root is None return True
    if root is None:
        return True
    # get the heights of each subtree
    left_height = get_height(root.left)
    right_height = get_height(root.right)
    # if the absolute value of left subtree - right subtree is less than or
    # equal to 1 and left tree is balanced and right tree is balanced then
    # the whole tree is balanced
    if (abs(left_height - right_height) <= 1) and balancedBinaryTree(
            root.left) is True and balancedBinaryTree(root.right) is True:
        return True
    return False

"""
You are given a binary tree and you are asked to write a function that finds its minimum depth. The minimum depth can be defined as the number of nodes along the shortest path from the root down to the nearest leaf node. As a reminder, a leaf node is a node with no children.

Example:
Given the binary tree [5,7,22,None,None,17,9],

    5
   / \
  7  22
    /  \
   17   9
your function should return its minimum depth = 2.

[execution time limit] 4 seconds (py3)

[input] tree.integer root

[output] integer
"""

def minimumDepthBinaryTree(root):
    # if root is None return 0
    if root is None:
        return 0
    # if root has no children return 1
    if root.left is None and root.right is None:
        return 1

    # if no left child traverse the right tree
    if root.left is None:
        return minimumDepthBinaryTree(root.right) + 1
    # if not right child traverse the left sree
    if root.right is None:
        return minimumDepthBinaryTree(root.left) + 1

    # return the minimum depth after recursion
    return min(minimumDepthBinaryTree(root.left), minimumDepthBinaryTree(
        root.right)) + 1

""""
week 5 Tree traversal Warm up
"""

"""
Depth first inorder traversal 
"""

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def helper(root, res):
    if root is None:
        return
    helper(root.left, res)
    res.append(root.val)
    helper(root.right, res)

def inorder_traversal(root):
    result = []
    helper(root, result)
    return result

"""
Depth first pre-order traversal
"""

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def helper(root, res):
    if root is None:
        return
    res.append(root.val)
    helper(root.left, res)
    helper(root.right, res)

def preorder_traversal(root):
    result = []
    helper(root, result)
    return result

"""
Depth first  first post-order traversal
"""

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def helper(root, res):
    if root is None:
        return
    helper(root.left, res)
    helper(root.right, res)
    res.append(root.val)

def postorder_traversal(root):
    result = []
    helper(root, result)
    return result

"""
Breadth first level order traversal
"""

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def breadth_first_traversal(root):
    if root is None:
        return []

    result = []
    queue = []
    queue.append(root)

    while len(queue) != 0:
        node = queue.pop(0)
        result.append(node.val)

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)

    return result


"""
*** Challenge ***
-----------------
What data structure could you use to write an iterative depth-first traversal method?
-- a binary tree
In your own words, explain how a depth-first traversal and a breadth-first traversal are different?
-- depth first traversal uses recursion to visit the length of the tree and 
returns the node of left subtree and then right subtree whereas breadth first traversal uses a queue to remember the visited nodes while checking a level at a time down the height of both subtrees together 
"""


"""
*** Tree traversal Guided ***
---------------------------------
"""

"""
*** Demo 1 ***
--------------
You are given a binary tree.
Write a function that can return the inorder traversal of node values.
Example:
Input:
   3
    \
     1
    /
   5
Output: [3,5,1]
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(root):
    pass

"""
*** Demo 2 ***
--------------
You are given the values from a preorder and an inorder tree traversal. Write a
function that can take those inputs and output a binary tree.
*Note: assume that there will not be any duplicates in the tree.*
Example:
Inputs:
preorder = [5,7,22,13,9]
inorder = [7,5,13,22,9]
Output:
    5
   / \
  7  22
    /  \
   13   9
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(preorder, inorder):
    pass
