# Sorting Algorithms

Welcome to the Sorting Algorithms world, where you will explore various techniques for arranging elements in order. This module visualizes sorting algorithms as animated bar charts where elements physically move, swap, and merge, making the mechanics of each algorithm visually intuitive.

## Concept Overview

Sorting is the process of arranging elements in a specific order, typically ascending or descending. It's one of the most studied problems in computer science because sorted data enables efficient searching, simplifies many algorithms, and is fundamental to countless applications.

Different sorting algorithms have different characteristics. Some are simple but slow (O(n²)), while others are more complex but faster (O(n log n)). Some are stable (preserve relative order of equal elements), while others are not. Some work in-place (using O(1) extra space), while others require additional memory.

Bubble Sort repeatedly swaps adjacent elements if they're in the wrong order, "bubbling" large elements to the end. Selection Sort finds the minimum element and places it at the beginning, then repeats for the remaining elements. Insertion Sort builds the sorted array one element at a time by inserting each element into its correct position.

Merge Sort divides the array in half, recursively sorts each half, then merges them back together. Quick Sort selects a pivot element and partitions the array so elements smaller than the pivot come before it and larger elements come after, then recursively sorts the partitions.

## Learning Objectives

- Understand the mechanics of comparison-based sorting algorithms
- Implement bubble sort, selection sort, and insertion sort (O(n²) algorithms)
- Implement merge sort and quick sort (O(n log n) algorithms)
- Analyze time and space complexity of each algorithm
- Understand stability and when it matters

## The 3D Metaphor: Animated Bar Chart

**Array as Bar Chart**: Imagine a row of vertical bars, each bar's height representing an element's value. The bars are arranged on a platform, and sorting means rearranging them so heights increase from left to right.

**Bubble Sort**: Adjacent bars compare heights. If the left bar is taller, they swap positions with a hopping animation. Large bars "bubble" toward the right end through repeated swaps.

**Selection Sort**: A scanner moves through the unsorted portion, finding the shortest bar. That bar then slides to the beginning of the unsorted section, building the sorted portion from left to right.

**Insertion Sort**: Bars are picked up one at a time and inserted into their correct position in the sorted portion. The bar slides left until it finds its place, pushing other bars aside.

**Merge Sort**: The bar array splits in half repeatedly until single bars remain. Then pairs merge back together, with bars interleaving in sorted order. The merging animation shows two sorted groups combining.

**Quick Sort**: A pivot bar is selected and highlighted. Other bars partition around it: shorter bars slide left, taller bars slide right. The pivot drops into its final position, and the process recurses on each side.

## How This Maps to the 3D World

When you call `bubble_sort(arr)`, the visualization shows pairs of adjacent bars comparing and swapping. After each pass, the largest unsorted bar reaches its final position at the right end. The sorted portion grows from right to left.

When you call `merge_sort(arr)`, the visualization shows the array splitting into smaller pieces, then merging back together. The merge operation shows two sorted groups combining into one, with bars interleaving based on their heights.

When you call `quick_sort(arr)`, the visualization shows a pivot bar highlighted, then other bars moving to either side based on comparison with the pivot. The pivot then drops into its final sorted position.

## Exercises

1. **Sort Colors (Dutch National Flag)**: Given an array with values 0, 1, and 2, sort it in-place in a single pass. This is a variation of quick sort's partition step with three categories instead of two.

2. **Merge Intervals**: Given a collection of intervals, merge all overlapping intervals. First sort by start time, then merge adjacent intervals that overlap.

3. **Kth Largest Element**: Find the kth largest element in an unsorted array. Use quick select (a variation of quick sort's partition) to achieve O(n) average time complexity.
