# Heaps and Priority Queues

Welcome to the Heaps world, where you will explore a specialized tree structure that maintains a priority ordering. This module visualizes heaps as glowing pyramids where priority flows upward, making heap operations and the array-tree relationship intuitive.

## Concept Overview

A heap is a complete binary tree that satisfies the heap property. In a max-heap, every parent node is greater than or equal to its children, so the maximum element is always at the root. In a min-heap, every parent is less than or equal to its children, so the minimum is at the root.

The beauty of heaps lies in their efficient implementation using arrays. Because heaps are complete binary trees (filled level by level from left to right), we can store them in arrays without explicit pointers. For a node at index i, its left child is at 2i+1, right child at 2i+2, and parent at (i-1)//2.

Priority queues are abstract data types that provide efficient access to the highest (or lowest) priority element. Heaps are the most common implementation of priority queues, offering O(log n) insertion and extraction of the priority element, and O(1) access to peek at it.

Heaps are essential for algorithms like heap sort, Dijkstra's shortest path, Prim's minimum spanning tree, and for scheduling systems where tasks have different priorities.

## Learning Objectives

- Understand the heap property and the difference between min-heaps and max-heaps
- Implement heap operations: insert (with bubble-up) and extract (with bubble-down)
- Understand the array representation of heaps and index calculations
- Use Python's heapq module for priority queue operations
- Apply heaps to solve problems like finding k largest/smallest elements

## The 3D Metaphor: Glowing Pyramid with Priority Flow

**Heap as Pyramid**: Imagine a pyramid structure where each level represents a tier of priority. In a max-heap, the highest priority (largest value) sits at the apex, glowing brightest. Lower priority elements occupy lower tiers, with brightness decreasing as you descend. The pyramid shape emphasizes that there's only one element at the top.

**Array Ring**: Surrounding the pyramid base is a glowing ring representing the array storage. Lines connect each array position to its corresponding node in the pyramid, showing the index-to-node mapping. This dual visualization helps understand how the tree structure maps to linear storage.

**Bubble-Up Animation**: When inserting, a new element appears at the bottom of the pyramid and "bubbles up" through the levels, swapping with parents until it finds its correct position. The element glows brighter as it rises if it has higher priority.

**Bubble-Down Animation**: When extracting the root, the last element moves to the top and "bubbles down," swapping with the larger (max-heap) or smaller (min-heap) child until the heap property is restored.

## How This Maps to the 3D World

When you call `heap.insert(value)`, the visualization shows the value appearing at the next available position in the array ring, then rising through the pyramid as it compares with parents and swaps if necessary. The bubble-up path glows to show the insertion route.

When you call `heap.extract_max()` (or extract_min), the root element lifts off the pyramid apex, the last element teleports to the top, and then bubbles down through the structure. The extracted value floats away while the heap reorganizes.

When you call `heapify(array)`, the visualization shows the array transforming into a heap structure, with elements rearranging in a bottom-up fashion, starting from the last non-leaf node.

## Exercises

1. **Kth Largest Element**: Given an unsorted array and an integer k, find the kth largest element. Use a min-heap of size k to efficiently track the k largest elements seen so far. This is more efficient than sorting the entire array.

2. **Merge K Sorted Lists**: Given k sorted linked lists, merge them into one sorted list. Use a min-heap to always extract the smallest element among the k list heads, achieving O(n log k) time complexity.

3. **Task Scheduler**: Given tasks with cooldown periods, find the minimum time to complete all tasks. Use a max-heap to always schedule the most frequent task first, maximizing efficiency.
