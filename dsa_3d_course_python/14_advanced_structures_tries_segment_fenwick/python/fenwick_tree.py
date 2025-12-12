"""
Fenwick Tree (Binary Indexed Tree) Implementation

This module provides a Fenwick Tree implementation for efficient prefix sums
with step-by-step visualization tracking for 3D animation synchronization.

Operations included:
- Build: Construct Fenwick tree from array
- Point Update: Add a value to an element
- Prefix Sum: Query sum from index 0 to i
- Range Sum: Query sum from index l to r

All functions include visualization step recording for 3D animation.
"""

from dataclasses import dataclass, field
import json


@dataclass
class FenwickStep:
    """Represents a single step in a Fenwick Tree operation for visualization."""
    step_number: int
    action: str
    description: str
    index: int = 0
    value: int = 0
    binary: str = ""
    lsb: int = 0
    extra: dict = field(default_factory=dict)


class FenwickVisualizer:
    """Tracks Fenwick Tree operation steps for visualization."""
    
    def __init__(self) -> None:
        self.steps: list[FenwickStep] = []
        self.step_count: int = 0
    
    def record(self, action: str, description: str,
               index: int = 0,
               value: int = 0,
               binary: str = "",
               lsb: int = 0,
               **extra) -> None:
        """Record a visualization step."""
        self.step_count += 1
        step = FenwickStep(
            step_number=self.step_count,
            action=action,
            description=description,
            index=index,
            value=value,
            binary=binary,
            lsb=lsb,
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
            'index': s.index,
            'value': s.value,
            'binary': s.binary,
            'lsb': s.lsb,
            **s.extra
        } for s in self.steps], indent=2)


