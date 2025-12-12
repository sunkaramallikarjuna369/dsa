"""
Searching Algorithm Exercises

Complete the functions below. Each function has a docstring
describing what it should do and example test cases.
"""

from typing import Any


# =============================================================================
# EXERCISE 1: Basic Search
# =============================================================================

def linear_search(arr: list[int], target: int) -> int:
    """
    Find target in array using linear search.
    
    Args:
        arr: List of integers (may be unsorted)
        target: Value to find
    
    Returns:
        Index of target if found, -1 otherwise
    
    Example:
        >>> linear_search([5, 3, 8, 1, 9], 8)
        2
        >>> linear_search([5, 3, 8, 1, 9], 7)
        -1
    """
    # TODO: Implement linear search
    pass


def binary_search_iterative(arr: list[int], target: int) -> int:
    """
    Find target in sorted array using iterative binary search.
    
    Args:
        arr: Sorted list of integers
        target: Value to find
    
    Returns:
        Index of target if found, -1 otherwise
    
    Example:
        >>> binary_search_iterative([1, 3, 5, 7, 9, 11], 7)
        3
        >>> binary_search_iterative([1, 3, 5, 7, 9, 11], 6)
        -1
    """
    # TODO: Implement iterative binary search
    pass


def binary_search_recursive(arr: list[int], target: int, low: int = 0, high: int | None = None) -> int:
    """
    Find target in sorted array using recursive binary search.
    
    Args:
        arr: Sorted list of integers
        target: Value to find
        low: Left boundary (default 0)
        high: Right boundary (default len(arr) - 1)
    
    Returns:
        Index of target if found, -1 otherwise
    
    Example:
        >>> binary_search_recursive([1, 3, 5, 7, 9, 11], 7)
        3
        >>> binary_search_recursive([1, 3, 5, 7, 9, 11], 6)
        -1
    """
    # TODO: Implement recursive binary search
    pass


# =============================================================================
# EXERCISE 2: Binary Search Variations
# =============================================================================

def search_insert_position(arr: list[int], target: int) -> int:
    """
    Find index where target should be inserted to maintain sorted order.
    
    If target exists, return its index.
    
    Args:
        arr: Sorted list of integers
        target: Value to insert
    
    Returns:
        Index where target should be inserted
    
    Example:
        >>> search_insert_position([1, 3, 5, 6], 5)
        2
        >>> search_insert_position([1, 3, 5, 6], 2)
        1
        >>> search_insert_position([1, 3, 5, 6], 7)
        4
    """
    # TODO: Implement using binary search
    pass


def find_first_occurrence(arr: list[int], target: int) -> int:
    """
    Find the first occurrence of target in sorted array with duplicates.
    
    Args:
        arr: Sorted list of integers (may have duplicates)
        target: Value to find
    
    Returns:
        Index of first occurrence, -1 if not found
    
    Example:
        >>> find_first_occurrence([1, 2, 2, 2, 3, 4], 2)
        1
        >>> find_first_occurrence([1, 2, 2, 2, 3, 4], 5)
        -1
    """
    # TODO: Implement using modified binary search
    pass


def find_last_occurrence(arr: list[int], target: int) -> int:
    """
    Find the last occurrence of target in sorted array with duplicates.
    
    Args:
        arr: Sorted list of integers (may have duplicates)
        target: Value to find
    
    Returns:
        Index of last occurrence, -1 if not found
    
    Example:
        >>> find_last_occurrence([1, 2, 2, 2, 3, 4], 2)
        3
        >>> find_last_occurrence([1, 2, 2, 2, 3, 4], 5)
        -1
    """
    # TODO: Implement using modified binary search
    pass


def count_occurrences(arr: list[int], target: int) -> int:
    """
    Count occurrences of target in sorted array.
    
    Args:
        arr: Sorted list of integers
        target: Value to count
    
    Returns:
        Number of occurrences
    
    Example:
        >>> count_occurrences([1, 2, 2, 2, 3, 4], 2)
        3
        >>> count_occurrences([1, 2, 2, 2, 3, 4], 5)
        0
    """
    # TODO: Use find_first and find_last
    pass


# =============================================================================
# EXERCISE 3: Rotated Array Search
# =============================================================================

