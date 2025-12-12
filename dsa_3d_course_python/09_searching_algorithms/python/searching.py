"""
Searching Algorithms Module

This module provides implementations of various searching algorithms
with step-by-step tracking for 3D visualization synchronization.

Includes linear search, binary search, and variations.
"""

from typing import TypeVar, Sequence, Any
from dataclasses import dataclass, field

T = TypeVar('T')


@dataclass
class SearchStep:
    """Represents a single step in search visualization."""
    step_number: int
    operation: str
    description: str
    index: int = -1
    value: Any = None
    low: int = -1
    mid: int = -1
    high: int = -1
    comparison: str = ""
    found: bool = False
    search_space: tuple[int, int] = (-1, -1)


class SearchVisualizer:
    """Tracks search steps for visualization."""
    
    def __init__(self) -> None:
        self._steps: list[SearchStep] = []
        self._step_count: int = 0
    
    def record_step(
        self,
        operation: str,
        description: str,
        index: int = -1,
        value: Any = None,
        low: int = -1,
        mid: int = -1,
        high: int = -1,
        comparison: str = "",
        found: bool = False,
        search_space: tuple[int, int] = (-1, -1)
    ) -> None:
        """Record a visualization step."""
        self._step_count += 1
        step = SearchStep(
            step_number=self._step_count,
            operation=operation,
            description=description,
            index=index,
            value=value,
            low=low,
            mid=mid,
            high=high,
            comparison=comparison,
            found=found,
            search_space=search_space
        )
        self._steps.append(step)
    
    def clear_steps(self) -> None:
        """Clear recorded steps."""
        self._steps = []
        self._step_count = 0
    
    @property
    def steps(self) -> list[SearchStep]:
        """Return all recorded steps."""
        return self._steps


def linear_search(arr: Sequence[T], target: T, visualizer: SearchVisualizer | None = None) -> int:
    """
    Linear search - scan array from left to right.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Args:
        arr: Sequence to search
        target: Value to find
        visualizer: Optional visualizer for step tracking
    
    Returns:
        Index of target if found, -1 otherwise
    """
    if visualizer:
        visualizer.record_step(
            "init",
            f"Linear search for {target} in array of size {len(arr)}",
            search_space=(0, len(arr) - 1)
        )
    
    for i, value in enumerate(arr):
        if visualizer:
            visualizer.record_step(
                "check",
                f"Checking index {i}: {value}",
                index=i,
                value=value,
                comparison=f"{value} == {target}?"
            )
        
        if value == target:
            if visualizer:
                visualizer.record_step(
                    "found",
                    f"Found {target} at index {i}",
                    index=i,
                    value=value,
                    found=True
                )
            return i
    
    if visualizer:
        visualizer.record_step(
            "not_found",
            f"{target} not found in array"
        )
    
    return -1


def binary_search(arr: Sequence[T], target: T, visualizer: SearchVisualizer | None = None) -> int:
    """
    Binary search - divide and conquer on sorted array.
    
    Time Complexity: O(log n)
    Space Complexity: O(1)
    
    Args:
        arr: Sorted sequence to search
        target: Value to find
        visualizer: Optional visualizer for step tracking
    
    Returns:
        Index of target if found, -1 otherwise
    """
    low, high = 0, len(arr) - 1
    
    if visualizer:
        visualizer.record_step(
            "init",
            f"Binary search for {target} in sorted array",
            low=low,
            high=high,
            search_space=(low, high)
        )
    
    while low <= high:
        mid = (low + high) // 2
        mid_value = arr[mid]
        
        if visualizer:
            visualizer.record_step(
                "compare",
                f"Compare mid (index {mid}, value {mid_value}) with {target}",
                index=mid,
                value=mid_value,
                low=low,
                mid=mid,
                high=high,
                comparison=f"{mid_value} vs {target}",
                search_space=(low, high)
            )
        
        if mid_value == target:
            if visualizer:
                visualizer.record_step(
                    "found",
                    f"Found {target} at index {mid}",
                    index=mid,
                    value=mid_value,
                    found=True
                )
            return mid
        elif mid_value < target:
            if visualizer:
                visualizer.record_step(
                    "eliminate_left",
                    f"{mid_value} < {target}, eliminate left half",
                    low=mid + 1,
                    high=high,
                    search_space=(mid + 1, high)
                )
            low = mid + 1
        else:
            if visualizer:
                visualizer.record_step(
                    "eliminate_right",
                    f"{mid_value} > {target}, eliminate right half",
                    low=low,
                    high=mid - 1,
                    search_space=(low, mid - 1)
                )
            high = mid - 1
    
    if visualizer:
        visualizer.record_step(
            "not_found",
            f"{target} not found (search space empty)"
        )
    
    return -1


def binary_search_recursive(
    arr: Sequence[T],
    target: T,
    low: int = 0,
    high: int | None = None
) -> int:
    """
    Binary search - recursive implementation.
    
    Time Complexity: O(log n)
    Space Complexity: O(log n) due to recursion stack
    """
    if high is None:
        high = len(arr) - 1
    
    if low > high:
        return -1
    
    mid = (low + high) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)


def search_insert_position(arr: Sequence[T], target: T) -> int:
    """
    Find index to insert target to maintain sorted order.
    
    If target exists, return its index.
    If not, return the index where it would be inserted.
    
    Time Complexity: O(log n)
    """
    low, high = 0, len(arr)
    
    while low < high:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid
    
    return low


def find_first_occurrence(arr: Sequence[T], target: T) -> int:
    """
    Find the first occurrence of target in sorted array with duplicates.
    
    Time Complexity: O(log n)
    """
    low, high = 0, len(arr) - 1
    result = -1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            result = mid
            high = mid - 1  # Continue searching left
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return result


