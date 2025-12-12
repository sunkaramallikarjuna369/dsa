"""
Arrays Module

This module provides demonstrations of array operations and common
array algorithms with step-by-step tracking for 3D visualization.

Arrays are the most fundamental data structure, providing O(1) access
by index due to contiguous memory storage.
"""

from typing import Any, TypeVar, Generic
from dataclasses import dataclass, field

T = TypeVar('T')


@dataclass
class ArrayStep:
    """Represents a single step in array visualization."""
    step_number: int
    operation: str
    description: str
    indices_accessed: list[int] = field(default_factory=list)
    indices_modified: list[int] = field(default_factory=list)
    array_state: list[Any] = field(default_factory=list)
    pointer_positions: dict[str, int] = field(default_factory=dict)


class VisualArray(Generic[T]):
    """
    A wrapper around Python lists that tracks operations for visualization.
    
    This class records every access, modification, and traversal operation
    to generate step-by-step data for 3D animation synchronization.
    """
    
    def __init__(self, initial_data: list[T] | None = None) -> None:
        """
        Initialize the visual array.
        
        Args:
            initial_data: Optional list to initialize the array with
        """
        self._data: list[T] = list(initial_data) if initial_data else []
        self._steps: list[ArrayStep] = []
        self._step_count: int = 0
    
    def _record_step(
        self,
        operation: str,
        description: str,
        indices_accessed: list[int] | None = None,
        indices_modified: list[int] | None = None,
        pointer_positions: dict[str, int] | None = None
    ) -> None:
        """Record a visualization step."""
        self._step_count += 1
        step = ArrayStep(
            step_number=self._step_count,
            operation=operation,
            description=description,
            indices_accessed=indices_accessed or [],
            indices_modified=indices_modified or [],
            array_state=list(self._data),
            pointer_positions=pointer_positions or {}
        )
        self._steps.append(step)
    
    def __getitem__(self, index: int) -> T:
        """
        Access element at index with O(1) time complexity.
        
        Args:
            index: The index to access
            
        Returns:
            The element at the specified index
        """
        self._record_step(
            "access",
            f"Access element at index {index}: {self._data[index]}",
            indices_accessed=[index]
        )
        return self._data[index]
    
    def __setitem__(self, index: int, value: T) -> None:
        """
        Set element at index with O(1) time complexity.
        
        Args:
            index: The index to modify
            value: The new value
        """
        old_value = self._data[index]
        self._data[index] = value
        self._record_step(
            "modify",
            f"Set index {index}: {old_value} -> {value}",
            indices_modified=[index]
        )
    
    def __len__(self) -> int:
        """Return the length of the array."""
        return len(self._data)
    
    def append(self, value: T) -> None:
        """
        Append element to end with O(1) amortized time complexity.
        
        Args:
            value: The value to append
        """
        self._data.append(value)
        self._record_step(
            "append",
            f"Append {value} at index {len(self._data) - 1}",
            indices_modified=[len(self._data) - 1]
        )
    
    def insert(self, index: int, value: T) -> None:
        """
        Insert element at index with O(n) time complexity.
        
        All elements from index onward must shift right.
        
        Args:
            index: The index to insert at
            value: The value to insert
        """
        shifted_indices = list(range(index, len(self._data)))
        self._data.insert(index, value)
        self._record_step(
            "insert",
            f"Insert {value} at index {index}, shifting {len(shifted_indices)} elements",
            indices_modified=[index] + [i + 1 for i in shifted_indices]
        )
    
    def pop(self, index: int = -1) -> T:
        """
        Remove and return element at index.
        
        O(1) for last element, O(n) for others due to shifting.
        
        Args:
            index: The index to remove (default: last element)
            
        Returns:
            The removed element
        """
        actual_index = index if index >= 0 else len(self._data) + index
        value = self._data.pop(index)
        shifted_indices = list(range(actual_index, len(self._data)))
        self._record_step(
            "pop",
            f"Remove {value} from index {actual_index}, shifting {len(shifted_indices)} elements",
            indices_modified=shifted_indices
        )
        return value
    
    def swap(self, i: int, j: int) -> None:
        """
        Swap elements at indices i and j.
        
        Args:
            i: First index
            j: Second index
        """
        self._data[i], self._data[j] = self._data[j], self._data[i]
        self._record_step(
            "swap",
            f"Swap indices {i} and {j}: {self._data[j]} <-> {self._data[i]}",
            indices_modified=[i, j]
        )
    
    @property
    def data(self) -> list[T]:
        """Return a copy of the underlying data."""
        return list(self._data)
    
    @property
    def steps(self) -> list[ArrayStep]:
        """Return all recorded steps."""
        return self._steps
    
    def clear_steps(self) -> None:
        """Clear recorded steps for a new operation sequence."""
        self._steps = []
        self._step_count = 0
    
    def print_steps(self) -> None:
        """Print all recorded steps in a readable format."""
        print(f"\n{'='*60}")
        print(f"Array Operation Steps ({len(self._steps)} total)")
        print(f"{'='*60}")
        for step in self._steps:
            print(f"Step {step.step_number}: [{step.operation}] {step.description}")
            if step.pointer_positions:
                print(f"  Pointers: {step.pointer_positions}")
            print(f"  Array: {step.array_state}")
        print(f"{'='*60}\n")


