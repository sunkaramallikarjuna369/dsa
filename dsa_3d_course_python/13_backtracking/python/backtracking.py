"""
Backtracking Algorithm Implementation

This module provides implementations of classic backtracking algorithms
with step-by-step visualization tracking for 3D animation synchronization.

Algorithms included:
- N-Queens: Place N queens on N×N board with no conflicts
- Subsets: Generate all subsets of a set
- Permutations: Generate all permutations of elements
- Maze Solving: Find path through a maze
- Sudoku Solver: Fill Sudoku grid with valid numbers
- Combination Sum: Find combinations that sum to target

All functions include visualization step recording for 3D animation.
"""

from dataclasses import dataclass, field
from typing import TypeVar, Callable
import json

T = TypeVar('T')


@dataclass
class BacktrackStep:
    """Represents a single step in a backtracking algorithm for visualization."""
    step_number: int
    action: str
    description: str
    state: list | dict = field(default_factory=list)
    choice: str = ""
    depth: int = 0
    extra: dict = field(default_factory=dict)


class BacktrackVisualizer:
    """Tracks backtracking algorithm steps for visualization."""
    
    def __init__(self) -> None:
        self.steps: list[BacktrackStep] = []
        self.step_count: int = 0
    
    def record(self, action: str, description: str,
               state: list | dict | None = None,
               choice: str = "",
               depth: int = 0,
               **extra) -> None:
        """Record a visualization step."""
        self.step_count += 1
        step = BacktrackStep(
            step_number=self.step_count,
            action=action,
            description=description,
            state=state if state is not None else [],
            choice=choice,
            depth=depth,
            extra=extra
        )
        self.steps.append(step)
    
    def reset(self) -> None:
        """Reset the visualizer."""
        self.steps = []
        self.step_count = 0
    
    def to_json(self) -> str:
        """Export steps as JSON."""
        return json.dumps([{
            'step': s.step_number,
            'action': s.action,
            'description': s.description,
            'state': s.state,
            'choice': s.choice,
            'depth': s.depth,
            **s.extra
        } for s in self.steps], indent=2)


def n_queens(n: int, visualizer: BacktrackVisualizer | None = None) -> list[list[int]]:
    """
    Solve the N-Queens problem.
    
    Place N queens on an N×N chessboard such that no two queens
    threaten each other (no two queens share row, column, or diagonal).
    
    Args:
        n: Size of the board and number of queens
        visualizer: Optional visualizer for step tracking
    
    Returns:
        List of solutions, each solution is a list of column positions
        where solution[row] = column of queen in that row
    
    Time Complexity: O(N!)
    Space Complexity: O(N) for recursion stack
    
    Example:
        >>> solutions = n_queens(4)
        >>> len(solutions)
        2
    """
    solutions: list[list[int]] = []
    board: list[int] = []
    
    if visualizer:
        visualizer.record("init", f"Solving {n}-Queens problem", depth=0)
    
    def is_safe(row: int, col: int) -> bool:
        """Check if placing queen at (row, col) is safe."""
        for r in range(row):
            c = board[r]
            if c == col or abs(c - col) == abs(r - row):
                return False
        return True
    
    def solve(row: int) -> None:
        if row == n:
            solutions.append(board.copy())
            if visualizer:
                visualizer.record("solution", f"Solution found: {board}",
                                 state=board.copy(), depth=row)
            return
        
        for col in range(n):
            if visualizer:
                visualizer.record("try", f"Try queen at row {row}, col {col}",
                                 state=board.copy(), choice=f"({row},{col})", depth=row)
            
            if is_safe(row, col):
                board.append(col)
                
                if visualizer:
                    visualizer.record("place", f"Place queen at ({row}, {col})",
                                     state=board.copy(), choice=f"({row},{col})", depth=row)
                
                solve(row + 1)
                
                board.pop()
                
                if visualizer:
                    visualizer.record("backtrack", f"Remove queen from ({row}, {col})",
                                     state=board.copy(), depth=row)
            else:
                if visualizer:
                    visualizer.record("conflict", f"Conflict at ({row}, {col})",
                                     state=board.copy(), depth=row)
    
    solve(0)
    
    if visualizer:
        visualizer.record("complete", f"Found {len(solutions)} solutions",
                         extra={"solution_count": len(solutions)})
    
    return solutions


