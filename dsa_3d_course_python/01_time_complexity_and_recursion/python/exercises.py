"""
Exercises: Time Complexity and Recursion

Complete the following exercises to practice analyzing time complexity
and implementing recursive algorithms. Each function has a docstring
explaining what to implement and the expected time/space complexity.

Run this file to test your implementations against the provided test cases.
"""

from typing import Any


# =============================================================================
# EXERCISE 1: Complexity Analysis
# =============================================================================

def find_max_element(arr: list[int]) -> int | None:
    """
    Find the maximum element in an array.
    
    TODO: Implement this function.
    
    Args:
        arr: A list of integers (may be empty)
        
    Returns:
        The maximum element, or None if array is empty
        
    Expected Time Complexity: O(n)
    Expected Space Complexity: O(1)
    
    Hint: You need to look at every element at least once to be sure
    you've found the maximum.
    """
    # TODO: Implement this function
    pass


def has_duplicate(arr: list[Any]) -> bool:
    """
    Check if an array contains any duplicate elements.
    
    TODO: Implement this function using a set for O(n) time complexity.
    
    Args:
        arr: A list of elements
        
    Returns:
        True if there are duplicates, False otherwise
        
    Expected Time Complexity: O(n)
    Expected Space Complexity: O(n)
    
    Hint: A set allows O(1) lookup. As you iterate through the array,
    check if each element is already in the set.
    """
    # TODO: Implement this function
    pass


def count_pairs_with_sum(arr: list[int], target_sum: int) -> int:
    """
    Count the number of pairs in the array that sum to target_sum.
    
    TODO: Implement this function. Try to achieve O(n) time complexity
    using a hash map approach.
    
    Args:
        arr: A list of integers
        target_sum: The target sum to find
        
    Returns:
        The count of pairs that sum to target_sum
        
    Expected Time Complexity: O(n)
    Expected Space Complexity: O(n)
    
    Hint: For each element x, check if (target_sum - x) exists in a set
    of previously seen elements.
    """
    # TODO: Implement this function
    pass


# =============================================================================
# EXERCISE 2: Basic Recursion
# =============================================================================

def sum_of_list(arr: list[int]) -> int:
    """
    Calculate the sum of all elements in a list using recursion.
    
    TODO: Implement this function recursively.
    
    Base case: Empty list returns 0
    Recursive case: First element + sum of rest of list
    
    Args:
        arr: A list of integers
        
    Returns:
        The sum of all elements
        
    Expected Time Complexity: O(n)
    Expected Space Complexity: O(n) due to call stack
    """
    # TODO: Implement this function
    pass


def count_occurrences(arr: list[Any], target: Any) -> int:
    """
    Count how many times target appears in the array using recursion.
    
    TODO: Implement this function recursively.
    
    Base case: Empty list returns 0
    Recursive case: (1 if first element matches else 0) + count in rest
    
    Args:
        arr: A list of elements
        target: The element to count
        
    Returns:
        The number of occurrences of target
        
    Expected Time Complexity: O(n)
    Expected Space Complexity: O(n) due to call stack
    """
    # TODO: Implement this function
    pass


def is_palindrome(s: str) -> bool:
    """
    Check if a string is a palindrome using recursion.
    
    TODO: Implement this function recursively.
    
    Base case: Empty string or single character is a palindrome
    Recursive case: First char == last char AND middle is palindrome
    
    Args:
        s: A string to check
        
    Returns:
        True if s is a palindrome, False otherwise
        
    Expected Time Complexity: O(n)
    Expected Space Complexity: O(n) due to call stack
    """
    # TODO: Implement this function
    pass


# =============================================================================
# EXERCISE 3: Advanced Recursion
# =============================================================================

