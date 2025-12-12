"""
Graph and Traversal Exercises

Complete the functions below. Each function has a docstring
describing what it should do and example test cases.
"""

from typing import Any
from collections import deque


# =============================================================================
# EXERCISE 1: Graph Traversals
# =============================================================================

def bfs_level_order(graph: dict[int, list[int]], start: int) -> list[list[int]]:
    """
    Return BFS traversal as a list of levels.
    
    Each inner list contains all nodes at that distance from start.
    
    Args:
        graph: Adjacency list representation
        start: Starting node
    
    Returns:
        List of levels, each level is a list of nodes
    
    Example:
        >>> graph = {0: [1, 2], 1: [3], 2: [3], 3: []}
        >>> bfs_level_order(graph, 0)
        [[0], [1, 2], [3]]
    """
    # TODO: Implement BFS that groups nodes by level
    pass


def dfs_preorder(graph: dict[int, list[int]], start: int) -> list[int]:
    """
    Return DFS preorder traversal (visit node before children).
    
    Args:
        graph: Adjacency list representation
        start: Starting node
    
    Returns:
        List of nodes in preorder
    
    Example:
        >>> graph = {0: [1, 2], 1: [3], 2: [], 3: []}
        >>> dfs_preorder(graph, 0)
        [0, 1, 3, 2]
    """
    # TODO: Implement recursive DFS preorder
    pass


def dfs_postorder(graph: dict[int, list[int]], start: int) -> list[int]:
    """
    Return DFS postorder traversal (visit node after children).
    
    Args:
        graph: Adjacency list representation
        start: Starting node
    
    Returns:
        List of nodes in postorder
    
    Example:
        >>> graph = {0: [1, 2], 1: [3], 2: [], 3: []}
        >>> dfs_postorder(graph, 0)
        [3, 1, 2, 0]
    """
    # TODO: Implement recursive DFS postorder
    pass


# =============================================================================
# EXERCISE 2: Path Finding
# =============================================================================

def has_path(graph: dict[int, list[int]], start: int, end: int) -> bool:
    """
    Check if there's a path from start to end.
    
    Args:
        graph: Adjacency list representation
        start: Starting node
        end: Target node
    
    Returns:
        True if path exists, False otherwise
    
    Example:
        >>> graph = {0: [1, 2], 1: [3], 2: [], 3: [4], 4: []}
        >>> has_path(graph, 0, 4)
        True
        >>> has_path(graph, 2, 4)
        False
    """
    # TODO: Use BFS or DFS to check path existence
    pass


def shortest_path_length(graph: dict[int, list[int]], start: int, end: int) -> int:
    """
    Find the length of shortest path from start to end.
    
    Args:
        graph: Adjacency list representation (unweighted)
        start: Starting node
        end: Target node
    
    Returns:
        Length of shortest path, or -1 if no path exists
    
    Example:
        >>> graph = {0: [1, 2], 1: [3], 2: [3], 3: []}
        >>> shortest_path_length(graph, 0, 3)
        2
    """
    # TODO: Use BFS to find shortest path length
    pass


def all_paths(graph: dict[int, list[int]], start: int, end: int) -> list[list[int]]:
    """
    Find all paths from start to end (no cycles).
    
    Args:
        graph: Adjacency list representation
        start: Starting node
        end: Target node
    
    Returns:
        List of all paths, each path is a list of nodes
    
    Example:
        >>> graph = {0: [1, 2], 1: [3], 2: [3], 3: []}
        >>> sorted(all_paths(graph, 0, 3))
        [[0, 1, 3], [0, 2, 3]]
    """
    # TODO: Use DFS backtracking to find all paths
    pass


# =============================================================================
# EXERCISE 3: Connected Components
# =============================================================================

def count_connected_components(n: int, edges: list[tuple[int, int]]) -> int:
    """
    Count the number of connected components in an undirected graph.
    
    Args:
        n: Number of nodes (0 to n-1)
        edges: List of edges as (u, v) tuples
    
    Returns:
        Number of connected components
    
    Example:
        >>> count_connected_components(5, [(0, 1), (1, 2), (3, 4)])
        2
        >>> count_connected_components(4, [(0, 1), (2, 3)])
        2
    """
    # TODO: Build graph and count components using BFS/DFS
    pass


def largest_component_size(n: int, edges: list[tuple[int, int]]) -> int:
    """
    Find the size of the largest connected component.
    
    Args:
        n: Number of nodes (0 to n-1)
        edges: List of edges as (u, v) tuples
    
    Returns:
        Size of largest component
    
    Example:
        >>> largest_component_size(6, [(0, 1), (1, 2), (3, 4)])
        3
    """
    # TODO: Find all components and return max size
    pass


