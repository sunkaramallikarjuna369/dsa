# Greedy Algorithms

Welcome to the Greedy Algorithms world, where you will explore techniques that make locally optimal choices at each step with the hope of finding a global optimum. This module visualizes greedy decision-making as selecting the "best" option at each moment, like picking the brightest coin from a floating cloud or choosing the shortest glowing edge in a network.

## Concept Overview

A greedy algorithm builds a solution piece by piece, always choosing the next piece that offers the most immediate benefit. The key insight is that for certain problems, making the locally optimal choice at each step leads to a globally optimal solution.

Greedy algorithms work when a problem has two properties: the greedy choice property (a locally optimal choice leads to a globally optimal solution) and optimal substructure (an optimal solution contains optimal solutions to subproblems).

Activity Selection is a classic greedy problem: given a set of activities with start and end times, select the maximum number of non-overlapping activities. The greedy approach sorts by end time and always picks the activity that finishes earliest, leaving maximum room for subsequent activities.

The Coin Change problem (when greedy works) involves making change with the fewest coins. With standard denominations like [25, 10, 5, 1], always picking the largest coin that fits works perfectly. However, greedy fails for arbitrary denominations like [1, 3, 4] where making 6 cents greedily gives [4, 1, 1] (3 coins) instead of optimal [3, 3] (2 coins).

Huffman Coding builds an optimal prefix-free encoding by repeatedly combining the two lowest-frequency symbols. This greedy approach produces the most efficient variable-length encoding for data compression.

## Learning Objectives

- Understand when greedy algorithms produce optimal solutions
- Identify the greedy choice property and optimal substructure
- Implement activity selection and interval scheduling algorithms
- Understand Huffman coding for data compression
- Recognize problems where greedy fails and dynamic programming is needed

## The 3D Metaphor: Coin Cloud and Edge Selection

**Coin Cloud**: Imagine a floating cloud of glowing coins of different sizes (denominations). To make change, you reach into the cloud and grab the largest coin that doesn't exceed your remaining amount. The selected coins float down to form your solution pile.

**Activity Selection**: Activities are represented as horizontal bars on a timeline. The greedy algorithm scans from left to right, selecting bars that don't overlap with previously selected ones. Selected activities glow green while rejected ones fade to gray.

**Minimum Spanning Tree**: A network of floating cities connected by potential roads (edges) of varying lengths. The greedy algorithm (Kruskal's or Prim's) selects the shortest available edge that doesn't create a cycle, building a tree that connects all cities with minimum total distance.

**Huffman Tree**: Characters are weighted spheres that combine bottom-up. The two lightest spheres merge into a parent node, and this process repeats until a single tree remains. The tree structure determines the binary encoding for each character.

## How This Maps to the 3D World

When you call `activity_selection(activities)`, the visualization shows activities as bars on a timeline. The algorithm sorts by end time, then scans left to right. Each activity that doesn't conflict with the last selected one gets highlighted and added to the solution.

When you call `coin_change_greedy(amount, coins)`, the visualization shows a coin cloud. For each step, the largest valid coin glows brighter, gets selected, and floats down to the solution pile. The remaining amount updates until it reaches zero.

When you call `huffman_encoding(frequencies)`, the visualization shows weighted character nodes. The two smallest nodes rise and merge into a parent. This continues until a single tree forms, with paths from root to leaves defining the encoding.

## Exercises

1. **Jump Game**: Given an array where each element represents the maximum jump length from that position, determine if you can reach the last index. Use a greedy approach tracking the farthest reachable position.

2. **Gas Station**: There are N gas stations along a circular route. Given gas available and cost to travel to the next station, find the starting station index that allows completing the circuit, or return -1 if impossible.

3. **Task Scheduler**: Given tasks with cooldown periods, find the minimum time to complete all tasks. Greedily schedule the most frequent tasks first, inserting idle time as needed.