class FenwickTree:
    """
    Fenwick Tree (Binary Indexed Tree) data structure.
    
    An array-based structure that supports O(log n) prefix sum queries
    and point updates using binary representation of indices.
    
    Time Complexity:
        - Build: O(n log n)
        - Point Update: O(log n)
        - Prefix Sum: O(log n)
        - Range Sum: O(log n)
    
    Space Complexity: O(n)
    
    Example:
        >>> ft = FenwickTree([1, 3, 5, 7, 9, 11])
        >>> ft.prefix_sum(4)  # sum of indices 0-4
        25
        >>> ft.range_sum(2, 4)  # sum of indices 2-4
        21
    """
    
    def __init__(self, arr: list[int] | None = None, size: int = 0) -> None:
        """
        Initialize Fenwick Tree.
        
        Args:
            arr: Optional array to build tree from
            size: Size if creating empty tree
        """
        if arr is not None:
            self.n = len(arr)
            self.tree = [0] * (self.n + 1)
            for i, val in enumerate(arr):
                self._update(i + 1, val)
        else:
            self.n = size
            self.tree = [0] * (self.n + 1)
    
    @staticmethod
    def _lsb(i: int) -> int:
        """Get the lowest set bit of i."""
        return i & (-i)
    
    def _update(self, i: int, delta: int) -> None:
        """Internal update (1-indexed)."""
        while i <= self.n:
            self.tree[i] += delta
            i += self._lsb(i)
    
    def update(self, index: int, delta: int,
               visualizer: FenwickVisualizer | None = None) -> None:
        """
        Add delta to element at index (0-indexed).
        
        Args:
            index: Index to update (0-indexed)
            delta: Value to add
            visualizer: Optional visualizer for step tracking
        """
        i = index + 1
        
        if visualizer:
            visualizer.record("update_start", f"Update index {index} by +{delta}",
                             index=index, value=delta,
                             extra={"delta": delta})
        
        while i <= self.n:
            lsb = self._lsb(i)
            binary = bin(i)[2:]
            
            if visualizer:
                visualizer.record("update_step", f"Update BIT[{i}] += {delta}",
                                 index=i, value=self.tree[i] + delta,
                                 binary=binary, lsb=lsb,
                                 extra={"next": i + lsb if i + lsb <= self.n else None})
            
            self.tree[i] += delta
            i += lsb
        
        if visualizer:
            visualizer.record("update_done", f"Update complete")
    
    def prefix_sum(self, index: int,
                   visualizer: FenwickVisualizer | None = None) -> int:
        """
        Get sum of elements from index 0 to index (inclusive, 0-indexed).
        
        Args:
            index: End index (0-indexed, inclusive)
            visualizer: Optional visualizer for step tracking
        
        Returns:
            Sum of elements [0, index]
        """
        i = index + 1
        result = 0
        
        if visualizer:
            visualizer.record("query_start", f"Prefix sum [0, {index}]",
                             index=index)
        
        while i > 0:
            lsb = self._lsb(i)
            binary = bin(i)[2:]
            
            if visualizer:
                visualizer.record("query_step", f"Add BIT[{i}] = {self.tree[i]}",
                                 index=i, value=self.tree[i],
                                 binary=binary, lsb=lsb,
                                 extra={"running_sum": result + self.tree[i],
                                       "next": i - lsb if i - lsb > 0 else None})
            
            result += self.tree[i]
            i -= lsb
        
        if visualizer:
            visualizer.record("query_done", f"Prefix sum [0, {index}] = {result}",
                             value=result)
        
        return result
    
    def range_sum(self, left: int, right: int,
                  visualizer: FenwickVisualizer | None = None) -> int:
        """
        Get sum of elements from left to right (inclusive, 0-indexed).
        
        Args:
            left: Start index (0-indexed)
            right: End index (0-indexed)
            visualizer: Optional visualizer for step tracking
        
        Returns:
            Sum of elements [left, right]
        """
        if visualizer:
            visualizer.record("range_start", f"Range sum [{left}, {right}]",
                             extra={"left": left, "right": right})
        
        right_sum = self.prefix_sum(right, visualizer)
        
        if left == 0:
            result = right_sum
        else:
            left_sum = self.prefix_sum(left - 1, visualizer)
            result = right_sum - left_sum
            
            if visualizer:
                visualizer.record("range_calc", f"Range sum = {right_sum} - {left_sum} = {result}",
                                 value=result)
        
        if visualizer:
            visualizer.record("range_done", f"Range sum [{left}, {right}] = {result}",
                             value=result)
        
        return result
    
    def set(self, index: int, value: int,
            visualizer: FenwickVisualizer | None = None) -> None:
        """
        Set element at index to value (0-indexed).
        
        Args:
            index: Index to set (0-indexed)
            value: New value
            visualizer: Optional visualizer for step tracking
        """
        current = self.range_sum(index, index)
        delta = value - current
        self.update(index, delta, visualizer)


class FenwickTree2D:
    """
    2D Fenwick Tree for 2D prefix sums.
    
    Supports O(log n * log m) queries and updates on a 2D grid.
    """
    
    def __init__(self, rows: int, cols: int) -> None:
        self.rows = rows
        self.cols = cols
        self.tree = [[0] * (cols + 1) for _ in range(rows + 1)]
    
    @staticmethod
    def _lsb(i: int) -> int:
        return i & (-i)
    
    def update(self, row: int, col: int, delta: int) -> None:
        """Add delta to element at (row, col) (0-indexed)."""
        i = row + 1
        while i <= self.rows:
            j = col + 1
            while j <= self.cols:
                self.tree[i][j] += delta
                j += self._lsb(j)
            i += self._lsb(i)
    
    def prefix_sum(self, row: int, col: int) -> int:
        """Get sum of rectangle from (0,0) to (row, col) (0-indexed)."""
        result = 0
        i = row + 1
        while i > 0:
            j = col + 1
            while j > 0:
                result += self.tree[i][j]
                j -= self._lsb(j)
            i -= self._lsb(i)
        return result
    
    def range_sum(self, r1: int, c1: int, r2: int, c2: int) -> int:
        """Get sum of rectangle from (r1, c1) to (r2, c2) (0-indexed)."""
        result = self.prefix_sum(r2, c2)
        if r1 > 0:
            result -= self.prefix_sum(r1 - 1, c2)
        if c1 > 0:
            result -= self.prefix_sum(r2, c1 - 1)
        if r1 > 0 and c1 > 0:
            result += self.prefix_sum(r1 - 1, c1 - 1)
        return result


