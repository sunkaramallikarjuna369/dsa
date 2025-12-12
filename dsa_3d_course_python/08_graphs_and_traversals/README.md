# Graphs and Traversals

Welcome to the Graphs world, where you will explore one of the most versatile data structures in computer science. This module visualizes graphs as floating nodes connected by glowing edges in 3D space, making traversal algorithms and graph properties intuitive to understand.

## Concept Overview

A graph is a collection of vertices (nodes) connected by edges. Unlike trees, graphs can have cycles, multiple paths between nodes, and nodes with any number of connections. Graphs model countless real-world scenarios: social networks (people connected by friendships), road maps (cities connected by roads), web pages (pages connected by links), and dependencies (tasks connected by prerequisites).

Graphs come in two main varieties. In directed graphs, edges have a direction (like one-way streets), while in undirected graphs, edges work both ways. Edges can also have weights representing costs, distances, or capacities.

Two common ways to represent graphs are adjacency lists (each node stores a list of its neighbors) and adjacency matrices (a 2D grid where entry [i][j] indicates an edge from node i to node j). Adjacency lists are more space-efficient for sparse graphs, while matrices allow O(1) edge lookup.

Graph traversal algorithms systematically visit all nodes. Breadth-First Search (BFS) explores level by level, like ripples spreading from a stone dropped in water. Depth-First Search (DFS) explores as deep as possible before backtracking, like navigating a maze by always taking the first available path.

## Learning Objectives

- Understand graph terminology: vertices, edges, directed vs undirected, weighted vs unweighted
- Implement graphs using adjacency lists and adjacency matrices
- Master BFS traversal and understand its level-by-level exploration pattern
- Master DFS traversal and understand its depth-first exploration pattern
- Apply graph traversals to solve problems like finding connected components and shortest paths

## The 3D Metaphor: Floating Cities Connected by Roads

**Graph as City Network**: Imagine a 3D space filled with floating cities (nodes) connected by glowing roads (edges). Each city is a sphere with a label, and roads are beams of light connecting them. The camera can orbit around this network, zoom into specific cities, or follow traversal paths.

**BFS as Expanding Wavefront**: When BFS starts from a source city, a wave of light expands outward, illuminating cities level by level. First the source glows, then all its direct neighbors, then their neighbors, and so on. The wavefront shows the "distance" from the source.

**DFS as Deep Exploration**: When DFS starts, a single beam of light dives deep into the network, following one path until it hits a dead end, then backtracking to explore other branches. The path glows as it's explored and dims when backtracked.

**Directed Edges**: For directed graphs, roads have arrow indicators showing the allowed direction of travel. Attempting to traverse against the arrow is blocked.

## How This Maps to the 3D World

When you call `graph.add_edge(u, v)`, a glowing beam connects city u to city v. For undirected graphs, the beam glows equally in both directions. For directed graphs, an arrow appears pointing from u to v.

When you call `bfs(graph, start)`, the visualization shows waves emanating from the start city. Each wave represents one level of BFS, with cities lighting up as they're discovered. The queue of cities to visit is shown as a line of highlighted nodes.

When you call `dfs(graph, start)`, a single exploration beam leaves the start city and dives deep into the network. When it backtracks, the beam retraces its path before branching to unexplored neighbors. The recursion stack is visualized as a glowing trail.

When finding connected components, each component lights up in a different color, showing which cities can reach each other.

## Exercises

1. **Number of Islands**: Given a 2D grid of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and formed by connecting adjacent lands horizontally or vertically. Use BFS or DFS to explore each island.

2. **Clone Graph**: Given a reference to a node in a connected undirected graph, return a deep copy of the graph. Each node contains a value and a list of neighbors. Use BFS or DFS to traverse and clone.

3. **Course Schedule**: Given n courses and prerequisites as pairs [a, b] meaning you must take course b before course a, determine if you can finish all courses. This is cycle detection in a directed graph.
