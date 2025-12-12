"""
Trie (Prefix Tree) Implementation

This module provides a Trie implementation for efficient string operations
with step-by-step visualization tracking for 3D animation synchronization.

Operations included:
- Insert: Add a word to the trie
- Search: Check if a word exists
- StartsWith: Check if any word starts with a prefix
- Delete: Remove a word from the trie
- Autocomplete: Find all words with a given prefix

All functions include visualization step recording for 3D animation.
"""

from dataclasses import dataclass, field
from typing import Iterator
import json


@dataclass
class TrieStep:
    """Represents a single step in a Trie operation for visualization."""
    step_number: int
    action: str
    description: str
    node_path: str = ""
    character: str = ""
    is_word_end: bool = False
    extra: dict = field(default_factory=dict)


class TrieVisualizer:
    """Tracks Trie operation steps for visualization."""
    
    def __init__(self) -> None:
        self.steps: list[TrieStep] = []
        self.step_count: int = 0
    
    def record(self, action: str, description: str,
               node_path: str = "",
               character: str = "",
               is_word_end: bool = False,
               **extra) -> None:
        """Record a visualization step."""
        self.step_count += 1
        step = TrieStep(
            step_number=self.step_count,
            action=action,
            description=description,
            node_path=node_path,
            character=character,
            is_word_end=is_word_end,
            extra=extra
        )
        self.steps.append(step)
    
    def reset(self) -> None:
        """Reset the visualizer."""
        self.steps = []
        self.step_count = 0
    
    def to_json(self) -> str:
        """Export steps as JSON."""
        return json.dumps([{
            'step': s.step_number,
            'action': s.action,
            'description': s.description,
            'node_path': s.node_path,
            'character': s.character,
            'is_word_end': s.is_word_end,
            **s.extra
        } for s in self.steps], indent=2)


class TrieNode:
    """A node in the Trie."""
    
    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}
        self.is_word_end: bool = False
        self.word_count: int = 0


