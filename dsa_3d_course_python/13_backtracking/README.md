# Backtracking

Welcome to the Backtracking world, where you will explore techniques for systematically searching through all possible solutions by building candidates incrementally and abandoning paths that cannot lead to valid solutions. This module visualizes backtracking as navigating a 3D maze where paths light up when explored and dim when backtracked.

## Concept Overview

Backtracking is a general algorithmic technique for finding solutions by incrementally building candidates and abandoning a candidate ("backtracking") as soon as it determines that the candidate cannot possibly lead to a valid solution.

The key insight is that backtracking prunes the search space by recognizing invalid partial solutions early. Instead of generating all possible combinations and then filtering, backtracking avoids exploring branches that are guaranteed to fail.

The general pattern follows three phases: Choose (select an option to try), Explore (recursively explore with that choice), and Unchoose (undo the choice and try the next option). This pattern is sometimes called "choose-explore-unchoose" or "try-recurse-undo".

N-Queens is a classic backtracking problem: place N queens on an N×N chessboard such that no two queens threaten each other. The algorithm places queens row by row, backtracking when a placement leads to conflicts.

Subset generation explores all 2^n subsets of a set by deciding for each element whether to include it or not. The decision tree has two branches at each level: include the current element or exclude it.

Permutation generation produces all n! arrangements of n elements. At each position, we try each remaining unused element, recurse, then undo the choice.

Maze solving navigates from start to goal by trying each direction, marking visited cells, and backtracking when hitting dead ends or previously visited cells.

## Learning Objectives

- Understand the backtracking paradigm: choose, explore, unchoose
- Implement classic backtracking problems: N-Queens, subsets, permutations
- Visualize the search tree and pruning of invalid branches
- Recognize when backtracking is appropriate versus other approaches
- Analyze time complexity of backtracking solutions

## The 3D Metaphor: Branching Maze

**Search Space as Maze**: Imagine a 3D maze where each junction represents a decision point. Paths branch out representing different choices. The goal is to find paths that lead to valid solutions.

**Exploration**: As the algorithm explores, paths light up in a glowing color. The current position is marked with a bright indicator. The path from start to current position shows the choices made so far.

**Backtracking**: When a dead end is reached (invalid solution or no more options), the path dims and the algorithm returns to the previous junction. The dimmed path shows that this branch has been explored and rejected.

**Pruning**: Invalid branches are marked with a red glow before being abandoned. This shows how backtracking avoids exploring paths that cannot lead to solutions.

**Solution Discovery**: When a valid solution is found, the entire path from start to solution glows brightly. Multiple solutions create multiple glowing paths through the maze.

## How This Maps to the 3D World

When you call `n_queens(n)`, the visualization shows an N×N chessboard. Queens are placed row by row. When a conflict is detected, the invalid placement flashes red and the queen is removed (backtrack). Valid placements glow green.

When you call `generate_subsets(nums)`, the visualization shows a binary decision tree. Each level represents an element, with left branch for "include" and right branch for "exclude". Leaf nodes show the resulting subsets.

When you call `generate_permutations(nums)`, the visualization shows a tree where each level fills one position. Branches represent choosing each remaining element. The tree expands as choices are made and contracts during backtracking.

When you call `solve_maze(maze)`, the visualization shows a 3D maze. The algorithm tries each direction, marking the path. Dead ends cause backtracking, and the solution path glows when found.

## Exercises

1. **Sudoku Solver**: Fill a 9×9 grid so each row, column, and 3×3 box contains digits 1-9. Use backtracking to try digits and undo when conflicts arise.

2. **Word Search**: Given a 2D board of characters and a word, find if the word exists in the grid by moving horizontally or vertically to adjacent cells.

3. **Combination Sum**: Find all unique combinations of candidates that sum to a target. Each number can be used unlimited times.