def search_rotated_array(arr: list[int], target: int) -> int:
    """
    Search in a rotated sorted array (no duplicates).
    
    A sorted array has been rotated at some pivot.
    Example: [4, 5, 6, 7, 0, 1, 2] was [0, 1, 2, 4, 5, 6, 7] rotated.
    
    Args:
        arr: Rotated sorted array
        target: Value to find
    
    Returns:
        Index of target if found, -1 otherwise
    
    Example:
        >>> search_rotated_array([4, 5, 6, 7, 0, 1, 2], 0)
        4
        >>> search_rotated_array([4, 5, 6, 7, 0, 1, 2], 3)
        -1
    """
    # TODO: Implement modified binary search
    pass


def find_rotation_count(arr: list[int]) -> int:
    """
    Find how many times a sorted array has been rotated.
    
    This is equivalent to finding the index of the minimum element.
    
    Args:
        arr: Rotated sorted array
    
    Returns:
        Number of rotations (index of minimum)
    
    Example:
        >>> find_rotation_count([4, 5, 6, 7, 0, 1, 2])
        4
        >>> find_rotation_count([1, 2, 3, 4, 5])
        0
    """
    # TODO: Find minimum element index using binary search
    pass


def find_minimum_rotated(arr: list[int]) -> int:
    """
    Find the minimum element in a rotated sorted array.
    
    Args:
        arr: Rotated sorted array
    
    Returns:
        Minimum element value
    
    Example:
        >>> find_minimum_rotated([4, 5, 6, 7, 0, 1, 2])
        0
        >>> find_minimum_rotated([3, 4, 5, 1, 2])
        1
    """
    # TODO: Use binary search to find minimum
    pass


# =============================================================================
# EXERCISE 4: Advanced Binary Search
# =============================================================================

def find_peak_element(arr: list[int]) -> int:
    """
    Find a peak element (greater than neighbors).
    
    Array may have multiple peaks; return any peak index.
    Assume arr[-1] = arr[n] = -infinity.
    
    Args:
        arr: List of integers
    
    Returns:
        Index of a peak element
    
    Example:
        >>> arr = [1, 2, 3, 1]
        >>> find_peak_element(arr)
        2
        >>> arr = [1, 2, 1, 3, 5, 6, 4]
        >>> find_peak_element(arr) in [1, 5]
        True
    """
    # TODO: Use binary search to find peak
    pass


def sqrt_integer(x: int) -> int:
    """
    Compute integer square root of x.
    
    Return the largest integer n such that n*n <= x.
    
    Args:
        x: Non-negative integer
    
    Returns:
        Integer square root
    
    Example:
        >>> sqrt_integer(8)
        2
        >>> sqrt_integer(16)
        4
        >>> sqrt_integer(0)
        0
    """
    # TODO: Use binary search
    pass


def find_smallest_letter_greater(letters: list[str], target: str) -> str:
    """
    Find smallest letter greater than target in sorted list.
    
    Letters wrap around (if target >= all letters, return first letter).
    
    Args:
        letters: Sorted list of lowercase letters
        target: Target letter
    
    Returns:
        Smallest letter greater than target
    
    Example:
        >>> find_smallest_letter_greater(['c', 'f', 'j'], 'a')
        'c'
        >>> find_smallest_letter_greater(['c', 'f', 'j'], 'c')
        'f'
        >>> find_smallest_letter_greater(['c', 'f', 'j'], 'j')
        'c'
    """
    # TODO: Use binary search with wrap-around
    pass


# =============================================================================
# EXERCISE 5: 2D Search
# =============================================================================

def search_matrix(matrix: list[list[int]], target: int) -> bool:
    """
    Search in a row-wise and column-wise sorted matrix.
    
    Each row is sorted left to right.
    First element of each row is greater than last element of previous row.
    
    Args:
        matrix: 2D sorted matrix
        target: Value to find
    
    Returns:
        True if target exists in matrix
    
    Example:
        >>> matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        >>> search_matrix(matrix, 3)
        True
        >>> search_matrix(matrix, 13)
        False
    """
    # TODO: Treat as 1D array or use two binary searches
    pass


def search_matrix_2(matrix: list[list[int]], target: int) -> bool:
    """
    Search in a matrix where each row and column is sorted.
    
    Each row is sorted left to right.
    Each column is sorted top to bottom.
    (But first element of row may not be > last element of previous row)
    
    Args:
        matrix: 2D matrix with sorted rows and columns
        target: Value to find
    
    Returns:
        True if target exists in matrix
    
    Example:
        >>> matrix = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
        >>> search_matrix_2(matrix, 5)
        True
        >>> search_matrix_2(matrix, 10)
        False
    """
    # TODO: Start from top-right or bottom-left corner
    pass


