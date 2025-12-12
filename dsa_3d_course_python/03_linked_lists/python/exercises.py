"""
Exercises: Linked Lists

Complete the following exercises to practice linked list operations.
Each function has a docstring explaining what to implement.

Run this file to test your implementations against the provided test cases.
"""

from typing import Any, TypeVar, Generic

T = TypeVar('T')


class ListNode(Generic[T]):
    """A simple node class for exercises."""
    
    def __init__(self, value: T) -> None:
        self.value: T = value
        self.next: ListNode[T] | None = None
    
    def __repr__(self) -> str:
        return f"ListNode({self.value})"


def list_to_linked(arr: list[T]) -> ListNode[T] | None:
    """Helper: Convert a Python list to a linked list."""
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_to_list(head: ListNode[T] | None) -> list[T]:
    """Helper: Convert a linked list to a Python list."""
    result: list[T] = []
    current = head
    visited = set()
    while current and id(current) not in visited:
        visited.add(id(current))
        result.append(current.value)
        current = current.next
    return result


# =============================================================================
# EXERCISE 1: Basic Operations
# =============================================================================

def get_length(head: ListNode[Any] | None) -> int:
    """
    Calculate the length of a linked list.
    
    TODO: Implement this function.
    
    Args:
        head: Head of the linked list
        
    Returns:
        Number of nodes in the list
        
    Expected Time Complexity: O(n)
    Expected Space Complexity: O(1)
    """
    # TODO: Implement this function
    pass


def get_nth_node(head: ListNode[T] | None, n: int) -> ListNode[T] | None:
    """
    Get the nth node (0-indexed) from the linked list.
    
    TODO: Implement this function.
    
    Args:
        head: Head of the linked list
        n: Index of the node to retrieve
        
    Returns:
        The nth node, or None if n is out of bounds
        
    Expected Time Complexity: O(n)
    Expected Space Complexity: O(1)
    """
    # TODO: Implement this function
    pass


def insert_at_position(head: ListNode[T] | None, value: T, position: int) -> ListNode[T]:
    """
    Insert a new node at the specified position.
    
    TODO: Implement this function.
    
    Args:
        head: Head of the linked list
        value: Value to insert
        position: Position to insert at (0-indexed)
        
    Returns:
        Head of the modified list
        
    Expected Time Complexity: O(n)
    Expected Space Complexity: O(1)
    """
    # TODO: Implement this function
    pass


# =============================================================================
# EXERCISE 2: Reversal and Manipulation
# =============================================================================

def reverse_linked_list(head: ListNode[T] | None) -> ListNode[T] | None:
    """
    Reverse a singly linked list in place.
    
    TODO: Implement this function.
    
    Args:
        head: Head of the linked list
        
    Returns:
        Head of the reversed list
        
    Expected Time Complexity: O(n)
    Expected Space Complexity: O(1)
    
    Hint: Use three pointers: prev, current, and next_temp.
    """
    # TODO: Implement this function
    pass


def reverse_between(head: ListNode[T] | None, left: int, right: int) -> ListNode[T] | None:
    """
    Reverse nodes between positions left and right (1-indexed, inclusive).
    
    TODO: Implement this function.
    
    Args:
        head: Head of the linked list
        left: Start position (1-indexed)
        right: End position (1-indexed)
        
    Returns:
        Head of the modified list
        
    Example:
        Input: 1->2->3->4->5, left=2, right=4
        Output: 1->4->3->2->5
        
    Expected Time Complexity: O(n)
    Expected Space Complexity: O(1)
    """
    # TODO: Implement this function
    pass


def remove_duplicates_sorted(head: ListNode[T] | None) -> ListNode[T] | None:
    """
    Remove duplicates from a sorted linked list.
    
    TODO: Implement this function.
    
    Args:
        head: Head of a sorted linked list
        
    Returns:
        Head of the list with duplicates removed
        
    Example:
        Input: 1->1->2->3->3
        Output: 1->2->3
        
    Expected Time Complexity: O(n)
    Expected Space Complexity: O(1)
    """
    # TODO: Implement this function
    pass


# =============================================================================
# EXERCISE 3: Two-Pointer Techniques
# =============================================================================

def find_middle_node(head: ListNode[T] | None) -> ListNode[T] | None:
    """
    Find the middle node of a linked list.
    
    TODO: Implement this function using the slow/fast pointer technique.
    
    Args:
        head: Head of the linked list
        
    Returns:
        The middle node (for even length, return the second middle)
        
    Example:
        Input: 1->2->3->4->5
        Output: Node(3)
        
        Input: 1->2->3->4
        Output: Node(3) (second middle)
        
    Expected Time Complexity: O(n)
    Expected Space Complexity: O(1)
    """
    # TODO: Implement this function
    pass


