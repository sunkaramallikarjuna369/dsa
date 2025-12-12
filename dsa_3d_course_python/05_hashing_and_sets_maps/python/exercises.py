"""
Exercises: Hashing and Sets/Maps

Complete the following exercises to practice hash table operations.
Each function has a docstring explaining what to implement.

Run this file to test your implementations against the provided test cases.
"""

from typing import Any


# =============================================================================
# EXERCISE 1: Hash Table Basics
# =============================================================================

def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Find two numbers that add up to target and return their indices.
    
    TODO: Implement this function using a hash map.
    
    Args:
        nums: List of integers
        target: Target sum
        
    Returns:
        List of two indices whose values sum to target
        
    Expected Time Complexity: O(n)
    Expected Space Complexity: O(n)
    
    Example:
        two_sum([2, 7, 11, 15], 9) -> [0, 1]  # nums[0] + nums[1] = 2 + 7 = 9
    
    Hint: For each number, check if (target - number) exists in the hash map.
    """
    # TODO: Implement this function
    pass


def first_non_repeating_char(s: str) -> str:
    """
    Find the first non-repeating character in a string.
    
    TODO: Implement this function using a hash map.
    
    Args:
        s: Input string
        
    Returns:
        First character that appears only once, or "" if none
        
    Expected Time Complexity: O(n)
    Expected Space Complexity: O(1) - at most 26 letters
    
    Example:
        first_non_repeating_char("leetcode") -> "l"
        first_non_repeating_char("aabb") -> ""
    """
    # TODO: Implement this function
    pass


def contains_duplicate(nums: list[int]) -> bool:
    """
    Check if any value appears at least twice in the array.
    
    TODO: Implement this function using a set.
    
    Args:
        nums: List of integers
        
    Returns:
        True if any duplicate exists, False otherwise
        
    Expected Time Complexity: O(n)
    Expected Space Complexity: O(n)
    
    Example:
        contains_duplicate([1, 2, 3, 1]) -> True
        contains_duplicate([1, 2, 3, 4]) -> False
    """
    # TODO: Implement this function
    pass


# =============================================================================
# EXERCISE 2: Frequency Counting
# =============================================================================

def frequency_count(arr: list[Any]) -> dict[Any, int]:
    """
    Count the frequency of each element in the array.
    
    TODO: Implement this function using a hash map.
    
    Args:
        arr: List of elements
        
    Returns:
        Dictionary mapping each element to its count
        
    Expected Time Complexity: O(n)
    Expected Space Complexity: O(n)
    
    Example:
        frequency_count([1, 2, 2, 3, 3, 3]) -> {1: 1, 2: 2, 3: 3}
    """
    # TODO: Implement this function
    pass


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    """
    Find the k most frequent elements.
    
    TODO: Implement this function.
    
    Args:
        nums: List of integers
        k: Number of top frequent elements to return
        
    Returns:
        List of k most frequent elements (order doesn't matter)
        
    Expected Time Complexity: O(n log k) or O(n) with bucket sort
    Expected Space Complexity: O(n)
    
    Example:
        top_k_frequent([1, 1, 1, 2, 2, 3], 2) -> [1, 2]
    """
    # TODO: Implement this function
    pass


def is_anagram(s: str, t: str) -> bool:
    """
    Check if t is an anagram of s.
    
    TODO: Implement this function using a hash map.
    
    Args:
        s: First string
        t: Second string
        
    Returns:
        True if t is an anagram of s
        
    Expected Time Complexity: O(n)
    Expected Space Complexity: O(1) - at most 26 letters
    
    Example:
        is_anagram("anagram", "nagaram") -> True
        is_anagram("rat", "car") -> False
    """
    # TODO: Implement this function
    pass


# =============================================================================
# EXERCISE 3: Set Operations
# =============================================================================

def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    """
    Find the intersection of two arrays (unique elements in both).
    
    TODO: Implement this function using sets.
    
    Args:
        nums1: First array
        nums2: Second array
        
    Returns:
        List of unique elements present in both arrays
        
    Expected Time Complexity: O(n + m)
    Expected Space Complexity: O(min(n, m))
    
    Example:
        intersection([1, 2, 2, 1], [2, 2]) -> [2]
        intersection([4, 9, 5], [9, 4, 9, 8, 4]) -> [4, 9] or [9, 4]
    """
    # TODO: Implement this function
    pass


def union(nums1: list[int], nums2: list[int]) -> list[int]:
    """
    Find the union of two arrays (all unique elements from both).
    
    TODO: Implement this function using sets.
    
    Args:
        nums1: First array
        nums2: Second array
        
    Returns:
        List of all unique elements from both arrays
        
    Expected Time Complexity: O(n + m)
    Expected Space Complexity: O(n + m)
    
    Example:
        union([1, 2, 3], [2, 3, 4]) -> [1, 2, 3, 4]
    """
    # TODO: Implement this function
    pass


def difference(nums1: list[int], nums2: list[int]) -> list[int]:
    """
    Find elements in nums1 that are not in nums2.
    
    TODO: Implement this function using sets.
    
    Args:
        nums1: First array
        nums2: Second array
        
    Returns:
        List of unique elements in nums1 but not in nums2
        
    Expected Time Complexity: O(n + m)
    Expected Space Complexity: O(n)
    
    Example:
        difference([1, 2, 3, 4], [2, 4]) -> [1, 3]
    """
    # TODO: Implement this function
    pass


# =============================================================================
# EXERCISE 4: Advanced Hash Map Problems
# =============================================================================

def group_anagrams(strs: list[str]) -> list[list[str]]:
    """
    Group anagrams together.
    
    TODO: Implement this function using a hash map.
    
    Args:
        strs: List of strings
        
    Returns:
        List of groups, where each group contains anagrams
        
    Expected Time Complexity: O(n * k log k) where k is max string length
    Expected Space Complexity: O(n * k)
    
    Example:
        group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        -> [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
    
    Hint: Use sorted string as the key for grouping.
    """
    # TODO: Implement this function
    pass


def longest_consecutive_sequence(nums: list[int]) -> int:
    """
    Find the length of the longest consecutive elements sequence.
    
    TODO: Implement this function using a set.
    
    Args:
        nums: Unsorted array of integers
        
    Returns:
        Length of longest consecutive sequence
        
    Expected Time Complexity: O(n)
    Expected Space Complexity: O(n)
    
    Example:
        longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) -> 4
        # The longest consecutive sequence is [1, 2, 3, 4]
    
    Hint: Only start counting from numbers that are the start of a sequence
    (i.e., num-1 is not in the set).
    """
    # TODO: Implement this function
    pass


def subarray_sum_equals_k(nums: list[int], k: int) -> int:
    """
    Count subarrays with sum equal to k.
    
    TODO: Implement this function using a hash map with prefix sums.
    
    Args:
        nums: Array of integers
        k: Target sum
        
    Returns:
        Number of subarrays with sum equal to k
        
    Expected Time Complexity: O(n)
    Expected Space Complexity: O(n)
    
    Example:
        subarray_sum_equals_k([1, 1, 1], 2) -> 2
        # Subarrays: [1, 1] at index 0-1 and [1, 1] at index 1-2
    
    Hint: Use prefix sum. If prefix_sum[j] - prefix_sum[i] = k,
    then subarray from i+1 to j has sum k.
    """
    # TODO: Implement this function
    pass


def implement_lru_cache(capacity: int) -> type:
    """
    Implement an LRU (Least Recently Used) Cache.
    
    TODO: Implement the LRUCache class.
    
    Args:
        capacity: Maximum number of items in cache
        
    Returns:
        The LRUCache class
        
    The class should support:
        - get(key): Return value if key exists, else -1
        - put(key, value): Insert or update key-value pair
        - When capacity is exceeded, evict least recently used item
    
    Expected Time Complexity: O(1) for both get and put
    
    Hint: Use a hash map combined with a doubly linked list,
    or use Python's OrderedDict.
    """
    class LRUCache:
        def __init__(self, cap: int) -> None:
            # TODO: Initialize data structures
            pass
        
        def get(self, key: int) -> int:
            # TODO: Implement get
            pass
        
        def put(self, key: int, value: int) -> None:
            # TODO: Implement put
            pass
    
    return LRUCache


# =============================================================================
# TEST CASES
# =============================================================================

def run_tests() -> None:
    """Run all test cases for the exercises."""
    print("\n" + "="*60)
    print("RUNNING EXERCISE TESTS")
    print("="*60)
    
    all_passed = True
    
    # Test two_sum
    print("\n--- Testing two_sum ---")
    tests = [
        ([2, 7, 11, 15], 9, {0, 1}),
        ([3, 2, 4], 6, {1, 2}),
        ([3, 3], 6, {0, 1}),
    ]
    for nums, target, expected in tests:
        result = two_sum(nums, target)
        result_set = set(result) if result else set()
        status = "PASS" if result_set == expected else "FAIL"
        if status == "FAIL":
            all_passed = False
        print(f"  two_sum({nums}, {target}) = {result}, expected indices {expected} [{status}]")
    
    # Test first_non_repeating_char
    print("\n--- Testing first_non_repeating_char ---")
    tests = [
        ("leetcode", "l"),
        ("loveleetcode", "v"),
        ("aabb", ""),
    ]
    for s, expected in tests:
        result = first_non_repeating_char(s)
        status = "PASS" if result == expected else "FAIL"
        if status == "FAIL":
            all_passed = False
        print(f"  first_non_repeating_char('{s}') = '{result}', expected '{expected}' [{status}]")
    
    # Test contains_duplicate
    print("\n--- Testing contains_duplicate ---")
    tests = [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
    ]
    for nums, expected in tests:
        result = contains_duplicate(nums)
        status = "PASS" if result == expected else "FAIL"
        if status == "FAIL":
            all_passed = False
        print(f"  contains_duplicate({nums}) = {result}, expected {expected} [{status}]")
    
    # Test frequency_count
    print("\n--- Testing frequency_count ---")
    tests = [
        ([1, 2, 2, 3, 3, 3], {1: 1, 2: 2, 3: 3}),
        (['a', 'b', 'a'], {'a': 2, 'b': 1}),
    ]
    for arr, expected in tests:
        result = frequency_count(arr)
        status = "PASS" if result == expected else "FAIL"
        if status == "FAIL":
            all_passed = False
        print(f"  frequency_count({arr}) = {result}, expected {expected} [{status}]")
    
    # Test is_anagram
    print("\n--- Testing is_anagram ---")
    tests = [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("listen", "silent", True),
    ]
    for s, t, expected in tests:
        result = is_anagram(s, t)
        status = "PASS" if result == expected else "FAIL"
        if status == "FAIL":
            all_passed = False
        print(f"  is_anagram('{s}', '{t}') = {result}, expected {expected} [{status}]")
    
    # Test intersection
    print("\n--- Testing intersection ---")
    tests = [
        ([1, 2, 2, 1], [2, 2], {2}),
        ([4, 9, 5], [9, 4, 9, 8, 4], {4, 9}),
    ]
    for nums1, nums2, expected in tests:
        result = intersection(nums1, nums2)
        result_set = set(result) if result else set()
        status = "PASS" if result_set == expected else "FAIL"
        if status == "FAIL":
            all_passed = False
        print(f"  intersection({nums1}, {nums2}) = {result}, expected {expected} [{status}]")
    
    # Test group_anagrams
    print("\n--- Testing group_anagrams ---")
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = group_anagrams(strs)
    if result:
        result_sorted = [sorted(group) for group in result]
        result_sorted.sort()
        expected_sorted = [['ate', 'eat', 'tea'], ['bat'], ['nat', 'tan']]
        status = "PASS" if result_sorted == expected_sorted else "FAIL"
    else:
        status = "FAIL"
    if status == "FAIL":
        all_passed = False
    print(f"  group_anagrams({strs}) [{status}]")
    
    # Test longest_consecutive_sequence
    print("\n--- Testing longest_consecutive_sequence ---")
    tests = [
        ([100, 4, 200, 1, 3, 2], 4),
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
        ([], 0),
    ]
    for nums, expected in tests:
        result = longest_consecutive_sequence(nums)
        status = "PASS" if result == expected else "FAIL"
        if status == "FAIL":
            all_passed = False
        print(f"  longest_consecutive_sequence({nums}) = {result}, expected {expected} [{status}]")
    
    # Test subarray_sum_equals_k
    print("\n--- Testing subarray_sum_equals_k ---")
    tests = [
        ([1, 1, 1], 2, 2),
        ([1, 2, 3], 3, 2),
    ]
    for nums, k, expected in tests:
        result = subarray_sum_equals_k(nums, k)
        status = "PASS" if result == expected else "FAIL"
        if status == "FAIL":
            all_passed = False
        print(f"  subarray_sum_equals_k({nums}, {k}) = {result}, expected {expected} [{status}]")
    
    # Test LRU Cache
    print("\n--- Testing LRUCache ---")
    LRUCache = implement_lru_cache(2)
    cache = LRUCache(2)
    try:
        cache.put(1, 1)
        cache.put(2, 2)
        r1 = cache.get(1)  # returns 1
        cache.put(3, 3)    # evicts key 2
        r2 = cache.get(2)  # returns -1 (not found)
        cache.put(4, 4)    # evicts key 1
        r3 = cache.get(1)  # returns -1 (not found)
        r4 = cache.get(3)  # returns 3
        r5 = cache.get(4)  # returns 4
        
        status = "PASS" if r1 == 1 and r2 == -1 and r3 == -1 and r4 == 3 and r5 == 4 else "FAIL"
        if status == "FAIL":
            all_passed = False
        print(f"  LRUCache operations: get(1)={r1}, get(2)={r2}, get(1)={r3}, get(3)={r4}, get(4)={r5} [{status}]")
    except Exception as e:
        print(f"  LRUCache operations: ERROR - {e} [FAIL]")
        all_passed = False
    
    print("\n" + "="*60)
    if all_passed:
        print("ALL TESTS PASSED!")
    else:
        print("SOME TESTS FAILED - Keep working on your implementations!")
    print("="*60 + "\n")


if __name__ == "__main__":
    run_tests()
