"""
Exercises: Stacks and Queues

Complete the following exercises to practice stack and queue operations.
Each function has a docstring explaining what to implement.

Run this file to test your implementations against the provided test cases.
"""

from typing import Any, TypeVar
from collections import deque

T = TypeVar('T')


# =============================================================================
# EXERCISE 1: Stack Basics
# =============================================================================

def reverse_list_with_stack(arr: list[T]) -> list[T]:
    """
    Reverse a list using a stack.
    
    TODO: Implement this function.
    
    Args:
        arr: The list to reverse
        
    Returns:
        A new reversed list
        
    Expected Time Complexity: O(n)
    Expected Space Complexity: O(n)
    
    Hint: Push all elements onto a stack, then pop them all off.
    """
    # TODO: Implement this function
    pass


def is_balanced_parentheses(s: str) -> bool:
    """
    Check if parentheses in a string are balanced.
    
    TODO: Implement this function using a stack.
    
    Args:
        s: String containing '(', ')', '[', ']', '{', '}'
        
    Returns:
        True if balanced, False otherwise
        
    Expected Time Complexity: O(n)
    Expected Space Complexity: O(n)
    
    Example:
        is_balanced_parentheses("({[]})") -> True
        is_balanced_parentheses("([)]") -> False
    """
    # TODO: Implement this function
    pass


def evaluate_postfix(expression: str) -> float:
    """
    Evaluate a postfix expression.
    
    TODO: Implement this function using a stack.
    
    Args:
        expression: Space-separated postfix expression
        
    Returns:
        The result of the expression
        
    Expected Time Complexity: O(n)
    Expected Space Complexity: O(n)
    
    Example:
        evaluate_postfix("3 4 + 2 *") -> 14.0  # (3+4)*2
        evaluate_postfix("5 1 2 + 4 * + 3 -") -> 14.0
    """
    # TODO: Implement this function
    pass


# =============================================================================
# EXERCISE 2: Advanced Stack Problems
# =============================================================================

def next_greater_element(arr: list[int]) -> list[int]:
    """
    Find the next greater element for each element in the array.
    
    TODO: Implement this function using a stack.
    
    Args:
        arr: List of integers
        
    Returns:
        List where result[i] is the next greater element for arr[i],
        or -1 if no greater element exists to the right
        
    Expected Time Complexity: O(n)
    Expected Space Complexity: O(n)
    
    Example:
        next_greater_element([4, 5, 2, 25]) -> [5, 25, 25, -1]
        next_greater_element([13, 7, 6, 12]) -> [-1, 12, 12, -1]
    """
    # TODO: Implement this function
    pass


def min_stack_operations() -> type:
    """
    Design a stack that supports push, pop, top, and getMin in O(1) time.
    
    TODO: Implement the MinStack class.
    
    Returns:
        The MinStack class
        
    The class should support:
        - push(val): Push element onto stack
        - pop(): Remove top element
        - top(): Get top element
        - get_min(): Retrieve minimum element in O(1)
    
    Hint: Use an auxiliary stack to track minimums.
    """
    class MinStack:
        def __init__(self) -> None:
            # TODO: Initialize data structures
            pass
        
        def push(self, val: int) -> None:
            # TODO: Implement push
            pass
        
        def pop(self) -> None:
            # TODO: Implement pop
            pass
        
        def top(self) -> int:
            # TODO: Implement top
            pass
        
        def get_min(self) -> int:
            # TODO: Implement get_min
            pass
    
    return MinStack


def daily_temperatures(temperatures: list[int]) -> list[int]:
    """
    Find how many days until a warmer temperature for each day.
    
    TODO: Implement this function using a stack.
    
    Args:
        temperatures: List of daily temperatures
        
    Returns:
        List where result[i] is days until warmer temp, or 0 if none
        
    Expected Time Complexity: O(n)
    Expected Space Complexity: O(n)
    
    Example:
        daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73])
        -> [1, 1, 4, 2, 1, 1, 0, 0]
    """
    # TODO: Implement this function
    pass


# =============================================================================
# EXERCISE 3: Queue Basics
# =============================================================================

