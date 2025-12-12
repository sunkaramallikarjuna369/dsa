"""
Sorting Algorithms Implementation

This module provides implementations of various sorting algorithms
with step-by-step visualization tracking for 3D animation synchronization.

Algorithms included:
- Bubble Sort: O(n²) - Simple comparison-based sorting
- Selection Sort: O(n²) - Find minimum and place at beginning
- Insertion Sort: O(n²) - Build sorted array one element at a time
- Merge Sort: O(n log n) - Divide and conquer with merging
- Quick Sort: O(n log n) average - Partition around pivot

All functions include visualization step recording for 3D animation.
"""

from dataclasses import dataclass, field
from typing import TypeVar, Callable
import json

T = TypeVar('T')


@dataclass
class SortStep:
    """Represents a single step in a sorting algorithm for visualization."""
    step_number: int
    action: str
    description: str
    indices: list[int] = field(default_factory=list)
    values: list[int] = field(default_factory=list)
    array_state: list[int] = field(default_factory=list)
    extra: dict = field(default_factory=dict)


class SortVisualizer:
    """Tracks sorting steps for visualization."""
    
    def __init__(self) -> None:
        self.steps: list[SortStep] = []
        self.step_count: int = 0
        self.comparisons: int = 0
        self.swaps: int = 0
    
    def record(self, action: str, description: str, 
               indices: list[int] | None = None,
               values: list[int] | None = None,
               array_state: list[int] | None = None,
               **extra) -> None:
        """Record a visualization step."""
        self.step_count += 1
        step = SortStep(
            step_number=self.step_count,
            action=action,
            description=description,
            indices=indices or [],
            values=values or [],
            array_state=array_state or [],
            extra=extra
        )
        self.steps.append(step)
    
    def reset(self) -> None:
        """Reset the visualizer."""
        self.steps = []
        self.step_count = 0
        self.comparisons = 0
        self.swaps = 0
    
    def to_json(self) -> str:
        """Export steps as JSON."""
        return json.dumps([{
            'step': s.step_number,
            'action': s.action,
            'description': s.description,
            'indices': s.indices,
            'values': s.values,
            'array_state': s.array_state,
            **s.extra
        } for s in self.steps], indent=2)


def bubble_sort(arr: list[int], visualizer: SortVisualizer | None = None) -> list[int]:
    """
    Sort array using bubble sort algorithm.
    
    Repeatedly steps through the list, compares adjacent elements,
    and swaps them if they are in the wrong order. The pass through
    the list is repeated until the list is sorted.
    
    Args:
        arr: List of integers to sort
        visualizer: Optional visualizer for step tracking
    
    Returns:
        Sorted list (sorts in-place and returns same list)
    
    Time Complexity: O(n²) worst and average, O(n) best (already sorted)
    Space Complexity: O(1)
    Stable: Yes
    
    Example:
        >>> bubble_sort([64, 34, 25, 12, 22, 11, 90])
        [11, 12, 22, 25, 34, 64, 90]
    """
    n = len(arr)
    
    if visualizer:
        visualizer.record("init", f"Starting bubble sort on {n} elements",
                         array_state=arr.copy())
    
    for i in range(n):
        swapped = False
        
        if visualizer:
            visualizer.record("pass_start", f"Starting pass {i + 1}",
                             extra={"pass": i + 1, "unsorted_end": n - i - 1})
        
        for j in range(0, n - i - 1):
            if visualizer:
                visualizer.comparisons += 1
                visualizer.record("compare", f"Compare {arr[j]} and {arr[j + 1]}",
                                 indices=[j, j + 1],
                                 values=[arr[j], arr[j + 1]],
                                 array_state=arr.copy())
            
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                
                if visualizer:
                    visualizer.swaps += 1
                    visualizer.record("swap", f"Swap {arr[j + 1]} and {arr[j]}",
                                     indices=[j, j + 1],
                                     values=[arr[j], arr[j + 1]],
                                     array_state=arr.copy())
        
        if visualizer:
            visualizer.record("pass_end", f"Pass {i + 1} complete, largest element at position {n - i - 1}",
                             indices=[n - i - 1],
                             array_state=arr.copy())
        
        if not swapped:
            if visualizer:
                visualizer.record("early_exit", "No swaps in this pass, array is sorted",
                                 array_state=arr.copy())
            break
    
    if visualizer:
        visualizer.record("complete", "Bubble sort complete",
                         array_state=arr.copy(),
                         extra={"comparisons": visualizer.comparisons,
                               "swaps": visualizer.swaps})
    
    return arr


