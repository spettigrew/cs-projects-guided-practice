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
- Preorder Traversal
--- Visit the root node first
--- Traverse the left subtree in preorder
--- Traverse the right subtree in preorder
- Inorder Traversal
--- Traverse the left subtree inorder first
--- Visit the root node
--- Traverse the right subtree inorder
- Postorder Traversal
--- Traverse the left subtree postorder first
--- Traverse the right subtree postorder
--- Visit the root node
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
- Preorder Traversal
--- Visit the root node first
--- Traverse the left subtree in preorder
--- Traverse the right subtree in preorder
- Inorder Traversal
--- Traverse the left subtree inorder first
--- Visit the root node
--- Traverse the right subtree inorder
- Postorder Traversal
--- Traverse the left subtree postorder first
--- Traverse the right subtree postorder
--- Visit the root node
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# go all the way down to left then back to root then right in iterative or
# recursive
# for recursive solution keep track of base case (when there is no root) and
# the recursive way
def inorder_traversal(root):
    # base case
    if root is None:
        return []
    # recursively call the function on the left child until no more left
    # children then the root will be none and the values are returned up the
    # chain inorder
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(
        root.right)


# the iterative way with a stack
# declare the stack and the result array
# stack = []
# result = []
# # if a left child exists add it onto the stack when no more left children
# # add the last root to the result
# # then go back to the previous root on the stack and add it and check if
# # it has right children, if so repeat steps on the right child as new root
# while root is not None or stack != []:
#     while root is not None:
#         stack.append(root)
#         root = root.left
#     root = stack.pop()
#     result.append(root.val)
#     root = root.right


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
   - Preorder Traversal
--- Visit the root node first
--- Traverse the left subtree in preorder
--- Traverse the right subtree in preorder
- Inorder Traversal
--- Traverse the left subtree inorder first
--- Visit the root node
--- Traverse the right subtree inorder
- Postorder Traversal
--- Traverse the left subtree postorder first
--- Traverse the right subtree postorder
--- Visit the root node
"""

preorder = [5, 7, 22, 13, 9]
inorder = [7, 5, 13, 22, 9]


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(preorder, inorder):
    # inorder (left -> right -> root ->)
    # preorder (root -> left -> right)
    # the absolute root will be preorder[0]
    # all items to the left of inorder[root] will be the left subtree
    # all items to the right of inorder[root] will be the right subtree

    # pick the next element in preorder starting with item[0]
    # create a new node with val set to the element
    # delete it from preorder
    # get the index of that element from inorder list using hashMaps to
    # reduce time complexity for finding the index
    # recursively call the function for elements in the left of the picked
    # element and assign it to the left of the picked node
    # recursively call the function for elements in teh right of hte picked
    # element and assign it to the right of hte picked node
    # return root node
    if inorder:
        root = TreeNode(preorder.pop(0))
        root_index = inorder.index(root.val)
        root.left = build_tree(preorder, inorder[:root_index])
        root.right = build_tree(preorder, inorder[root_index + 1:])
        return root


# print(build_tree(preorder, inorder))

"""
*** CodeSignal ***
------------------
"""
"""
You are given a binary tree. Write a function that returns the binary tree's node values using an in-order traversal.

Example:
Input: [2,None,3,4]

   2
    \
     3
    /
   4
Output: [2,4,3]
"""


#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def binaryTreeInOrderTraversal(root):
    stack = []
    result = []
    while root is not None or stack != []:
        while root is not None:
            stack.append(root)
            root = root.left
        root = stack.pop()
        result.append(root.value)
        root = root.right
    return result


"""
Note: Try to solve this task without using recursion, since this is what you'll be asked to do during an interview.

Given a binary tree of integers t, return its node values in the following format:

The first element should be the value of the tree root;
The next elements should be the values of the nodes at height 1 (i.e. the root children), ordered from the leftmost to the rightmost one;
The elements after that should be the values of the nodes at height 2 (i.e. the children of the nodes at height 1) ordered in the same way;
Etc.
Example

For

t = {
    "value": 1,
    "left": {
        "value": 2,
        "left": null,
        "right": {
            "value": 3,
            "left": null,
            "right": null
        }
    },
    "right": {
        "value": 4,
        "left": {
            "value": 5,
            "left": null,
            "right": null
        },
        "right": null
    }
}
the output should be
traverseTree(t) = [1, 2, 4, 3, 5].

This t looks like this:

     1
   /   \
  2     4
   \   /
    3 5
"""

t = {
    "value": 1,
    "left": {
        "value": 2,
        "left": None,
        "right": {
            "value": 3,
            "left": None,
            "right": None
        }
    },
    "right": {
        "value": 4,
        "left": {
            "value": 5,
            "left": None,
            "right": None
        },
        "right": None
    }
}


# ********* Breadth first

#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def traverseTree(t):
    queue = []
    result = []
    if t is None:
        return result
    root = t
    queue.append(root)
    while len(queue) > 0:
        root = queue.pop(0)
        result.append(root.value)
        if root.left is not None:
            queue.append(root.left)
        if root.right is not None:
            queue.append(root.right)

    return result


# print(traverseTree(t))


"""
Given a binary tree of integers, return all the paths from the tree's root to its leaves as an array of strings. The strings should have the following format:
"root->node1->node2->...->noden", representing the path from root to noden, where root is the value stored in the root and node1,node2,...,noden are the values stored in the 1st, 2nd,..., and nth nodes in the path respectively (noden representing the leaf).