def implement_queue_using_stacks() -> type:
    """
    Implement a queue using two stacks.
    
    TODO: Implement the MyQueue class.
    
    Returns:
        The MyQueue class
        
    The class should support:
        - enqueue(val): Add element to rear
        - dequeue(): Remove and return front element
        - front(): Get front element without removing
        - is_empty(): Check if queue is empty
    
    Expected: Amortized O(1) for all operations
    """
    class MyQueue:
        def __init__(self) -> None:
            # TODO: Initialize two stacks
            pass
        
        def enqueue(self, val: Any) -> None:
            # TODO: Implement enqueue
            pass
        
        def dequeue(self) -> Any:
            # TODO: Implement dequeue
            pass
        
        def front(self) -> Any:
            # TODO: Implement front
            pass
        
        def is_empty(self) -> bool:
            # TODO: Implement is_empty
            pass
    
    return MyQueue


def implement_stack_using_queues() -> type:
    """
    Implement a stack using two queues.
    
    TODO: Implement the MyStack class.
    
    Returns:
        The MyStack class
        
    The class should support:
        - push(val): Push element onto stack
        - pop(): Remove and return top element
        - top(): Get top element without removing
        - is_empty(): Check if stack is empty
    """
    class MyStack:
        def __init__(self) -> None:
            # TODO: Initialize two queues
            pass
        
        def push(self, val: Any) -> None:
            # TODO: Implement push
            pass
        
        def pop(self) -> Any:
            # TODO: Implement pop
            pass
        
        def top(self) -> Any:
            # TODO: Implement top
            pass
        
        def is_empty(self) -> bool:
            # TODO: Implement is_empty
            pass
    
    return MyStack


# =============================================================================
# EXERCISE 4: Advanced Queue Problems
# =============================================================================

def sliding_window_maximum(nums: list[int], k: int) -> list[int]:
    """
    Find maximum in each sliding window of size k.
    
    TODO: Implement this function using a deque.
    
    Args:
        nums: Input array
        k: Window size
        
    Returns:
        List of maximums for each window position
        
    Expected Time Complexity: O(n)
    Expected Space Complexity: O(k)
    
    Example:
        sliding_window_maximum([1, 3, -1, -3, 5, 3, 6, 7], 3)
        -> [3, 3, 5, 5, 6, 7]
    
    Hint: Use a deque to store indices. Keep the deque in decreasing order
    of values. The front always has the maximum for current window.
    """
    # TODO: Implement this function
    pass


def first_non_repeating_in_stream(stream: str) -> list[str]:
    """
    Find first non-repeating character at each point in a stream.
    
    TODO: Implement this function using a queue.
    
    Args:
        stream: String representing a stream of characters
        
    Returns:
        List where result[i] is the first non-repeating char after
        processing stream[0:i+1], or '#' if none exists
        
    Expected Time Complexity: O(n)
    Expected Space Complexity: O(n)
    
    Example:
        first_non_repeating_in_stream("aabcbc")
        -> ['a', '#', 'b', 'b', 'c', '#']
    """
    # TODO: Implement this function
    pass


