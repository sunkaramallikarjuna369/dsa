"""
Exercises: Trees and Binary Search Trees

Complete the following exercises to practice tree operations.
Each function has a docstring explaining what to implement.

Run this file to test your implementations against the provided test cases.
"""

from typing import Any


class TreeNode:
    """A node in a binary tree."""
    def __init__(self, val: int = 0, left: 'TreeNode | None' = None, right: 'TreeNode | None' = None):
        self.val = val
        self.left = left
        self.right = right


# =============================================================================
# EXERCISE 1: Tree Traversals
# =============================================================================

def inorder_traversal(root: TreeNode | None) -> list[int]:
    """
    Perform in-order traversal of a binary tree.
    
    TODO: Implement this function (iteratively or recursively).
    
    Args:
        root: Root of the binary tree
        
    Returns:
        List of values in in-order sequence (Left, Root, Right)
        
    Expected Time Complexity: O(n)
    Expected Space Complexity: O(n)
    
    Example:
        Tree:    1
                  \
                   2
                  /
                 3
        inorder_traversal(root) -> [1, 3, 2]
    """
    # TODO: Implement this function
    pass


def preorder_traversal(root: TreeNode | None) -> list[int]:
    """
    Perform pre-order traversal of a binary tree.
    
    TODO: Implement this function.
    
    Args:
        root: Root of the binary tree
        
    Returns:
        List of values in pre-order sequence (Root, Left, Right)
        
    Expected Time Complexity: O(n)
    Expected Space Complexity: O(n)
    """
    # TODO: Implement this function
    pass


def postorder_traversal(root: TreeNode | None) -> list[int]:
    """
    Perform post-order traversal of a binary tree.
    
    TODO: Implement this function.
    
    Args:
        root: Root of the binary tree
        
    Returns:
        List of values in post-order sequence (Left, Right, Root)
        
    Expected Time Complexity: O(n)
    Expected Space Complexity: O(n)
    """
    # TODO: Implement this function
    pass


def levelorder_traversal(root: TreeNode | None) -> list[list[int]]:
    """
    Perform level-order traversal of a binary tree.
    
    TODO: Implement this function using a queue.
    
    Args:
        root: Root of the binary tree
        
    Returns:
        List of lists, where each inner list contains values at that level
        
    Expected Time Complexity: O(n)
    Expected Space Complexity: O(n)
    
    Example:
        Tree:    3
                / \
               9  20
                  / \
                 15  7
        levelorder_traversal(root) -> [[3], [9, 20], [15, 7]]
    """
    # TODO: Implement this function
    pass


# =============================================================================
# EXERCISE 2: BST Operations
# =============================================================================

def search_bst(root: TreeNode | None, val: int) -> TreeNode | None:
    """
    Search for a value in a BST.
    
    TODO: Implement this function.
    
    Args:
        root: Root of the BST
        val: Value to search for
        
    Returns:
        The node with the value, or None if not found
        
    Expected Time Complexity: O(log n) average, O(n) worst
    Expected Space Complexity: O(1) iterative, O(log n) recursive
    """
    # TODO: Implement this function
    pass


def insert_into_bst(root: TreeNode | None, val: int) -> TreeNode:
    """
    Insert a value into a BST.
    
    TODO: Implement this function.
    
    Args:
        root: Root of the BST (can be None for empty tree)
        val: Value to insert
        
    Returns:
        Root of the BST after insertion
        
    Expected Time Complexity: O(log n) average, O(n) worst
    Expected Space Complexity: O(1) iterative, O(log n) recursive
    """
    # TODO: Implement this function
    pass


def delete_from_bst(root: TreeNode | None, key: int) -> TreeNode | None:
    """
    Delete a value from a BST.
    
    TODO: Implement this function handling all three cases:
    1. Node is a leaf
    2. Node has one child
    3. Node has two children (use in-order successor)
    
    Args:
        root: Root of the BST
        key: Value to delete
        
    Returns:
        Root of the BST after deletion
        
    Expected Time Complexity: O(log n) average, O(n) worst
    Expected Space Complexity: O(log n) for recursion
    """
    # TODO: Implement this function
    pass


# =============================================================================
# EXERCISE 3: BST Validation and Properties
# =============================================================================

def is_valid_bst(root: TreeNode | None) -> bool:
    """
    Determine if a binary tree is a valid BST.
    
    TODO: Implement this function.
    
    Args:
        root: Root of the binary tree
        
    Returns:
        True if valid BST, False otherwise
        
    Expected Time Complexity: O(n)
    Expected Space Complexity: O(n) for recursion stack
    
    Hint: Use min/max bounds that update as you traverse.
    A common mistake is only checking immediate children.
    """
    # TODO: Implement this function
    pass