class Trie:
    """
    Trie (Prefix Tree) data structure.
    
    A tree-like structure for storing strings where each node represents
    a character. Words sharing common prefixes share the same path from root.
    
    Time Complexity:
        - Insert: O(m) where m is word length
        - Search: O(m)
        - StartsWith: O(m)
        - Delete: O(m)
    
    Space Complexity: O(total characters across all words)
    
    Example:
        >>> trie = Trie()
        >>> trie.insert("apple")
        >>> trie.search("apple")
        True
        >>> trie.starts_with("app")
        True
    """
    
    def __init__(self) -> None:
        self.root = TrieNode()
        self.word_count = 0
    
    def insert(self, word: str, visualizer: TrieVisualizer | None = None) -> None:
        """
        Insert a word into the trie.
        
        Args:
            word: The word to insert
            visualizer: Optional visualizer for step tracking
        """
        if visualizer:
            visualizer.record("insert_start", f"Inserting '{word}'",
                             extra={"word": word})
        
        node = self.root
        path = ""
        
        for char in word:
            path += char
            
            if char not in node.children:
                node.children[char] = TrieNode()
                
                if visualizer:
                    visualizer.record("create_node", f"Create node for '{char}'",
                                     node_path=path, character=char,
                                     extra={"created": True})
            else:
                if visualizer:
                    visualizer.record("traverse", f"Traverse to existing '{char}'",
                                     node_path=path, character=char)
            
            node = node.children[char]
        
        if not node.is_word_end:
            node.is_word_end = True
            self.word_count += 1
        node.word_count += 1
        
        if visualizer:
            visualizer.record("mark_end", f"Mark '{word}' as word end",
                             node_path=path, is_word_end=True,
                             extra={"word": word})
    
    def search(self, word: str, visualizer: TrieVisualizer | None = None) -> bool:
        """
        Search for a word in the trie.
        
        Args:
            word: The word to search for
            visualizer: Optional visualizer for step tracking
        
        Returns:
            True if the word exists in the trie
        """
        if visualizer:
            visualizer.record("search_start", f"Searching for '{word}'",
                             extra={"word": word})
        
        node = self.root
        path = ""
        
        for char in word:
            path += char
            
            if char not in node.children:
                if visualizer:
                    visualizer.record("not_found", f"Character '{char}' not found",
                                     node_path=path, character=char,
                                     extra={"found": False})
                return False
            
            if visualizer:
                visualizer.record("traverse", f"Found '{char}', continue",
                                 node_path=path, character=char)
            
            node = node.children[char]
        
        found = node.is_word_end
        
        if visualizer:
            if found:
                visualizer.record("found", f"'{word}' found in trie",
                                 node_path=path, is_word_end=True,
                                 extra={"found": True, "word": word})
            else:
                visualizer.record("prefix_only", f"'{word}' is prefix only, not a word",
                                 node_path=path, is_word_end=False,
                                 extra={"found": False})
        
        return found
    
    def starts_with(self, prefix: str, visualizer: TrieVisualizer | None = None) -> bool:
        """
        Check if any word starts with the given prefix.
        
        Args:
            prefix: The prefix to check
            visualizer: Optional visualizer for step tracking
        
        Returns:
            True if any word starts with the prefix
        """
        if visualizer:
            visualizer.record("prefix_start", f"Checking prefix '{prefix}'",
                             extra={"prefix": prefix})
        
        node = self.root
        path = ""
        
        for char in prefix:
            path += char
            
            if char not in node.children:
                if visualizer:
                    visualizer.record("prefix_not_found", f"Prefix '{prefix}' not found",
                                     node_path=path, character=char,
                                     extra={"exists": False})
                return False
            
            if visualizer:
                visualizer.record("traverse", f"Found '{char}'",
                                 node_path=path, character=char)
            
            node = node.children[char]
        
        if visualizer:
            visualizer.record("prefix_found", f"Prefix '{prefix}' exists",
                             node_path=path, extra={"exists": True})
        
        return True
    
    def autocomplete(self, prefix: str,
                     visualizer: TrieVisualizer | None = None) -> list[str]:
        """
        Find all words that start with the given prefix.
        
        Args:
            prefix: The prefix to search for
            visualizer: Optional visualizer for step tracking
        
        Returns:
            List of words starting with the prefix
        """
        if visualizer:
            visualizer.record("autocomplete_start", f"Autocomplete for '{prefix}'",
                             extra={"prefix": prefix})
        
        node = self.root
        
        for char in prefix:
            if char not in node.children:
                if visualizer:
                    visualizer.record("no_completions", f"No words with prefix '{prefix}'",
                                     extra={"completions": []})
                return []
            node = node.children[char]
        
        words: list[str] = []
        
        def dfs(current: TrieNode, path: str) -> None:
            if current.is_word_end:
                words.append(path)
                
                if visualizer:
                    visualizer.record("found_word", f"Found word: '{path}'",
                                     node_path=path, is_word_end=True)
            
            for char, child in current.children.items():
                dfs(child, path + char)
        
        dfs(node, prefix)
        
        if visualizer:
            visualizer.record("autocomplete_done", f"Found {len(words)} completions",
                             extra={"completions": words, "count": len(words)})
        
        return words
    
    def delete(self, word: str, visualizer: TrieVisualizer | None = None) -> bool:
        """
        Delete a word from the trie.
        
        Args:
            word: The word to delete
            visualizer: Optional visualizer for step tracking
        
        Returns:
            True if the word was deleted, False if not found
        """
        if visualizer:
            visualizer.record("delete_start", f"Deleting '{word}'",
                             extra={"word": word})
        
        def _delete(node: TrieNode, word: str, depth: int) -> bool:
            if depth == len(word):
                if not node.is_word_end:
                    return False
                node.is_word_end = False
                node.word_count -= 1
                self.word_count -= 1
                return len(node.children) == 0
            
            char = word[depth]
            if char not in node.children:
                return False
            
            should_delete = _delete(node.children[char], word, depth + 1)
            
            if should_delete:
                del node.children[char]
                
                if visualizer:
                    visualizer.record("delete_node", f"Delete node '{char}'",
                                     character=char)
                
                return len(node.children) == 0 and not node.is_word_end
            
            return False
        
        result = _delete(self.root, word, 0)
        
        if visualizer:
            visualizer.record("delete_done", f"Delete '{word}': {'success' if result else 'not found'}",
                             extra={"deleted": result})
        
        return result
    
    def get_all_words(self) -> list[str]:
        """Get all words in the trie."""
        return self.autocomplete("")
    
    def __len__(self) -> int:
        return self.word_count
    
    def __contains__(self, word: str) -> bool:
        return self.search(word)


def demo() -> None:
    """Demonstrate Trie operations with visualization."""
    print("=" * 60)
    print("TRIE (PREFIX TREE) DEMONSTRATION")
    print("=" * 60)
    
    trie = Trie()
    vis = TrieVisualizer()
    
    print("\n1. INSERT OPERATIONS")
    print("-" * 40)
    words = ["apple", "app", "application", "apply", "apt", "bat", "bath"]
    for word in words:
        trie.insert(word, vis)
        print(f"Inserted: {word}")
    print(f"Total words: {len(trie)}")
    
    print("\n2. SEARCH OPERATIONS")
    print("-" * 40)
    search_words = ["apple", "app", "apex", "bat", "batman"]
    for word in search_words:
        vis.reset()
        found = trie.search(word, vis)
        print(f"Search '{word}': {'Found' if found else 'Not found'}")
    
    print("\n3. PREFIX OPERATIONS")
    print("-" * 40)
    prefixes = ["app", "ba", "xyz"]
    for prefix in prefixes:
        vis.reset()
        exists = trie.starts_with(prefix, vis)
        print(f"Prefix '{prefix}' exists: {exists}")
    
    print("\n4. AUTOCOMPLETE")
    print("-" * 40)
    prefix = "app"
    vis.reset()
    completions = trie.autocomplete(prefix, vis)
    print(f"Autocomplete '{prefix}': {completions}")
    
    print("\n5. ALL WORDS")
    print("-" * 40)
    all_words = trie.get_all_words()
    print(f"All words in trie: {all_words}")
    
    print("\n" + "=" * 60)


if __name__ == "__main__":
    demo()