def linear_search(arr: list[T], target: T) -> tuple[int, list[ArrayStep]]:
    """
    Search for target in array using linear search.
    
    Args:
        arr: The array to search
        target: The value to find
        
    Returns:
        Tuple of (index or -1, list of visualization steps)
        
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    steps: list[ArrayStep] = []
    step_count = 0
    
    for i, element in enumerate(arr):
        step_count += 1
        found = element == target
        steps.append(ArrayStep(
            step_number=step_count,
            operation="compare",
            description=f"Compare arr[{i}]={element} with target={target}: {'MATCH' if found else 'no match'}",
            indices_accessed=[i],
            array_state=list(arr)
        ))
        if found:
            return i, steps
    
    step_count += 1
    steps.append(ArrayStep(
        step_number=step_count,
        operation="not_found",
        description=f"Target {target} not found in array",
        array_state=list(arr)
    ))
    return -1, steps


def two_pointer_reverse(arr: list[T]) -> tuple[list[T], list[ArrayStep]]:
    """
    Reverse array in-place using two-pointer technique.
    
    Args:
        arr: The array to reverse (modified in place)
        
    Returns:
        Tuple of (reversed array, list of visualization steps)
        
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    steps: list[ArrayStep] = []
    step_count = 0
    result = list(arr)
    left, right = 0, len(result) - 1
    
    step_count += 1
    steps.append(ArrayStep(
        step_number=step_count,
        operation="initialize",
        description=f"Initialize pointers: left=0, right={right}",
        array_state=list(result),
        pointer_positions={"left": left, "right": right}
    ))
    
    while left < right:
        step_count += 1
        steps.append(ArrayStep(
            step_number=step_count,
            operation="swap",
            description=f"Swap arr[{left}]={result[left]} with arr[{right}]={result[right]}",
            indices_modified=[left, right],
            array_state=list(result),
            pointer_positions={"left": left, "right": right}
        ))
        result[left], result[right] = result[right], result[left]
        
        left += 1
        right -= 1
        
        step_count += 1
        steps.append(ArrayStep(
            step_number=step_count,
            operation="move_pointers",
            description=f"Move pointers: left={left}, right={right}",
            array_state=list(result),
            pointer_positions={"left": left, "right": right}
        ))
    
    step_count += 1
    steps.append(ArrayStep(
        step_number=step_count,
        operation="complete",
        description="Reversal complete - pointers crossed",
        array_state=list(result)
    ))
    
    return result, steps


