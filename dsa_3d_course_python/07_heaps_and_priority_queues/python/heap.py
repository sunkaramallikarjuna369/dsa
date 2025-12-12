"""
Heap Module

This module provides implementations of heap data structures
with step-by-step tracking for 3D visualization synchronization.

Includes both max-heap and min-heap implementations.
"""

from typing import Any, TypeVar, Generic, Callable
from dataclasses import dataclass, field
import heapq

T = TypeVar('T')


@dataclass
class HeapStep:
    """Represents a single step in heap visualization."""
    step_number: int
    operation: str
    description: str
    value: Any = None
    index: int = -1
    parent_index: int = -1
    heap_state: list[Any] = field(default_factory=list)
    comparison: str = ""
    swap: bool = False


class MaxHeap(Generic[T]):
    """
    Max-heap implementation with visualization tracking.
    
    In a max-heap, the parent is always greater than or equal to its children.
    The maximum element is always at the root.
    
    Time Complexity:
    - Insert: O(log n)
    - Extract Max: O(log n)
    - Peek Max: O(1)
    - Heapify: O(n)
    """
    
    def __init__(self) -> None:
        """Initialize an empty max-heap."""
        self._data: list[T] = []
        self._steps: list[HeapStep] = []
        self._step_count: int = 0
    
    def _record_step(
        self,
        operation: str,
        description: str,
        value: Any = None,
        index: int = -1,
        parent_index: int = -1,
        comparison: str = "",
        swap: bool = False
    ) -> None:
        """Record a visualization step."""
        self._step_count += 1
        step = HeapStep(
            step_number=self._step_count,
            operation=operation,
            description=description,
            value=value,
            index=index,
            parent_index=parent_index,
            heap_state=list(self._data),
            comparison=comparison,
            swap=swap
        )
        self._steps.append(step)
    
    def clear_steps(self) -> None:
        """Clear recorded steps."""
        self._steps = []
        self._step_count = 0
    
    @property
    def steps(self) -> list[HeapStep]:
        """Return all recorded steps."""
        return self._steps
    
    def _parent(self, index: int) -> int:
        """Return parent index."""
        return (index - 1) // 2
    
    def _left_child(self, index: int) -> int:
        """Return left child index."""
        return 2 * index + 1
    
    def _right_child(self, index: int) -> int:
        """Return right child index."""
        return 2 * index + 2
    
    def _swap(self, i: int, j: int) -> None:
        """Swap elements at indices i and j."""
        self._data[i], self._data[j] = self._data[j], self._data[i]
    
    def _bubble_up(self, index: int) -> None:
        """Bubble up element at index to maintain heap property."""
        while index > 0:
            parent = self._parent(index)
            
            self._record_step(
                "compare",
                f"Compare {self._data[index]} with parent {self._data[parent]}",
                value=self._data[index],
                index=index,
                parent_index=parent,
                comparison=f"{self._data[index]} > {self._data[parent]}?"
            )
            
            if self._data[index] > self._data[parent]:
                self._record_step(
                    "swap",
                    f"Swap {self._data[index]} with {self._data[parent]}",
                    value=self._data[index],
                    index=index,
                    parent_index=parent,
                    swap=True
                )
                self._swap(index, parent)
                index = parent
            else:
                self._record_step(
                    "stop",
                    f"Heap property satisfied, stop bubbling up",
                    value=self._data[index],
                    index=index
                )
                break
    
    def _bubble_down(self, index: int) -> None:
        """Bubble down element at index to maintain heap property."""
        size = len(self._data)
        
        while True:
            largest = index
            left = self._left_child(index)
            right = self._right_child(index)
            
            if left < size:
                self._record_step(
                    "compare_child",
                    f"Compare with left child {self._data[left]}",
                    value=self._data[index],
                    index=index,
                    comparison=f"{self._data[left]} > {self._data[largest]}?"
                )
                if self._data[left] > self._data[largest]:
                    largest = left
            
            if right < size:
                self._record_step(
                    "compare_child",
                    f"Compare with right child {self._data[right]}",
                    value=self._data[index],
                    index=index,
                    comparison=f"{self._data[right]} > {self._data[largest]}?"
                )
                if self._data[right] > self._data[largest]:
                    largest = right
            
            if largest != index:
                self._record_step(
                    "swap",
                    f"Swap {self._data[index]} with {self._data[largest]}",
                    value=self._data[index],
                    index=index,
                    swap=True
                )
                self._swap(index, largest)
                index = largest
            else:
                self._record_step(
                    "stop",
                    f"Heap property satisfied, stop bubbling down",
                    value=self._data[index],
                    index=index
                )
                break
    
    def insert(self, value: T) -> None:
        """
        Insert a value into the heap.
        
        Time Complexity: O(log n)
        """
        self._record_step(
            "insert_start",
            f"Inserting {value} into heap",
            value=value
        )
        
        self._data.append(value)
        index = len(self._data) - 1
        
        self._record_step(
            "insert_end",
            f"Placed {value} at index {index}",
            value=value,
            index=index
        )
        
        self._bubble_up(index)
        
        self._record_step(
            "insert_complete",
            f"Insert complete. Heap: {self._data}",
            value=value
        )
    
    def extract_max(self) -> T | None:
        """
        Remove and return the maximum element.
        
        Time Complexity: O(log n)
        """
        if not self._data:
            self._record_step(
                "extract_empty",
                "Cannot extract from empty heap"
            )
            return None
        
        max_val = self._data[0]
        
        self._record_step(
            "extract_start",
            f"Extracting maximum: {max_val}",
            value=max_val,
            index=0
        )
        
        last_val = self._data.pop()
        
        if self._data:
            self._record_step(
                "move_last",
                f"Moving last element {last_val} to root",
                value=last_val,
                index=0
            )
            self._data[0] = last_val
            self._bubble_down(0)
        
        self._record_step(
            "extract_complete",
            f"Extracted {max_val}. Heap: {self._data}",
            value=max_val
        )
        
        return max_val
    
    def peek(self) -> T | None:
        """Return the maximum element without removing it."""
        return self._data[0] if self._data else None
    
    def size(self) -> int:
        """Return the number of elements."""
        return len(self._data)
    
    def is_empty(self) -> bool:
        """Check if heap is empty."""
        return len(self._data) == 0
    
    def to_list(self) -> list[T]:
        """Return heap as a list."""
        return list(self._data)
    
    @classmethod
    def heapify(cls, arr: list[T]) -> 'MaxHeap[T]':
        """
        Build a max-heap from an array in O(n) time.
        """
        heap: MaxHeap[T] = cls()
        heap._data = list(arr)
        
        heap._record_step(
            "heapify_start",
            f"Heapifying array: {arr}"
        )
        
        # Start from last non-leaf node
        start = len(arr) // 2 - 1
        
        for i in range(start, -1, -1):
            heap._record_step(
                "heapify_node",
                f"Processing node at index {i}",
                index=i
            )
            heap._bubble_down(i)
        
        heap._record_step(
            "heapify_complete",
            f"Heapify complete. Heap: {heap._data}"
        )
        
        return heap


