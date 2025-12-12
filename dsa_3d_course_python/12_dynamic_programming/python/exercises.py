"""
Dynamic Programming Exercises

Complete the functions below. Each function has a docstring
describing what it should do and example test cases.
"""

from typing import Any


# =============================================================================
# EXERCISE 1: Fibonacci Variations
# =============================================================================

def fibonacci_memo(n: int) -> int:
    """
    Compute nth Fibonacci number using memoization.
    
    Args:
        n: Index (0-indexed)
    
    Returns:
        nth Fibonacci number
    
    Example:
        >>> fibonacci_memo(10)
        55
    """
    # TODO: Implement with memoization (top-down)
    pass


def fibonacci_tab(n: int) -> int:
    """
    Compute nth Fibonacci number using tabulation.
    
    Args:
        n: Index (0-indexed)
    
    Returns:
        nth Fibonacci number
    
    Example:
        >>> fibonacci_tab(10)
        55
    """
    # TODO: Implement with tabulation (bottom-up)
    pass


def climbing_stairs(n: int) -> int:
    """
    Count distinct ways to climb n stairs (1 or 2 steps).
    
    Args:
        n: Number of stairs
    
    Returns:
        Number of distinct ways
    
    Example:
        >>> climbing_stairs(5)
        8
    """
    # TODO: This is Fibonacci in disguise
    pass


# =============================================================================
# EXERCISE 2: Knapsack Problems
# =============================================================================

def knapsack_01(weights: list[int], values: list[int], capacity: int) -> int:
    """
    Solve 0/1 knapsack problem.
    
    Args:
        weights: Item weights
        values: Item values
        capacity: Maximum capacity
    
    Returns:
        Maximum value achievable
    
    Example:
        >>> knapsack_01([1, 3, 4, 5], [1, 4, 5, 7], 7)
        9
    """
    # TODO: 2D DP table
    pass


def unbounded_knapsack(weights: list[int], values: list[int], capacity: int) -> int:
    """
    Solve unbounded knapsack (items can be used multiple times).
    
    Args:
        weights: Item weights
        values: Item values
        capacity: Maximum capacity
    
    Returns:
        Maximum value achievable
    
    Example:
        >>> unbounded_knapsack([1, 3, 4], [10, 40, 50], 8)
        110
    """
    # TODO: 1D DP, iterate through capacities
    pass


def subset_sum(nums: list[int], target: int) -> bool:
    """
    Check if subset with given sum exists.
    
    Args:
        nums: List of positive integers
        target: Target sum
    
    Returns:
        True if subset exists
    
    Example:
        >>> subset_sum([3, 34, 4, 12, 5, 2], 9)
        True
    """
    # TODO: Similar to knapsack
    pass


# =============================================================================
# EXERCISE 3: String DP
# =============================================================================

def longest_common_subsequence(s1: str, s2: str) -> int:
    """
    Find length of longest common subsequence.
    
    Args:
        s1: First string
        s2: Second string
    
    Returns:
        LCS length
    
    Example:
        >>> longest_common_subsequence("ABCDGH", "AEDFHR")
        3
    """
    # TODO: 2D DP table
    pass


def edit_distance(s1: str, s2: str) -> int:
    """
    Find minimum edit distance (insert, delete, replace).
    
    Args:
        s1: Source string
        s2: Target string
    
    Returns:
        Minimum operations
    
    Example:
        >>> edit_distance("horse", "ros")
        3
    """
    # TODO: 2D DP with three operations
    pass


def longest_palindromic_subsequence(s: str) -> int:
    """
    Find length of longest palindromic subsequence.
    
    Args:
        s: Input string
    
    Returns:
        Length of longest palindromic subsequence
    
    Example:
        >>> longest_palindromic_subsequence("bbbab")
        4
    """
    # TODO: LCS of s and reverse(s), or direct DP
    pass


# =============================================================================
# EXERCISE 4: Coin Change Variations
# =============================================================================

def coin_change_min(coins: list[int], amount: int) -> int:
    """
    Find minimum coins to make amount.
    
    Args:
        coins: Coin denominations
        amount: Target amount
    
    Returns:
        Minimum coins, or -1 if impossible
    
    Example:
        >>> coin_change_min([1, 3, 4], 6)
        2
    """
    # TODO: 1D DP
    pass


def coin_change_ways(coins: list[int], amount: int) -> int:
    """
    Count number of ways to make amount.
    
    Args:
        coins: Coin denominations
        amount: Target amount
    
    Returns:
        Number of combinations
    
    Example:
        >>> coin_change_ways([1, 2, 5], 5)
        4
    """
    # TODO: 1D DP, order matters for combinations vs permutations
    pass


# =============================================================================
# EXERCISE 5: Sequence DP
# =============================================================================

def longest_increasing_subsequence(nums: list[int]) -> int:
    """
    Find length of longest increasing subsequence.
    
    Args:
        nums: List of integers
    
    Returns:
        LIS length
    
    Example:
        >>> longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18])
        4
    """
    # TODO: O(n²) DP or O(n log n) with binary search
    pass


def max_subarray_sum(nums: list[int]) -> int:
    """
    Find maximum sum of contiguous subarray (Kadane's algorithm).
    
    Args:
        nums: List of integers
    
    Returns:
        Maximum subarray sum
    
    Example:
        >>> max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4])
        6
    """
    # TODO: Track current and global max
    pass


def max_product_subarray(nums: list[int]) -> int:
    """
    Find maximum product of contiguous subarray.
    
    Args:
        nums: List of integers
    
    Returns:
        Maximum product
    
    Example:
        >>> max_product_subarray([2, 3, -2, 4])
        6
    """
    # TODO: Track both max and min (negatives can flip)
    pass