def selection_sort(arr: list[int], visualizer: SortVisualizer | None = None) -> list[int]:
    """
    Sort array using selection sort algorithm.
    
    Divides the array into sorted and unsorted portions. Repeatedly
    finds the minimum element from the unsorted portion and places
    it at the beginning of the unsorted portion.
    
    Args:
        arr: List of integers to sort
        visualizer: Optional visualizer for step tracking
    
    Returns:
        Sorted list (sorts in-place and returns same list)
    
    Time Complexity: O(n²) for all cases
    Space Complexity: O(1)
    Stable: No (can be made stable with modifications)
    
    Example:
        >>> selection_sort([64, 25, 12, 22, 11])
        [11, 12, 22, 25, 64]
    """
    n = len(arr)
    
    if visualizer:
        visualizer.record("init", f"Starting selection sort on {n} elements",
                         array_state=arr.copy())
    
    for i in range(n):
        min_idx = i
        
        if visualizer:
            visualizer.record("find_min_start", f"Finding minimum in unsorted portion [{i}, {n-1}]",
                             indices=[i],
                             values=[arr[i]],
                             extra={"current_min_idx": min_idx})
        
        for j in range(i + 1, n):
            if visualizer:
                visualizer.comparisons += 1
                visualizer.record("compare", f"Compare {arr[j]} with current min {arr[min_idx]}",
                                 indices=[j, min_idx],
                                 values=[arr[j], arr[min_idx]])
            
            if arr[j] < arr[min_idx]:
                min_idx = j
                if visualizer:
                    visualizer.record("new_min", f"New minimum found: {arr[min_idx]} at index {min_idx}",
                                     indices=[min_idx],
                                     values=[arr[min_idx]])
        
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            if visualizer:
                visualizer.swaps += 1
                visualizer.record("swap", f"Place minimum {arr[i]} at position {i}",
                                 indices=[i, min_idx],
                                 values=[arr[i], arr[min_idx]],
                                 array_state=arr.copy())
        
        if visualizer:
            visualizer.record("position_sorted", f"Position {i} is now sorted with value {arr[i]}",
                             indices=[i],
                             array_state=arr.copy())
    
    if visualizer:
        visualizer.record("complete", "Selection sort complete",
                         array_state=arr.copy(),
                         extra={"comparisons": visualizer.comparisons,
                               "swaps": visualizer.swaps})
    
    return arr


def insertion_sort(arr: list[int], visualizer: SortVisualizer | None = None) -> list[int]:
    """
    Sort array using insertion sort algorithm.
    
    Builds the sorted array one element at a time by repeatedly
    picking the next element and inserting it into its correct
    position in the sorted portion.
    
    Args:
        arr: List of integers to sort
        visualizer: Optional visualizer for step tracking
    
    Returns:
        Sorted list (sorts in-place and returns same list)
    
    Time Complexity: O(n²) worst and average, O(n) best (already sorted)
    Space Complexity: O(1)
    Stable: Yes
    
    Example:
        >>> insertion_sort([12, 11, 13, 5, 6])
        [5, 6, 11, 12, 13]
    """
    n = len(arr)
    
    if visualizer:
        visualizer.record("init", f"Starting insertion sort on {n} elements",
                         array_state=arr.copy())
    
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        if visualizer:
            visualizer.record("pick", f"Pick element {key} at index {i} for insertion",
                             indices=[i],
                             values=[key],
                             array_state=arr.copy())
        
        while j >= 0 and arr[j] > key:
            if visualizer:
                visualizer.comparisons += 1
                visualizer.record("compare_shift", f"Compare {key} with {arr[j]}: {arr[j]} > {key}, shift right",
                                 indices=[j, j + 1],
                                 values=[arr[j], key])
            
            arr[j + 1] = arr[j]
            
            if visualizer:
                visualizer.swaps += 1
                visualizer.record("shift", f"Shift {arr[j + 1]} from position {j} to {j + 1}",
                                 indices=[j, j + 1],
                                 array_state=arr.copy())
            j -= 1
        
        if j >= 0 and visualizer:
            visualizer.comparisons += 1
            visualizer.record("compare_stop", f"Compare {key} with {arr[j]}: {arr[j]} <= {key}, stop",
                             indices=[j],
                             values=[arr[j], key])
        
        arr[j + 1] = key
        
        if visualizer:
            visualizer.record("insert", f"Insert {key} at position {j + 1}",
                             indices=[j + 1],
                             values=[key],
                             array_state=arr.copy())
    
    if visualizer:
        visualizer.record("complete", "Insertion sort complete",
                         array_state=arr.copy(),
                         extra={"comparisons": visualizer.comparisons,
                               "swaps": visualizer.swaps})
    
    return arr


