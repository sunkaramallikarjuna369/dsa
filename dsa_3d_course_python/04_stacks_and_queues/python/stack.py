"""
Stack Module

This module provides implementations of stack data structure
with step-by-step tracking for 3D visualization synchronization.

A stack follows the Last-In-First-Out (LIFO) principle where
the most recently added element is the first to be removed.
"""

from typing import Any, TypeVar, Generic
from dataclasses import dataclass, field

T = TypeVar('T')


@dataclass
class StackStep:
    """Represents a single step in stack visualization."""
    step_number: int
    operation: str
    description: str
    element_value: Any = None
    stack_state: list[Any] = field(default_factory=list)
    top_index: int = -1


class Stack(Generic[T]):
    """
    A stack implementation using a Python list with visualization tracking.
    
    Supports standard stack operations: push, pop, peek, is_empty.
    All operations are O(1) amortized time complexity.
    """
    
    def __init__(self, capacity: int | None = None) -> None:
        """
        Initialize an empty stack.
        
        Args:
            capacity: Optional maximum capacity (None for unlimited)
        """
        self._data: list[T] = []
        self._capacity = capacity
        self._steps: list[StackStep] = []
        self._step_count: int = 0
    
    def _record_step(
        self,
        operation: str,
        description: str,
        element_value: Any = None
    ) -> None:
        """Record a visualization step."""
        self._step_count += 1
        step = StackStep(
            step_number=self._step_count,
            operation=operation,
            description=description,
            element_value=element_value,
            stack_state=list(self._data),
            top_index=len(self._data) - 1
        )
        self._steps.append(step)
    
    def clear_steps(self) -> None:
        """Clear recorded steps for a new operation sequence."""
        self._steps = []
        self._step_count = 0
    
    @property
    def steps(self) -> list[StackStep]:
        """Return all recorded steps."""
        return self._steps
    
    def push(self, item: T) -> bool:
        """
        Push an item onto the top of the stack.
        
        Time Complexity: O(1) amortized
        
        Args:
            item: The item to push
            
        Returns:
            True if successful, False if stack is full
        """
        if self._capacity is not None and len(self._data) >= self._capacity:
            self._record_step(
                "overflow",
                f"Stack overflow! Cannot push {item} - stack is full",
                element_value=item
            )
            return False
        
        self._record_step(
            "push_start",
            f"Pushing {item} onto stack",
            element_value=item
        )
        
        self._data.append(item)
        
        self._record_step(
            "push_complete",
            f"Pushed {item} - now at top (index {len(self._data) - 1})",
            element_value=item
        )
        
        return True
    
    def pop(self) -> T | None:
        """
        Remove and return the top item from the stack.
        
        Time Complexity: O(1)
        
        Returns:
            The top item, or None if stack is empty
        """
        if self.is_empty():
            self._record_step(
                "underflow",
                "Stack underflow! Cannot pop from empty stack"
            )
            return None
        
        item = self._data[-1]
        self._record_step(
            "pop_start",
            f"Popping top element: {item}",
            element_value=item
        )
        
        self._data.pop()
        
        self._record_step(
            "pop_complete",
            f"Popped {item} - new top is {self._data[-1] if self._data else 'empty'}",
            element_value=item
        )
        
        return item
    
    def peek(self) -> T | None:
        """
        Return the top item without removing it.
        
        Time Complexity: O(1)
        
        Returns:
            The top item, or None if stack is empty
        """
        if self.is_empty():
            self._record_step(
                "peek_empty",
                "Cannot peek - stack is empty"
            )
            return None
        
        item = self._data[-1]
        self._record_step(
            "peek",
            f"Peeking at top element: {item}",
            element_value=item
        )
        
        return item
    
    def is_empty(self) -> bool:
        """Check if the stack is empty."""
        return len(self._data) == 0
    
    def is_full(self) -> bool:
        """Check if the stack is full (only relevant if capacity is set)."""
        if self._capacity is None:
            return False
        return len(self._data) >= self._capacity
    
    def size(self) -> int:
        """Return the number of elements in the stack."""
        return len(self._data)
    
    def to_list(self) -> list[T]:
        """Return a copy of the stack as a list (bottom to top)."""
        return list(self._data)
    
    def __len__(self) -> int:
        return len(self._data)
    
    def __repr__(self) -> str:
        return f"Stack({self._data})"
    
    def print_steps(self) -> None:
        """Print all recorded steps."""
        print(f"\n{'='*60}")
        print(f"Stack Operation Steps ({len(self._steps)} total)")
        print(f"{'='*60}")
        for step in self._steps:
            print(f"Step {step.step_number}: [{step.operation}] {step.description}")
            print(f"  Stack: {step.stack_state} (top index: {step.top_index})")
        print(f"{'='*60}\n")


class LinkedStack(Generic[T]):
    """
    A stack implementation using a linked list.
    
    Each node contains a value and a reference to the next node.
    The top of the stack is the head of the linked list.
    """
    
    class Node(Generic[T]):
        """A node in the linked stack."""
        def __init__(self, value: T) -> None:
            self.value: T = value
            self.next: LinkedStack.Node[T] | None = None
    
    def __init__(self) -> None:
        """Initialize an empty linked stack."""
        self._top: LinkedStack.Node[T] | None = None
        self._size: int = 0
    
    def push(self, item: T) -> None:
        """Push an item onto the stack - O(1)."""
        new_node = LinkedStack.Node(item)
        new_node.next = self._top
        self._top = new_node
        self._size += 1
    
    def pop(self) -> T | None:
        """Pop and return the top item - O(1)."""
        if self._top is None:
            return None
        item = self._top.value
        self._top = self._top.next
        self._size -= 1
        return item
    
    def peek(self) -> T | None:
        """Return the top item without removing - O(1)."""
        return self._top.value if self._top else None
    
    def is_empty(self) -> bool:
        """Check if stack is empty."""
        return self._top is None
    
    def size(self) -> int:
        """Return the number of elements."""
        return self._size
    
    def to_list(self) -> list[T]:
        """Convert to list (bottom to top)."""
        result: list[T] = []
        current = self._top
        while current:
            result.append(current.value)
            current = current.next
        return list(reversed(result))


