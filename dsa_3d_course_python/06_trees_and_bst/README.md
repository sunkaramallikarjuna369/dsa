# Trees and Binary Search Trees

Welcome to the Trees world, where you will explore hierarchical data structures that branch out like real trees. This module visualizes binary trees as 3D branching structures with the root at the top and children extending downward, making tree operations and traversals intuitive.

## Concept Overview

Trees are hierarchical data structures consisting of nodes connected by edges. Unlike linear structures like arrays and linked lists, trees organize data in a parent-child relationship, enabling efficient searching, insertion, and deletion operations.

A binary tree is a tree where each node has at most two children, called the left child and right child. Binary trees form the foundation for many important data structures and algorithms.

A Binary Search Tree (BST) is a binary tree with an ordering property: for every node, all values in its left subtree are smaller, and all values in its right subtree are larger. This property enables O(log n) average-case operations for search, insert, and delete, making BSTs extremely useful for maintaining sorted data.

Tree traversals are systematic ways to visit all nodes. The four main traversals are in-order (left, root, right), pre-order (root, left, right), post-order (left, right, root), and level-order (breadth-first). Each traversal has different applications: in-order gives sorted output for BSTs, pre-order is useful for copying trees, and post-order is useful for deletion.

## Learning Objectives

- Understand the structure and terminology of binary trees (root, parent, child, leaf, height, depth)
- Implement a Binary Search Tree with insert, search, and delete operations
- Perform all four tree traversals and understand their applications
- Analyze the time complexity of BST operations in balanced vs unbalanced cases
- Understand the concept of tree balancing and why it matters for performance

## The 3D Metaphor: Branching Structure in Space

**Binary Tree as 3D Branches**: Imagine a tree growing downward from the ceiling. The root node is at the top, glowing brightly as the entry point. From each node, up to two branches extend downward to child nodes. Left children branch to the left, right children to the right. The spatial arrangement makes the tree structure immediately visible.

**BST Ordering**: In a BST visualization, smaller values glow with cool blue colors and larger values glow with warm orange colors. This color gradient makes the ordering property visible at a glance. An in-order traversal follows a path that visits nodes in color order from blue to orange.

**Traversal Paths**: Each traversal type is shown as a glowing path through the tree. In-order creates a zigzag pattern visiting left subtrees first. Pre-order creates a path that always visits the current node before descending. Post-order visits children before parents, useful for cleanup operations.

## How This Maps to the 3D World

When you call `bst.insert(value)`, the visualization shows a new node materializing and descending through the tree, comparing at each level and branching left or right until finding its position. The path taken glows to show the insertion route.

When you call `bst.search(value)`, a search beam travels from the root, branching left or right at each node based on comparisons. Found nodes glow green; if the search reaches a null position, a red indicator shows the value is not present.

When you call `bst.delete(value)`, the node is found and removed. The three cases (leaf, one child, two children) are visualized differently: leaves simply disappear, one-child nodes are bypassed, and two-child deletions show the in-order successor being found and swapped.

Traversals are animated as a glowing path that visits nodes in the specified order, with each visited node lighting up sequentially.

## Exercises

1. **Validate BST**: Given a binary tree, determine if it is a valid Binary Search Tree. Remember that all nodes in the left subtree must be less than the root, and all nodes in the right subtree must be greater. A common mistake is only checking immediate children.

2. **Lowest Common Ancestor**: Given a BST and two node values, find their lowest common ancestor (LCA). The LCA is the deepest node that has both values as descendants. Use the BST property to efficiently find the LCA without traversing the entire tree.

3. **Convert Sorted Array to BST**: Given a sorted array, create a height-balanced BST. A height-balanced tree has the minimum possible height, achieved by always choosing the middle element as the root of each subtree.