def generate_subsets(nums: list[int],
                     visualizer: BacktrackVisualizer | None = None) -> list[list[int]]:
    """
    Generate all subsets (power set) of a list.
    
    Args:
        nums: List of distinct integers
        visualizer: Optional visualizer for step tracking
    
    Returns:
        List of all subsets
    
    Time Complexity: O(2^n)
    Space Complexity: O(n) for recursion stack
    
    Example:
        >>> generate_subsets([1, 2, 3])
        [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
    """
    result: list[list[int]] = []
    current: list[int] = []
    
    if visualizer:
        visualizer.record("init", f"Generate subsets of {nums}", depth=0)
    
    def backtrack(index: int) -> None:
        result.append(current.copy())
        
        if visualizer:
            visualizer.record("add_subset", f"Add subset: {current}",
                             state=current.copy(), depth=index)
        
        for i in range(index, len(nums)):
            current.append(nums[i])
            
            if visualizer:
                visualizer.record("include", f"Include {nums[i]}",
                                 state=current.copy(), choice=str(nums[i]), depth=index)
            
            backtrack(i + 1)
            
            current.pop()
            
            if visualizer:
                visualizer.record("exclude", f"Exclude {nums[i]} (backtrack)",
                                 state=current.copy(), depth=index)
    
    backtrack(0)
    
    if visualizer:
        visualizer.record("complete", f"Generated {len(result)} subsets",
                         extra={"subset_count": len(result)})
    
    return result


def generate_permutations(nums: list[int],
                          visualizer: BacktrackVisualizer | None = None) -> list[list[int]]:
    """
    Generate all permutations of a list.
    
    Args:
        nums: List of distinct integers
        visualizer: Optional visualizer for step tracking
    
    Returns:
        List of all permutations
    
    Time Complexity: O(n!)
    Space Complexity: O(n) for recursion stack
    
    Example:
        >>> generate_permutations([1, 2, 3])
        [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    """
    result: list[list[int]] = []
    current: list[int] = []
    used: list[bool] = [False] * len(nums)
    
    if visualizer:
        visualizer.record("init", f"Generate permutations of {nums}", depth=0)
    
    def backtrack() -> None:
        if len(current) == len(nums):
            result.append(current.copy())
            
            if visualizer:
                visualizer.record("add_perm", f"Add permutation: {current}",
                                 state=current.copy(), depth=len(current))
            return
        
        for i in range(len(nums)):
            if used[i]:
                continue
            
            current.append(nums[i])
            used[i] = True
            
            if visualizer:
                visualizer.record("choose", f"Choose {nums[i]} for position {len(current)-1}",
                                 state=current.copy(), choice=str(nums[i]), depth=len(current))
            
            backtrack()
            
            current.pop()
            used[i] = False
            
            if visualizer:
                visualizer.record("unchoose", f"Unchoose {nums[i]} (backtrack)",
                                 state=current.copy(), depth=len(current))
    
    backtrack()
    
    if visualizer:
        visualizer.record("complete", f"Generated {len(result)} permutations",
                         extra={"perm_count": len(result)})
    
    return result


