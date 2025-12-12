# Dynamic Programming

Welcome to the Dynamic Programming world, where you will explore techniques for solving complex problems by breaking them into overlapping subproblems. This module visualizes DP as a grid of tiles that light up as values are computed, showing how solutions build upon previously calculated results.

## Concept Overview

Dynamic Programming (DP) is an optimization technique that solves problems by combining solutions to overlapping subproblems. Unlike divide-and-conquer which solves independent subproblems, DP recognizes when the same subproblem appears multiple times and stores its solution to avoid redundant computation.

DP works when a problem has two key properties: optimal substructure (an optimal solution contains optimal solutions to subproblems) and overlapping subproblems (the same subproblems are solved multiple times in a naive recursive approach).

There are two main approaches to DP. Top-down (memoization) starts with the original problem and recursively breaks it down, caching results as they're computed. Bottom-up (tabulation) builds solutions from the smallest subproblems up to the original problem, filling a table iteratively.

The Fibonacci sequence is the classic introduction to DP. A naive recursive solution has exponential time complexity because it recomputes the same values repeatedly. With memoization or tabulation, we achieve linear time by storing each Fibonacci number once.

The 0/1 Knapsack problem asks: given items with weights and values, maximize value while staying within a weight capacity. The DP solution builds a 2D table where each cell represents the maximum value achievable with a subset of items and a given capacity.

Longest Common Subsequence (LCS) finds the longest sequence that appears in both strings (not necessarily contiguous). The DP table tracks the LCS length for each prefix pair, building the solution character by character.

## Learning Objectives

- Understand the principles of dynamic programming: optimal substructure and overlapping subproblems
- Implement both top-down (memoization) and bottom-up (tabulation) approaches
- Solve classic DP problems: Fibonacci, knapsack, LCS, LIS
- Analyze time and space complexity of DP solutions
- Recognize when DP is applicable versus greedy or other approaches

## The 3D Metaphor: Illuminating Grid

**DP Table as Grid**: Imagine a 2D grid of tiles on a platform. Each tile represents a subproblem. As the algorithm progresses, tiles light up when their values are computed. The final answer glows brightest in the corner.

**Memoization (Top-Down)**: Starting from the target tile, the algorithm recursively explores dependencies. Tiles light up in the order they're first computed, showing the recursive call pattern. Already-computed tiles glow immediately when revisited.

**Tabulation (Bottom-Up)**: Tiles fill systematically from one corner, row by row or column by column. Each tile's value depends on previously lit neighbors. The progression shows how small solutions combine into larger ones.

**Dependency Arrows**: Glowing arrows connect each tile to the tiles it depends on. For Fibonacci, each tile points to the two previous tiles. For LCS, diagonal arrows show character matches while horizontal/vertical arrows show skips.

**Optimal Path**: Once the table is complete, the optimal solution path lights up, tracing back through the decisions that led to the answer.

## How This Maps to the 3D World

When you call `fibonacci_memo(n)`, the visualization shows a 1D row of tiles. The recursive calls light up tiles in a tree-like pattern, but cached values prevent redundant computation. The final tile glows with the answer.

When you call `knapsack_dp(weights, values, capacity)`, the visualization shows a 2D grid where rows represent items and columns represent capacities. Each tile lights up showing the maximum value achievable, with arrows indicating whether the item was included or excluded.

When you call `lcs_dp(str1, str2)`, the visualization shows a grid where rows and columns represent characters. Diagonal arrows show matches, and the path through the grid reveals the longest common subsequence.

## Exercises

1. **Climbing Stairs**: You can climb 1 or 2 steps at a time. How many distinct ways can you climb n stairs? This is essentially Fibonacci with a different framing.

2. **Coin Change (Minimum Coins)**: Given coin denominations and a target amount, find the minimum number of coins needed. Unlike the greedy approach, DP guarantees the optimal solution for any denomination set.

3. **Edit Distance**: Find the minimum number of operations (insert, delete, replace) to transform one string into another. The DP table tracks the edit distance for each prefix pair.