def sliding_window_sum(arr: list[int], k: int) -> tuple[list[int], list[ArrayStep]]:
    """
    Calculate sum of each sliding window of size k.
    
    Args:
        arr: The array to process
        k: Window size
        
    Returns:
        Tuple of (list of window sums, list of visualization steps)
        
    Time Complexity: O(n)
    Space Complexity: O(1) excluding output
    """
    if len(arr) < k:
        return [], []
    
    steps: list[ArrayStep] = []
    step_count = 0
    results: list[int] = []
    
    window_sum = sum(arr[:k])
    results.append(window_sum)
    
    step_count += 1
    steps.append(ArrayStep(
        step_number=step_count,
        operation="initial_window",
        description=f"Initial window [0:{k}] sum = {window_sum}",
        indices_accessed=list(range(k)),
        array_state=list(arr),
        pointer_positions={"window_start": 0, "window_end": k - 1}
    ))
    
    for i in range(k, len(arr)):
        leaving = arr[i - k]
        entering = arr[i]
        window_sum = window_sum - leaving + entering
        results.append(window_sum)
        
        step_count += 1
        steps.append(ArrayStep(
            step_number=step_count,
            operation="slide_window",
            description=f"Slide window: remove {leaving}, add {entering}, new sum = {window_sum}",
            indices_accessed=[i - k, i],
            array_state=list(arr),
            pointer_positions={"window_start": i - k + 1, "window_end": i}
        ))
    
    return results, steps


def two_sum(arr: list[int], target: int) -> tuple[tuple[int, int] | None, list[ArrayStep]]:
    """
    Find two numbers that add up to target using hash map approach.
    
    Args:
        arr: The array to search
        target: The target sum
        
    Returns:
        Tuple of ((index1, index2) or None, list of visualization steps)
        
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    steps: list[ArrayStep] = []
    step_count = 0
    seen: dict[int, int] = {}
    
    for i, num in enumerate(arr):
        complement = target - num
        
        step_count += 1
        if complement in seen:
            steps.append(ArrayStep(
                step_number=step_count,
                operation="found",
                description=f"Found pair: arr[{seen[complement]}]={complement} + arr[{i}]={num} = {target}",
                indices_accessed=[seen[complement], i],
                array_state=list(arr)
            ))
            return (seen[complement], i), steps
        
        steps.append(ArrayStep(
            step_number=step_count,
            operation="store",
            description=f"Store arr[{i}]={num}, looking for complement {complement}",
            indices_accessed=[i],
            array_state=list(arr)
        ))
        seen[num] = i
    
    step_count += 1
    steps.append(ArrayStep(
        step_number=step_count,
        operation="not_found",
        description=f"No pair found that sums to {target}",
        array_state=list(arr)
    ))
    return None, steps


def demo() -> None:
    """Run demonstrations of array operations."""
    print("\n" + "="*60)
    print("ARRAY OPERATIONS DEMONSTRATIONS")
    print("="*60)
    
    # Visual Array Demo
    print("\n--- Visual Array Operations ---")
    va = VisualArray([10, 20, 30, 40, 50])
    print(f"Initial array: {va.data}")
    
    _ = va[2]
    va[2] = 35
    va.append(60)
    va.insert(1, 15)
    va.swap(0, 3)
    va.print_steps()
    
    # Linear Search Demo
    print("\n--- Linear Search ---")
    arr = [5, 2, 8, 1, 9, 3, 7]
    index, steps = linear_search(arr, 9)
    print(f"Searching for 9 in {arr}")
    print(f"Found at index: {index}")
    print(f"Steps taken: {len(steps)}")
    
    # Two-Pointer Reverse Demo
    print("\n--- Two-Pointer Reverse ---")
    arr = list("HELLO")
    reversed_arr, steps = two_pointer_reverse(arr)
    print(f"Original: {arr}")
    print(f"Reversed: {reversed_arr}")
    print(f"Swaps performed: {len([s for s in steps if s.operation == 'swap'])}")
    
    # Sliding Window Sum Demo
    print("\n--- Sliding Window Sum ---")
    arr = [2, 1, 5, 1, 3, 2]
    k = 3
    sums, steps = sliding_window_sum(arr, k)
    print(f"Array: {arr}, Window size: {k}")
    print(f"Window sums: {sums}")
    
    # Two Sum Demo
    print("\n--- Two Sum ---")
    arr = [2, 7, 11, 15]
    target = 9
    result, steps = two_sum(arr, target)
    print(f"Array: {arr}, Target: {target}")
    print(f"Indices: {result}")


if __name__ == "__main__":
    demo()