def find_last_occurrence(arr: Sequence[T], target: T) -> int:
    """
    Find the last occurrence of target in sorted array with duplicates.
    
    Time Complexity: O(log n)
    """
    low, high = 0, len(arr) - 1
    result = -1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            result = mid
            low = mid + 1  # Continue searching right
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return result


def find_first_and_last(arr: Sequence[T], target: T) -> tuple[int, int]:
    """
    Find the starting and ending position of target.
    
    Returns (-1, -1) if target not found.
    
    Time Complexity: O(log n)
    """
    first = find_first_occurrence(arr, target)
    if first == -1:
        return (-1, -1)
    last = find_last_occurrence(arr, target)
    return (first, last)


def search_rotated_array(arr: Sequence[T], target: T) -> int:
    """
    Search in a rotated sorted array.
    
    A sorted array has been rotated at some pivot.
    Example: [4, 5, 6, 7, 0, 1, 2] was [0, 1, 2, 4, 5, 6, 7] rotated at index 4.
    
    Time Complexity: O(log n)
    """
    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid
        
        # Check which half is sorted
        if arr[low] <= arr[mid]:
            # Left half is sorted
            if arr[low] <= target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            # Right half is sorted
            if arr[mid] < target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
    
    return -1


def find_peak_element(arr: Sequence[int]) -> int:
    """
    Find a peak element (greater than neighbors).
    
    Array may have multiple peaks; return any peak index.
    
    Time Complexity: O(log n)
    """
    low, high = 0, len(arr) - 1
    
    while low < high:
        mid = (low + high) // 2
        
        if arr[mid] < arr[mid + 1]:
            low = mid + 1
        else:
            high = mid
    
    return low


def find_minimum_rotated(arr: Sequence[T]) -> int:
    """
    Find minimum element in rotated sorted array.
    
    Returns the index of the minimum element.
    
    Time Complexity: O(log n)
    """
    low, high = 0, len(arr) - 1
    
    while low < high:
        mid = (low + high) // 2
        
        if arr[mid] > arr[high]:
            low = mid + 1
        else:
            high = mid
    
    return low


def lower_bound(arr: Sequence[T], target: T) -> int:
    """
    Find the first element >= target.
    
    Returns len(arr) if all elements are < target.
    
    Time Complexity: O(log n)
    """
    low, high = 0, len(arr)
    
    while low < high:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid
    
    return low


def upper_bound(arr: Sequence[T], target: T) -> int:
    """
    Find the first element > target.
    
    Returns len(arr) if all elements are <= target.
    
    Time Complexity: O(log n)
    """
    low, high = 0, len(arr)
    
    while low < high:
        mid = (low + high) // 2
        if arr[mid] <= target:
            low = mid + 1
        else:
            high = mid
    
    return low


def demo() -> None:
    """Run demonstrations of searching algorithms."""
    print("\n" + "="*60)
    print("SEARCHING ALGORITHM DEMONSTRATIONS")
    print("="*60)
    
    # Linear Search
    print("\n--- Linear Search ---")
    arr = [23, 45, 12, 67, 34, 89, 56, 78, 90, 11]
    target = 89
    visualizer = SearchVisualizer()
    
    result = linear_search(arr, target, visualizer)
    print(f"Array: {arr}")
    print(f"Target: {target}")
    print(f"Found at index: {result}")
    print(f"Steps taken: {len(visualizer.steps)}")
    
    # Binary Search
    print("\n--- Binary Search ---")
    sorted_arr = [11, 23, 34, 45, 56, 67, 78, 89, 90, 95]
    target = 78
    visualizer = SearchVisualizer()
    
    result = binary_search(sorted_arr, target, visualizer)
    print(f"Sorted array: {sorted_arr}")
    print(f"Target: {target}")
    print(f"Found at index: {result}")
    print(f"Steps taken: {len(visualizer.steps)}")
    
    # Search Insert Position
    print("\n--- Search Insert Position ---")
    arr = [1, 3, 5, 6]
    for target in [5, 2, 7, 0]:
        pos = search_insert_position(arr, target)
        print(f"Insert {target} at index: {pos}")
    
    # First and Last Occurrence
    print("\n--- First and Last Occurrence ---")
    arr = [1, 2, 3, 5, 5, 5, 5, 8, 9, 10]
    target = 5
    first, last = find_first_and_last(arr, target)
    print(f"Array: {arr}")
    print(f"Target {target}: first={first}, last={last}")
    
    # Search in Rotated Array
    print("\n--- Search in Rotated Array ---")
    rotated = [4, 5, 6, 7, 0, 1, 2]
    for target in [0, 3, 6]:
        result = search_rotated_array(rotated, target)
        print(f"Search {target} in {rotated}: index={result}")
    
    # Find Peak Element
    print("\n--- Find Peak Element ---")
    arr = [1, 2, 3, 1]
    peak = find_peak_element(arr)
    print(f"Array: {arr}")
    print(f"Peak at index: {peak} (value: {arr[peak]})")
    
    # Lower and Upper Bound
    print("\n--- Lower and Upper Bound ---")
    arr = [1, 2, 4, 4, 4, 5, 6]
    target = 4
    lb = lower_bound(arr, target)
    ub = upper_bound(arr, target)
    print(f"Array: {arr}")
    print(f"Target: {target}")
    print(f"Lower bound (first >= {target}): index {lb}")
    print(f"Upper bound (first > {target}): index {ub}")


if __name__ == "__main__":
    demo()
