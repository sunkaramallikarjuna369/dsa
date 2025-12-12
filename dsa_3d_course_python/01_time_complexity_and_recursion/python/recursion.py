"""
Recursion Module

This module provides demonstrations of recursive algorithms with
step-by-step tracking for 3D visualization synchronization.

Each recursive function tracks its call stack and return values
to enable animated visualization of the recursion process.
"""

from typing import Any, Callable
from dataclasses import dataclass, field
from functools import wraps


@dataclass
class RecursiveCall:
    """Represents a single recursive function call."""
    call_id: int
    function_name: str
    parameters: dict[str, Any]
    depth: int
    return_value: Any = None
    is_base_case: bool = False


@dataclass
class RecursionTracker:
    """Tracks recursive calls for visualization."""
    calls: list[RecursiveCall] = field(default_factory=list)
    call_stack: list[int] = field(default_factory=list)
    next_id: int = 0
    max_depth: int = 0
    
    def reset(self) -> None:
        """Reset the tracker for a new recursion."""
        self.calls = []
        self.call_stack = []
        self.next_id = 0
        self.max_depth = 0
    
    def enter_call(
        self,
        function_name: str,
        parameters: dict[str, Any],
        is_base_case: bool = False
    ) -> int:
        """Record entering a recursive call."""
        call_id = self.next_id
        self.next_id += 1
        depth = len(self.call_stack)
        self.max_depth = max(self.max_depth, depth + 1)
        
        call = RecursiveCall(
            call_id=call_id,
            function_name=function_name,
            parameters=parameters,
            depth=depth,
            is_base_case=is_base_case
        )
        self.calls.append(call)
        self.call_stack.append(call_id)
        return call_id
    
    def exit_call(self, call_id: int, return_value: Any) -> None:
        """Record exiting a recursive call with its return value."""
        for call in self.calls:
            if call.call_id == call_id:
                call.return_value = return_value
                break
        if self.call_stack and self.call_stack[-1] == call_id:
            self.call_stack.pop()
    
    def print_trace(self) -> None:
        """Print a visual trace of all recursive calls."""
        print(f"\n{'='*60}")
        print(f"Recursion Trace (max depth: {self.max_depth})")
        print(f"{'='*60}")
        
        for call in self.calls:
            indent = "  " * call.depth
            params_str = ", ".join(f"{k}={v}" for k, v in call.parameters.items())
            base_marker = " [BASE CASE]" if call.is_base_case else ""
            print(f"{indent}-> {call.function_name}({params_str}){base_marker}")
            if call.return_value is not None:
                print(f"{indent}<- returns {call.return_value}")
        
        print(f"{'='*60}")
        print(f"Total calls: {len(self.calls)}")
        print(f"{'='*60}\n")


# Global tracker instance
tracker = RecursionTracker()


def factorial_recursive(n: int) -> int:
    """
    Calculate factorial using recursion.
    
    The factorial of n (written as n!) is the product of all positive
    integers from 1 to n. This recursive implementation demonstrates
    how a problem can be broken into smaller subproblems.
    
    Base case: factorial(0) = factorial(1) = 1
    Recursive case: factorial(n) = n * factorial(n-1)
    
    Args:
        n: A non-negative integer
        
    Returns:
        The factorial of n
        
    Time Complexity: O(n)
    Space Complexity: O(n) due to call stack
    """
    is_base = n <= 1
    call_id = tracker.enter_call("factorial", {"n": n}, is_base_case=is_base)
    
    if n <= 1:
        result = 1
    else:
        result = n * factorial_recursive(n - 1)
    
    tracker.exit_call(call_id, result)
    return result


