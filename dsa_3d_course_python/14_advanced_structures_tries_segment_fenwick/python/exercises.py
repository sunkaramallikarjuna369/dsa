"""
Advanced Data Structures Exercises

Complete the functions below. Each function has a docstring
describing what it should do and example test cases.
"""

from typing import Any


# =============================================================================
# EXERCISE 1: Trie Operations
# =============================================================================

class TrieNode:
    """Trie node for exercises."""
    def __init__(self) -> None:
        self.children: dict[str, 'TrieNode'] = {}
        self.is_word_end: bool = False


class Trie:
    """
    Implement a Trie with insert, search, and startsWith.
    
    Example:
        >>> trie = Trie()
        >>> trie.insert("apple")
        >>> trie.search("apple")
        True
        >>> trie.search("app")
        False
        >>> trie.starts_with("app")
        True
    """
    
    def __init__(self) -> None:
        # TODO: Initialize root node
        pass
    
    def insert(self, word: str) -> None:
        """Insert a word into the trie."""
        # TODO: Traverse/create nodes for each character
        pass
    
    def search(self, word: str) -> bool:
        """Return True if word is in the trie."""
        # TODO: Traverse and check is_word_end
        pass
    
    def starts_with(self, prefix: str) -> bool:
        """Return True if any word starts with prefix."""
        # TODO: Traverse prefix path
        pass


def autocomplete(trie_root: TrieNode, prefix: str) -> list[str]:
    """
    Return all words in trie that start with prefix.
    
    Args:
        trie_root: Root of the trie
        prefix: Prefix to search for
    
    Returns:
        List of words starting with prefix
    
    Example:
        >>> # Trie contains: apple, app, application, apply
        >>> autocomplete(root, "app")
        ['app', 'apple', 'application', 'apply']
    """
    # TODO: Navigate to prefix node, then DFS to collect words
    pass


def word_dictionary_search(word: str, trie_root: TrieNode) -> bool:
    """
    Search with '.' as wildcard matching any character.
    
    Args:
        word: Word to search (may contain '.')
        trie_root: Root of the trie
    
    Returns:
        True if word matches any word in trie
    
    Example:
        >>> # Trie contains: bad, dad, mad
        >>> word_dictionary_search("b.d", root)
        True
        >>> word_dictionary_search("..d", root)
        True
    """
    # TODO: DFS with backtracking for '.'
    pass


# =============================================================================
# EXERCISE 2: Segment Tree
# =============================================================================

class SegmentTree:
    """
    Implement a Segment Tree for range sum queries.
    
    Example:
        >>> st = SegmentTree([1, 3, 5, 7, 9, 11])
        >>> st.range_sum(1, 4)
        24
        >>> st.update(2, 10)
        >>> st.range_sum(1, 4)
        29
    """
    
    def __init__(self, arr: list[int]) -> None:
        # TODO: Build segment tree
        pass
    
    def range_sum(self, left: int, right: int) -> int:
        """Return sum of elements in [left, right]."""
        # TODO: Query segment tree
        pass
    
    def update(self, index: int, value: int) -> None:
        """Update element at index to value."""
        # TODO: Update and propagate
        pass


def range_min_query(arr: list[int], queries: list[tuple[int, int]]) -> list[int]:
    """
    Answer range minimum queries using segment tree.
    
    Args:
        arr: Input array
        queries: List of (left, right) queries
    
    Returns:
        List of minimum values for each query
    
    Example:
        >>> range_min_query([1, 3, 2, 7, 9, 11], [(0, 2), (1, 4)])
        [1, 2]
    """
    # TODO: Build min segment tree, answer queries
    pass


def range_max_query(arr: list[int], queries: list[tuple[int, int]]) -> list[int]:
    """
    Answer range maximum queries using segment tree.
    
    Args:
        arr: Input array
        queries: List of (left, right) queries
    
    Returns:
        List of maximum values for each query
    
    Example:
        >>> range_max_query([1, 3, 2, 7, 9, 11], [(0, 2), (1, 4)])
        [3, 9]
    """
    # TODO: Build max segment tree, answer queries
    pass


