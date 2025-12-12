# Searching Algorithms

Welcome to the Searching Algorithms world, where you will explore techniques for finding elements in data structures. This module visualizes search algorithms as spotlight beams scanning through arrays and trees, making the efficiency differences between linear and binary search immediately apparent.

## Concept Overview

Searching is one of the most fundamental operations in computer science. Given a collection of data, we want to determine whether a specific element exists and, if so, where it is located. The efficiency of search operations depends heavily on the structure of the data and the algorithm used.

Linear search is the simplest approach: examine each element one by one until you find the target or exhaust the collection. It works on any data, sorted or unsorted, but takes O(n) time in the worst case. For small datasets or unsorted data, linear search is often the practical choice.

Binary search is dramatically more efficient but requires sorted data. By repeatedly dividing the search space in half, binary search achieves O(log n) time complexity. Each comparison eliminates half of the remaining elements, making it incredibly fast even for large datasets. A billion-element sorted array requires at most 30 comparisons.

Search operations also apply to tree structures. In a Binary Search Tree, the BST property (left subtree contains smaller values, right subtree contains larger values) enables efficient O(log n) search by following the appropriate branch at each node.

Understanding when to use each search algorithm and how to implement them correctly is essential for writing efficient code.

## Learning Objectives

- Understand linear search and when it's appropriate to use
- Master binary search on sorted arrays (iterative and recursive implementations)
- Understand the O(log n) efficiency of binary search through visualization
- Apply binary search to solve problems beyond simple element lookup
- Connect array binary search to BST search operations

## The 3D Metaphor: Spotlight Scanning a Corridor

**Array as Corridor**: Imagine a long corridor with numbered tiles on the floor, each tile holding a glowing cube representing an element value. The corridor stretches into the distance, with values visible on each cube.

**Linear Search as Scanning Spotlight**: A spotlight starts at one end of the corridor and moves tile by tile, illuminating each element in sequence. The spotlight checks each value against the target, moving forward until it finds a match or reaches the end.

**Binary Search as Shrinking Corridor**: For sorted arrays, the corridor has values in ascending order. Instead of scanning, the search focuses on the middle tile first. Based on the comparison, half the corridor dims and becomes inaccessible. The remaining half is the new search space. This process repeats, with the active corridor shrinking by half each time until the target is found.

**BST Search as Tree Navigation**: In a tree visualization, the search follows a glowing path from root to target, choosing left or right at each node based on value comparison.

## How This Maps to the 3D World

When you call `linear_search(arr, target)`, the visualization shows a spotlight starting at index 0, moving right one position at a time. Each element is briefly illuminated as it's checked. When the target is found, that tile glows green. If not found, the spotlight reaches the end and dims.

When you call `binary_search(arr, target)`, the visualization shows the entire sorted corridor initially lit. The middle element is highlighted, compared with the target, and then half the corridor dims. The process repeats on the remaining half until the target is found or the search space is empty.

When you call `bst_search(root, target)`, the visualization shows a path descending through the tree. At each node, the comparison result determines whether to go left or right. The path glows as it's traversed, and the target node (if found) pulses with success.

## Exercises

1. **Search Insert Position**: Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be inserted to maintain sorted order. Use binary search for O(log n) efficiency.

2. **First and Last Position**: Given a sorted array with duplicates and a target value, find the starting and ending position of the target. If not found, return [-1, -1]. Use binary search to find both boundaries.

3. **Search in Rotated Sorted Array**: A sorted array has been rotated at some pivot. Given the rotated array and a target, find the index of the target or return -1. Modify binary search to handle the rotation.