class MinHeap(Generic[T]):
    """
    Min-heap implementation with visualization tracking.
    
    In a min-heap, the parent is always less than or equal to its children.
    The minimum element is always at the root.
    """
    
    def __init__(self) -> None:
        """Initialize an empty min-heap."""
        self._data: list[T] = []
        self._steps: list[HeapStep] = []
        self._step_count: int = 0
    
    def _record_step(
        self,
        operation: str,
        description: str,
        value: Any = None,
        index: int = -1,
        parent_index: int = -1,
        comparison: str = "",
        swap: bool = False
    ) -> None:
        """Record a visualization step."""
        self._step_count += 1
        step = HeapStep(
            step_number=self._step_count,
            operation=operation,
            description=description,
            value=value,
            index=index,
            parent_index=parent_index,
            heap_state=list(self._data),
            comparison=comparison,
            swap=swap
        )
        self._steps.append(step)
    
    def clear_steps(self) -> None:
        """Clear recorded steps."""
        self._steps = []
        self._step_count = 0
    
    @property
    def steps(self) -> list[HeapStep]:
        """Return all recorded steps."""
        return self._steps
    
    def _parent(self, index: int) -> int:
        return (index - 1) // 2
    
    def _left_child(self, index: int) -> int:
        return 2 * index + 1
    
    def _right_child(self, index: int) -> int:
        return 2 * index + 2
    
    def _swap(self, i: int, j: int) -> None:
        self._data[i], self._data[j] = self._data[j], self._data[i]
    
    def _bubble_up(self, index: int) -> None:
        """Bubble up for min-heap (smaller values rise)."""
        while index > 0:
            parent = self._parent(index)
            if self._data[index] < self._data[parent]:
                self._swap(index, parent)
                index = parent
            else:
                break
    
    def _bubble_down(self, index: int) -> None:
        """Bubble down for min-heap (larger values sink)."""
        size = len(self._data)
        
        while True:
            smallest = index
            left = self._left_child(index)
            right = self._right_child(index)
            
            if left < size and self._data[left] < self._data[smallest]:
                smallest = left
            
            if right < size and self._data[right] < self._data[smallest]:
                smallest = right
            
            if smallest != index:
                self._swap(index, smallest)
                index = smallest
            else:
                break
    
    def insert(self, value: T) -> None:
        """Insert a value into the min-heap."""
        self._data.append(value)
        self._bubble_up(len(self._data) - 1)
    
    def extract_min(self) -> T | None:
        """Remove and return the minimum element."""
        if not self._data:
            return None
        
        min_val = self._data[0]
        last_val = self._data.pop()
        
        if self._data:
            self._data[0] = last_val
            self._bubble_down(0)
        
        return min_val
    
    def peek(self) -> T | None:
        """Return the minimum element without removing it."""
        return self._data[0] if self._data else None
    
    def size(self) -> int:
        return len(self._data)
    
    def is_empty(self) -> bool:
        return len(self._data) == 0
    
    def to_list(self) -> list[T]:
        return list(self._data)