def has_cycle(head: ListNode[Any] | None) -> bool:
    """
    Detect if a linked list has a cycle.
    
    TODO: Implement Floyd's cycle detection algorithm.
    
    Args:
        head: Head of the linked list
        
    Returns:
        True if there's a cycle, False otherwise
        
    Expected Time Complexity: O(n)
    Expected Space Complexity: O(1)
    
    Hint: Use slow (1 step) and fast (2 steps) pointers.
    If they meet, there's a cycle.
    """
    # TODO: Implement this function
    pass


def find_cycle_start(head: ListNode[T] | None) -> ListNode[T] | None:
    """
    Find the node where the cycle begins.
    
    TODO: Implement this function.
    
    Args:
        head: Head of the linked list
        
    Returns:
        The node where cycle starts, or None if no cycle
        
    Expected Time Complexity: O(n)
    Expected Space Complexity: O(1)
    
    Hint: After detecting cycle, reset one pointer to head.
    Move both pointers one step at a time. They meet at cycle start.
    """
    # TODO: Implement this function
    pass


def get_intersection_node(headA: ListNode[T] | None, headB: ListNode[T] | None) -> ListNode[T] | None:
    """
    Find the node where two linked lists intersect.
    
    TODO: Implement this function.
    
    Args:
        headA: Head of first linked list
        headB: Head of second linked list
        
    Returns:
        The intersection node, or None if no intersection
        
    Expected Time Complexity: O(n + m)
    Expected Space Complexity: O(1)
    
    Hint: When pointer reaches end of one list, redirect to head of other list.
    """
    # TODO: Implement this function
    pass


# =============================================================================
# EXERCISE 4: Merge and Sort
# =============================================================================

def merge_two_sorted_lists(l1: ListNode[int] | None, l2: ListNode[int] | None) -> ListNode[int] | None:
    """
    Merge two sorted linked lists into one sorted list.
    
    TODO: Implement this function.
    
    Args:
        l1: Head of first sorted list
        l2: Head of second sorted list
        
    Returns:
        Head of merged sorted list
        
    Expected Time Complexity: O(n + m)
    Expected Space Complexity: O(1) - reuse existing nodes
    """
    # TODO: Implement this function
    pass


def is_palindrome(head: ListNode[T] | None) -> bool:
    """
    Check if a linked list is a palindrome.
    
    TODO: Implement this function.
    
    Args:
        head: Head of the linked list
        
    Returns:
        True if palindrome, False otherwise
        
    Example:
        Input: 1->2->2->1
        Output: True
        
    Expected Time Complexity: O(n)
    Expected Space Complexity: O(1)
    
    Hint: Find middle, reverse second half, compare, restore (optional).
    """
    # TODO: Implement this function
    pass


def remove_nth_from_end(head: ListNode[T] | None, n: int) -> ListNode[T] | None:
    """
    Remove the nth node from the end of the list.
    
    TODO: Implement this function in one pass.
    
    Args:
        head: Head of the linked list
        n: Position from end (1-indexed)
        
    Returns:
        Head of modified list
        
    Example:
        Input: 1->2->3->4->5, n=2
        Output: 1->2->3->5 (removed 4)
        
    Expected Time Complexity: O(n)
    Expected Space Complexity: O(1)
    
    Hint: Use two pointers with n nodes gap between them.
    """
    # TODO: Implement this function
    pass


# =============================================================================
# TEST CASES
# =============================================================================