def solve_maze(maze: list[list[int]],
               visualizer: BacktrackVisualizer | None = None) -> list[tuple[int, int]] | None:
    """
    Find a path through a maze from top-left to bottom-right.
    
    Args:
        maze: 2D grid where 0 = path, 1 = wall
        visualizer: Optional visualizer for step tracking
    
    Returns:
        List of (row, col) coordinates forming the path, or None if no path
    
    Time Complexity: O(4^(m*n)) worst case
    Space Complexity: O(m*n) for visited array
    
    Example:
        >>> maze = [[0, 0, 1], [1, 0, 0], [1, 1, 0]]
        >>> solve_maze(maze)
        [(0, 0), (0, 1), (1, 1), (1, 2), (2, 2)]
    """
    if not maze or not maze[0]:
        return None
    
    rows, cols = len(maze), len(maze[0])
    path: list[tuple[int, int]] = []
    visited: set[tuple[int, int]] = set()
    
    if visualizer:
        visualizer.record("init", f"Solve {rows}x{cols} maze", depth=0)
    
    def is_valid(r: int, c: int) -> bool:
        return (0 <= r < rows and 0 <= c < cols and
                maze[r][c] == 0 and (r, c) not in visited)
    
    def backtrack(r: int, c: int) -> bool:
        if not is_valid(r, c):
            return False
        
        path.append((r, c))
        visited.add((r, c))
        
        if visualizer:
            visualizer.record("visit", f"Visit ({r}, {c})",
                             state=list(path), choice=f"({r},{c})", depth=len(path))
        
        if r == rows - 1 and c == cols - 1:
            if visualizer:
                visualizer.record("goal", f"Reached goal at ({r}, {c})",
                                 state=list(path), depth=len(path))
            return True
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction_names = ["right", "down", "left", "up"]
        
        for (dr, dc), name in zip(directions, direction_names):
            nr, nc = r + dr, c + dc
            
            if visualizer:
                visualizer.record("try_dir", f"Try {name} from ({r}, {c})",
                                 state=list(path), depth=len(path))
            
            if backtrack(nr, nc):
                return True
        
        path.pop()
        
        if visualizer:
            visualizer.record("backtrack", f"Backtrack from ({r}, {c})",
                             state=list(path), depth=len(path))
        
        return False
    
    if backtrack(0, 0):
        if visualizer:
            visualizer.record("complete", f"Path found with {len(path)} steps",
                             state=list(path))
        return path
    
    if visualizer:
        visualizer.record("no_path", "No path exists")
    
    return None


def solve_sudoku(board: list[list[int]],
                 visualizer: BacktrackVisualizer | None = None) -> bool:
    """
    Solve a Sudoku puzzle in-place.
    
    Args:
        board: 9×9 grid where 0 represents empty cells
        visualizer: Optional visualizer for step tracking
    
    Returns:
        True if solved, False if no solution exists
    
    Time Complexity: O(9^(empty cells))
    Space Complexity: O(81) for recursion stack
    
    Example:
        >>> board = [[5,3,0,0,7,0,0,0,0], ...]  # Sudoku puzzle
        >>> solve_sudoku(board)
        True
    """
    if visualizer:
        visualizer.record("init", "Solving Sudoku puzzle", depth=0)
    
    def is_valid(row: int, col: int, num: int) -> bool:
        """Check if placing num at (row, col) is valid."""
        for i in range(9):
            if board[row][i] == num:
                return False
        
        for i in range(9):
            if board[i][col] == num:
                return False
        
        box_row, box_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if board[i][j] == num:
                    return False
        
        return True
    
    def find_empty() -> tuple[int, int] | None:
        """Find the next empty cell."""
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return (i, j)
        return None
    
    def solve() -> bool:
        cell = find_empty()
        if cell is None:
            if visualizer:
                visualizer.record("solved", "Sudoku solved!")
            return True
        
        row, col = cell
        
        for num in range(1, 10):
            if visualizer:
                visualizer.record("try", f"Try {num} at ({row}, {col})",
                                 choice=str(num), depth=row * 9 + col)
            
            if is_valid(row, col, num):
                board[row][col] = num
                
                if visualizer:
                    visualizer.record("place", f"Place {num} at ({row}, {col})",
                                     choice=str(num), depth=row * 9 + col)
                
                if solve():
                    return True
                
                board[row][col] = 0
                
                if visualizer:
                    visualizer.record("backtrack", f"Remove {num} from ({row}, {col})",
                                     depth=row * 9 + col)
            else:
                if visualizer:
                    visualizer.record("invalid", f"{num} invalid at ({row}, {col})",
                                     depth=row * 9 + col)
        
        return False
    
    return solve()