def find_min_in_bst(root: TreeNode | None) -> int | None:
    """
    Find the minimum value in a BST.
    
    TODO: Implement this function.
    
    Args:
        root: Root of the BST
        
    Returns:
        Minimum value, or None if tree is empty
        
    Expected Time Complexity: O(log n) average, O(n) worst
    Expected Space Complexity: O(1)
    
    Hint: The minimum is always in the leftmost node.
    """
    # TODO: Implement this function
    pass


def find_max_in_bst(root: TreeNode | None) -> int | None:
    """
    Find the maximum value in a BST.
    
    TODO: Implement this function.
    
    Args:
        root: Root of the BST
        
    Returns:
        Maximum value, or None if tree is empty
        
    Expected Time Complexity: O(log n) average, O(n) worst
    Expected Space Complexity: O(1)
    """
    # TODO: Implement this function
    pass


# =============================================================================
# EXERCISE 4: Tree Properties
# =============================================================================

def max_depth(root: TreeNode | None) -> int:
    """
    Find the maximum depth (height) of a binary tree.
    
    TODO: Implement this function.
    
    Args:
        root: Root of the binary tree
        
    Returns:
        Maximum depth (0 for empty tree, 1 for single node)
        
    Expected Time Complexity: O(n)
    Expected Space Complexity: O(n) for recursion stack
    
    Example:
        Tree:    3
                / \
               9  20
                  / \
                 15  7
        max_depth(root) -> 3
    """
    # TODO: Implement this function
    pass


def is_balanced(root: TreeNode | None) -> bool:
    """
    Determine if a binary tree is height-balanced.
    
    TODO: Implement this function.
    
    A tree is balanced if for every node, the heights of left and right
    subtrees differ by at most 1.
    
    Args:
        root: Root of the binary tree
        
    Returns:
        True if balanced, False otherwise
        
    Expected Time Complexity: O(n)
    Expected Space Complexity: O(n) for recursion stack
    """
    # TODO: Implement this function
    pass


def is_same_tree(p: TreeNode | None, q: TreeNode | None) -> bool:
    """
    Check if two binary trees are identical.
    
    TODO: Implement this function.
    
    Args:
        p: Root of first tree
        q: Root of second tree
        
    Returns:
        True if trees are identical, False otherwise
        
    Expected Time Complexity: O(n)
    Expected Space Complexity: O(n) for recursion stack
    """
    # TODO: Implement this function
    pass


# =============================================================================
# EXERCISE 5: Advanced Tree Problems
# =============================================================================

def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode | None:
    """
    Find the lowest common ancestor of two nodes in a BST.
    
    TODO: Implement this function using BST properties.
    
    Args:
        root: Root of the BST
        p: First node
        q: Second node
        
    Returns:
        The LCA node
        
    Expected Time Complexity: O(log n) average, O(n) worst
    Expected Space Complexity: O(1) iterative, O(log n) recursive
    
    Hint: Use BST property - if both values are smaller, go left;
    if both are larger, go right; otherwise current node is LCA.
    """
    # TODO: Implement this function
    pass


def sorted_array_to_bst(nums: list[int]) -> TreeNode | None:
    """
    Convert a sorted array to a height-balanced BST.
    
    TODO: Implement this function.
    
    Args:
        nums: Sorted array of integers
        
    Returns:
        Root of the balanced BST
        
    Expected Time Complexity: O(n)
    Expected Space Complexity: O(log n) for recursion stack
    
    Hint: Always choose the middle element as root to ensure balance.
    """
    # TODO: Implement this function
    pass


def kth_smallest(root: TreeNode | None, k: int) -> int | None:
    """
    Find the kth smallest element in a BST.
    
    TODO: Implement this function.
    
    Args:
        root: Root of the BST
        k: The k value (1-indexed)
        
    Returns:
        The kth smallest value, or None if k is invalid
        
    Expected Time Complexity: O(H + k) where H is height
    Expected Space Complexity: O(H) for recursion/stack
    
    Hint: In-order traversal visits nodes in sorted order.
    """
    # TODO: Implement this function
    pass


# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def build_tree(values: list[int | None]) -> TreeNode | None:
    """Build a tree from level-order list representation."""
    if not values or values[0] is None:
        return None
    
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    
    while queue and i < len(values):
        node = queue.pop(0)
        
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    
    return root


def tree_to_list(root: TreeNode | None) -> list[int | None]:
    """Convert tree to level-order list representation."""
    if not root:
        return []
    
    result: list[int | None] = []
    queue = [root]
    
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    
    while result and result[-1] is None:
        result.pop()
    
    return result


# =============================================================================
# TEST CASES
# =============================================================================