def find_k_largest(nums: list[int], k: int) -> list[int]:
    """
    Find the k largest elements using a min-heap.
    
    Time Complexity: O(n log k)
    Space Complexity: O(k)
    """
    if k <= 0 or not nums:
        return []
    
    # Use min-heap of size k
    min_heap: list[int] = []
    
    for num in nums:
        if len(min_heap) < k:
            heapq.heappush(min_heap, num)
        elif num > min_heap[0]:
            heapq.heapreplace(min_heap, num)
    
    return sorted(min_heap, reverse=True)


def find_k_smallest(nums: list[int], k: int) -> list[int]:
    """
    Find the k smallest elements using a max-heap (negated values).
    
    Time Complexity: O(n log k)
    Space Complexity: O(k)
    """
    if k <= 0 or not nums:
        return []
    
    # Use max-heap (negate values) of size k
    max_heap: list[int] = []
    
    for num in nums:
        if len(max_heap) < k:
            heapq.heappush(max_heap, -num)
        elif num < -max_heap[0]:
            heapq.heapreplace(max_heap, -num)
    
    return sorted([-x for x in max_heap])


def heap_sort(arr: list[T]) -> list[T]:
    """
    Sort array using heap sort.
    
    Time Complexity: O(n log n)
    Space Complexity: O(1) in-place
    """
    result = list(arr)
    n = len(result)
    
    # Build max-heap
    for i in range(n // 2 - 1, -1, -1):
        _heapify_down(result, n, i)
    
    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        result[0], result[i] = result[i], result[0]
        _heapify_down(result, i, 0)
    
    return result


def _heapify_down(arr: list[T], size: int, index: int) -> None:
    """Helper for heap sort - bubble down."""
    largest = index
    left = 2 * index + 1
    right = 2 * index + 2
    
    if left < size and arr[left] > arr[largest]:
        largest = left
    
    if right < size and arr[right] > arr[largest]:
        largest = right
    
    if largest != index:
        arr[index], arr[largest] = arr[largest], arr[index]
        _heapify_down(arr, size, largest)


def demo() -> None:
    """Run demonstrations of heap operations."""
    print("\n" + "="*60)
    print("HEAP DEMONSTRATIONS")
    print("="*60)
    
    # Max-Heap Operations
    print("\n--- Max-Heap Operations ---")
    max_heap: MaxHeap[int] = MaxHeap()
    
    values = [30, 50, 80, 20, 60, 40, 90]
    print(f"Inserting values: {values}")
    
    for val in values:
        max_heap.insert(val)
    
    print(f"Max-Heap: {max_heap.to_list()}")
    print(f"Maximum: {max_heap.peek()}")
    
    print("\nExtracting maximums:")
    while not max_heap.is_empty():
        print(f"  Extracted: {max_heap.extract_max()}")
    
    # Heapify
    print("\n--- Heapify Operation ---")
    arr = [30, 50, 80, 20, 60, 40, 90]
    print(f"Original array: {arr}")
    heap = MaxHeap.heapify(arr)
    print(f"After heapify: {heap.to_list()}")
    
    # K Largest Elements
    print("\n--- K Largest Elements ---")
    nums = [3, 2, 1, 5, 6, 4]
    k = 3
    print(f"Array: {nums}")
    print(f"K = {k}")
    print(f"K largest: {find_k_largest(nums, k)}")
    
    # Heap Sort
    print("\n--- Heap Sort ---")
    unsorted = [64, 34, 25, 12, 22, 11, 90]
    print(f"Unsorted: {unsorted}")
    print(f"Sorted: {heap_sort(unsorted)}")
    
    # Using Python's heapq
    print("\n--- Python heapq Module ---")
    import heapq
    pq: list[int] = []
    for val in [5, 3, 7, 1, 9]:
        heapq.heappush(pq, val)
    print(f"Min-heap using heapq: {pq}")
    print(f"Smallest: {heapq.heappop(pq)}")


if __name__ == "__main__":
    demo()
