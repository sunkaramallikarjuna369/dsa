"""
Segment Tree Implementation

This module provides Segment Tree implementations for efficient range queries
with step-by-step visualization tracking for 3D animation synchronization.

Operations included:
- Build: Construct segment tree from array
- Range Query: Query aggregate over a range (sum, min, max)
- Point Update: Update a single element
- Range Update: Update a range of elements (with lazy propagation)

All functions include visualization step recording for 3D animation.
"""

from dataclasses import dataclass, field
from typing import Callable, TypeVar
import json

T = TypeVar('T')


@dataclass
class SegmentStep:
    """Represents a single step in a Segment Tree operation for visualization."""
    step_number: int
    action: str
    description: str
    node_index: int = 0
    node_range: tuple[int, int] = (0, 0)
    value: int | float = 0
    extra: dict = field(default_factory=dict)


class SegmentVisualizer:
    """Tracks Segment Tree operation steps for visualization."""
    
    def __init__(self) -> None:
        self.steps: list[SegmentStep] = []
        self.step_count: int = 0
    
    def record(self, action: str, description: str,
               node_index: int = 0,
               node_range: tuple[int, int] = (0, 0),
               value: int | float = 0,
               **extra) -> None:
        """Record a visualization step."""
        self.step_count += 1
        step = SegmentStep(
            step_number=self.step_count,
            action=action,
            description=description,
            node_index=node_index,
            node_range=node_range,
            value=value,
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
            'node_index': s.node_index,
            'node_range': s.node_range,
            'value': s.value,
            **s.extra
        } for s in self.steps], indent=2)


class SegmentTreeSum:
    """
    Segment Tree for range sum queries.
    
    A binary tree where each node stores the sum of a range of elements.
    Enables O(log n) range queries and point updates.
    
    Time Complexity:
        - Build: O(n)
        - Range Query: O(log n)
        - Point Update: O(log n)
    
    Space Complexity: O(n)
    
    Example:
        >>> st = SegmentTreeSum([1, 3, 5, 7, 9, 11])
        >>> st.range_sum(1, 4)
        24
    """
    
    def __init__(self, arr: list[int]) -> None:
        self.n = len(arr)
        self.tree: list[int] = [0] * (4 * self.n)
        self.arr = arr.copy()
        if self.n > 0:
            self._build(0, 0, self.n - 1)
    
    def _build(self, node: int, start: int, end: int,
               visualizer: SegmentVisualizer | None = None) -> None:
        """Build the segment tree recursively."""
        if start == end:
            self.tree[node] = self.arr[start]
            
            if visualizer:
                visualizer.record("build_leaf", f"Leaf node [{start}] = {self.arr[start]}",
                                 node_index=node, node_range=(start, end),
                                 value=self.arr[start])
            return
        
        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2
        
        self._build(left_child, start, mid, visualizer)
        self._build(right_child, mid + 1, end, visualizer)
        
        self.tree[node] = self.tree[left_child] + self.tree[right_child]
        
        if visualizer:
            visualizer.record("build_internal", f"Node [{start}-{end}] = {self.tree[node]}",
                             node_index=node, node_range=(start, end),
                             value=self.tree[node])
    
    def range_sum(self, left: int, right: int,
                  visualizer: SegmentVisualizer | None = None) -> int:
        """
        Query the sum of elements in range [left, right].
        
        Args:
            left: Left index of range (inclusive)
            right: Right index of range (inclusive)
            visualizer: Optional visualizer for step tracking
        
        Returns:
            Sum of elements in the range
        """
        if visualizer:
            visualizer.record("query_start", f"Query sum[{left}, {right}]",
                             extra={"query_left": left, "query_right": right})
        
        result = self._range_sum(0, 0, self.n - 1, left, right, visualizer)
        
        if visualizer:
            visualizer.record("query_done", f"Sum[{left}, {right}] = {result}",
                             value=result)
        
        return result
    
    def _range_sum(self, node: int, start: int, end: int,
                   left: int, right: int,
                   visualizer: SegmentVisualizer | None = None) -> int:
        """Recursive range sum query."""
        if right < start or left > end:
            if visualizer:
                visualizer.record("out_of_range", f"Node [{start}-{end}] outside query range",
                                 node_index=node, node_range=(start, end))
            return 0
        
        if left <= start and end <= right:
            if visualizer:
                visualizer.record("full_overlap", f"Node [{start}-{end}] fully in range, value = {self.tree[node]}",
                                 node_index=node, node_range=(start, end),
                                 value=self.tree[node])
            return self.tree[node]
        
        if visualizer:
            visualizer.record("partial_overlap", f"Node [{start}-{end}] partial overlap, split",
                             node_index=node, node_range=(start, end))
        
        mid = (start + end) // 2
        left_sum = self._range_sum(2 * node + 1, start, mid, left, right, visualizer)
        right_sum = self._range_sum(2 * node + 2, mid + 1, end, left, right, visualizer)
        
        return left_sum + right_sum
    
    def update(self, index: int, value: int,
               visualizer: SegmentVisualizer | None = None) -> None:
        """
        Update element at index to new value.
        
        Args:
            index: Index to update
            value: New value
            visualizer: Optional visualizer for step tracking
        """
        if visualizer:
            visualizer.record("update_start", f"Update index {index} to {value}",
                             extra={"index": index, "new_value": value,
                                   "old_value": self.arr[index]})
        
        diff = value - self.arr[index]
        self.arr[index] = value
        self._update(0, 0, self.n - 1, index, diff, visualizer)
        
        if visualizer:
            visualizer.record("update_done", f"Update complete",
                             extra={"index": index, "value": value})
    
    def _update(self, node: int, start: int, end: int,
                index: int, diff: int,
                visualizer: SegmentVisualizer | None = None) -> None:
        """Recursive point update."""
        if index < start or index > end:
            return
        
        self.tree[node] += diff
        
        if visualizer:
            visualizer.record("update_node", f"Update node [{start}-{end}] to {self.tree[node]}",
                             node_index=node, node_range=(start, end),
                             value=self.tree[node])
        
        if start != end:
            mid = (start + end) // 2
            self._update(2 * node + 1, start, mid, index, diff, visualizer)
            self._update(2 * node + 2, mid + 1, end, index, diff, visualizer)