def merge_sort(arr: list[int], visualizer: SortVisualizer | None = None) -> list[int]:
    """
    Sort array using merge sort algorithm.
    
    Divides the array into halves, recursively sorts each half,
    then merges the sorted halves back together.
    
    Args:
        arr: List of integers to sort
        visualizer: Optional visualizer for step tracking
    
    Returns:
        Sorted list (creates new list, does not sort in-place)
    
    Time Complexity: O(n log n) for all cases
    Space Complexity: O(n)
    Stable: Yes
    
    Example:
        >>> merge_sort([38, 27, 43, 3, 9, 82, 10])
        [3, 9, 10, 27, 38, 43, 82]
    """
    if visualizer:
        visualizer.record("init", f"Starting merge sort on {len(arr)} elements",
                         array_state=arr.copy())
    
    def _merge_sort(arr: list[int], left: int, right: int, depth: int = 0) -> None:
        if left >= right:
            return
        
        mid = (left + right) // 2
        
        if visualizer:
            visualizer.record("divide", f"Divide [{left}:{right}] at mid={mid}",
                             indices=[left, mid, right],
                             array_state=arr.copy(),
                             extra={"depth": depth, "left": left, "mid": mid, "right": right})
        
        _merge_sort(arr, left, mid, depth + 1)
        _merge_sort(arr, mid + 1, right, depth + 1)
        
        _merge(arr, left, mid, right, depth)
    
    def _merge(arr: list[int], left: int, mid: int, right: int, depth: int) -> None:
        left_half = arr[left:mid + 1]
        right_half = arr[mid + 1:right + 1]
        
        if visualizer:
            visualizer.record("merge_start", f"Merge [{left}:{mid}] and [{mid+1}:{right}]",
                             indices=list(range(left, right + 1)),
                             values=left_half + right_half,
                             extra={"depth": depth, "left_half": left_half, "right_half": right_half})
        
        i = j = 0
        k = left
        
        while i < len(left_half) and j < len(right_half):
            if visualizer:
                visualizer.comparisons += 1
                visualizer.record("merge_compare", f"Compare {left_half[i]} and {right_half[j]}",
                                 values=[left_half[i], right_half[j]])
            
            if left_half[i] <= right_half[j]:
                arr[k] = left_half[i]
                if visualizer:
                    visualizer.record("merge_place", f"Place {left_half[i]} at position {k}",
                                     indices=[k],
                                     values=[left_half[i]])
                i += 1
            else:
                arr[k] = right_half[j]
                if visualizer:
                    visualizer.record("merge_place", f"Place {right_half[j]} at position {k}",
                                     indices=[k],
                                     values=[right_half[j]])
                j += 1
            k += 1
        
        while i < len(left_half):
            arr[k] = left_half[i]
            if visualizer:
                visualizer.record("merge_remaining", f"Place remaining {left_half[i]} at position {k}",
                                 indices=[k],
                                 values=[left_half[i]])
            i += 1
            k += 1
        
        while j < len(right_half):
            arr[k] = right_half[j]
            if visualizer:
                visualizer.record("merge_remaining", f"Place remaining {right_half[j]} at position {k}",
                                 indices=[k],
                                 values=[right_half[j]])
            j += 1
            k += 1
        
        if visualizer:
            visualizer.record("merge_complete", f"Merge complete for [{left}:{right}]",
                             indices=list(range(left, right + 1)),
                             array_state=arr.copy())
    
    result = arr.copy()
    _merge_sort(result, 0, len(result) - 1)
    
    if visualizer:
        visualizer.record("complete", "Merge sort complete",
                         array_state=result,
                         extra={"comparisons": visualizer.comparisons})
    
    return result


