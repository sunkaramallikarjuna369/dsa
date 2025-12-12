"""
Exercises: Arrays and Strings

Complete the following exercises to practice array and string manipulation.
Each function has a docstring explaining what to implement.

Run this file to test your implementations against the provided test cases.
"""

from typing import Any


# =============================================================================
# EXERCISE 1: Array Basics
# =============================================================================

def find_second_largest(arr: list[int]) -> int | None:
    """
    Find the second largest element in an array.
    
    TODO: Implement this function.
    
    Args:
        arr: A list of integers (may have duplicates)
        
    Returns:
        The second largest unique element, or None if it doesn't exist
        
    Expected Time Complexity: O(n)
    Expected Space Complexity: O(1)
    
    Example:
        find_second_largest([1, 5, 2, 5, 3]) -> 3
        find_second_largest([1, 1, 1]) -> None
    """
    # TODO: Implement this function
    pass


def rotate_array(arr: list[Any], k: int) -> list[Any]:
    """
    Rotate array to the right by k positions.
    
    TODO: Implement this function in-place (modify the input array).
    
    Args:
        arr: The array to rotate
        k: Number of positions to rotate right
        
    Returns:
        The rotated array (same object, modified in place)
        
    Expected Time Complexity: O(n)
    Expected Space Complexity: O(1)
    
    Example:
        rotate_array([1, 2, 3, 4, 5], 2) -> [4, 5, 1, 2, 3]
    
    Hint: Use the reversal algorithm:
        1. Reverse entire array
        2. Reverse first k elements
        3. Reverse remaining elements
    """
    # TODO: Implement this function
    pass


def merge_sorted_arrays(arr1: list[int], arr2: list[int]) -> list[int]:
    """
    Merge two sorted arrays into one sorted array.
    
    TODO: Implement this function.
    
    Args:
        arr1: First sorted array
        arr2: Second sorted array
        
    Returns:
        A new sorted array containing all elements
        
    Expected Time Complexity: O(n + m)
    Expected Space Complexity: O(n + m)
    
    Hint: Use two pointers, one for each array.
    """
    # TODO: Implement this function
    pass


# =============================================================================
# EXERCISE 2: Two-Pointer Techniques
# =============================================================================

def remove_duplicates_sorted(arr: list[int]) -> int:
    """
    Remove duplicates from a sorted array in-place.
    
    TODO: Implement this function.
    
    Args:
        arr: A sorted array (modified in place)
        
    Returns:
        The new length of the array after removing duplicates
        
    Expected Time Complexity: O(n)
    Expected Space Complexity: O(1)
    
    Example:
        arr = [1, 1, 2, 2, 3]
        length = remove_duplicates_sorted(arr)
        # length = 3, arr[:length] = [1, 2, 3]
    
    Hint: Use two pointers - one for reading, one for writing.
    """
    # TODO: Implement this function
    pass


def container_with_most_water(heights: list[int]) -> int:
    """
    Find two lines that together with x-axis form a container with most water.
    
    TODO: Implement this function.
    
    Args:
        heights: List of line heights
        
    Returns:
        Maximum area of water the container can hold
        
    Expected Time Complexity: O(n)
    Expected Space Complexity: O(1)
    
    Example:
        container_with_most_water([1, 8, 6, 2, 5, 4, 8, 3, 7]) -> 49
    
    Hint: Use two pointers starting at opposite ends.
    Area = min(height[left], height[right]) * (right - left)
    Move the pointer with smaller height inward.
    """
    # TODO: Implement this function
    pass


def three_sum(arr: list[int], target: int) -> list[tuple[int, int, int]]:
    """
    Find all unique triplets that sum to target.
    
    TODO: Implement this function.
    
    Args:
        arr: List of integers
        target: Target sum
        
    Returns:
        List of unique triplets (as tuples) that sum to target
        
    Expected Time Complexity: O(n²)
    Expected Space Complexity: O(1) excluding output
    
    Hint: Sort the array first, then for each element, use two-pointer
    technique to find pairs that sum to (target - element).
    """
    # TODO: Implement this function
    pass


