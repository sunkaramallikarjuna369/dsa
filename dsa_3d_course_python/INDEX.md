# Data Structures & Algorithms with 3D Visualizations (Python)

Welcome to the complete DSA learning experience with 360-degree interactive 3D visualizations. This course covers fundamental to advanced data structures and algorithms, each presented as an immersive "world" with visual metaphors designed to make abstract concepts tangible and memorable.

## Course Overview

This course is designed for learners who want to deeply understand data structures and algorithms through visual, interactive learning. Each world contains:

- **README.md**: Concept overview, learning objectives, and exercises
- **visual_design.md**: 3D environment specifications and visual metaphors
- **prompts_for_3d_generator.md**: Ready-to-use prompts for 3D scene generation
- **python/**: Modern Python implementations with visualization step tracking

All Python code uses Python 3.12+ features including type hints, dataclasses, and comprehensive docstrings.

---

## Learning Path

### Foundation (Worlds 1-4)

These worlds establish the fundamental concepts that everything else builds upon.

#### World 1: Time Complexity and Recursion
**Folder**: [01_time_complexity_and_recursion](./01_time_complexity_and_recursion/README.md)

**Estimated Time**: 3-4 hours

**Topics**: Big O notation, complexity classes (O(1), O(log n), O(n), O(n log n), O(n²)), recursion mechanics, call stack visualization, recursive vs iterative solutions.

**3D Metaphor**: A cosmic observatory where different complexity classes are represented as celestial bodies at varying distances, and recursion is visualized as nested portals.

---

#### World 2: Arrays and Strings
**Folder**: [02_arrays_and_strings](./02_arrays_and_strings/README.md)

**Estimated Time**: 4-5 hours

**Topics**: Array indexing, iteration patterns, two-pointer technique, sliding window, string operations, in-place modifications.

**3D Metaphor**: A circular corridor with numbered floor tiles representing indices, floating cubes as element values, and a scanning spotlight for iteration.

---

#### World 3: Linked Lists
**Folder**: [03_linked_lists](./03_linked_lists/README.md)

**Estimated Time**: 3-4 hours

**Topics**: Node structure, singly and doubly linked lists, insertion, deletion, traversal, cycle detection, list reversal.

**3D Metaphor**: Floating nodes connected by glowing chains in space, with operations shown as chain manipulation.

---

#### World 4: Stacks and Queues
**Folder**: [04_stacks_and_queues](./04_stacks_and_queues/README.md)

**Estimated Time**: 3-4 hours

**Topics**: LIFO and FIFO principles, push/pop operations, stack applications (expression evaluation, backtracking), queue applications (BFS, scheduling).

**3D Metaphor**: Stacks as glowing plates that can only be added/removed from the top; queues as elevator lobbies with people entering and exiting.

---

### Core Data Structures (Worlds 5-8)

These worlds cover essential data structures used in most software applications.

#### World 5: Hashing and Sets/Maps
**Folder**: [05_hashing_and_sets_maps](./05_hashing_and_sets_maps/README.md)

**Estimated Time**: 4-5 hours

**Topics**: Hash functions, collision handling (chaining, open addressing), load factor, hash maps, hash sets, frequency counting.

**3D Metaphor**: A honeycomb grid of glowing buckets, with collisions shown as chains extending from buckets or probing paths along the grid.

---

#### World 6: Trees and Binary Search Trees
**Folder**: [06_trees_and_bst](./06_trees_and_bst/README.md)

**Estimated Time**: 5-6 hours

**Topics**: Binary trees, BST properties, insertion, deletion, traversals (in-order, pre-order, post-order, level-order), tree balancing concepts.

**3D Metaphor**: A branching structure with root at top, children extending downward, and traversals shown as glowing paths through the tree.

---

#### World 7: Heaps and Priority Queues
**Folder**: [07_heaps_and_priority_queues](./07_heaps_and_priority_queues/README.md)

**Estimated Time**: 3-4 hours

**Topics**: Min-heap and max-heap properties, heap operations (insert, extract, heapify), priority queue applications, heap sort.

**3D Metaphor**: A glowing pyramid where priority flows upward, with the array representation shown as a ring around the base.

---

#### World 8: Graphs and Traversals
**Folder**: [08_graphs_and_traversals](./08_graphs_and_traversals/README.md)

**Estimated Time**: 5-6 hours

**Topics**: Graph representations (adjacency list, matrix), BFS, DFS, connected components, cycle detection, topological sort.

**3D Metaphor**: Floating cities (nodes) connected by glowing roads (edges), with BFS as an expanding wavefront and DFS as a single diving path.

---

### Algorithms (Worlds 9-13)

These worlds cover fundamental algorithmic techniques and problem-solving strategies.

#### World 9: Searching Algorithms
**Folder**: [09_searching_algorithms](./09_searching_algorithms/README.md)

**Estimated Time**: 3-4 hours

**Topics**: Linear search, binary search (iterative and recursive), search in rotated arrays, search in BST.

**3D Metaphor**: Linear search as a spotlight scanning a corridor; binary search as repeatedly splitting a tunnel into halves.

---

#### World 10: Sorting Algorithms
**Folder**: [10_sorting_algorithms](./10_sorting_algorithms/README.md)

**Estimated Time**: 5-6 hours

**Topics**: Bubble sort, insertion sort, selection sort, merge sort, quick sort, counting sort, comparison of algorithms.

**3D Metaphor**: Array elements as 3D bars with varying heights, with each algorithm having a distinct motion pattern (swapping, sliding, splitting, pivoting).

---

#### World 11: Greedy Algorithms
**Folder**: [11_greedy_algorithms](./11_greedy_algorithms/README.md)

**Estimated Time**: 4-5 hours

**Topics**: Greedy choice property, activity selection, interval scheduling, coin change (greedy approach), Huffman coding concepts.

**3D Metaphor**: Selecting coins from a floating cloud, choosing shortest glowing edges for MST, activity bars on a timeline.

---

#### World 12: Dynamic Programming
**Folder**: [12_dynamic_programming](./12_dynamic_programming/README.md)

**Estimated Time**: 6-8 hours

**Topics**: Optimal substructure, overlapping subproblems, memoization vs tabulation, classic problems (Fibonacci, knapsack, LCS, LIS, edit distance).

**3D Metaphor**: A grid of tiles that light up as values are computed, with dependency arrows showing how solutions build on subproblems.

---

#### World 13: Backtracking
**Folder**: [13_backtracking](./13_backtracking/README.md)

**Estimated Time**: 4-5 hours

**Topics**: Choose-explore-unchoose pattern, N-Queens, subset generation, permutation generation, maze solving, Sudoku.

**3D Metaphor**: A branching maze where paths light up when explored and dim when backtracked, with pruning shown as red-marked dead ends.

---

### Advanced Topics (World 14)

This world covers specialized data structures for specific problem domains.

#### World 14: Advanced Structures (Tries, Segment Trees, Fenwick Trees)
**Folder**: [14_advanced_structures_tries_segment_fenwick](./14_advanced_structures_tries_segment_fenwick/README.md)

**Estimated Time**: 6-8 hours

**Topics**: Trie (prefix tree) for string operations, Segment Tree for range queries, Fenwick Tree (BIT) for prefix sums.

**3D Metaphor**: Trie as branching word paths, Segment Tree as a pyramid over an array, Fenwick Tree as binary-indexed connections.

---

## Recommended Study Order

For beginners, follow the worlds in numerical order. For those with some experience:

1. **Quick Review Path** (if you know basics): Start with World 5, then 6-8, then 9-14
2. **Algorithm Focus Path**: Worlds 1, 9-13, then backfill data structures as needed
3. **Interview Prep Path**: Worlds 2, 3, 6, 8, 10, 12, 13 (most common interview topics)

## Total Estimated Time

- **Complete Course**: 55-70 hours
- **Foundation + Core**: 30-40 hours
- **Algorithms Only**: 25-35 hours

## How to Use This Course

1. **Read the README.md** for each world to understand concepts
2. **Study visual_design.md** to understand the 3D metaphors
3. **Run the Python implementations** to see algorithms in action
4. **Complete the exercises** in exercises.py
5. **Use prompts_for_3d_generator.md** to create interactive visualizations

## Prerequisites

- Python 3.12 or higher
- Basic programming knowledge
- No external libraries required (standard library only)

## Running the Code

Each world's Python folder contains runnable demos:

```bash
cd 01_time_complexity_and_recursion/python
python recursion.py
```

Run exercises to test your implementations:

```bash
python exercises.py
```

## Future Extensions

This course structure is designed to integrate with:
- WebGL/Three.js 3D renderers
- PyOpenGL visualizations
- Interactive web frontends
- VR/AR learning experiences

The prompts_for_3d_generator.md files provide detailed specifications for building these integrations.

---

Happy learning! May your algorithms be efficient and your data structures well-organized.