def quick_sort(arr: list[int], visualizer: SortVisualizer | None = None) -> list[int]:
    """
    Sort array using quick sort algorithm.
    
    Selects a pivot element and partitions the array so that
    elements smaller than the pivot come before it and elements
    larger come after. Recursively sorts the partitions.
    
    Args:
        arr: List of integers to sort
        visualizer: Optional visualizer for step tracking
    
    Returns:
        Sorted list (sorts in-place and returns same list)
    
    Time Complexity: O(n log n) average, O(n²) worst (sorted array with bad pivot)
    Space Complexity: O(log n) for recursion stack
    Stable: No
    
    Example:
        >>> quick_sort([10, 80, 30, 90, 40, 50, 70])
        [10, 30, 40, 50, 70, 80, 90]
    """
    if visualizer:
        visualizer.record("init", f"Starting quick sort on {len(arr)} elements",
                         array_state=arr.copy())
    
    def _partition(arr: list[int], low: int, high: int) -> int:
        pivot = arr[high]
        
        if visualizer:
            visualizer.record("pivot_select", f"Select pivot {pivot} at index {high}",
                             indices=[high],
                             values=[pivot],
                             array_state=arr.copy())
        
        i = low - 1
        
        for j in range(low, high):
            if visualizer:
                visualizer.comparisons += 1
                visualizer.record("compare", f"Compare {arr[j]} with pivot {pivot}",
                                 indices=[j, high],
                                 values=[arr[j], pivot],
                                 extra={"i": i, "j": j})
            
            if arr[j] <= pivot:
                i += 1
                if i != j:
                    arr[i], arr[j] = arr[j], arr[i]
                    if visualizer:
                        visualizer.swaps += 1
                        visualizer.record("swap", f"Swap {arr[j]} and {arr[i]} (i={i}, j={j})",
                                         indices=[i, j],
                                         values=[arr[i], arr[j]],
                                         array_state=arr.copy())
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        
        if visualizer:
            visualizer.swaps += 1
            visualizer.record("pivot_place", f"Place pivot {pivot} at final position {i + 1}",
                             indices=[i + 1],
                             values=[pivot],
                             array_state=arr.copy())
        
        return i + 1
    
    def _quick_sort(arr: list[int], low: int, high: int, depth: int = 0) -> None:
        if low < high:
            if visualizer:
                visualizer.record("partition_start", f"Partition [{low}:{high}]",
                                 indices=list(range(low, high + 1)),
                                 array_state=arr.copy(),
                                 extra={"depth": depth})
            
            pi = _partition(arr, low, high)
            
            if visualizer:
                visualizer.record("partition_done", f"Pivot at {pi}, recurse on [{low}:{pi-1}] and [{pi+1}:{high}]",
                                 indices=[pi],
                                 array_state=arr.copy())
            
            _quick_sort(arr, low, pi - 1, depth + 1)
            _quick_sort(arr, pi + 1, high, depth + 1)
    
    _quick_sort(arr, 0, len(arr) - 1)
    
    if visualizer:
        visualizer.record("complete", "Quick sort complete",
                         array_state=arr.copy(),
                         extra={"comparisons": visualizer.comparisons,
                               "swaps": visualizer.swaps})
    
    return arr


def counting_sort(arr: list[int], visualizer: SortVisualizer | None = None) -> list[int]:
    """
    Sort array using counting sort algorithm.
    
    Counts occurrences of each value and uses the counts to
    place elements in sorted order. Only works for non-negative integers.
    
    Args:
        arr: List of non-negative integers to sort
        visualizer: Optional visualizer for step tracking
    
    Returns:
        Sorted list (creates new list)
    
    Time Complexity: O(n + k) where k is the range of values
    Space Complexity: O(n + k)
    Stable: Yes
    
    Example:
        >>> counting_sort([4, 2, 2, 8, 3, 3, 1])
        [1, 2, 2, 3, 3, 4, 8]
    """
    if not arr:
        return []
    
    max_val = max(arr)
    
    if visualizer:
        visualizer.record("init", f"Starting counting sort, max value = {max_val}",
                         array_state=arr.copy())
    
    count = [0] * (max_val + 1)
    
    for num in arr:
        count[num] += 1
        if visualizer:
            visualizer.record("count", f"Count {num}: now {count[num]}",
                             indices=[num],
                             values=[count[num]])
    
    if visualizer:
        visualizer.record("count_complete", "Counting complete",
                         extra={"count_array": count.copy()})
    
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    
    if visualizer:
        visualizer.record("cumulative", "Cumulative count computed",
                         extra={"cumulative_count": count.copy()})
    
    output = [0] * len(arr)
    
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
        
        if visualizer:
            visualizer.record("place", f"Place {arr[i]} at position {count[arr[i]]}",
                             indices=[count[arr[i]]],
                             values=[arr[i]],
                             array_state=output.copy())
    
    if visualizer:
        visualizer.record("complete", "Counting sort complete",
                         array_state=output)
    
    return output


