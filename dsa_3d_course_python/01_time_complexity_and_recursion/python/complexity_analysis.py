"""
Time Complexity Analysis Module

This module provides demonstrations of different time complexity classes
with step-by-step output that can be synchronized with 3D visualizations.

Each function includes complexity analysis and generates visual step events.
"""

from typing import Any
from dataclasses import dataclass, field
import time


@dataclass
class VisualStep:
    """Represents a single step in the visualization."""
    step_number: int
    description: str
    operation_count: int
    highlight_indices: list[int] = field(default_factory=list)
    complexity_class: str = ""


class ComplexityDemonstrator:
    """
    Demonstrates various time complexity classes with visual step tracking.
    
    Each method performs operations characteristic of its complexity class
    and records steps that can be used to drive 3D animations.
    """
    
    def __init__(self) -> None:
        self.steps: list[VisualStep] = []
        self.operation_count: int = 0
    
    def reset(self) -> None:
        """Reset the step tracker for a new demonstration."""
        self.steps = []
        self.operation_count = 0
    
    def _record_step(
        self,
        description: str,
        highlight_indices: list[int] | None = None,
        complexity_class: str = ""
    ) -> None:
        """Record a visualization step."""
        self.operation_count += 1
        step = VisualStep(
            step_number=self.operation_count,
            description=description,
            operation_count=self.operation_count,
            highlight_indices=highlight_indices or [],
            complexity_class=complexity_class
        )
        self.steps.append(step)
    
    def constant_time_access(self, arr: list[Any], index: int) -> Any:
        """
        Demonstrate O(1) constant time array access.
        
        Accessing an element by index takes the same time regardless
        of array size because we can jump directly to the memory location.
        
        Args:
            arr: The array to access
            index: The index to retrieve
            
        Returns:
            The element at the specified index
            
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self.reset()
        self._record_step(
            f"Direct access to index {index}",
            highlight_indices=[index],
            complexity_class="O(1)"
        )
        return arr[index]
    
    def linear_search(self, arr: list[Any], target: Any) -> int:
        """
        Demonstrate O(n) linear time search.
        
        We must potentially check every element in the array,
        so time grows linearly with input size.
        
        Args:
            arr: The array to search
            target: The value to find
            
        Returns:
            Index of target if found, -1 otherwise
            
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        self.reset()
        self._record_step(
            "Begin linear search",
            complexity_class="O(n)"
        )
        
        for i, element in enumerate(arr):
            self._record_step(
                f"Check index {i}: {element} == {target}?",
                highlight_indices=[i],
                complexity_class="O(n)"
            )
            if element == target:
                self._record_step(
                    f"Found target at index {i}",
                    highlight_indices=[i],
                    complexity_class="O(n)"
                )
                return i
        
        self._record_step(
            "Target not found in array",
            complexity_class="O(n)"
        )
        return -1
    
    def quadratic_pairs(self, arr: list[Any]) -> list[tuple[Any, Any]]:
        """
        Demonstrate O(n²) quadratic time with nested loops.
        
        Finding all pairs requires checking each element against
        every other element, resulting in n * n operations.
        
        Args:
            arr: The array to process
            
        Returns:
            List of all unique pairs
            
        Time Complexity: O(n²)
        Space Complexity: O(n²) for storing pairs
        """
        self.reset()
        pairs: list[tuple[Any, Any]] = []
        n = len(arr)
        
        self._record_step(
            f"Begin finding all pairs in array of size {n}",
            complexity_class="O(n²)"
        )
        
        for i in range(n):
            self._record_step(
                f"Outer loop: fixing element at index {i}",
                highlight_indices=[i],
                complexity_class="O(n²)"
            )
            for j in range(i + 1, n):
                self._record_step(
                    f"Inner loop: pairing indices {i} and {j}",
                    highlight_indices=[i, j],
                    complexity_class="O(n²)"
                )
                pairs.append((arr[i], arr[j]))
        
        self._record_step(
            f"Found {len(pairs)} pairs total",
            complexity_class="O(n²)"
        )
        return pairs
    
    def logarithmic_search(self, arr: list[int], target: int) -> int:
        """
        Demonstrate O(log n) logarithmic time with binary search.
        
        By halving the search space each iteration, we only need
        log₂(n) comparisons to find the target.
        
        Args:
            arr: A sorted array to search
            target: The value to find
            
        Returns:
            Index of target if found, -1 otherwise
            
        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        self.reset()
        left, right = 0, len(arr) - 1
        
        self._record_step(
            f"Begin binary search for {target}",
            highlight_indices=list(range(left, right + 1)),
            complexity_class="O(log n)"
        )
        
        while left <= right:
            mid = (left + right) // 2
            self._record_step(
                f"Check middle index {mid}: {arr[mid]}",
                highlight_indices=[mid],
                complexity_class="O(log n)"
            )
            
            if arr[mid] == target:
                self._record_step(
                    f"Found target at index {mid}",
                    highlight_indices=[mid],
                    complexity_class="O(log n)"
                )
                return mid
            elif arr[mid] < target:
                self._record_step(
                    f"Target is larger, search right half [{mid + 1}, {right}]",
                    highlight_indices=list(range(mid + 1, right + 1)),
                    complexity_class="O(log n)"
                )
                left = mid + 1
            else:
                self._record_step(
                    f"Target is smaller, search left half [{left}, {mid - 1}]",
                    highlight_indices=list(range(left, mid)),
                    complexity_class="O(log n)"
                )
                right = mid - 1
        
        self._record_step(
            "Target not found",
            complexity_class="O(log n)"
        )
        return -1
    
    def print_steps(self) -> None:
        """Print all recorded steps in a readable format."""
        print(f"\n{'='*60}")
        print(f"Visualization Steps ({len(self.steps)} total operations)")
        print(f"{'='*60}")
        for step in self.steps:
            indices_str = f" [indices: {step.highlight_indices}]" if step.highlight_indices else ""
            print(f"Step {step.step_number}: {step.description}{indices_str}")
        print(f"{'='*60}\n")


def compare_complexities(n: int) -> dict[str, int]:
    """
    Compare operation counts for different complexity classes.
    
    Args:
        n: Input size to analyze
        
    Returns:
        Dictionary mapping complexity class to operation count
    """
    import math
    
    return {
        "O(1)": 1,
        "O(log n)": max(1, int(math.log2(n))) if n > 0 else 0,
        "O(n)": n,
        "O(n log n)": n * max(1, int(math.log2(n))) if n > 0 else 0,
        "O(n²)": n * n,
        "O(2^n)": 2 ** min(n, 20),  # Cap to prevent overflow
    }


def demo() -> None:
    """Run demonstrations of all complexity classes."""
    demonstrator = ComplexityDemonstrator()
    test_array = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    sorted_array = list(range(1, 11))
    
    print("\n" + "="*60)
    print("TIME COMPLEXITY DEMONSTRATIONS")
    print("="*60)
    
    # O(1) Demo
    print("\n--- O(1) Constant Time: Array Access ---")
    result = demonstrator.constant_time_access(test_array, 5)
    print(f"Accessed element: {result}")
    demonstrator.print_steps()
    
    # O(n) Demo
    print("\n--- O(n) Linear Time: Linear Search ---")
    result = demonstrator.linear_search(test_array, 70)
    print(f"Found at index: {result}")
    demonstrator.print_steps()
    
    # O(log n) Demo
    print("\n--- O(log n) Logarithmic Time: Binary Search ---")
    result = demonstrator.logarithmic_search(sorted_array, 7)
    print(f"Found at index: {result}")
    demonstrator.print_steps()
    
    # O(n²) Demo
    print("\n--- O(n²) Quadratic Time: Find All Pairs ---")
    small_array = [1, 2, 3, 4]
    pairs = demonstrator.quadratic_pairs(small_array)
    print(f"Pairs found: {pairs}")
    demonstrator.print_steps()
    
    # Complexity Comparison
    print("\n--- Complexity Comparison for n=100 ---")
    comparison = compare_complexities(100)
    for complexity, ops in comparison.items():
        print(f"{complexity}: {ops:,} operations")


if __name__ == "__main__":
    demo()