def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor using Euclidean algorithm.
    
    TODO: Implement this function recursively.
    
    Base case: If b is 0, return a
    Recursive case: gcd(b, a % b)
    
    Args:
        a: First positive integer
        b: Second positive integer
        
    Returns:
        The greatest common divisor of a and b
        
    Expected Time Complexity: O(log(min(a, b)))
    Expected Space Complexity: O(log(min(a, b))) due to call stack
    """
    # TODO: Implement this function
    pass


def flatten_list(nested: list) -> list:
    """
    Flatten a nested list structure into a single-level list.
    
    TODO: Implement this function recursively.
    
    Example: [[1, 2], [3, [4, 5]], 6] -> [1, 2, 3, 4, 5, 6]
    
    Args:
        nested: A potentially nested list
        
    Returns:
        A flattened list with all elements at one level
        
    Hint: Check if each element is a list. If so, recursively flatten it.
    """
    # TODO: Implement this function
    pass


def tower_of_hanoi(n: int, source: str, auxiliary: str, target: str) -> list[tuple[str, str]]:
    """
    Solve the Tower of Hanoi puzzle and return the sequence of moves.
    
    TODO: Implement this function recursively.
    
    The puzzle: Move n disks from source peg to target peg, using auxiliary peg.
    Rules: Only one disk can be moved at a time, and a larger disk cannot
    be placed on top of a smaller disk.
    
    Base case: n == 1, move disk directly from source to target
    Recursive case:
        1. Move n-1 disks from source to auxiliary
        2. Move largest disk from source to target
        3. Move n-1 disks from auxiliary to target
    
    Args:
        n: Number of disks
        source: Name of source peg
        auxiliary: Name of auxiliary peg
        target: Name of target peg
        
    Returns:
        List of moves as tuples (from_peg, to_peg)
        
    Expected Time Complexity: O(2^n)
    Expected Space Complexity: O(n) for call stack, O(2^n) for output
    """
    # TODO: Implement this function
    pass


# =============================================================================
# EXERCISE 4: Iteration to Recursion Conversion
# =============================================================================

def binary_to_decimal_iterative(binary_str: str) -> int:
    """
    Convert a binary string to decimal (iterative version provided).
    
    This is the iterative reference implementation.
    """
    result = 0
    for digit in binary_str:
        result = result * 2 + int(digit)
    return result


def binary_to_decimal_recursive(binary_str: str) -> int:
    """
    Convert a binary string to decimal using recursion.
    
    TODO: Convert the iterative version above to a recursive implementation.
    
    Hint: Process one digit at a time. The value of a binary number is:
    (value of all but last digit) * 2 + (last digit)
    
    Args:
        binary_str: A string of '0's and '1's
        
    Returns:
        The decimal equivalent
        
    Expected Time Complexity: O(n) where n is length of string
    Expected Space Complexity: O(n) due to call stack
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
    
    # Test find_max_element
    print("\n--- Testing find_max_element ---")
    tests = [
        ([3, 1, 4, 1, 5, 9, 2, 6], 9),
        ([1], 1),
        ([-5, -2, -8, -1], -1),
        ([], None),
    ]
    for arr, expected in tests:
        result = find_max_element(arr)
        status = "PASS" if result == expected else "FAIL"
        if status == "FAIL":
            all_passed = False
        print(f"  find_max_element({arr}) = {result}, expected {expected} [{status}]")
    
    # Test has_duplicate
    print("\n--- Testing has_duplicate ---")
    tests = [
        ([1, 2, 3, 4, 5], False),
        ([1, 2, 3, 2, 5], True),
        ([], False),
        ([1], False),
    ]
    for arr, expected in tests:
        result = has_duplicate(arr)
        status = "PASS" if result == expected else "FAIL"
        if status == "FAIL":
            all_passed = False
        print(f"  has_duplicate({arr}) = {result}, expected {expected} [{status}]")
    
    # Test count_pairs_with_sum
    print("\n--- Testing count_pairs_with_sum ---")
    tests = [
        ([1, 2, 3, 4, 5], 5, 2),  # (1,4), (2,3)
        ([1, 1, 1, 1], 2, 6),  # All pairs of 1s
        ([1, 2, 3], 10, 0),
    ]
    for arr, target, expected in tests:
        result = count_pairs_with_sum(arr, target)
        status = "PASS" if result == expected else "FAIL"
        if status == "FAIL":
            all_passed = False
        print(f"  count_pairs_with_sum({arr}, {target}) = {result}, expected {expected} [{status}]")
    
    # Test sum_of_list
    print("\n--- Testing sum_of_list ---")
    tests = [
        ([1, 2, 3, 4, 5], 15),
        ([], 0),
        ([10], 10),
        ([-1, 1, -2, 2], 0),
    ]
    for arr, expected in tests:
        result = sum_of_list(arr)
        status = "PASS" if result == expected else "FAIL"
        if status == "FAIL":
            all_passed = False
        print(f"  sum_of_list({arr}) = {result}, expected {expected} [{status}]")
    
    # Test count_occurrences
    print("\n--- Testing count_occurrences ---")
    tests = [
        ([1, 2, 3, 2, 2, 4], 2, 3),
        ([1, 2, 3], 5, 0),
        ([], 1, 0),
    ]
    for arr, target, expected in tests:
        result = count_occurrences(arr, target)
        status = "PASS" if result == expected else "FAIL"
        if status == "FAIL":
            all_passed = False
        print(f"  count_occurrences({arr}, {target}) = {result}, expected {expected} [{status}]")
    
    # Test is_palindrome
    print("\n--- Testing is_palindrome ---")
    tests = [
        ("racecar", True),
        ("hello", False),
        ("a", True),
        ("", True),
        ("abba", True),
    ]
    for s, expected in tests:
        result = is_palindrome(s)
        status = "PASS" if result == expected else "FAIL"
        if status == "FAIL":
            all_passed = False
        print(f"  is_palindrome('{s}') = {result}, expected {expected} [{status}]")
    
    # Test gcd
    print("\n--- Testing gcd ---")
    tests = [
        (48, 18, 6),
        (17, 13, 1),
        (100, 25, 25),
    ]
    for a, b, expected in tests:
        result = gcd(a, b)
        status = "PASS" if result == expected else "FAIL"
        if status == "FAIL":
            all_passed = False
        print(f"  gcd({a}, {b}) = {result}, expected {expected} [{status}]")
    
    # Test flatten_list
    print("\n--- Testing flatten_list ---")
    tests = [
        ([[1, 2], [3, [4, 5]], 6], [1, 2, 3, 4, 5, 6]),
        ([1, 2, 3], [1, 2, 3]),
        ([[[[1]]]], [1]),
        ([], []),
    ]
    for nested, expected in tests:
        result = flatten_list(nested)
        status = "PASS" if result == expected else "FAIL"
        if status == "FAIL":
            all_passed = False
        print(f"  flatten_list({nested}) = {result}, expected {expected} [{status}]")
    
    # Test tower_of_hanoi
    print("\n--- Testing tower_of_hanoi ---")
    result = tower_of_hanoi(3, 'A', 'B', 'C')
    expected_length = 7  # 2^3 - 1 moves
    if result is not None:
        status = "PASS" if len(result) == expected_length else "FAIL"
        if status == "FAIL":
            all_passed = False
        print(f"  tower_of_hanoi(3, 'A', 'B', 'C') returned {len(result)} moves, expected {expected_length} [{status}]")
    else:
        print(f"  tower_of_hanoi(3, 'A', 'B', 'C') returned None [FAIL]")
        all_passed = False
    
    # Test binary_to_decimal_recursive
    print("\n--- Testing binary_to_decimal_recursive ---")
    tests = [
        ("1010", 10),
        ("1111", 15),
        ("1", 1),
        ("0", 0),
        ("11001", 25),
    ]
    for binary_str, expected in tests:
        result = binary_to_decimal_recursive(binary_str)
        status = "PASS" if result == expected else "FAIL"
        if status == "FAIL":
            all_passed = False
        print(f"  binary_to_decimal_recursive('{binary_str}') = {result}, expected {expected} [{status}]")
    
    print("\n" + "="*60)
    if all_passed:
        print("ALL TESTS PASSED!")
    else:
        print("SOME TESTS FAILED - Keep working on your implementations!")
    print("="*60 + "\n")


if __name__ == "__main__":
    run_tests()