# =============================================================================
# EXERCISE 3: Sliding Window
# =============================================================================

def max_sum_subarray(arr: list[int], k: int) -> int:
    """
    Find maximum sum of any contiguous subarray of size k.
    
    TODO: Implement this function using sliding window.
    
    Args:
        arr: List of integers
        k: Window size
        
    Returns:
        Maximum sum of any k consecutive elements
        
    Expected Time Complexity: O(n)
    Expected Space Complexity: O(1)
    """
    # TODO: Implement this function
    pass


def longest_substring_k_distinct(s: str, k: int) -> int:
    """
    Find length of longest substring with at most k distinct characters.
    
    TODO: Implement this function using sliding window.
    
    Args:
        s: Input string
        k: Maximum number of distinct characters
        
    Returns:
        Length of longest valid substring
        
    Expected Time Complexity: O(n)
    Expected Space Complexity: O(k)
    
    Example:
        longest_substring_k_distinct("eceba", 2) -> 3  # "ece"
    """
    # TODO: Implement this function
    pass


def minimum_window_substring(s: str, t: str) -> str:
    """
    Find minimum window in s that contains all characters of t.
    
    TODO: Implement this function using sliding window.
    
    Args:
        s: Source string
        t: Target string (characters to include)
        
    Returns:
        Minimum window substring, or "" if not found
        
    Expected Time Complexity: O(n + m)
    Expected Space Complexity: O(m)
    
    Example:
        minimum_window_substring("ADOBECODEBANC", "ABC") -> "BANC"
    """
    # TODO: Implement this function
    pass


# =============================================================================
# EXERCISE 4: String Manipulation
# =============================================================================

def valid_anagram(s: str, t: str) -> bool:
    """
    Check if t is an anagram of s.
    
    TODO: Implement this function.
    
    Args:
        s: First string
        t: Second string
        
    Returns:
        True if t is an anagram of s
        
    Expected Time Complexity: O(n)
    Expected Space Complexity: O(1) - only 26 letters
    """
    # TODO: Implement this function
    pass


def group_anagrams(strs: list[str]) -> list[list[str]]:
    """
    Group anagrams together.
    
    TODO: Implement this function.
    
    Args:
        strs: List of strings
        
    Returns:
        List of groups, where each group contains anagrams
        
    Expected Time Complexity: O(n * k log k) where k is max string length
    Expected Space Complexity: O(n * k)
    
    Example:
        group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        -> [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
    """
    # TODO: Implement this function
    pass