def is_valid_parentheses(s: str) -> tuple[bool, list[StackStep]]:
    """
    Check if a string of parentheses is valid using a stack.
    
    A string is valid if:
    - Every opening bracket has a matching closing bracket
    - Brackets are closed in the correct order
    
    Args:
        s: String containing only '(', ')', '[', ']', '{', '}'
        
    Returns:
        Tuple of (is_valid, visualization steps)
        
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    stack = Stack[str]()
    matching = {')': '(', ']': '[', '}': '{'}
    
    stack._record_step("start", f"Checking string: '{s}'")
    
    for i, char in enumerate(s):
        if char in '([{':
            stack.push(char)
            stack._record_step(
                "push_open",
                f"Position {i}: Found '{char}' - push onto stack"
            )
        elif char in ')]}':
            if stack.is_empty():
                stack._record_step(
                    "invalid",
                    f"Position {i}: Found '{char}' but stack is empty - INVALID"
                )
                return False, stack.steps
            
            top = stack.pop()
            if top != matching[char]:
                stack._record_step(
                    "mismatch",
                    f"Position {i}: '{char}' doesn't match '{top}' - INVALID"
                )
                return False, stack.steps
            
            stack._record_step(
                "match",
                f"Position {i}: '{char}' matches '{top}' - valid pair"
            )
    
    is_valid = stack.is_empty()
    stack._record_step(
        "result",
        f"End of string: stack is {'empty - VALID' if is_valid else 'not empty - INVALID'}"
    )
    
    return is_valid, stack.steps


def evaluate_postfix(expression: str) -> tuple[float, list[StackStep]]:
    """
    Evaluate a postfix expression using a stack.
    
    Args:
        expression: Space-separated postfix expression (e.g., "3 4 + 2 *")
        
    Returns:
        Tuple of (result, visualization steps)
        
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    stack = Stack[float]()
    operators = {'+', '-', '*', '/'}
    
    stack._record_step("start", f"Evaluating postfix: '{expression}'")
    
    tokens = expression.split()
    
    for token in tokens:
        if token in operators:
            b = stack.pop()
            a = stack.pop()
            
            if a is None or b is None:
                stack._record_step("error", "Not enough operands")
                return 0, stack.steps
            
            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            else:  # token == '/'
                result = a / b
            
            stack._record_step(
                "operate",
                f"Apply {token}: {a} {token} {b} = {result}"
            )
            stack.push(result)
        else:
            num = float(token)
            stack.push(num)
            stack._record_step(
                "push_operand",
                f"Push operand: {num}"
            )
    
    result = stack.pop()
    stack._record_step("result", f"Final result: {result}")
    
    return result if result is not None else 0, stack.steps


def reverse_string_with_stack(s: str) -> tuple[str, list[StackStep]]:
    """
    Reverse a string using a stack.
    
    Args:
        s: The string to reverse
        
    Returns:
        Tuple of (reversed string, visualization steps)
    """
    stack = Stack[str]()
    
    stack._record_step("start", f"Reversing string: '{s}'")
    
    for char in s:
        stack.push(char)
    
    stack._record_step("pushed_all", f"All characters pushed onto stack")
    
    result: list[str] = []
    while not stack.is_empty():
        char = stack.pop()
        if char:
            result.append(char)
    
    reversed_str = ''.join(result)
    stack._record_step("result", f"Reversed string: '{reversed_str}'")
    
    return reversed_str, stack.steps


def demo() -> None:
    """Run demonstrations of stack operations."""
    print("\n" + "="*60)
    print("STACK DEMONSTRATIONS")
    print("="*60)
    
    # Basic Stack Operations
    print("\n--- Basic Stack Operations ---")
    stack = Stack[int](capacity=5)
    
    print("Pushing 10, 20, 30:")
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print(f"Stack: {stack.to_list()}")
    
    print(f"\nPeek: {stack.peek()}")
    print(f"Pop: {stack.pop()}")
    print(f"Stack after pop: {stack.to_list()}")
    stack.print_steps()
    
    # Valid Parentheses
    print("\n--- Valid Parentheses ---")
    test_cases = ["([]{})", "([)]", "((()))", ""]
    for test in test_cases:
        is_valid, steps = is_valid_parentheses(test)
        print(f"'{test}' is valid: {is_valid}")
    
    # Postfix Evaluation
    print("\n--- Postfix Expression Evaluation ---")
    expression = "3 4 + 2 * 7 /"
    result, steps = evaluate_postfix(expression)
    print(f"Expression: {expression}")
    print(f"Result: {result}")
    
    # String Reversal
    print("\n--- String Reversal with Stack ---")
    original = "HELLO"
    reversed_str, steps = reverse_string_with_stack(original)
    print(f"Original: {original}")
    print(f"Reversed: {reversed_str}")


if __name__ == "__main__":
    demo()
