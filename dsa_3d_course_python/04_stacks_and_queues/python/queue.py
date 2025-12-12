"""
Queue Module

This module provides implementations of queue data structure
with step-by-step tracking for 3D visualization synchronization.

A queue follows the First-In-First-Out (FIFO) principle where
the first element added is the first to be removed.
"""

from typing import Any, TypeVar, Generic
from dataclasses import dataclass, field
from collections import deque

T = TypeVar('T')


@dataclass
class QueueStep:
    """Represents a single step in queue visualization."""
    step_number: int
    operation: str
    description: str
    element_value: Any = None
    queue_state: list[Any] = field(default_factory=list)
    front_index: int = 0
    rear_index: int = -1


class Queue(Generic[T]):
    """
    A queue implementation using Python's deque with visualization tracking.
    
    Supports standard queue operations: enqueue, dequeue, front, is_empty.
    All operations are O(1) time complexity.
    """
    
    def __init__(self, capacity: int | None = None) -> None:
        """
        Initialize an empty queue.
        
        Args:
            capacity: Optional maximum capacity (None for unlimited)
        """
        self._data: deque[T] = deque()
        self._capacity = capacity
        self._steps: list[QueueStep] = []
        self._step_count: int = 0
    
    def _record_step(
        self,
        operation: str,
        description: str,
        element_value: Any = None
    ) -> None:
        """Record a visualization step."""
        self._step_count += 1
        step = QueueStep(
            step_number=self._step_count,
            operation=operation,
            description=description,
            element_value=element_value,
            queue_state=list(self._data),
            front_index=0,
            rear_index=len(self._data) - 1
        )
        self._steps.append(step)
    
    def clear_steps(self) -> None:
        """Clear recorded steps for a new operation sequence."""
        self._steps = []
        self._step_count = 0
    
    @property
    def steps(self) -> list[QueueStep]:
        """Return all recorded steps."""
        return self._steps
    
    def enqueue(self, item: T) -> bool:
        """
        Add an item to the rear of the queue.
        
        Time Complexity: O(1)
        
        Args:
            item: The item to add
            
        Returns:
            True if successful, False if queue is full
        """
        if self._capacity is not None and len(self._data) >= self._capacity:
            self._record_step(
                "overflow",
                f"Queue overflow! Cannot enqueue {item} - queue is full",
                element_value=item
            )
            return False
        
        self._record_step(
            "enqueue_start",
            f"Enqueueing {item} at rear of queue",
            element_value=item
        )
        
        self._data.append(item)
        
        self._record_step(
            "enqueue_complete",
            f"Enqueued {item} - now at rear (position {len(self._data) - 1})",
            element_value=item
        )
        
        return True
    
    def dequeue(self) -> T | None:
        """
        Remove and return the front item from the queue.
        
        Time Complexity: O(1)
        
        Returns:
            The front item, or None if queue is empty
        """
        if self.is_empty():
            self._record_step(
                "underflow",
                "Queue underflow! Cannot dequeue from empty queue"
            )
            return None
        
        item = self._data[0]
        self._record_step(
            "dequeue_start",
            f"Dequeueing front element: {item}",
            element_value=item
        )
        
        self._data.popleft()
        
        self._record_step(
            "dequeue_complete",
            f"Dequeued {item} - new front is {self._data[0] if self._data else 'empty'}",
            element_value=item
        )
        
        return item
    
    def front(self) -> T | None:
        """
        Return the front item without removing it.
        
        Time Complexity: O(1)
        
        Returns:
            The front item, or None if queue is empty
        """
        if self.is_empty():
            self._record_step(
                "front_empty",
                "Cannot get front - queue is empty"
            )
            return None
        
        item = self._data[0]
        self._record_step(
            "front",
            f"Front element: {item}",
            element_value=item
        )
        
        return item
    
    def rear(self) -> T | None:
        """
        Return the rear item without removing it.
        
        Time Complexity: O(1)
        
        Returns:
            The rear item, or None if queue is empty
        """
        if self.is_empty():
            return None
        return self._data[-1]
    
    def is_empty(self) -> bool:
        """Check if the queue is empty."""
        return len(self._data) == 0
    
    def is_full(self) -> bool:
        """Check if the queue is full (only relevant if capacity is set)."""
        if self._capacity is None:
            return False
        return len(self._data) >= self._capacity
    
    def size(self) -> int:
        """Return the number of elements in the queue."""
        return len(self._data)
    
    def to_list(self) -> list[T]:
        """Return a copy of the queue as a list (front to rear)."""
        return list(self._data)
    
    def __len__(self) -> int:
        return len(self._data)
    
    def __repr__(self) -> str:
        return f"Queue({list(self._data)})"
    
    def print_steps(self) -> None:
        """Print all recorded steps."""
        print(f"\n{'='*60}")
        print(f"Queue Operation Steps ({len(self._steps)} total)")
        print(f"{'='*60}")
        for step in self._steps:
            print(f"Step {step.step_number}: [{step.operation}] {step.description}")
            print(f"  Queue: {step.queue_state} (front: {step.front_index}, rear: {step.rear_index})")
        print(f"{'='*60}\n")