# =============================================================================
# EXERCISE 3: Fenwick Tree
# =============================================================================

class FenwickTree:
    """
    Implement a Fenwick Tree (Binary Indexed Tree).
    
    Example:
        >>> ft = FenwickTree([1, 3, 5, 7, 9])
        >>> ft.prefix_sum(3)
        16
        >>> ft.update(2, 3)  # Add 3 to index 2
        >>> ft.prefix_sum(3)
        19
    """
    
    def __init__(self, arr: list[int]) -> None:
        # TODO: Build Fenwick tree
        pass
    
    def update(self, index: int, delta: int) -> None:
        """Add delta to element at index."""
        # TODO: Update using i += i & (-i)
        pass
    
    def prefix_sum(self, index: int) -> int:
        """Return sum of elements [0, index]."""
        # TODO: Query using i -= i & (-i)
        pass
    
    def range_sum(self, left: int, right: int) -> int:
        """Return sum of elements [left, right]."""
        # TODO: prefix_sum(right) - prefix_sum(left - 1)
        pass


def count_inversions(arr: list[int]) -> int:
    """
    Count inversions using Fenwick Tree.
    
    An inversion is a pair (i, j) where i < j but arr[i] > arr[j].
    
    Args:
        arr: Input array
    
    Returns:
        Number of inversions
    
    Example:
        >>> count_inversions([2, 4, 1, 3, 5])
        3
    """
    # TODO: Process from right, count smaller elements seen
    pass


def count_smaller_after(nums: list[int]) -> list[int]:
    """
    For each element, count smaller elements to its right.
    
    Args:
        nums: Input array
    
    Returns:
        List where result[i] = count of nums[j] < nums[i] for j > i
    
    Example:
        >>> count_smaller_after([5, 2, 6, 1])
        [2, 1, 1, 0]
    """
    # TODO: Process from right using Fenwick tree
    pass


# =============================================================================
# EXERCISE 4: Advanced Trie Problems
# =============================================================================

def longest_common_prefix_trie(words: list[str]) -> str:
    """
    Find longest common prefix using a Trie.
    
    Args:
        words: List of words
    
    Returns:
        Longest common prefix
    
    Example:
        >>> longest_common_prefix_trie(["flower", "flow", "flight"])
        "fl"
    """
    # TODO: Build trie, traverse while single child and not word end
    pass


def word_search_ii(board: list[list[str]], words: list[str]) -> list[str]:
    """
    Find all words from dictionary that exist in board.
    
    Args:
        board: 2D grid of characters
        words: List of words to find
    
    Returns:
        List of found words
    
    Example:
        >>> board = [['o','a','a','n'],['e','t','a','e'],['i','h','k','r'],['i','f','l','v']]
        >>> words = ["oath","pea","eat","rain"]
        >>> word_search_ii(board, words)
        ['oath', 'eat']
    """
    # TODO: Build trie from words, DFS on board
    pass


def replace_words(dictionary: list[str], sentence: str) -> str:
    """
    Replace words with their shortest root from dictionary.
    
    Args:
        dictionary: List of root words
        sentence: Sentence to process
    
    Returns:
        Sentence with words replaced by roots
    
    Example:
        >>> replace_words(["cat", "bat", "rat"], "the cattle was rattled by the battery")
        "the cat was rat by the bat"
    """
    # TODO: Build trie from dictionary, find shortest prefix for each word
    pass


# =============================================================================
# EXERCISE 5: 2D Range Queries
# =============================================================================

class NumMatrix:
    """
    2D range sum queries with updates using 2D Fenwick Tree.
    
    Example:
        >>> matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5]]
        >>> nm = NumMatrix(matrix)
        >>> nm.sum_region(1, 1, 2, 2)
        11
        >>> nm.update(1, 1, 10)
        >>> nm.sum_region(1, 1, 2, 2)
        15
    """
    
    def __init__(self, matrix: list[list[int]]) -> None:
        # TODO: Build 2D Fenwick tree
        pass
    
    def update(self, row: int, col: int, val: int) -> None:
        """Update element at (row, col) to val."""
        # TODO: Update 2D Fenwick tree
        pass
    
    def sum_region(self, row1: int, col1: int, row2: int, col2: int) -> int:
        """Return sum of rectangle from (row1, col1) to (row2, col2)."""
        # TODO: Use inclusion-exclusion
        pass