def heap_sort(arr: list[int], visualizer: SortVisualizer | None = None) -> list[int]:
    """
    Sort array using heap sort algorithm.
    
    Builds a max heap from the array, then repeatedly extracts
    the maximum element and places it at the end.
    
    Args:
        arr: List of integers to sort
        visualizer: Optional visualizer for step tracking
    
    Returns:
        Sorted list (sorts in-place and returns same list)
    
    Time Complexity: O(n log n) for all cases
    Space Complexity: O(1)
    Stable: No
    
    Example:
        >>> heap_sort([12, 11, 13, 5, 6, 7])
        [5, 6, 7, 11, 12, 13]
    """
    n = len(arr)
    
    if visualizer:
        visualizer.record("init", f"Starting heap sort on {n} elements",
                         array_state=arr.copy())
    
    def heapify(arr: list[int], n: int, i: int) -> None:
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < n:
            if visualizer:
                visualizer.comparisons += 1
            if arr[left] > arr[largest]:
                largest = left
        
        if right < n:
            if visualizer:
                visualizer.comparisons += 1
            if arr[right] > arr[largest]:
                largest = right
        
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            if visualizer:
                visualizer.swaps += 1
                visualizer.record("heapify_swap", f"Swap {arr[largest]} and {arr[i]}",
                                 indices=[i, largest],
                                 array_state=arr.copy())
            heapify(arr, n, largest)
    
    if visualizer:
        visualizer.record("build_heap_start", "Building max heap")
    
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    if visualizer:
        visualizer.record("build_heap_complete", "Max heap built",
                         array_state=arr.copy())
    
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        
        if visualizer:
            visualizer.swaps += 1
            visualizer.record("extract_max", f"Extract max {arr[i]} to position {i}",
                             indices=[0, i],
                             array_state=arr.copy())
        
        heapify(arr, i, 0)
    
    if visualizer:
        visualizer.record("complete", "Heap sort complete",
                         array_state=arr.copy(),
                         extra={"comparisons": visualizer.comparisons,
                               "swaps": visualizer.swaps})
    
    return arr


def demo() -> None:
    """Demonstrate sorting algorithms with visualization."""
    print("=" * 60)
    print("SORTING ALGORITHMS DEMONSTRATION")
    print("=" * 60)
    
    test_array = [64, 34, 25, 12, 22, 11, 90, 45]
    
    print(f"\nOriginal array: {test_array}")
    print("-" * 60)
    
    print("\n1. BUBBLE SORT")
    vis = SortVisualizer()
    arr = test_array.copy()
    result = bubble_sort(arr, vis)
    print(f"   Sorted: {result}")
    print(f"   Comparisons: {vis.comparisons}, Swaps: {vis.swaps}")
    
    print("\n2. SELECTION SORT")
    vis = SortVisualizer()
    arr = test_array.copy()
    result = selection_sort(arr, vis)
    print(f"   Sorted: {result}")
    print(f"   Comparisons: {vis.comparisons}, Swaps: {vis.swaps}")
    
    print("\n3. INSERTION SORT")
    vis = SortVisualizer()
    arr = test_array.copy()
    result = insertion_sort(arr, vis)
    print(f"   Sorted: {result}")
    print(f"   Comparisons: {vis.comparisons}, Swaps: {vis.swaps}")
    
    print("\n4. MERGE SORT")
    vis = SortVisualizer()
    arr = test_array.copy()
    result = merge_sort(arr, vis)
    print(f"   Sorted: {result}")
    print(f"   Comparisons: {vis.comparisons}")
    
    print("\n5. QUICK SORT")
    vis = SortVisualizer()
    arr = test_array.copy()
    result = quick_sort(arr, vis)
    print(f"   Sorted: {result}")
    print(f"   Comparisons: {vis.comparisons}, Swaps: {vis.swaps}")
    
    print("\n6. COUNTING SORT")
    vis = SortVisualizer()
    arr = test_array.copy()
    result = counting_sort(arr, vis)
    print(f"   Sorted: {result}")
    
    print("\n7. HEAP SORT")
    vis = SortVisualizer()
    arr = test_array.copy()
    result = heap_sort(arr, vis)
    print(f"   Sorted: {result}")
    print(f"   Comparisons: {vis.comparisons}, Swaps: {vis.swaps}")
    
    print("\n" + "=" * 60)
    print("VISUALIZATION STEPS EXAMPLE (Bubble Sort first 5 steps)")
    print("=" * 60)
    
    vis = SortVisualizer()
    arr = [5, 3, 8, 1]
    bubble_sort(arr, vis)
    
    for step in vis.steps[:5]:
        print(f"\nStep {step.step_number}: {step.action}")
        print(f"  Description: {step.description}")
        if step.indices:
            print(f"  Indices: {step.indices}")
        if step.array_state:
            print(f"  Array: {step.array_state}")


if __name__ == "__main__":
    demo()