class CircularQueue(Generic[T]):
    """
    A circular queue implementation using a fixed-size array.
    
    Uses front and rear pointers that wrap around the array,
    making efficient use of space.
    """
    
    def __init__(self, capacity: int) -> None:
        """
        Initialize a circular queue with fixed capacity.
        
        Args:
            capacity: Maximum number of elements
        """
        self._data: list[T | None] = [None] * capacity
        self._capacity = capacity
        self._front = 0
        self._rear = -1
        self._size = 0
    
    def enqueue(self, item: T) -> bool:
        """Add item to rear - O(1)."""
        if self.is_full():
            return False
        
        self._rear = (self._rear + 1) % self._capacity
        self._data[self._rear] = item
        self._size += 1
        return True
    
    def dequeue(self) -> T | None:
        """Remove and return front item - O(1)."""
        if self.is_empty():
            return None
        
        item = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % self._capacity
        self._size -= 1
        return item
    
    def front(self) -> T | None:
        """Return front item without removing - O(1)."""
        if self.is_empty():
            return None
        return self._data[self._front]
    
    def is_empty(self) -> bool:
        """Check if queue is empty."""
        return self._size == 0
    
    def is_full(self) -> bool:
        """Check if queue is full."""
        return self._size == self._capacity
    
    def size(self) -> int:
        """Return number of elements."""
        return self._size


class LinkedQueue(Generic[T]):
    """
    A queue implementation using a linked list.
    
    Maintains front and rear pointers for O(1) operations.
    """
    
    class Node(Generic[T]):
        """A node in the linked queue."""
        def __init__(self, value: T) -> None:
            self.value: T = value
            self.next: LinkedQueue.Node[T] | None = None
    
    def __init__(self) -> None:
        """Initialize an empty linked queue."""
        self._front: LinkedQueue.Node[T] | None = None
        self._rear: LinkedQueue.Node[T] | None = None
        self._size: int = 0
    
    def enqueue(self, item: T) -> None:
        """Add item to rear - O(1)."""
        new_node = LinkedQueue.Node(item)
        
        if self._rear is None:
            self._front = self._rear = new_node
        else:
            self._rear.next = new_node
            self._rear = new_node
        
        self._size += 1
    
    def dequeue(self) -> T | None:
        """Remove and return front item - O(1)."""
        if self._front is None:
            return None
        
        item = self._front.value
        self._front = self._front.next
        
        if self._front is None:
            self._rear = None
        
        self._size -= 1
        return item
    
    def front(self) -> T | None:
        """Return front item without removing - O(1)."""
        return self._front.value if self._front else None
    
    def is_empty(self) -> bool:
        """Check if queue is empty."""
        return self._front is None
    
    def size(self) -> int:
        """Return number of elements."""
        return self._size
    
    def to_list(self) -> list[T]:
        """Convert to list (front to rear)."""
        result: list[T] = []
        current = self._front
        while current:
            result.append(current.value)
            current = current.next
        return result


class Deque(Generic[T]):
    """
    A double-ended queue (deque) implementation.
    
    Supports insertion and deletion at both ends in O(1) time.
    """
    
    def __init__(self) -> None:
        """Initialize an empty deque."""
        self._data: deque[T] = deque()
    
    def add_front(self, item: T) -> None:
        """Add item to front - O(1)."""
        self._data.appendleft(item)
    
    def add_rear(self, item: T) -> None:
        """Add item to rear - O(1)."""
        self._data.append(item)
    
    def remove_front(self) -> T | None:
        """Remove and return front item - O(1)."""
        if self.is_empty():
            return None
        return self._data.popleft()
    
    def remove_rear(self) -> T | None:
        """Remove and return rear item - O(1)."""
        if self.is_empty():
            return None
        return self._data.pop()
    
    def front(self) -> T | None:
        """Return front item without removing - O(1)."""
        return self._data[0] if self._data else None
    
    def rear(self) -> T | None:
        """Return rear item without removing - O(1)."""
        return self._data[-1] if self._data else None
    
    def is_empty(self) -> bool:
        """Check if deque is empty."""
        return len(self._data) == 0
    
    def size(self) -> int:
        """Return number of elements."""
        return len(self._data)
    
    def to_list(self) -> list[T]:
        """Convert to list."""
        return list(self._data)


