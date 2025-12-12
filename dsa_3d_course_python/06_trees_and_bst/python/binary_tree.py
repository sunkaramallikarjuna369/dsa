"""
Binary Tree Module

This module provides implementations of binary tree data structures
with step-by-step tracking for 3D visualization synchronization.

Includes basic binary tree and Binary Search Tree (BST) implementations.
"""

from typing import Any, TypeVar, Generic, Callable
from dataclasses import dataclass, field
from collections import deque

T = TypeVar('T')


@dataclass
class TreeStep:
    """Represents a single step in tree visualization."""
    step_number: int
    operation: str
    description: str
    node_value: Any = None
    path: list[Any] = field(default_factory=list)
    comparison: str = ""
    direction: str = ""


class TreeNode(Generic[T]):
    """A node in a binary tree."""
    
    def __init__(self, value: T) -> None:
        self.value: T = value
        self.left: TreeNode[T] | None = None
        self.right: TreeNode[T] | None = None
    
    def __repr__(self) -> str:
        return f"TreeNode({self.value})"


class BinarySearchTree(Generic[T]):
    """
    Binary Search Tree implementation with visualization tracking.
    
    BST Property: For every node, all values in left subtree are smaller,
    and all values in right subtree are larger.
    
    Average case: O(log n) for insert, search, delete
    Worst case: O(n) when tree becomes unbalanced
    """
    
    def __init__(self) -> None:
        """Initialize an empty BST."""
        self.root: TreeNode[T] | None = None
        self._size: int = 0
        self._steps: list[TreeStep] = []
        self._step_count: int = 0
    
    def _record_step(
        self,
        operation: str,
        description: str,
        node_value: Any = None,
        path: list[Any] | None = None,
        comparison: str = "",
        direction: str = ""
    ) -> None:
        """Record a visualization step."""
        self._step_count += 1
        step = TreeStep(
            step_number=self._step_count,
            operation=operation,
            description=description,
            node_value=node_value,
            path=path or [],
            comparison=comparison,
            direction=direction
        )
        self._steps.append(step)
    
    def clear_steps(self) -> None:
        """Clear recorded steps."""
        self._steps = []
        self._step_count = 0
    
    @property
    def steps(self) -> list[TreeStep]:
        """Return all recorded steps."""
        return self._steps
    
    def insert(self, value: T) -> None:
        """
        Insert a value into the BST.
        
        Time Complexity: O(log n) average, O(n) worst case
        """
        path: list[T] = []
        
        self._record_step(
            "insert_start",
            f"Inserting value {value} into BST",
            node_value=value
        )
        
        if self.root is None:
            self.root = TreeNode(value)
            self._size += 1
            self._record_step(
                "insert_root",
                f"Tree was empty, {value} becomes root",
                node_value=value
            )
            return
        
        current = self.root
        while True:
            path.append(current.value)
            
            if value < current.value:
                self._record_step(
                    "compare",
                    f"{value} < {current.value}, go LEFT",
                    node_value=current.value,
                    path=list(path),
                    comparison=f"{value} < {current.value}",
                    direction="LEFT"
                )
                
                if current.left is None:
                    current.left = TreeNode(value)
                    self._size += 1
                    self._record_step(
                        "insert_complete",
                        f"Inserted {value} as left child of {current.value}",
                        node_value=value,
                        path=list(path)
                    )
                    return
                current = current.left
            else:
                self._record_step(
                    "compare",
                    f"{value} >= {current.value}, go RIGHT",
                    node_value=current.value,
                    path=list(path),
                    comparison=f"{value} >= {current.value}",
                    direction="RIGHT"
                )
                
                if current.right is None:
                    current.right = TreeNode(value)
                    self._size += 1
                    self._record_step(
                        "insert_complete",
                        f"Inserted {value} as right child of {current.value}",
                        node_value=value,
                        path=list(path)
                    )
                    return
                current = current.right
    
    def search(self, value: T) -> bool:
        """
        Search for a value in the BST.
        
        Time Complexity: O(log n) average, O(n) worst case
        
        Returns:
            True if value exists, False otherwise
        """
        path: list[T] = []
        
        self._record_step(
            "search_start",
            f"Searching for value {value}",
            node_value=value
        )
        
        current = self.root
        while current is not None:
            path.append(current.value)
            
            if value == current.value:
                self._record_step(
                    "found",
                    f"Found {value}!",
                    node_value=value,
                    path=list(path)
                )
                return True
            elif value < current.value:
                self._record_step(
                    "compare",
                    f"{value} < {current.value}, go LEFT",
                    node_value=current.value,
                    path=list(path),
                    comparison=f"{value} < {current.value}",
                    direction="LEFT"
                )
                current = current.left
            else:
                self._record_step(
                    "compare",
                    f"{value} > {current.value}, go RIGHT",
                    node_value=current.value,
                    path=list(path),
                    comparison=f"{value} > {current.value}",
                    direction="RIGHT"
                )
                current = current.right
        
        self._record_step(
            "not_found",
            f"Value {value} not found in BST",
            node_value=value,
            path=list(path)
        )
        return False
    
    def delete(self, value: T) -> bool:
        """
        Delete a value from the BST.
        
        Time Complexity: O(log n) average, O(n) worst case
        
        Returns:
            True if value was deleted, False if not found
        """
        self._record_step(
            "delete_start",
            f"Deleting value {value}",
            node_value=value
        )
        
        self.root, deleted = self._delete_recursive(self.root, value)
        
        if deleted:
            self._size -= 1
        
        return deleted
    
    def _delete_recursive(
        self,
        node: TreeNode[T] | None,
        value: T
    ) -> tuple[TreeNode[T] | None, bool]:
        """Recursively delete a value from the subtree."""
        if node is None:
            self._record_step(
                "not_found",
                f"Value {value} not found",
                node_value=value
            )
            return None, False
        
        if value < node.value:
            node.left, deleted = self._delete_recursive(node.left, value)
            return node, deleted
        elif value > node.value:
            node.right, deleted = self._delete_recursive(node.right, value)
            return node, deleted
        else:
            # Found the node to delete
            if node.left is None and node.right is None:
                # Case 1: Leaf node
                self._record_step(
                    "delete_leaf",
                    f"Deleting leaf node {value}",
                    node_value=value
                )
                return None, True
            elif node.left is None:
                # Case 2: Only right child
                self._record_step(
                    "delete_one_child",
                    f"Deleting {value}, replacing with right child",
                    node_value=value
                )
                return node.right, True
            elif node.right is None:
                # Case 2: Only left child
                self._record_step(
                    "delete_one_child",
                    f"Deleting {value}, replacing with left child",
                    node_value=value
                )
                return node.left, True
            else:
                # Case 3: Two children - find in-order successor
                successor = self._find_min(node.right)
                self._record_step(
                    "delete_two_children",
                    f"Deleting {value}, replacing with successor {successor.value}",
                    node_value=value
                )
                node.value = successor.value
                node.right, _ = self._delete_recursive(node.right, successor.value)
                return node, True
    
    def _find_min(self, node: TreeNode[T]) -> TreeNode[T]:
        """Find the minimum value node in a subtree."""
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def _find_max(self, node: TreeNode[T]) -> TreeNode[T]:
        """Find the maximum value node in a subtree."""
        current = node
        while current.right is not None:
            current = current.right
        return current
    
    def inorder_traversal(self) -> list[T]:
        """
        In-order traversal: Left, Root, Right.
        Returns values in sorted order for BST.
        """
        result: list[T] = []
        self._record_step("traversal_start", "Starting in-order traversal")
        self._inorder_recursive(self.root, result)
        self._record_step(
            "traversal_complete",
            f"In-order traversal complete: {result}"
        )
        return result
    
    def _inorder_recursive(self, node: TreeNode[T] | None, result: list[T]) -> None:
        """Recursive in-order traversal helper."""
        if node is None:
            return
        
        self._inorder_recursive(node.left, result)
        result.append(node.value)
        self._record_step(
            "visit",
            f"Visiting node {node.value}",
            node_value=node.value
        )
        self._inorder_recursive(node.right, result)
    
    def preorder_traversal(self) -> list[T]:
        """
        Pre-order traversal: Root, Left, Right.
        Useful for copying tree structure.
        """
        result: list[T] = []
        self._record_step("traversal_start", "Starting pre-order traversal")
        self._preorder_recursive(self.root, result)
        self._record_step(
            "traversal_complete",
            f"Pre-order traversal complete: {result}"
        )
        return result
    
    def _preorder_recursive(self, node: TreeNode[T] | None, result: list[T]) -> None:
        """Recursive pre-order traversal helper."""
        if node is None:
            return
        
        result.append(node.value)
        self._record_step(
            "visit",
            f"Visiting node {node.value}",
            node_value=node.value
        )
        self._preorder_recursive(node.left, result)
        self._preorder_recursive(node.right, result)
    
    def postorder_traversal(self) -> list[T]:
        """
        Post-order traversal: Left, Right, Root.
        Useful for deleting tree (children before parent).
        """
        result: list[T] = []
        self._record_step("traversal_start", "Starting post-order traversal")
        self._postorder_recursive(self.root, result)
        self._record_step(
            "traversal_complete",
            f"Post-order traversal complete: {result}"
        )
        return result
    
    def _postorder_recursive(self, node: TreeNode[T] | None, result: list[T]) -> None:
        """Recursive post-order traversal helper."""
        if node is None:
            return
        
        self._postorder_recursive(node.left, result)
        self._postorder_recursive(node.right, result)
        result.append(node.value)
        self._record_step(
            "visit",
            f"Visiting node {node.value}",
            node_value=node.value
        )
    
    def levelorder_traversal(self) -> list[T]:
        """
        Level-order traversal (BFS): Visit nodes level by level.
        """
        result: list[T] = []
        
        if self.root is None:
            return result
        
        self._record_step("traversal_start", "Starting level-order traversal")
        
        queue: deque[TreeNode[T]] = deque([self.root])
        
        while queue:
            node = queue.popleft()
            result.append(node.value)
            self._record_step(
                "visit",
                f"Visiting node {node.value}",
                node_value=node.value
            )
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        self._record_step(
            "traversal_complete",
            f"Level-order traversal complete: {result}"
        )
        return result
    
    def height(self) -> int:
        """Return the height of the tree."""
        return self._height_recursive(self.root)
    
    def _height_recursive(self, node: TreeNode[T] | None) -> int:
        """Recursive height calculation."""
        if node is None:
            return -1
        return 1 + max(
            self._height_recursive(node.left),
            self._height_recursive(node.right)
        )
    
    def is_valid_bst(self) -> bool:
        """Check if the tree satisfies BST property."""
        return self._is_valid_recursive(self.root, None, None)
    
    def _is_valid_recursive(
        self,
        node: TreeNode[T] | None,
        min_val: T | None,
        max_val: T | None
    ) -> bool:
        """Recursive BST validation."""
        if node is None:
            return True
        
        if min_val is not None and node.value <= min_val:
            return False
        if max_val is not None and node.value >= max_val:
            return False
        
        return (
            self._is_valid_recursive(node.left, min_val, node.value) and
            self._is_valid_recursive(node.right, node.value, max_val)
        )
    
    def __len__(self) -> int:
        return self._size
    
    def __contains__(self, value: T) -> bool:
        return self.search(value)