def count_inversions(arr: list[int]) -> int:
    """
    Count inversions in array using Fenwick Tree.
    
    An inversion is a pair (i, j) where i < j but arr[i] > arr[j].
    
    Args:
        arr: Input array
    
    Returns:
        Number of inversions
    
    Time Complexity: O(n log n)
    
    Example:
        >>> count_inversions([2, 4, 1, 3, 5])
        3
    """
    if not arr:
        return 0
    
    sorted_arr = sorted(set(arr))
    rank = {v: i for i, v in enumerate(sorted_arr)}
    
    ft = FenwickTree(size=len(sorted_arr))
    inversions = 0
    
    for i in range(len(arr) - 1, -1, -1):
        r = rank[arr[i]]
        if r > 0:
            inversions += ft.prefix_sum(r - 1)
        ft.update(r, 1)
    
    return inversions


def demo() -> None:
    """Demonstrate Fenwick Tree operations with visualization."""
    print("=" * 60)
    print("FENWICK TREE (BINARY INDEXED TREE) DEMONSTRATION")
    print("=" * 60)
    
    arr = [3, 2, -1, 6, 5, 4, -3, 3, 7, 2]
    print(f"\nArray: {arr}")
    print(f"Indices: {list(range(len(arr)))}")
    
    ft = FenwickTree(arr)
    vis = FenwickVisualizer()
    
    print("\n1. PREFIX SUM QUERIES")
    print("-" * 40)
    for i in [0, 3, 6, 9]:
        vis.reset()
        result = ft.prefix_sum(i, vis)
        expected = sum(arr[:i+1])
        print(f"Prefix sum [0, {i}] = {result} (expected: {expected})")
    
    print("\n2. RANGE SUM QUERIES")
    print("-" * 40)
    ranges = [(0, 4), (2, 7), (5, 9)]
    for left, right in ranges:
        vis.reset()
        result = ft.range_sum(left, right, vis)
        expected = sum(arr[left:right+1])
        print(f"Range sum [{left}, {right}] = {result} (expected: {expected})")
    
    print("\n3. POINT UPDATE")
    print("-" * 40)
    print(f"Before: arr[3] contributes to prefix sums")
    vis.reset()
    ft.update(3, 4, vis)
    print(f"Update: add 4 to index 3")
    result = ft.prefix_sum(5)
    expected = sum(arr[:6]) + 4
    print(f"New prefix sum [0, 5] = {result} (expected: {expected})")
    
    print("\n4. COUNT INVERSIONS")
    print("-" * 40)
    test_arr = [2, 4, 1, 3, 5]
    inversions = count_inversions(test_arr)
    print(f"Array: {test_arr}")
    print(f"Inversions: {inversions}")
    print("Pairs: (2,1), (4,1), (4,3)")
    
    print("\n5. 2D FENWICK TREE")
    print("-" * 40)
    ft2d = FenwickTree2D(3, 3)
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    for i in range(3):
        for j in range(3):
            ft2d.update(i, j, matrix[i][j])
    
    print("Matrix:")
    for row in matrix:
        print(f"  {row}")
    
    result = ft2d.prefix_sum(1, 1)
    expected = 1 + 2 + 4 + 5
    print(f"Prefix sum (0,0) to (1,1) = {result} (expected: {expected})")
    
    result = ft2d.range_sum(1, 1, 2, 2)
    expected = 5 + 6 + 8 + 9
    print(f"Range sum (1,1) to (2,2) = {result} (expected: {expected})")
    
    print("\n" + "=" * 60)


if __name__ == "__main__":
    demo()