def combination_sum(candidates: list[int], target: int,
                    visualizer: BacktrackVisualizer | None = None) -> list[list[int]]:
    """
    Find all unique combinations that sum to target.
    
    Each number can be used unlimited times.
    
    Args:
        candidates: List of distinct positive integers
        target: Target sum
        visualizer: Optional visualizer for step tracking
    
    Returns:
        List of combinations that sum to target
    
    Time Complexity: O(n^(target/min))
    Space Complexity: O(target/min) for recursion
    
    Example:
        >>> combination_sum([2, 3, 6, 7], 7)
        [[2, 2, 3], [7]]
    """
    result: list[list[int]] = []
    current: list[int] = []
    
    if visualizer:
        visualizer.record("init", f"Find combinations summing to {target}",
                         extra={"candidates": candidates, "target": target})
    
    def backtrack(start: int, remaining: int) -> None:
        if remaining == 0:
            result.append(current.copy())
            
            if visualizer:
                visualizer.record("found", f"Found combination: {current}",
                                 state=current.copy())
            return
        
        if remaining < 0:
            if visualizer:
                visualizer.record("prune", f"Sum exceeded, prune branch",
                                 state=current.copy())
            return
        
        for i in range(start, len(candidates)):
            current.append(candidates[i])
            
            if visualizer:
                visualizer.record("add", f"Add {candidates[i]}, sum = {target - remaining + candidates[i]}",
                                 state=current.copy(), choice=str(candidates[i]),
                                 depth=len(current))
            
            backtrack(i, remaining - candidates[i])
            
            current.pop()
            
            if visualizer:
                visualizer.record("remove", f"Remove {candidates[i]} (backtrack)",
                                 state=current.copy(), depth=len(current))
    
    backtrack(0, target)
    
    if visualizer:
        visualizer.record("complete", f"Found {len(result)} combinations",
                         extra={"count": len(result)})
    
    return result


def demo() -> None:
    """Demonstrate backtracking algorithms with visualization."""
    print("=" * 60)
    print("BACKTRACKING ALGORITHMS DEMONSTRATION")
    print("=" * 60)
    
    print("\n1. N-QUEENS (N=4)")
    print("-" * 40)
    vis = BacktrackVisualizer()
    solutions = n_queens(4, vis)
    print(f"Solutions found: {len(solutions)}")
    for i, sol in enumerate(solutions):
        print(f"  Solution {i+1}: {sol}")
    
    print("\n2. SUBSETS")
    print("-" * 40)
    nums = [1, 2, 3]
    vis = BacktrackVisualizer()
    subsets = generate_subsets(nums, vis)
    print(f"Subsets of {nums}:")
    print(f"  {subsets}")
    print(f"  Count: {len(subsets)}")
    
    print("\n3. PERMUTATIONS")
    print("-" * 40)
    nums = [1, 2, 3]
    vis = BacktrackVisualizer()
    perms = generate_permutations(nums, vis)
    print(f"Permutations of {nums}:")
    for perm in perms:
        print(f"  {perm}")
    print(f"  Count: {len(perms)}")
    
    print("\n4. MAZE SOLVING")
    print("-" * 40)
    maze = [
        [0, 0, 1, 0],
        [1, 0, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 0]
    ]
    print("Maze (0=path, 1=wall):")
    for row in maze:
        print(f"  {row}")
    vis = BacktrackVisualizer()
    path = solve_maze(maze, vis)
    print(f"Path found: {path}")
    
    print("\n5. COMBINATION SUM")
    print("-" * 40)
    candidates = [2, 3, 6, 7]
    target = 7
    vis = BacktrackVisualizer()
    combos = combination_sum(candidates, target, vis)
    print(f"Candidates: {candidates}, Target: {target}")
    print(f"Combinations: {combos}")
    
    print("\n" + "=" * 60)


if __name__ == "__main__":
    demo()