# =============================================================================
# EXERCISE 6: Segment Tree with Lazy Propagation
# =============================================================================

class LazySegmentTree:
    """
    Segment Tree with lazy propagation for range updates.
    
    Example:
        >>> lst = LazySegmentTree([1, 3, 5, 7, 9])
        >>> lst.range_sum(1, 3)
        15
        >>> lst.range_update(1, 3, 2)  # Add 2 to indices 1-3
        >>> lst.range_sum(1, 3)
        21
    """
    
    def __init__(self, arr: list[int]) -> None:
        # TODO: Build segment tree with lazy array
        pass
    
    def range_update(self, left: int, right: int, delta: int) -> None:
        """Add delta to all elements in [left, right]."""
        # TODO: Update with lazy propagation
        pass
    
    def range_sum(self, left: int, right: int) -> int:
        """Return sum of elements in [left, right]."""
        # TODO: Query with lazy propagation
        pass


# =============================================================================
# TEST CASES
# =============================================================================

def run_tests() -> None:
    """Run all test cases."""
    print("Running Advanced Data Structures Exercise Tests...")
    print("=" * 60)
    
    # Test Trie
    print("\n1. Testing Trie:")
    trie = Trie()
    if trie.insert is not None:
        trie.insert("apple")
        trie.insert("app")
        result = trie.search("apple") if trie.search else None
        expected = True
        status = "PASS" if result == expected else "FAIL"
        print(f"  trie.search('apple') = {result}, expected {expected} [{status}]")
        
        result = trie.starts_with("app") if trie.starts_with else None
        expected = True
        status = "PASS" if result == expected else "FAIL"
        print(f"  trie.starts_with('app') = {result}, expected {expected} [{status}]")
    else:
        print("  Trie not implemented")
    
    # Test SegmentTree
    print("\n2. Testing SegmentTree:")
    st = SegmentTree([1, 3, 5, 7, 9, 11])
    if st.range_sum is not None:
        result = st.range_sum(1, 4)
        expected = 24
        status = "PASS" if result == expected else "FAIL"
        print(f"  range_sum(1, 4) = {result}, expected {expected} [{status}]")
    else:
        print("  SegmentTree not implemented")
    
    # Test FenwickTree
    print("\n3. Testing FenwickTree:")
    ft = FenwickTree([1, 3, 5, 7, 9])
    if ft.prefix_sum is not None:
        result = ft.prefix_sum(3)
        expected = 16
        status = "PASS" if result == expected else "FAIL"
        print(f"  prefix_sum(3) = {result}, expected {expected} [{status}]")
    else:
        print("  FenwickTree not implemented")
    
    # Test count_inversions
    print("\n4. Testing count_inversions:")
    result = count_inversions([2, 4, 1, 3, 5])
    expected = 3
    status = "PASS" if result == expected else "FAIL"
    print(f"  count_inversions([2,4,1,3,5]) = {result}, expected {expected} [{status}]")
    
    # Test longest_common_prefix_trie
    print("\n5. Testing longest_common_prefix_trie:")
    result = longest_common_prefix_trie(["flower", "flow", "flight"])
    expected = "fl"
    status = "PASS" if result == expected else "FAIL"
    print(f"  longest_common_prefix_trie(...) = '{result}', expected '{expected}' [{status}]")
    
    # Test replace_words
    print("\n6. Testing replace_words:")
    result = replace_words(["cat", "bat", "rat"], "the cattle was rattled by the battery")
    expected = "the cat was rat by the bat"
    status = "PASS" if result == expected else "FAIL"
    print(f"  replace_words(...) = '{result}'")
    print(f"  expected: '{expected}' [{status}]")
    
    print("\n" + "=" * 60)
    print("Tests complete! Implement the functions to make them pass.")


if __name__ == "__main__":
    run_tests()