def sorted_array_to_bst(arr: list[T]) -> BinarySearchTree[T]:
    """
    Convert a sorted array to a height-balanced BST.
    
    Time Complexity: O(n)
    Space Complexity: O(log n) for recursion stack
    """
    bst: BinarySearchTree[T] = BinarySearchTree()
    
    if not arr:
        return bst
    
    def build(left: int, right: int) -> TreeNode[T] | None:
        if left > right:
            return None
        
        mid = (left + right) // 2
        node = TreeNode(arr[mid])
        node.left = build(left, mid - 1)
        node.right = build(mid + 1, right)
        return node
    
    bst.root = build(0, len(arr) - 1)
    bst._size = len(arr)
    return bst


def lowest_common_ancestor(
    bst: BinarySearchTree[T],
    val1: T,
    val2: T
) -> T | None:
    """
    Find the lowest common ancestor of two values in a BST.
    
    Time Complexity: O(log n) average, O(n) worst case
    """
    node = bst.root
    
    while node:
        if val1 < node.value and val2 < node.value:
            node = node.left
        elif val1 > node.value and val2 > node.value:
            node = node.right
        else:
            return node.value
    
    return None


def demo() -> None:
    """Run demonstrations of BST operations."""
    print("\n" + "="*60)
    print("BINARY SEARCH TREE DEMONSTRATIONS")
    print("="*60)
    
    # Create and populate BST
    print("\n--- Creating BST ---")
    bst: BinarySearchTree[int] = BinarySearchTree()
    values = [50, 30, 70, 20, 40, 60, 80]
    
    for val in values:
        bst.insert(val)
        print(f"Inserted {val}")
    
    print(f"\nTree height: {bst.height()}")
    print(f"Tree size: {len(bst)}")
    print(f"Is valid BST: {bst.is_valid_bst()}")
    
    # Traversals
    print("\n--- Traversals ---")
    print(f"In-order:    {bst.inorder_traversal()}")
    bst.clear_steps()
    print(f"Pre-order:   {bst.preorder_traversal()}")
    bst.clear_steps()
    print(f"Post-order:  {bst.postorder_traversal()}")
    bst.clear_steps()
    print(f"Level-order: {bst.levelorder_traversal()}")
    
    # Search
    print("\n--- Search Operations ---")
    bst.clear_steps()
    print(f"Search 40: {bst.search(40)}")
    print(f"Search 45: {bst.search(45)}")
    
    # Delete
    print("\n--- Delete Operations ---")
    bst.clear_steps()
    print(f"Delete 20 (leaf): {bst.delete(20)}")
    print(f"In-order after delete: {bst.inorder_traversal()}")
    
    # Sorted array to BST
    print("\n--- Sorted Array to Balanced BST ---")
    sorted_arr = [10, 20, 30, 40, 50, 60, 70]
    balanced_bst = sorted_array_to_bst(sorted_arr)
    print(f"Input: {sorted_arr}")
    print(f"Balanced BST height: {balanced_bst.height()}")
    print(f"Level-order: {balanced_bst.levelorder_traversal()}")
    
    # LCA
    print("\n--- Lowest Common Ancestor ---")
    bst2: BinarySearchTree[int] = BinarySearchTree()
    for val in [50, 30, 70, 20, 40, 60, 80]:
        bst2.insert(val)
    print(f"LCA of 20 and 40: {lowest_common_ancestor(bst2, 20, 40)}")
    print(f"LCA of 20 and 60: {lowest_common_ancestor(bst2, 20, 60)}")


if __name__ == "__main__":
    demo()