def run_tests() -> None:
    """Run all test cases for the exercises."""
    print("\n" + "="*60)
    print("RUNNING EXERCISE TESTS")
    print("="*60)
    
    all_passed = True
    
    # Test get_length
    print("\n--- Testing get_length ---")
    tests = [
        ([1, 2, 3, 4, 5], 5),
        ([1], 1),
        ([], 0),
    ]
    for arr, expected in tests:
        head = list_to_linked(arr)
        result = get_length(head)
        status = "PASS" if result == expected else "FAIL"
        if status == "FAIL":
            all_passed = False
        print(f"  get_length({arr}) = {result}, expected {expected} [{status}]")
    
    # Test get_nth_node
    print("\n--- Testing get_nth_node ---")
    tests = [
        ([1, 2, 3, 4, 5], 2, 3),
        ([1, 2, 3], 0, 1),
        ([1, 2, 3], 5, None),
    ]
    for arr, n, expected in tests:
        head = list_to_linked(arr)
        result = get_nth_node(head, n)
        result_val = result.value if result else None
        status = "PASS" if result_val == expected else "FAIL"
        if status == "FAIL":
            all_passed = False
        print(f"  get_nth_node({arr}, {n}) = {result_val}, expected {expected} [{status}]")
    
    # Test reverse_linked_list
    print("\n--- Testing reverse_linked_list ---")
    tests = [
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([1, 2], [2, 1]),
        ([1], [1]),
        ([], []),
    ]
    for arr, expected in tests:
        head = list_to_linked(arr)
        result = reverse_linked_list(head)
        result_list = linked_to_list(result)
        status = "PASS" if result_list == expected else "FAIL"
        if status == "FAIL":
            all_passed = False
        print(f"  reverse_linked_list({arr}) = {result_list}, expected {expected} [{status}]")
    
    # Test find_middle_node
    print("\n--- Testing find_middle_node ---")
    tests = [
        ([1, 2, 3, 4, 5], 3),
        ([1, 2, 3, 4], 3),
        ([1], 1),
    ]
    for arr, expected in tests:
        head = list_to_linked(arr)
        result = find_middle_node(head)
        result_val = result.value if result else None
        status = "PASS" if result_val == expected else "FAIL"
        if status == "FAIL":
            all_passed = False
        print(f"  find_middle_node({arr}) = {result_val}, expected {expected} [{status}]")
    
    # Test has_cycle
    print("\n--- Testing has_cycle ---")
    head1 = list_to_linked([1, 2, 3, 4])
    result1 = has_cycle(head1)
    status1 = "PASS" if result1 == False else "FAIL"
    if status1 == "FAIL":
        all_passed = False
    print(f"  has_cycle([1,2,3,4] no cycle) = {result1}, expected False [{status1}]")
    
    head2 = list_to_linked([1, 2, 3, 4])
    if head2 and head2.next and head2.next.next and head2.next.next.next:
        head2.next.next.next.next = head2.next  # Create cycle
    result2 = has_cycle(head2)
    status2 = "PASS" if result2 == True else "FAIL"
    if status2 == "FAIL":
        all_passed = False
    print(f"  has_cycle([1,2,3,4] with cycle) = {result2}, expected True [{status2}]")
    
    # Test merge_two_sorted_lists
    print("\n--- Testing merge_two_sorted_lists ---")
    tests = [
        ([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]),
        ([1, 2, 3], [], [1, 2, 3]),
        ([], [1, 2], [1, 2]),
    ]
    for arr1, arr2, expected in tests:
        l1 = list_to_linked(arr1)
        l2 = list_to_linked(arr2)
        result = merge_two_sorted_lists(l1, l2)
        result_list = linked_to_list(result)
        status = "PASS" if result_list == expected else "FAIL"
        if status == "FAIL":
            all_passed = False
        print(f"  merge_two_sorted_lists({arr1}, {arr2}) = {result_list}, expected {expected} [{status}]")
    
    # Test is_palindrome
    print("\n--- Testing is_palindrome ---")
    tests = [
        ([1, 2, 2, 1], True),
        ([1, 2, 3, 2, 1], True),
        ([1, 2, 3], False),
        ([1], True),
    ]
    for arr, expected in tests:
        head = list_to_linked(arr)
        result = is_palindrome(head)
        status = "PASS" if result == expected else "FAIL"
        if status == "FAIL":
            all_passed = False
        print(f"  is_palindrome({arr}) = {result}, expected {expected} [{status}]")
    
    # Test remove_nth_from_end
    print("\n--- Testing remove_nth_from_end ---")
    tests = [
        ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
        ([1, 2], 1, [1]),
        ([1], 1, []),
    ]
    for arr, n, expected in tests:
        head = list_to_linked(arr)
        result = remove_nth_from_end(head, n)
        result_list = linked_to_list(result)
        status = "PASS" if result_list == expected else "FAIL"
        if status == "FAIL":
            all_passed = False
        print(f"  remove_nth_from_end({arr}, {n}) = {result_list}, expected {expected} [{status}]")
    
    print("\n" + "="*60)
    if all_passed:
        print("ALL TESTS PASSED!")
    else:
        print("SOME TESTS FAILED - Keep working on your implementations!")
    print("="*60 + "\n")


if __name__ == "__main__":
    run_tests()