def run_tests() -> None:
    """Run all test cases for the exercises."""
    print("\n" + "="*60)
    print("RUNNING EXERCISE TESTS")
    print("="*60)
    
    all_passed = True
    
    # Test inorder_traversal
    print("\n--- Testing inorder_traversal ---")
    root1 = build_tree([1, None, 2, None, None, 3])
    result = inorder_traversal(root1)
    expected = [1, 3, 2]
    status = "PASS" if result == expected else "FAIL"
    if status == "FAIL":
        all_passed = False
    print(f"  inorder_traversal([1,null,2,3]) = {result}, expected {expected} [{status}]")
    
    # Test preorder_traversal
    print("\n--- Testing preorder_traversal ---")
    root2 = build_tree([1, 2, 3, 4, 5])
    result = preorder_traversal(root2)
    expected = [1, 2, 4, 5, 3]
    status = "PASS" if result == expected else "FAIL"
    if status == "FAIL":
        all_passed = False
    print(f"  preorder_traversal([1,2,3,4,5]) = {result}, expected {expected} [{status}]")
    
    # Test levelorder_traversal
    print("\n--- Testing levelorder_traversal ---")
    root3 = build_tree([3, 9, 20, None, None, 15, 7])
    result = levelorder_traversal(root3)
    expected = [[3], [9, 20], [15, 7]]
    status = "PASS" if result == expected else "FAIL"
    if status == "FAIL":
        all_passed = False
    print(f"  levelorder_traversal([3,9,20,null,null,15,7]) = {result}, expected {expected} [{status}]")
    
    # Test is_valid_bst
    print("\n--- Testing is_valid_bst ---")
    valid_bst = build_tree([2, 1, 3])
    invalid_bst = build_tree([5, 1, 4, None, None, 3, 6])
    
    result1 = is_valid_bst(valid_bst)
    result2 = is_valid_bst(invalid_bst)
    status1 = "PASS" if result1 == True else "FAIL"
    status2 = "PASS" if result2 == False else "FAIL"
    if status1 == "FAIL" or status2 == "FAIL":
        all_passed = False
    print(f"  is_valid_bst([2,1,3]) = {result1}, expected True [{status1}]")
    print(f"  is_valid_bst([5,1,4,null,null,3,6]) = {result2}, expected False [{status2}]")
    
    # Test max_depth
    print("\n--- Testing max_depth ---")
    root4 = build_tree([3, 9, 20, None, None, 15, 7])
    result = max_depth(root4)
    expected = 3
    status = "PASS" if result == expected else "FAIL"
    if status == "FAIL":
        all_passed = False
    print(f"  max_depth([3,9,20,null,null,15,7]) = {result}, expected {expected} [{status}]")
    
    # Test is_balanced
    print("\n--- Testing is_balanced ---")
    balanced = build_tree([3, 9, 20, None, None, 15, 7])
    unbalanced = build_tree([1, 2, 2, 3, 3, None, None, 4, 4])
    
    result1 = is_balanced(balanced)
    result2 = is_balanced(unbalanced)
    status1 = "PASS" if result1 == True else "FAIL"
    status2 = "PASS" if result2 == False else "FAIL"
    if status1 == "FAIL" or status2 == "FAIL":
        all_passed = False
    print(f"  is_balanced(balanced tree) = {result1}, expected True [{status1}]")
    print(f"  is_balanced(unbalanced tree) = {result2}, expected False [{status2}]")
    
    # Test sorted_array_to_bst
    print("\n--- Testing sorted_array_to_bst ---")
    nums = [-10, -3, 0, 5, 9]
    result_root = sorted_array_to_bst(nums)
    if result_root:
        result_valid = is_valid_bst(result_root)
        result_balanced = is_balanced(result_root)
        status = "PASS" if result_valid and result_balanced else "FAIL"
    else:
        status = "FAIL"
    if status == "FAIL":
        all_passed = False
    print(f"  sorted_array_to_bst({nums}) creates valid balanced BST [{status}]")
    
    # Test kth_smallest
    print("\n--- Testing kth_smallest ---")
    bst = build_tree([5, 3, 6, 2, 4, None, None, 1])
    tests = [(1, 1), (3, 3), (5, 5)]
    for k, expected in tests:
        result = kth_smallest(bst, k)
        status = "PASS" if result == expected else "FAIL"
        if status == "FAIL":
            all_passed = False
        print(f"  kth_smallest(bst, {k}) = {result}, expected {expected} [{status}]")
    
    print("\n" + "="*60)
    if all_passed:
        print("ALL TESTS PASSED!")
    else:
        print("SOME TESTS FAILED - Keep working on your implementations!")
    print("="*60 + "\n")


if __name__ == "__main__":
    run_tests()