Example

For

t = {
    "value": 5,
    "left": {
        "value": 2,
        "left": {
            "value": 10,
            "left": null,
            "right": null
        },
        "right": {
            "value": 4,
            "left": null,
            "right": null
        }
    },
    "right": {
        "value": -3,
        "left": null,
        "right": null
    }
}
the output should be
treePaths(t) = ["5->2->10", "5->2->4", "5->-3"].

The given tree looks like this:

    5
   / \
  2  -3
 / \
10  4
"""


#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def treePaths(t):
    if t is None:
        return []
    result, stack = [], [(t, '')]
    while stack:
        root, el = stack.pop()
        if root.left is None and root.right is None:
            result.append(el + str(root.value))
        if root.right:
            stack.append((root.right, el + str(root.value) + '->'))
        if root.left:
            stack.append((root.left, el + str(root.value) + '->'))
    return result


"""
Warm up
"""

"""
Challenge
Objective 2
* Represent a graph as an adjacency list and an adjacency matrix and compare 
    and contrast the respective  representations
- Using the graph shown in the picture above, write python code to represent 
  the graph in an adjacency list.
- Using the same graph you used for the first exercise, write python code to 
  represent the graph in an adjacency matrix.
Objective 3
*  Implement user-defined Vertex and Graph classes that allow basic operations
- Load the Vertex class and Graph class into an interactive Python environment and use the classes to create an instance of the graph shown below.
"""


# 1
class Graph:
    def __init__(self):
        self.vertices = {
            'A': {'B': 1},
            'B': {'C': 3, 'D': 2, 'E': 1},
            'C': {'E': 4},
            'D': {'E': 2},
            'E': {'F': 3},
            'F': {},
            'G': {'D': 1},
        }


# 2
class Graph:
    def __init__(self):
        self.edges = [
            [0, 1, 0, 0, 0, 0, 0],
            [0, 0, 3, 3, 1, 0, 0],
            [0, 0, 0, 0, 4, 0, 0],
            [0, 0, 0, 0, 2, 0, 0],
            [0, 0, 0, 0, 0, 3, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
        ]


# 3

class Vertex:
    def __init__(self, value):
        self.value = value
        self.connections = {}

    def __str__(self):
        return str(self.value) + ' connections: ' + str(
            [x.value for x in self.connections])

    def add_connection(self, vert, weight=0):
        self.connections[vert] = weight

    def get_connections(self):
        return self.connections.keys()

    def get_value(self):
        return self.value

    def get_weight(self, vert):
        return self.connections[vert]


class Graph:
    def __init__(self):
        self.vertices = {}
        self.count = 0

    def __contains__(self, vert):
        return vert in self.vertices

    def __iter__(self):
        return iter(self.vertices.values())

    def add_vertex(self, value):
        self.count += 1
        new_vert = Vertex(value)
        self.vertices[value] = new_vert
        return new_vert

    def add_edge(self, v1, v2, weight=0):
        if v1 not in self.vertices:
            self.add_vertex(v1)
        if v2 not in self.vertices:
            self.add_vertex(v2)
        self.vertices[v1].add_connection(self.vertices[v2], weight)

    def get_vertices(self):
        return self.vertices.keys()


g_verts = ['A', 'B', 'C', 'D', 'E']

g = Graph()
for v in g_verts:
    g.add_vertex(g)

g.add_edge('A', 'B', 1)
g.add_edge('B', 'C', 3)
g.add_edge('B', 'D', 2)
g.add_edge('E', 'D', 1)

# for v in g:
#     for w in v.get_connections():
#         print("( %s, %s )" % (v.get_value(), w.get_value()))


"""
Guided Project for Graphs I
"""

"""
*** Demo 1 ***
--------------
You are given an undirected graph with its maximum degree (the degree of a node
is the number of edges connected to the node).
You need to write a function that can take an undirected graph as its argument
and color the graph legally (a legal graph coloring is when no adjacent nodes
have the same color).
The number of colors necessary to complete a legal coloring is always one more
than the graph's maximum degree.
*Note: We can color a graph in linear time and space. Also, make sure that your
solution can handle a loop in a reasonable way.*
"""
# Definition for a graph node.
class GraphNode:
    def __init__(self, label):
        self.label = label
        self.neighbors = set()
        self.color = None

def color_graph(graph, colors):
    pass

"""
*** Demo 2 ***
--------------
You are given a 2d grid of `"1"`s and `"0"`s that represents a "map". The
`"1"`s represent land and the `"0"s` represent water.
You need to write a function that, given a "map" as an argument, counts the
number of islands. Islands are defined as adjacent pieces of land that are
connected horizontally or vertically. You can also assume that the edges of the
map are surrounded by water.
Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""
from collections import deque

def numIslands(grid):
    pass