def number_of_islands(grid: list[list[str]]) -> int:
    """
    Count the number of islands in a 2D grid.
    
    '1' represents land, '0' represents water.
    An island is surrounded by water and formed by connecting
    adjacent lands horizontally or vertically.
    
    Args:
        grid: 2D grid of '1's and '0's
    
    Returns:
        Number of islands
    
    Example:
        >>> grid = [
        ...     ['1', '1', '0', '0', '0'],
        ...     ['1', '1', '0', '0', '0'],
        ...     ['0', '0', '1', '0', '0'],
        ...     ['0', '0', '0', '1', '1']
        ... ]
        >>> number_of_islands(grid)
        3
    """
    # TODO: Use BFS/DFS to explore each island
    pass


# =============================================================================
# EXERCISE 4: Cycle Detection
# =============================================================================

def has_cycle_undirected(n: int, edges: list[tuple[int, int]]) -> bool:
    """
    Check if an undirected graph has a cycle.
    
    Args:
        n: Number of nodes
        edges: List of edges
    
    Returns:
        True if cycle exists
    
    Example:
        >>> has_cycle_undirected(3, [(0, 1), (1, 2), (2, 0)])
        True
        >>> has_cycle_undirected(3, [(0, 1), (1, 2)])
        False
    """
    # TODO: Use DFS with parent tracking
    pass


def has_cycle_directed(n: int, edges: list[tuple[int, int]]) -> bool:
    """
    Check if a directed graph has a cycle.
    
    Args:
        n: Number of nodes
        edges: List of directed edges (from, to)
    
    Returns:
        True if cycle exists
    
    Example:
        >>> has_cycle_directed(4, [(0, 1), (1, 2), (2, 3), (3, 1)])
        True
        >>> has_cycle_directed(3, [(0, 1), (1, 2)])
        False
    """
    # TODO: Use DFS with coloring (white, gray, black)
    pass


def can_finish_courses(num_courses: int, prerequisites: list[list[int]]) -> bool:
    """
    Determine if you can finish all courses given prerequisites.
    
    prerequisites[i] = [a, b] means you must take course b before course a.
    
    Args:
        num_courses: Total number of courses
        prerequisites: List of [course, prerequisite] pairs
    
    Returns:
        True if all courses can be finished (no cycle in dependencies)
    
    Example:
        >>> can_finish_courses(2, [[1, 0]])
        True
        >>> can_finish_courses(2, [[1, 0], [0, 1]])
        False
    """
    # TODO: Check for cycle in course dependency graph
    pass


# =============================================================================
# EXERCISE 5: Topological Sort
# =============================================================================

def topological_sort(n: int, edges: list[tuple[int, int]]) -> list[int]:
    """
    Return a topological ordering of nodes in a DAG.
    
    Args:
        n: Number of nodes
        edges: List of directed edges (from, to)
    
    Returns:
        List of nodes in topological order, or empty list if cycle exists
    
    Example:
        >>> topological_sort(4, [(0, 1), (0, 2), (1, 3), (2, 3)])
        [0, 1, 2, 3]  # or [0, 2, 1, 3]
    """
    # TODO: Use DFS or Kahn's algorithm
    pass


def course_order(num_courses: int, prerequisites: list[list[int]]) -> list[int]:
    """
    Find an order to take all courses given prerequisites.
    
    Args:
        num_courses: Total number of courses
        prerequisites: List of [course, prerequisite] pairs
    
    Returns:
        Valid course order, or empty list if impossible
    
    Example:
        >>> course_order(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
        [0, 1, 2, 3]  # or [0, 2, 1, 3]
    """
    # TODO: Topological sort of course dependency graph
    pass


# =============================================================================
# EXERCISE 6: Advanced Graph Problems
# =============================================================================

def clone_graph(node: dict | None) -> dict | None:
    """
    Deep clone a graph given a reference to a node.
    
    Each node is represented as {'val': int, 'neighbors': [node, ...]}.
    
    Args:
        node: Reference to a node in the graph
    
    Returns:
        Reference to the same node in the cloned graph
    
    Example:
        >>> node1 = {'val': 1, 'neighbors': []}
        >>> node2 = {'val': 2, 'neighbors': []}
        >>> node1['neighbors'] = [node2]
        >>> node2['neighbors'] = [node1]
        >>> cloned = clone_graph(node1)
        >>> cloned['val']
        1
        >>> cloned is not node1
        True
    """
    # TODO: Use BFS/DFS with a mapping from original to clone
    pass