def factorial_iterative(n: int) -> int:
    """
    Calculate factorial using iteration.
    
    This iterative version uses a simple loop instead of recursion,
    demonstrating that the same result can be achieved with O(1) space.
    
    Args:
        n: A non-negative integer
        
    Returns:
        The factorial of n
        
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def fibonacci_recursive(n: int) -> int:
    """
    Calculate the nth Fibonacci number using naive recursion.
    
    This implementation demonstrates the inefficiency of naive recursion
    due to overlapping subproblems. The same values are computed multiple
    times, leading to exponential time complexity.
    
    Base cases: fib(0) = 0, fib(1) = 1
    Recursive case: fib(n) = fib(n-1) + fib(n-2)
    
    Args:
        n: A non-negative integer
        
    Returns:
        The nth Fibonacci number
        
    Time Complexity: O(2^n) - exponential due to redundant calculations
    Space Complexity: O(n) due to call stack depth
    """
    is_base = n <= 1
    call_id = tracker.enter_call("fibonacci", {"n": n}, is_base_case=is_base)
    
    if n <= 1:
        result = n
    else:
        result = fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
    
    tracker.exit_call(call_id, result)
    return result


def fibonacci_memoized(n: int, memo: dict[int, int] | None = None) -> int:
    """
    Calculate the nth Fibonacci number using memoization.
    
    By caching previously computed values, we avoid redundant calculations
    and achieve linear time complexity. This demonstrates how memoization
    can dramatically improve recursive algorithm efficiency.
    
    Args:
        n: A non-negative integer
        memo: Cache for previously computed values
        
    Returns:
        The nth Fibonacci number
        
    Time Complexity: O(n)
    Space Complexity: O(n) for memoization cache and call stack
    """
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    
    is_base = n <= 1
    call_id = tracker.enter_call("fibonacci_memo", {"n": n}, is_base_case=is_base)
    
    if n <= 1:
        result = n
    else:
        result = fibonacci_memoized(n - 1, memo) + fibonacci_memoized(n - 2, memo)
    
    memo[n] = result
    tracker.exit_call(call_id, result)
    return result


def sum_digits(n: int) -> int:
    """
    Calculate the sum of digits in a positive integer using recursion.
    
    Base case: single digit number (n < 10)
    Recursive case: last digit + sum of remaining digits
    
    Args:
        n: A non-negative integer
        
    Returns:
        Sum of all digits in n
        
    Time Complexity: O(d) where d is the number of digits
    Space Complexity: O(d) due to call stack
    """
    is_base = n < 10
    call_id = tracker.enter_call("sum_digits", {"n": n}, is_base_case=is_base)
    
    if n < 10:
        result = n
    else:
        result = (n % 10) + sum_digits(n // 10)
    
    tracker.exit_call(call_id, result)
    return result


def power_recursive(base: float, exponent: int) -> float:
    """
    Calculate base raised to exponent using recursion.
    
    This implementation uses the divide-and-conquer approach:
    - If exponent is even: base^exp = (base^(exp/2))^2
    - If exponent is odd: base^exp = base * base^(exp-1)
    
    Args:
        base: The base number
        exponent: The exponent (non-negative integer)
        
    Returns:
        base raised to the power of exponent
        
    Time Complexity: O(log n) due to halving the exponent
    Space Complexity: O(log n) due to call stack
    """
    is_base = exponent == 0
    call_id = tracker.enter_call(
        "power",
        {"base": base, "exponent": exponent},
        is_base_case=is_base
    )
    
    if exponent == 0:
        result = 1.0
    elif exponent % 2 == 0:
        half_power = power_recursive(base, exponent // 2)
        result = half_power * half_power
    else:
        result = base * power_recursive(base, exponent - 1)
    
    tracker.exit_call(call_id, result)
    return result


def reverse_string(s: str) -> str:
    """
    Reverse a string using recursion.
    
    Base case: empty string or single character
    Recursive case: last character + reverse of remaining string
    
    Args:
        s: The string to reverse
        
    Returns:
        The reversed string
        
    Time Complexity: O(n²) due to string concatenation
    Space Complexity: O(n) for call stack and string storage
    """
    is_base = len(s) <= 1
    call_id = tracker.enter_call("reverse_string", {"s": s}, is_base_case=is_base)
    
    if len(s) <= 1:
        result = s
    else:
        result = s[-1] + reverse_string(s[:-1])
    
    tracker.exit_call(call_id, result)
    return result


def binary_search_recursive(
    arr: list[int],
    target: int,
    left: int = 0,
    right: int | None = None
) -> int:
    """
    Search for a target in a sorted array using recursive binary search.
    
    Base case: left > right (target not found) or arr[mid] == target
    Recursive case: search left or right half based on comparison
    
    Args:
        arr: A sorted array of integers
        target: The value to search for
        left: Left boundary of search range
        right: Right boundary of search range
        
    Returns:
        Index of target if found, -1 otherwise
        
    Time Complexity: O(log n)
    Space Complexity: O(log n) due to call stack
    """
    if right is None:
        right = len(arr) - 1
    
    is_base = left > right
    call_id = tracker.enter_call(
        "binary_search",
        {"target": target, "left": left, "right": right},
        is_base_case=is_base
    )
    
    if left > right:
        tracker.exit_call(call_id, -1)
        return -1
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        tracker.exit_call(call_id, mid)
        return mid
    elif arr[mid] < target:
        result = binary_search_recursive(arr, target, mid + 1, right)
    else:
        result = binary_search_recursive(arr, target, left, mid - 1)
    
    tracker.exit_call(call_id, result)
    return result


def demo() -> None:
    """Run demonstrations of recursive algorithms."""
    global tracker
    
    print("\n" + "="*60)
    print("RECURSION DEMONSTRATIONS")
    print("="*60)
    
    # Factorial Demo
    print("\n--- Factorial (Recursive) ---")
    tracker.reset()
    result = factorial_recursive(5)
    print(f"factorial(5) = {result}")
    tracker.print_trace()
    
    # Fibonacci Demo (small n to avoid too many calls)
    print("\n--- Fibonacci (Naive Recursive) ---")
    tracker.reset()
    result = fibonacci_recursive(6)
    print(f"fibonacci(6) = {result}")
    tracker.print_trace()
    
    # Fibonacci with Memoization
    print("\n--- Fibonacci (Memoized) ---")
    tracker.reset()
    result = fibonacci_memoized(6)
    print(f"fibonacci_memo(6) = {result}")
    tracker.print_trace()
    print("Notice: Memoized version makes far fewer calls!")
    
    # Sum of Digits Demo
    print("\n--- Sum of Digits ---")
    tracker.reset()
    result = sum_digits(12345)
    print(f"sum_digits(12345) = {result}")
    tracker.print_trace()
    
    # Power Demo
    print("\n--- Power (Divide and Conquer) ---")
    tracker.reset()
    result = power_recursive(2, 10)
    print(f"power(2, 10) = {result}")
    tracker.print_trace()
    
    # String Reversal Demo
    print("\n--- String Reversal ---")
    tracker.reset()
    result = reverse_string("hello")
    print(f"reverse_string('hello') = '{result}'")
    tracker.print_trace()
    
    # Binary Search Demo
    print("\n--- Binary Search (Recursive) ---")
    tracker.reset()
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    result = binary_search_recursive(arr, 11)
    print(f"binary_search({arr}, 11) = {result}")
    tracker.print_trace()


if __name__ == "__main__":
    demo()