# =============================================================================
# TEST CASES
# =============================================================================

def run_tests() -> None:
    """Run all test cases."""
    print("Running Searching Algorithm Exercise Tests...")
    print("=" * 60)
    
    # Test linear_search
    print("\n1. Testing linear_search:")
    test_cases = [
        (([5, 3, 8, 1, 9], 8), 2),
        (([5, 3, 8, 1, 9], 7), -1),
        (([1], 1), 0),
    ]
    for (arr, target), expected in test_cases:
        result = linear_search(arr, target)
        status = "PASS" if result == expected else "FAIL"
        print(f"  linear_search({arr}, {target}) = {result}, expected {expected} [{status}]")
    
    # Test binary_search_iterative
    print("\n2. Testing binary_search_iterative:")
    test_cases = [
        (([1, 3, 5, 7, 9, 11], 7), 3),
        (([1, 3, 5, 7, 9, 11], 6), -1),
        (([1, 3, 5, 7, 9, 11], 1), 0),
    ]
    for (arr, target), expected in test_cases:
        result = binary_search_iterative(arr, target)
        status = "PASS" if result == expected else "FAIL"
        print(f"  binary_search_iterative({arr}, {target}) = {result}, expected {expected} [{status}]")
    
    # Test search_insert_position
    print("\n3. Testing search_insert_position:")
    test_cases = [
        (([1, 3, 5, 6], 5), 2),
        (([1, 3, 5, 6], 2), 1),
        (([1, 3, 5, 6], 7), 4),
        (([1, 3, 5, 6], 0), 0),
    ]
    for (arr, target), expected in test_cases:
        result = search_insert_position(arr, target)
        status = "PASS" if result == expected else "FAIL"
        print(f"  search_insert_position({arr}, {target}) = {result}, expected {expected} [{status}]")
    
    # Test find_first_occurrence
    print("\n4. Testing find_first_occurrence:")
    test_cases = [
        (([1, 2, 2, 2, 3, 4], 2), 1),
        (([1, 2, 2, 2, 3, 4], 5), -1),
    ]
    for (arr, target), expected in test_cases:
        result = find_first_occurrence(arr, target)
        status = "PASS" if result == expected else "FAIL"
        print(f"  find_first_occurrence({arr}, {target}) = {result}, expected {expected} [{status}]")
    
    # Test search_rotated_array
    print("\n5. Testing search_rotated_array:")
    test_cases = [
        (([4, 5, 6, 7, 0, 1, 2], 0), 4),
        (([4, 5, 6, 7, 0, 1, 2], 3), -1),
        (([1], 1), 0),
    ]
    for (arr, target), expected in test_cases:
        result = search_rotated_array(arr, target)
        status = "PASS" if result == expected else "FAIL"
        print(f"  search_rotated_array({arr}, {target}) = {result}, expected {expected} [{status}]")
    
    # Test find_peak_element
    print("\n6. Testing find_peak_element:")
    arr = [1, 2, 3, 1]
    result = find_peak_element(arr)
    expected = 2
    status = "PASS" if result == expected else "FAIL"
    print(f"  find_peak_element({arr}) = {result}, expected {expected} [{status}]")
    
    # Test sqrt_integer
    print("\n7. Testing sqrt_integer:")
    test_cases = [
        (8, 2),
        (16, 4),
        (0, 0),
        (1, 1),
    ]
    for x, expected in test_cases:
        result = sqrt_integer(x)
        status = "PASS" if result == expected else "FAIL"
        print(f"  sqrt_integer({x}) = {result}, expected {expected} [{status}]")
    
    # Test search_matrix
    print("\n8. Testing search_matrix:")
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    test_cases = [
        (3, True),
        (13, False),
    ]
    for target, expected in test_cases:
        result = search_matrix(matrix, target)
        status = "PASS" if result == expected else "FAIL"
        print(f"  search_matrix(matrix, {target}) = {result}, expected {expected} [{status}]")
    
    print("\n" + "=" * 60)
    print("Tests complete! Implement the functions to make them pass.")


if __name__ == "__main__":
    run_tests()