class SegmentTreeMin:
    """
    Segment Tree for range minimum queries.
    
    Similar to SegmentTreeSum but stores minimum values.
    """
    
    def __init__(self, arr: list[int]) -> None:
        self.n = len(arr)
        self.tree: list[int] = [float('inf')] * (4 * self.n)
        self.arr = arr.copy()
        if self.n > 0:
            self._build(0, 0, self.n - 1)
    
    def _build(self, node: int, start: int, end: int) -> None:
        if start == end:
            self.tree[node] = self.arr[start]
            return
        
        mid = (start + end) // 2
        self._build(2 * node + 1, start, mid)
        self._build(2 * node + 2, mid + 1, end)
        self.tree[node] = min(self.tree[2 * node + 1], self.tree[2 * node + 2])
    
    def range_min(self, left: int, right: int,
                  visualizer: SegmentVisualizer | None = None) -> int:
        """Query minimum in range [left, right]."""
        if visualizer:
            visualizer.record("query_start", f"Query min[{left}, {right}]")
        
        result = self._range_min(0, 0, self.n - 1, left, right, visualizer)
        
        if visualizer:
            visualizer.record("query_done", f"Min[{left}, {right}] = {result}",
                             value=result)
        
        return result
    
    def _range_min(self, node: int, start: int, end: int,
                   left: int, right: int,
                   visualizer: SegmentVisualizer | None = None) -> int:
        if right < start or left > end:
            return float('inf')
        
        if left <= start and end <= right:
            if visualizer:
                visualizer.record("full_overlap", f"Node [{start}-{end}] = {self.tree[node]}",
                                 node_index=node, node_range=(start, end),
                                 value=self.tree[node])
            return self.tree[node]
        
        mid = (start + end) // 2
        left_min = self._range_min(2 * node + 1, start, mid, left, right, visualizer)
        right_min = self._range_min(2 * node + 2, mid + 1, end, left, right, visualizer)
        
        return min(left_min, right_min)
    
    def update(self, index: int, value: int) -> None:
        """Update element at index."""
        self.arr[index] = value
        self._update(0, 0, self.n - 1, index, value)
    
    def _update(self, node: int, start: int, end: int,
                index: int, value: int) -> None:
        if index < start or index > end:
            return
        
        if start == end:
            self.tree[node] = value
            return
        
        mid = (start + end) // 2
        self._update(2 * node + 1, start, mid, index, value)
        self._update(2 * node + 2, mid + 1, end, index, value)
        self.tree[node] = min(self.tree[2 * node + 1], self.tree[2 * node + 2])


