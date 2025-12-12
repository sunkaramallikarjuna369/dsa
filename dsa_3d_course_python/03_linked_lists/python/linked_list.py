"""
Linked List Module

This module provides implementations of singly and doubly linked lists
with step-by-step tracking for 3D visualization synchronization.

Linked lists store elements in nodes connected by pointers, enabling
efficient insertions and deletions at the cost of O(n) random access.
"""

from typing import Any, TypeVar, Generic, Iterator
from dataclasses import dataclass, field

T = TypeVar('T')


@dataclass
class LinkedListStep:
    """Represents a single step in linked list visualization."""
    step_number: int
    operation: str
    description: str
    current_node_value: Any = None
    affected_nodes: list[Any] = field(default_factory=list)
    pointer_changes: dict[str, Any] = field(default_factory=dict)
    list_state: list[Any] = field(default_factory=list)


class SinglyNode(Generic[T]):
    """
    A node in a singly linked list.
    
    Each node contains a value and a reference to the next node.
    
    Attributes:
        value: The data stored in this node
        next: Reference to the next node, or None if this is the tail
    """
    
    def __init__(self, value: T) -> None:
        self.value: T = value
        self.next: SinglyNode[T] | None = None
    
    def __repr__(self) -> str:
        return f"Node({self.value})"