class QueueUsingStacks(Generic[T]):
    """
    A queue implemented using two stacks.
    
    Demonstrates how to achieve FIFO behavior using LIFO structures.
    Amortized O(1) for all operations.
    """
    
    def __init__(self) -> None:
        """Initialize queue with two stacks."""
        self._stack_in: list[T] = []   # For enqueue
        self._stack_out: list[T] = []  # For dequeue
    
    def enqueue(self, item: T) -> None:
        """Add item to queue - O(1)."""
        self._stack_in.append(item)
    
    def dequeue(self) -> T | None:
        """Remove and return front item - Amortized O(1)."""
        if not self._stack_out:
            while self._stack_in:
                self._stack_out.append(self._stack_in.pop())
        
        if not self._stack_out:
            return None
        
        return self._stack_out.pop()
    
    def front(self) -> T | None:
        """Return front item without removing - Amortized O(1)."""
        if not self._stack_out:
            while self._stack_in:
                self._stack_out.append(self._stack_in.pop())
        
        return self._stack_out[-1] if self._stack_out else None
    
    def is_empty(self) -> bool:
        """Check if queue is empty."""
        return len(self._stack_in) == 0 and len(self._stack_out) == 0
    
    def size(self) -> int:
        """Return number of elements."""
        return len(self._stack_in) + len(self._stack_out)


def sliding_window_maximum(nums: list[int], k: int) -> tuple[list[int], list[QueueStep]]:
    """
    Find maximum in each sliding window of size k using a deque.
    
    Args:
        nums: Input array
        k: Window size
        
    Returns:
        Tuple of (list of maximums, visualization steps)
        
    Time Complexity: O(n)
    Space Complexity: O(k)
    """
    steps: list[QueueStep] = []
    step_count = 0
    
    if not nums or k == 0:
        return [], steps
    
    result: list[int] = []
    dq: deque[int] = deque()  # Store indices
    
    step_count += 1
    steps.append(QueueStep(
        step_number=step_count,
        operation="start",
        description=f"Finding max in sliding windows of size {k}",
        queue_state=list(dq)
    ))
    
    for i in range(len(nums)):
        # Remove indices outside current window
        while dq and dq[0] < i - k + 1:
            removed = dq.popleft()
            step_count += 1
            steps.append(QueueStep(
                step_number=step_count,
                operation="remove_old",
                description=f"Remove index {removed} (outside window)",
                queue_state=list(dq)
            ))
        
        # Remove smaller elements from rear
        while dq and nums[dq[-1]] < nums[i]:
            removed = dq.pop()
            step_count += 1
            steps.append(QueueStep(
                step_number=step_count,
                operation="remove_smaller",
                description=f"Remove index {removed} (value {nums[removed]} < {nums[i]})",
                queue_state=list(dq)
            ))
        
        dq.append(i)
        step_count += 1
        steps.append(QueueStep(
            step_number=step_count,
            operation="add",
            description=f"Add index {i} (value {nums[i]})",
            element_value=nums[i],
            queue_state=list(dq)
        ))
        
        if i >= k - 1:
            max_val = nums[dq[0]]
            result.append(max_val)
            step_count += 1
            steps.append(QueueStep(
                step_number=step_count,
                operation="window_max",
                description=f"Window [{i-k+1}:{i+1}] max = {max_val}",
                element_value=max_val,
                queue_state=list(dq)
            ))
    
    return result, steps


def demo() -> None:
    """Run demonstrations of queue operations."""
    print("\n" + "="*60)
    print("QUEUE DEMONSTRATIONS")
    print("="*60)
    
    # Basic Queue Operations
    print("\n--- Basic Queue Operations ---")
    queue = Queue[int](capacity=5)
    
    print("Enqueueing 10, 20, 30:")
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print(f"Queue: {queue.to_list()}")
    
    print(f"\nFront: {queue.front()}")
    print(f"Dequeue: {queue.dequeue()}")
    print(f"Queue after dequeue: {queue.to_list()}")
    queue.print_steps()
    
    # Queue Using Stacks
    print("\n--- Queue Using Two Stacks ---")
    q_stacks = QueueUsingStacks[str]()
    for item in ['A', 'B', 'C', 'D']:
        q_stacks.enqueue(item)
    
    print(f"Enqueued: A, B, C, D")
    print(f"Dequeue order: ", end="")
    while not q_stacks.is_empty():
        print(q_stacks.dequeue(), end=" ")
    print()
    
    # Sliding Window Maximum
    print("\n--- Sliding Window Maximum ---")
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    result, steps = sliding_window_maximum(nums, k)
    print(f"Array: {nums}")
    print(f"Window size: {k}")
    print(f"Maximums: {result}")
    
    # Deque Operations
    print("\n--- Deque (Double-Ended Queue) ---")
    dq = Deque[int]()
    dq.add_rear(1)
    dq.add_rear(2)
    dq.add_front(0)
    dq.add_rear(3)
    print(f"After adding 0 (front), 1, 2, 3 (rear): {dq.to_list()}")
    print(f"Remove front: {dq.remove_front()}")
    print(f"Remove rear: {dq.remove_rear()}")
    print(f"Remaining: {dq.to_list()}")


if __name__ == "__main__":
    demo()