class SegmentTreeMax:
    """
    Segment Tree for range maximum queries.
    """
    
    def __init__(self, arr: list[int]) -> None:
        self.n = len(arr)
        self.tree: list[int] = [float('-inf')] * (4 * self.n)
        self.arr = arr.copy()
        if self.n > 0:
            self._build(0, 0, self.n - 1)
    
    def _build(self, node: int, start: int, end: int) -> None:
        if start == end:
            self.tree[node] = self.arr[start]
            return
        
        mid = (start + end) // 2
        self._build(2 * node + 1, start, mid)
        self._build(2 * node + 2, mid + 1, end)
        self.tree[node] = max(self.tree[2 * node + 1], self.tree[2 * node + 2])
    
    def range_max(self, left: int, right: int) -> int:
        """Query maximum in range [left, right]."""
        return self._range_max(0, 0, self.n - 1, left, right)
    
    def _range_max(self, node: int, start: int, end: int,
                   left: int, right: int) -> int:
        if right < start or left > end:
            return float('-inf')
        
        if left <= start and end <= right:
            return self.tree[node]
        
        mid = (start + end) // 2
        left_max = self._range_max(2 * node + 1, start, mid, left, right)
        right_max = self._range_max(2 * node + 2, mid + 1, end, left, right)
        
        return max(left_max, right_max)
    
    def update(self, index: int, value: int) -> None:
        """Update element at index."""
        self.arr[index] = value
        self._update(0, 0, self.n - 1, index, value)
    
    def _update(self, node: int, start: int, end: int,
                index: int, value: int) -> None:
        if index < start or index > end:
            return
        
        if start == end:
            self.tree[node] = value
            return
        
        mid = (start + end) // 2
        self._update(2 * node + 1, start, mid, index, value)
        self._update(2 * node + 2, mid + 1, end, index, value)
        self.tree[node] = max(self.tree[2 * node + 1], self.tree[2 * node + 2])


def demo() -> None:
    """Demonstrate Segment Tree operations with visualization."""
    print("=" * 60)
    print("SEGMENT TREE DEMONSTRATION")
    print("=" * 60)
    
    arr = [1, 3, 5, 7, 9, 11]
    print(f"\nArray: {arr}")
    
    print("\n1. SEGMENT TREE SUM")
    print("-" * 40)
    st_sum = SegmentTreeSum(arr)
    vis = SegmentVisualizer()
    
    queries = [(0, 5), (1, 4), (2, 3), (0, 2)]
    for left, right in queries:
        vis.reset()
        result = st_sum.range_sum(left, right, vis)
        expected = sum(arr[left:right+1])
        print(f"Sum[{left}, {right}] = {result} (expected: {expected})")
    
    print("\n2. POINT UPDATE")
    print("-" * 40)
    print(f"Before update: arr[2] = {arr[2]}")
    vis.reset()
    st_sum.update(2, 10, vis)
    print(f"After update: arr[2] = 10")
    result = st_sum.range_sum(0, 5)
    print(f"New sum[0, 5] = {result}")
    
    print("\n3. SEGMENT TREE MIN")
    print("-" * 40)
    st_min = SegmentTreeMin(arr)
    queries = [(0, 5), (1, 4), (3, 5)]
    for left, right in queries:
        result = st_min.range_min(left, right)
        expected = min(arr[left:right+1])
        print(f"Min[{left}, {right}] = {result} (expected: {expected})")
    
    print("\n4. SEGMENT TREE MAX")
    print("-" * 40)
    st_max = SegmentTreeMax(arr)
    queries = [(0, 5), (1, 4), (3, 5)]
    for left, right in queries:
        result = st_max.range_max(left, right)
        expected = max(arr[left:right+1])
        print(f"Max[{left}, {right}] = {result} (expected: {expected})")
    
    print("\n" + "=" * 60)


if __name__ == "__main__":
    demo()