def is_bipartite(n: int, edges: list[tuple[int, int]]) -> bool:
    """
    Check if a graph is bipartite (can be 2-colored).
    
    A graph is bipartite if nodes can be divided into two sets
    such that no two nodes in the same set are adjacent.
    
    Args:
        n: Number of nodes
        edges: List of edges
    
    Returns:
        True if graph is bipartite
    
    Example:
        >>> is_bipartite(4, [(0, 1), (1, 2), (2, 3), (3, 0)])
        True
        >>> is_bipartite(3, [(0, 1), (1, 2), (2, 0)])
        False
    """
    # TODO: Use BFS/DFS with 2-coloring
    pass


# =============================================================================
# TEST CASES
# =============================================================================

def run_tests() -> None:
    """Run all test cases."""
    print("Running Graph and Traversal Exercise Tests...")
    print("=" * 60)
    
    # Test bfs_level_order
    print("\n1. Testing bfs_level_order:")
    graph1 = {0: [1, 2], 1: [3], 2: [3], 3: []}
    result = bfs_level_order(graph1, 0)
    expected = [[0], [1, 2], [3]]
    status = "PASS" if result == expected else "FAIL"
    print(f"  bfs_level_order({graph1}, 0) = {result}, expected {expected} [{status}]")
    
    # Test has_path
    print("\n2. Testing has_path:")
    graph2 = {0: [1, 2], 1: [3], 2: [], 3: [4], 4: []}
    test_cases = [
        ((graph2, 0, 4), True),
        ((graph2, 2, 4), False),
        ((graph2, 0, 0), True),
    ]
    for (g, s, e), expected in test_cases:
        result = has_path(g, s, e)
        status = "PASS" if result == expected else "FAIL"
        print(f"  has_path(graph, {s}, {e}) = {result}, expected {expected} [{status}]")
    
    # Test shortest_path_length
    print("\n3. Testing shortest_path_length:")
    graph3 = {0: [1, 2], 1: [3], 2: [3], 3: []}
    test_cases = [
        ((graph3, 0, 3), 2),
        ((graph3, 0, 0), 0),
    ]
    for (g, s, e), expected in test_cases:
        result = shortest_path_length(g, s, e)
        status = "PASS" if result == expected else "FAIL"
        print(f"  shortest_path_length(graph, {s}, {e}) = {result}, expected {expected} [{status}]")
    
    # Test count_connected_components
    print("\n4. Testing count_connected_components:")
    test_cases = [
        ((5, [(0, 1), (1, 2), (3, 4)]), 2),
        ((4, [(0, 1), (2, 3)]), 2),
        ((3, []), 3),
    ]
    for (n, edges), expected in test_cases:
        result = count_connected_components(n, edges)
        status = "PASS" if result == expected else "FAIL"
        print(f"  count_connected_components({n}, {edges}) = {result}, expected {expected} [{status}]")
    
    # Test number_of_islands
    print("\n5. Testing number_of_islands:")
    grid = [
        ['1', '1', '0', '0', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '1', '0', '0'],
        ['0', '0', '0', '1', '1']
    ]
    result = number_of_islands(grid)
    expected = 3
    status = "PASS" if result == expected else "FAIL"
    print(f"  number_of_islands(grid) = {result}, expected {expected} [{status}]")
    
    # Test has_cycle_undirected
    print("\n6. Testing has_cycle_undirected:")
    test_cases = [
        ((3, [(0, 1), (1, 2), (2, 0)]), True),
        ((3, [(0, 1), (1, 2)]), False),
    ]
    for (n, edges), expected in test_cases:
        result = has_cycle_undirected(n, edges)
        status = "PASS" if result == expected else "FAIL"
        print(f"  has_cycle_undirected({n}, {edges}) = {result}, expected {expected} [{status}]")
    
    # Test can_finish_courses
    print("\n7. Testing can_finish_courses:")
    test_cases = [
        ((2, [[1, 0]]), True),
        ((2, [[1, 0], [0, 1]]), False),
    ]
    for (n, prereqs), expected in test_cases:
        result = can_finish_courses(n, prereqs)
        status = "PASS" if result == expected else "FAIL"
        print(f"  can_finish_courses({n}, {prereqs}) = {result}, expected {expected} [{status}]")
    
    # Test is_bipartite
    print("\n8. Testing is_bipartite:")
    test_cases = [
        ((4, [(0, 1), (1, 2), (2, 3), (3, 0)]), True),
        ((3, [(0, 1), (1, 2), (2, 0)]), False),
    ]
    for (n, edges), expected in test_cases:
        result = is_bipartite(n, edges)
        status = "PASS" if result == expected else "FAIL"
        print(f"  is_bipartite({n}, {edges}) = {result}, expected {expected} [{status}]")
    
    print("\n" + "=" * 60)
    print("Tests complete! Implement the functions to make them pass.")


if __name__ == "__main__":
    run_tests()