def circular_tour(petrol: list[int], distance: list[int]) -> int:
    """
    Find starting point for circular tour of petrol pumps.
    
    TODO: Implement this function.
    
    Args:
        petrol: Petrol available at each pump
        distance: Distance to next pump from each pump
        
    Returns:
        Index of starting pump, or -1 if no solution
        
    Expected Time Complexity: O(n)
    Expected Space Complexity: O(1)
    
    Example:
        circular_tour([4, 6, 7, 4], [6, 5, 3, 5]) -> 1
        (Start at pump 1, can complete the circuit)
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
    
    # Test reverse_list_with_stack
    print("\n--- Testing reverse_list_with_stack ---")
    tests = [
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        (['a', 'b', 'c'], ['c', 'b', 'a']),
        ([], []),
        ([1], [1]),
    ]
    for arr, expected in tests:
        result = reverse_list_with_stack(arr.copy())
        status = "PASS" if result == expected else "FAIL"
        if status == "FAIL":
            all_passed = False
        print(f"  reverse_list_with_stack({arr}) = {result}, expected {expected} [{status}]")
    
    # Test is_balanced_parentheses
    print("\n--- Testing is_balanced_parentheses ---")
    tests = [
        ("({[]})", True),
        ("([)]", False),
        ("((()))", True),
        ("", True),
        ("(", False),
        ("{[]}", True),
    ]
    for s, expected in tests:
        result = is_balanced_parentheses(s)
        status = "PASS" if result == expected else "FAIL"
        if status == "FAIL":
            all_passed = False
        print(f"  is_balanced_parentheses('{s}') = {result}, expected {expected} [{status}]")
    
    # Test evaluate_postfix
    print("\n--- Testing evaluate_postfix ---")
    tests = [
        ("3 4 +", 7.0),
        ("3 4 + 2 *", 14.0),
        ("5 1 2 + 4 * + 3 -", 14.0),
        ("2 3 * 5 +", 11.0),
    ]
    for expr, expected in tests:
        result = evaluate_postfix(expr)
        status = "PASS" if result == expected else "FAIL"
        if status == "FAIL":
            all_passed = False
        print(f"  evaluate_postfix('{expr}') = {result}, expected {expected} [{status}]")
    
    # Test next_greater_element
    print("\n--- Testing next_greater_element ---")
    tests = [
        ([4, 5, 2, 25], [5, 25, 25, -1]),
        ([13, 7, 6, 12], [-1, 12, 12, -1]),
        ([1, 2, 3, 4], [2, 3, 4, -1]),
        ([4, 3, 2, 1], [-1, -1, -1, -1]),
    ]
    for arr, expected in tests:
        result = next_greater_element(arr)
        status = "PASS" if result == expected else "FAIL"
        if status == "FAIL":
            all_passed = False
        print(f"  next_greater_element({arr}) = {result}, expected {expected} [{status}]")
    
    # Test MinStack
    print("\n--- Testing MinStack ---")
    MinStack = min_stack_operations()
    ms = MinStack()
    try:
        ms.push(-2)
        ms.push(0)
        ms.push(-3)
        min1 = ms.get_min()  # Should be -3
        ms.pop()
        top1 = ms.top()  # Should be 0
        min2 = ms.get_min()  # Should be -2
        
        status = "PASS" if min1 == -3 and top1 == 0 and min2 == -2 else "FAIL"
        if status == "FAIL":
            all_passed = False
        print(f"  MinStack operations: min={min1}, top={top1}, min after pop={min2} [{status}]")
    except Exception as e:
        print(f"  MinStack operations: ERROR - {e} [FAIL]")
        all_passed = False
    
    # Test daily_temperatures
    print("\n--- Testing daily_temperatures ---")
    tests = [
        ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
        ([30, 40, 50, 60], [1, 1, 1, 0]),
        ([30, 60, 90], [1, 1, 0]),
    ]
    for temps, expected in tests:
        result = daily_temperatures(temps)
        status = "PASS" if result == expected else "FAIL"
        if status == "FAIL":
            all_passed = False
        print(f"  daily_temperatures({temps}) = {result}, expected {expected} [{status}]")
    
    # Test Queue using Stacks
    print("\n--- Testing Queue using Stacks ---")
    MyQueue = implement_queue_using_stacks()
    q = MyQueue()
    try:
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        d1 = q.dequeue()  # Should be 1
        d2 = q.dequeue()  # Should be 2
        q.enqueue(4)
        d3 = q.dequeue()  # Should be 3
        
        status = "PASS" if d1 == 1 and d2 == 2 and d3 == 3 else "FAIL"
        if status == "FAIL":
            all_passed = False
        print(f"  Queue using stacks: dequeue order = {d1}, {d2}, {d3} [{status}]")
    except Exception as e:
        print(f"  Queue using stacks: ERROR - {e} [FAIL]")
        all_passed = False
    
    # Test sliding_window_maximum
    print("\n--- Testing sliding_window_maximum ---")
    tests = [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7]),
        ([1], 1, [1]),
        ([1, -1], 1, [1, -1]),
        ([9, 11], 2, [11]),
    ]
    for nums, k, expected in tests:
        result = sliding_window_maximum(nums, k)
        status = "PASS" if result == expected else "FAIL"
        if status == "FAIL":
            all_passed = False
        print(f"  sliding_window_maximum({nums}, {k}) = {result}, expected {expected} [{status}]")
    
    # Test circular_tour
    print("\n--- Testing circular_tour ---")
    tests = [
        ([4, 6, 7, 4], [6, 5, 3, 5], 1),
        ([6, 3, 7], [4, 6, 3], 2),
    ]
    for petrol, distance, expected in tests:
        result = circular_tour(petrol, distance)
        status = "PASS" if result == expected else "FAIL"
        if status == "FAIL":
            all_passed = False
        print(f"  circular_tour({petrol}, {distance}) = {result}, expected {expected} [{status}]")
    
    print("\n" + "="*60)
    if all_passed:
        print("ALL TESTS PASSED!")
    else:
        print("SOME TESTS FAILED - Keep working on your implementations!")
    print("="*60 + "\n")


if __name__ == "__main__":
    run_tests()