def longest_palindromic_substring(s: str) -> str:
    """
    Find the longest palindromic substring.
    
    TODO: Implement this function.
    
    Args:
        s: Input string
        
    Returns:
        Longest palindromic substring
        
    Expected Time Complexity: O(n²)
    Expected Space Complexity: O(1)
    
    Hint: Expand around center for each position (and between positions).
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
    
    # Test find_second_largest
    print("\n--- Testing find_second_largest ---")
    tests = [
        ([1, 5, 2, 5, 3], 3),
        ([1, 1, 1], None),
        ([1, 2], 1),
        ([5], None),
        ([3, 1, 4, 1, 5, 9, 2, 6], 6),
    ]
    for arr, expected in tests:
        result = find_second_largest(arr.copy())
        status = "PASS" if result == expected else "FAIL"
        if status == "FAIL":
            all_passed = False
        print(f"  find_second_largest({arr}) = {result}, expected {expected} [{status}]")
    
    # Test rotate_array
    print("\n--- Testing rotate_array ---")
    tests = [
        ([1, 2, 3, 4, 5], 2, [4, 5, 1, 2, 3]),
        ([1, 2, 3], 1, [3, 1, 2]),
        ([1, 2, 3], 3, [1, 2, 3]),
        ([1], 5, [1]),
    ]
    for arr, k, expected in tests:
        arr_copy = arr.copy()
        result = rotate_array(arr_copy, k)
        status = "PASS" if result == expected else "FAIL"
        if status == "FAIL":
            all_passed = False
        print(f"  rotate_array({arr}, {k}) = {result}, expected {expected} [{status}]")
    
    # Test merge_sorted_arrays
    print("\n--- Testing merge_sorted_arrays ---")
    tests = [
        ([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]),
        ([1, 2, 3], [], [1, 2, 3]),
        ([], [1, 2], [1, 2]),
    ]
    for arr1, arr2, expected in tests:
        result = merge_sorted_arrays(arr1, arr2)
        status = "PASS" if result == expected else "FAIL"
        if status == "FAIL":
            all_passed = False
        print(f"  merge_sorted_arrays({arr1}, {arr2}) = {result}, expected {expected} [{status}]")
    
    # Test remove_duplicates_sorted
    print("\n--- Testing remove_duplicates_sorted ---")
    tests = [
        ([1, 1, 2, 2, 3], 3, [1, 2, 3]),
        ([1, 1, 1], 1, [1]),
        ([1, 2, 3], 3, [1, 2, 3]),
    ]
    for arr, expected_len, expected_arr in tests:
        arr_copy = arr.copy()
        result_len = remove_duplicates_sorted(arr_copy)
        status = "PASS" if result_len == expected_len and arr_copy[:result_len] == expected_arr else "FAIL"
        if status == "FAIL":
            all_passed = False
        print(f"  remove_duplicates_sorted({arr}) = {result_len}, arr[:len] = {arr_copy[:result_len] if result_len else []}, expected {expected_len}, {expected_arr} [{status}]")
    
    # Test container_with_most_water
    print("\n--- Testing container_with_most_water ---")
    tests = [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
        ([4, 3, 2, 1, 4], 16),
    ]
    for heights, expected in tests:
        result = container_with_most_water(heights)
        status = "PASS" if result == expected else "FAIL"
        if status == "FAIL":
            all_passed = False
        print(f"  container_with_most_water({heights}) = {result}, expected {expected} [{status}]")
    
    # Test max_sum_subarray
    print("\n--- Testing max_sum_subarray ---")
    tests = [
        ([2, 1, 5, 1, 3, 2], 3, 9),
        ([1, 2, 3, 4, 5], 2, 9),
        ([5, -1, -2, 3, 4], 3, 5),
    ]
    for arr, k, expected in tests:
        result = max_sum_subarray(arr, k)
        status = "PASS" if result == expected else "FAIL"
        if status == "FAIL":
            all_passed = False
        print(f"  max_sum_subarray({arr}, {k}) = {result}, expected {expected} [{status}]")
    
    # Test valid_anagram
    print("\n--- Testing valid_anagram ---")
    tests = [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("", "", True),
    ]
    for s, t, expected in tests:
        result = valid_anagram(s, t)
        status = "PASS" if result == expected else "FAIL"
        if status == "FAIL":
            all_passed = False
        print(f"  valid_anagram('{s}', '{t}') = {result}, expected {expected} [{status}]")
    
    # Test longest_palindromic_substring
    print("\n--- Testing longest_palindromic_substring ---")
    tests = [
        ("babad", ["bab", "aba"]),  # Either is valid
        ("cbbd", ["bb"]),
        ("a", ["a"]),
    ]
    for s, valid_answers in tests:
        result = longest_palindromic_substring(s)
        status = "PASS" if result in valid_answers else "FAIL"
        if status == "FAIL":
            all_passed = False
        print(f"  longest_palindromic_substring('{s}') = '{result}', valid answers: {valid_answers} [{status}]")
    
    print("\n" + "="*60)
    if all_passed:
        print("ALL TESTS PASSED!")
    else:
        print("SOME TESTS FAILED - Keep working on your implementations!")
    print("="*60 + "\n")


if __name__ == "__main__":
    run_tests()
