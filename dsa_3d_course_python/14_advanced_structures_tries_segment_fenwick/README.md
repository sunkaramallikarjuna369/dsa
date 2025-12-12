# Advanced Data Structures: Tries, Segment Trees, and Fenwick Trees

Welcome to the Advanced Data Structures world, where you will explore specialized tree structures designed for efficient string operations and range queries. This module visualizes Tries as branching word paths, Segment Trees as hierarchical range aggregators, and Fenwick Trees as efficient prefix sum calculators.

## Concept Overview

This world covers three powerful data structures that solve specific problems more efficiently than general-purpose structures.

**Trie (Prefix Tree)** is a tree-like structure for storing strings where each node represents a character. Words sharing common prefixes share the same path from the root. Tries enable O(m) search, insert, and prefix operations where m is the word length, regardless of how many words are stored.

**Segment Tree** is a binary tree where each node stores aggregate information (sum, min, max, etc.) about a range of elements. The root covers the entire array, and each node's children cover the left and right halves of the parent's range. This enables O(log n) range queries and point updates.

**Fenwick Tree (Binary Indexed Tree)** is a clever array-based structure that supports O(log n) prefix sum queries and point updates. It uses binary representation of indices to determine which elements contribute to each position, achieving the same complexity as segment trees with less memory and simpler implementation for certain operations.

These structures are essential for competitive programming, database indexing, autocomplete systems, and any application requiring fast range queries or string operations.

## Learning Objectives

- Understand Trie structure and implement insert, search, and prefix operations
- Build Segment Trees for range sum, min, and max queries
- Implement Fenwick Trees for prefix sums and point updates
- Compare trade-offs between Segment Trees and Fenwick Trees
- Apply these structures to solve real-world problems

## The 3D Metaphor: Layered Trees and Word Paths

**Trie as Word Paths**: Imagine a 3D tree where each branch is labeled with a character. Words are formed by following paths from root to marked endpoints. Common prefixes share the same initial path, then diverge. Searching for a word is like walking down a glowing path.

**Segment Tree as Range Pyramid**: Visualize a pyramid of nodes layered over an array. The bottom layer contains individual elements. Each higher layer aggregates pairs of nodes below. Queries travel up and down the pyramid, combining relevant ranges.

**Fenwick Tree as Binary Connections**: Picture an array where each position has invisible connections to specific previous positions based on binary patterns. Updates propagate through these connections, and queries accumulate values along connection paths.

## How This Maps to the 3D World

When you call `trie.insert("apple")`, the visualization shows characters being added as nodes along a path: root → 'a' → 'p' → 'p' → 'l' → 'e'. The final node is marked as a word endpoint.

When you call `segment_tree.range_sum(2, 5)`, the visualization highlights the minimal set of nodes that cover the range [2, 5]. Values from these nodes combine to produce the answer without examining every element.

When you call `fenwick.update(3, 5)`, the visualization shows the update propagating through positions determined by binary arithmetic. The affected positions light up in sequence.

## Exercises

1. **Implement Autocomplete**: Build a Trie that supports inserting words and returning all words with a given prefix. This is the foundation of search engine suggestions.

2. **Range Minimum Query**: Build a Segment Tree that answers "what is the minimum value in range [l, r]?" in O(log n) time with O(log n) updates.

3. **Count Inversions**: Use a Fenwick Tree to count inversions in an array (pairs where i < j but arr[i] > arr[j]) in O(n log n) time.