# =============================================================================
# EXERCISE 6: Grid DP
# =============================================================================

def unique_paths(m: int, n: int) -> int:
    """
    Count unique paths in m x n grid (only right and down moves).
    
    Args:
        m: Number of rows
        n: Number of columns
    
    Returns:
        Number of unique paths
    
    Example:
        >>> unique_paths(3, 7)
        28
    """
    # TODO: 2D DP or combinatorics
    pass


def min_path_sum(grid: list[list[int]]) -> int:
    """
    Find minimum path sum from top-left to bottom-right.
    
    Args:
        grid: 2D grid of non-negative integers
    
    Returns:
        Minimum path sum
    
    Example:
        >>> min_path_sum([[1, 3, 1], [1, 5, 1], [4, 2, 1]])
        7
    """
    # TODO: 2D DP
    pass


def unique_paths_with_obstacles(grid: list[list[int]]) -> int:
    """
    Count unique paths with obstacles (1 = obstacle).
    
    Args:
        grid: 2D grid with obstacles
    
    Returns:
        Number of unique paths
    
    Example:
        >>> unique_paths_with_obstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
        2
    """
    # TODO: 2D DP, handle obstacles
    pass


# =============================================================================
# EXERCISE 7: Advanced DP
# =============================================================================

def word_break(s: str, word_dict: list[str]) -> bool:
    """
    Check if string can be segmented into dictionary words.
    
    Args:
        s: Input string
        word_dict: List of valid words
    
    Returns:
        True if segmentation possible
    
    Example:
        >>> word_break("leetcode", ["leet", "code"])
        True
    """
    # TODO: 1D DP with word matching
    pass


def decode_ways(s: str) -> int:
    """
    Count ways to decode string (A=1, B=2, ..., Z=26).
    
    Args:
        s: String of digits
    
    Returns:
        Number of decodings
    
    Example:
        >>> decode_ways("226")
        3
    """
    # TODO: 1D DP, handle single and double digits
    pass


def house_robber(nums: list[int]) -> int:
    """
    Maximum money without robbing adjacent houses.
    
    Args:
        nums: Money in each house
    
    Returns:
        Maximum money
    
    Example:
        >>> house_robber([1, 2, 3, 1])
        4
    """
    # TODO: dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    pass


# =============================================================================
# TEST CASES
# =============================================================================

def run_tests() -> None:
    """Run all test cases."""
    print("Running Dynamic Programming Exercise Tests...")
    print("=" * 60)
    
    # Test fibonacci
    print("\n1. Testing fibonacci_memo:")
    result = fibonacci_memo(10)
    expected = 55
    status = "PASS" if result == expected else "FAIL"
    print(f"  fibonacci_memo(10) = {result}, expected {expected} [{status}]")
    
    # Test climbing_stairs
    print("\n2. Testing climbing_stairs:")
    result = climbing_stairs(5)
    expected = 8
    status = "PASS" if result == expected else "FAIL"
    print(f"  climbing_stairs(5) = {result}, expected {expected} [{status}]")
    
    # Test knapsack_01
    print("\n3. Testing knapsack_01:")
    result = knapsack_01([1, 3, 4, 5], [1, 4, 5, 7], 7)
    expected = 9
    status = "PASS" if result == expected else "FAIL"
    print(f"  knapsack_01(...) = {result}, expected {expected} [{status}]")
    
    # Test longest_common_subsequence
    print("\n4. Testing longest_common_subsequence:")
    result = longest_common_subsequence("ABCDGH", "AEDFHR")
    expected = 3
    status = "PASS" if result == expected else "FAIL"
    print(f"  lcs('ABCDGH', 'AEDFHR') = {result}, expected {expected} [{status}]")
    
    # Test edit_distance
    print("\n5. Testing edit_distance:")
    result = edit_distance("horse", "ros")
    expected = 3
    status = "PASS" if result == expected else "FAIL"
    print(f"  edit_distance('horse', 'ros') = {result}, expected {expected} [{status}]")
    
    # Test coin_change_min
    print("\n6. Testing coin_change_min:")
    result = coin_change_min([1, 3, 4], 6)
    expected = 2
    status = "PASS" if result == expected else "FAIL"
    print(f"  coin_change_min([1,3,4], 6) = {result}, expected {expected} [{status}]")
    
    # Test longest_increasing_subsequence
    print("\n7. Testing longest_increasing_subsequence:")
    result = longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18])
    expected = 4
    status = "PASS" if result == expected else "FAIL"
    print(f"  lis([10,9,2,5,3,7,101,18]) = {result}, expected {expected} [{status}]")
    
    # Test max_subarray_sum
    print("\n8. Testing max_subarray_sum:")
    result = max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    expected = 6
    status = "PASS" if result == expected else "FAIL"
    print(f"  max_subarray_sum(...) = {result}, expected {expected} [{status}]")
    
    # Test unique_paths
    print("\n9. Testing unique_paths:")
    result = unique_paths(3, 7)
    expected = 28
    status = "PASS" if result == expected else "FAIL"
    print(f"  unique_paths(3, 7) = {result}, expected {expected} [{status}]")
    
    # Test house_robber
    print("\n10. Testing house_robber:")
    result = house_robber([1, 2, 3, 1])
    expected = 4
    status = "PASS" if result == expected else "FAIL"
    print(f"  house_robber([1,2,3,1]) = {result}, expected {expected} [{status}]")
    
    print("\n" + "=" * 60)
    print("Tests complete! Implement the functions to make them pass.")


if __name__ == "__main__":
    run_tests()