class SinglyLinkedList(Generic[T]):
    """
    A singly linked list implementation with visualization tracking.
    
    Supports standard operations: insert, delete, search, and traversal.
    All operations are tracked for 3D animation synchronization.
    """
    
    def __init__(self) -> None:
        self._head: SinglyNode[T] | None = None
        self._size: int = 0
        self._steps: list[LinkedListStep] = []
        self._step_count: int = 0
    
    def _record_step(
        self,
        operation: str,
        description: str,
        current_node_value: Any = None,
        affected_nodes: list[Any] | None = None,
        pointer_changes: dict[str, Any] | None = None
    ) -> None:
        """Record a visualization step."""
        self._step_count += 1
        step = LinkedListStep(
            step_number=self._step_count,
            operation=operation,
            description=description,
            current_node_value=current_node_value,
            affected_nodes=affected_nodes or [],
            pointer_changes=pointer_changes or {},
            list_state=self.to_list()
        )
        self._steps.append(step)
    
    def clear_steps(self) -> None:
        """Clear recorded steps for a new operation sequence."""
        self._steps = []
        self._step_count = 0
    
    @property
    def steps(self) -> list[LinkedListStep]:
        """Return all recorded steps."""
        return self._steps
    
    @property
    def head(self) -> SinglyNode[T] | None:
        """Return the head node."""
        return self._head
    
    def __len__(self) -> int:
        """Return the number of elements in the list."""
        return self._size
    
    def is_empty(self) -> bool:
        """Check if the list is empty."""
        return self._head is None
    
    def to_list(self) -> list[T]:
        """Convert linked list to Python list."""
        result: list[T] = []
        current = self._head
        while current:
            result.append(current.value)
            current = current.next
        return result
    
    def insert_at_head(self, value: T) -> None:
        """
        Insert a new node at the head of the list.
        
        Time Complexity: O(1)
        
        Args:
            value: The value to insert
        """
        new_node = SinglyNode(value)
        self._record_step(
            "create_node",
            f"Create new node with value {value}",
            current_node_value=value
        )
        
        if self._head:
            self._record_step(
                "update_pointer",
                f"Set new node's next to current head ({self._head.value})",
                pointer_changes={"new_node.next": self._head.value}
            )
        
        new_node.next = self._head
        self._head = new_node
        self._size += 1
        
        self._record_step(
            "update_head",
            f"Update head to point to new node ({value})",
            pointer_changes={"head": value}
        )
    
    def insert_at_tail(self, value: T) -> None:
        """
        Insert a new node at the tail of the list.
        
        Time Complexity: O(n) - must traverse to find tail
        
        Args:
            value: The value to insert
        """
        new_node = SinglyNode(value)
        self._record_step(
            "create_node",
            f"Create new node with value {value}",
            current_node_value=value
        )
        
        if not self._head:
            self._head = new_node
            self._size += 1
            self._record_step(
                "update_head",
                f"List was empty, set head to new node ({value})",
                pointer_changes={"head": value}
            )
            return
        
        current = self._head
        self._record_step(
            "traverse_start",
            f"Start traversal from head ({current.value})",
            current_node_value=current.value
        )
        
        while current.next:
            self._record_step(
                "traverse",
                f"Move to next node ({current.next.value})",
                current_node_value=current.next.value
            )
            current = current.next
        
        self._record_step(
            "found_tail",
            f"Found tail node ({current.value})",
            current_node_value=current.value
        )
        
        current.next = new_node
        self._size += 1
        
        self._record_step(
            "update_pointer",
            f"Set tail's next to new node ({value})",
            pointer_changes={f"node({current.value}).next": value}
        )
    
    def insert_at_index(self, index: int, value: T) -> bool:
        """
        Insert a new node at the specified index.
        
        Time Complexity: O(n)
        
        Args:
            index: The position to insert at (0-indexed)
            value: The value to insert
            
        Returns:
            True if insertion was successful, False if index out of bounds
        """
        if index < 0 or index > self._size:
            return False
        
        if index == 0:
            self.insert_at_head(value)
            return True
        
        new_node = SinglyNode(value)
        self._record_step(
            "create_node",
            f"Create new node with value {value}",
            current_node_value=value
        )
        
        current = self._head
        for i in range(index - 1):
            self._record_step(
                "traverse",
                f"Traverse to index {i}: node({current.value})",
                current_node_value=current.value
            )
            current = current.next
        
        self._record_step(
            "found_position",
            f"Found insertion point after node({current.value})",
            current_node_value=current.value
        )
        
        new_node.next = current.next
        current.next = new_node
        self._size += 1
        
        self._record_step(
            "insert_complete",
            f"Inserted {value} at index {index}",
            affected_nodes=[current.value, value],
            pointer_changes={
                f"node({current.value}).next": value,
                f"node({value}).next": new_node.next.value if new_node.next else None
            }
        )
        return True
    
    def delete_at_head(self) -> T | None:
        """
        Delete and return the head node's value.
        
        Time Complexity: O(1)
        
        Returns:
            The deleted value, or None if list is empty
        """
        if not self._head:
            return None
        
        value = self._head.value
        self._record_step(
            "mark_deletion",
            f"Mark head node ({value}) for deletion",
            current_node_value=value
        )
        
        self._head = self._head.next
        self._size -= 1
        
        self._record_step(
            "update_head",
            f"Update head to next node ({self._head.value if self._head else None})",
            pointer_changes={"head": self._head.value if self._head else None}
        )
        
        self._record_step(
            "garbage_collect",
            f"Node ({value}) removed, memory freed",
            current_node_value=value
        )
        
        return value
    
    def delete_value(self, value: T) -> bool:
        """
        Delete the first node with the specified value.
        
        Time Complexity: O(n)
        
        Args:
            value: The value to delete
            
        Returns:
            True if deletion was successful, False if value not found
        """
        if not self._head:
            return False
        
        if self._head.value == value:
            self.delete_at_head()
            return True
        
        current = self._head
        self._record_step(
            "search_start",
            f"Search for value {value} starting from head",
            current_node_value=current.value
        )
        
        while current.next and current.next.value != value:
            self._record_step(
                "traverse",
                f"Check node({current.next.value}): not target",
                current_node_value=current.next.value
            )
            current = current.next
        
        if not current.next:
            self._record_step(
                "not_found",
                f"Value {value} not found in list"
            )
            return False
        
        self._record_step(
            "found_target",
            f"Found target node({value})",
            current_node_value=value
        )
        
        deleted_node = current.next
        current.next = deleted_node.next
        self._size -= 1
        
        self._record_step(
            "delete_complete",
            f"Deleted node({value}), linked {current.value} to {current.next.value if current.next else None}",
            pointer_changes={f"node({current.value}).next": current.next.value if current.next else None}
        )
        
        return True
    
    def search(self, value: T) -> int:
        """
        Search for a value and return its index.
        
        Time Complexity: O(n)
        
        Args:
            value: The value to search for
            
        Returns:
            Index of the value, or -1 if not found
        """
        current = self._head
        index = 0
        
        self._record_step(
            "search_start",
            f"Search for value {value}",
            current_node_value=current.value if current else None
        )
        
        while current:
            self._record_step(
                "compare",
                f"Compare node({current.value}) with target {value}",
                current_node_value=current.value
            )
            
            if current.value == value:
                self._record_step(
                    "found",
                    f"Found {value} at index {index}",
                    current_node_value=value
                )
                return index
            
            current = current.next
            index += 1
        
        self._record_step(
            "not_found",
            f"Value {value} not found in list"
        )
        return -1
    
    def reverse(self) -> None:
        """
        Reverse the linked list in place.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        prev: SinglyNode[T] | None = None
        current = self._head
        
        self._record_step(
            "reverse_start",
            "Initialize: prev=None, current=head",
            pointer_changes={"prev": None, "current": current.value if current else None}
        )
        
        while current:
            next_temp = current.next
            
            self._record_step(
                "save_next",
                f"Save next pointer: next_temp = {next_temp.value if next_temp else None}",
                current_node_value=current.value,
                pointer_changes={"next_temp": next_temp.value if next_temp else None}
            )
            
            current.next = prev
            
            self._record_step(
                "reverse_link",
                f"Reverse link: node({current.value}).next = {prev.value if prev else None}",
                current_node_value=current.value,
                pointer_changes={f"node({current.value}).next": prev.value if prev else None}
            )
            
            prev = current
            current = next_temp
            
            self._record_step(
                "advance",
                f"Advance: prev={prev.value}, current={current.value if current else None}",
                pointer_changes={"prev": prev.value, "current": current.value if current else None}
            )
        
        self._head = prev
        
        self._record_step(
            "reverse_complete",
            f"Reversal complete, new head = {self._head.value if self._head else None}",
            pointer_changes={"head": self._head.value if self._head else None}
        )
    
    def __iter__(self) -> Iterator[T]:
        """Iterate over the list values."""
        current = self._head
        while current:
            yield current.value
            current = current.next
    
    def print_steps(self) -> None:
        """Print all recorded steps."""
        print(f"\n{'='*60}")
        print(f"Linked List Operation Steps ({len(self._steps)} total)")
        print(f"{'='*60}")
        for step in self._steps:
            print(f"Step {step.step_number}: [{step.operation}] {step.description}")
            if step.pointer_changes:
                print(f"  Pointer changes: {step.pointer_changes}")
            print(f"  List state: {step.list_state}")
        print(f"{'='*60}\n")


class DoublyNode(Generic[T]):
    """
    A node in a doubly linked list.
    
    Each node contains a value and references to both next and previous nodes.
    """
    
    def __init__(self, value: T) -> None:
        self.value: T = value
        self.next: DoublyNode[T] | None = None
        self.prev: DoublyNode[T] | None = None
    
    def __repr__(self) -> str:
        return f"DoublyNode({self.value})"


class DoublyLinkedList(Generic[T]):
    """
    A doubly linked list implementation.
    
    Supports bidirectional traversal and O(1) deletion with node reference.
    """
    
    def __init__(self) -> None:
        self._head: DoublyNode[T] | None = None
        self._tail: DoublyNode[T] | None = None
        self._size: int = 0
    
    def __len__(self) -> int:
        return self._size
    
    def is_empty(self) -> bool:
        return self._head is None
    
    def to_list(self) -> list[T]:
        """Convert to Python list."""
        result: list[T] = []
        current = self._head
        while current:
            result.append(current.value)
            current = current.next
        return result
    
    def insert_at_head(self, value: T) -> None:
        """Insert at head - O(1)."""
        new_node = DoublyNode(value)
        
        if not self._head:
            self._head = self._tail = new_node
        else:
            new_node.next = self._head
            self._head.prev = new_node
            self._head = new_node
        
        self._size += 1
    
    def insert_at_tail(self, value: T) -> None:
        """Insert at tail - O(1) due to tail pointer."""
        new_node = DoublyNode(value)
        
        if not self._tail:
            self._head = self._tail = new_node
        else:
            new_node.prev = self._tail
            self._tail.next = new_node
            self._tail = new_node
        
        self._size += 1
    
    def delete_node(self, node: DoublyNode[T]) -> T:
        """
        Delete a specific node - O(1) with node reference.
        
        This is the key advantage of doubly linked lists.
        """
        value = node.value
        
        if node.prev:
            node.prev.next = node.next
        else:
            self._head = node.next
        
        if node.next:
            node.next.prev = node.prev
        else:
            self._tail = node.prev
        
        self._size -= 1
        return value
    
    def traverse_forward(self) -> list[T]:
        """Traverse from head to tail."""
        result: list[T] = []
        current = self._head
        while current:
            result.append(current.value)
            current = current.next
        return result
    
    def traverse_backward(self) -> list[T]:
        """Traverse from tail to head."""
        result: list[T] = []
        current = self._tail
        while current:
            result.append(current.value)
            current = current.prev
        return result


def has_cycle(head: SinglyNode[Any] | None) -> bool:
    """
    Detect if a linked list has a cycle using Floyd's algorithm.
    
    Uses two pointers: slow (tortoise) moves 1 step, fast (hare) moves 2 steps.
    If there's a cycle, they will eventually meet.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Args:
        head: The head of the linked list
        
    Returns:
        True if cycle exists, False otherwise
    """
    if not head or not head.next:
        return False
    
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
    
    return False


def find_middle(head: SinglyNode[T] | None) -> SinglyNode[T] | None:
    """
    Find the middle node of a linked list.
    
    Uses slow/fast pointer technique.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not head:
        return None
    
    slow = head
    fast = head
    
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow


def merge_sorted_lists(
    l1: SinglyNode[int] | None,
    l2: SinglyNode[int] | None
) -> SinglyNode[int] | None:
    """
    Merge two sorted linked lists into one sorted list.
    
    Time Complexity: O(n + m)
    Space Complexity: O(1) - reuses existing nodes
    """
    dummy = SinglyNode(0)
    current = dummy
    
    while l1 and l2:
        if l1.value <= l2.value:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    
    current.next = l1 if l1 else l2
    
    return dummy.next


def demo() -> None:
    """Run demonstrations of linked list operations."""
    print("\n" + "="*60)
    print("LINKED LIST DEMONSTRATIONS")
    print("="*60)
    
    # Singly Linked List Demo
    print("\n--- Singly Linked List Operations ---")
    sll = SinglyLinkedList[int]()
    
    print("Inserting at head: 30, 20, 10")
    sll.insert_at_head(30)
    sll.insert_at_head(20)
    sll.insert_at_head(10)
    print(f"List: {sll.to_list()}")
    
    print("\nInserting at tail: 40, 50")
    sll.clear_steps()
    sll.insert_at_tail(40)
    sll.insert_at_tail(50)
    print(f"List: {sll.to_list()}")
    
    print("\nSearching for 30:")
    sll.clear_steps()
    index = sll.search(30)
    print(f"Found at index: {index}")
    
    print("\nReversing the list:")
    sll.clear_steps()
    sll.reverse()
    print(f"Reversed: {sll.to_list()}")
    sll.print_steps()
    
    # Doubly Linked List Demo
    print("\n--- Doubly Linked List Operations ---")
    dll = DoublyLinkedList[int]()
    
    for val in [10, 20, 30, 40, 50]:
        dll.insert_at_tail(val)
    
    print(f"Forward traversal: {dll.traverse_forward()}")
    print(f"Backward traversal: {dll.traverse_backward()}")
    
    # Cycle Detection Demo
    print("\n--- Cycle Detection ---")
    node1 = SinglyNode(1)
    node2 = SinglyNode(2)
    node3 = SinglyNode(3)
    node4 = SinglyNode(4)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    
    print(f"List without cycle: has_cycle = {has_cycle(node1)}")
    
    node4.next = node2  # Create cycle
    print(f"List with cycle: has_cycle = {has_cycle(node1)}")


if __name__ == "__main__":
    demo()
