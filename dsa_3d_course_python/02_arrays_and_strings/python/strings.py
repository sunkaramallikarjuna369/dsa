"""
Strings Module

This module provides demonstrations of string operations and common
string algorithms with step-by-step tracking for 3D visualization.

Strings in Python are immutable sequences of characters. Understanding
immutability is crucial for writing efficient string manipulation code.
"""

from typing import Any
from dataclasses import dataclass, field


@dataclass
class StringStep:
    """Represents a single step in string visualization."""
    step_number: int
    operation: str
    description: str
    string_state: str
    indices_accessed: list[int] = field(default_factory=list)
    new_string_created: bool = False
    comparison_indices: list[tuple[int, int]] = field(default_factory=list)


class StringVisualizer:
    """
    Tracks string operations for visualization.
    
    Demonstrates string immutability by recording when new string
    objects are created versus when existing strings are accessed.
    """
    
    def __init__(self) -> None:
        self._steps: list[StringStep] = []
        self._step_count: int = 0
    
    def reset(self) -> None:
        """Reset the step tracker."""
        self._steps = []
        self._step_count = 0
    
    def _record_step(
        self,
        operation: str,
        description: str,
        string_state: str,
        indices_accessed: list[int] | None = None,
        new_string_created: bool = False,
        comparison_indices: list[tuple[int, int]] | None = None
    ) -> None:
        """Record a visualization step."""
        self._step_count += 1
        step = StringStep(
            step_number=self._step_count,
            operation=operation,
            description=description,
            string_state=string_state,
            indices_accessed=indices_accessed or [],
            new_string_created=new_string_created,
            comparison_indices=comparison_indices or []
        )
        self._steps.append(step)
    
    @property
    def steps(self) -> list[StringStep]:
        """Return all recorded steps."""
        return self._steps
    
    def print_steps(self) -> None:
        """Print all recorded steps."""
        print(f"\n{'='*60}")
        print(f"String Operation Steps ({len(self._steps)} total)")
        print(f"{'='*60}")
        for step in self._steps:
            new_str_marker = " [NEW STRING]" if step.new_string_created else ""
            print(f"Step {step.step_number}: [{step.operation}] {step.description}{new_str_marker}")
            print(f"  String: \"{step.string_state}\"")
        print(f"{'='*60}\n")


def demonstrate_immutability(visualizer: StringVisualizer) -> None:
    """
    Demonstrate string immutability through various operations.
    
    Shows that string operations create new objects rather than
    modifying existing ones.
    """
    visualizer.reset()
    
    s = "hello"
    visualizer._record_step(
        "create",
        f"Create string s = 'hello' at memory address {id(s)}",
        s
    )
    
    original_id = id(s)
    s_upper = s.upper()
    visualizer._record_step(
        "upper",
        f"s.upper() creates NEW string at address {id(s_upper)} (original unchanged at {original_id})",
        s_upper,
        new_string_created=True
    )
    
    s_concat = s + " world"
    visualizer._record_step(
        "concatenate",
        f"s + ' world' creates NEW string at address {id(s_concat)}",
        s_concat,
        new_string_created=True
    )
    
    s_slice = s[1:4]
    visualizer._record_step(
        "slice",
        f"s[1:4] creates NEW string at address {id(s_slice)}",
        s_slice,
        indices_accessed=[1, 2, 3],
        new_string_created=True
    )
    
    visualizer._record_step(
        "verify",
        f"Original string s is still 'hello' at address {id(s)} (unchanged)",
        s
    )


def is_palindrome(s: str) -> tuple[bool, list[StringStep]]:
    """
    Check if a string is a palindrome using two-pointer technique.
    
    Args:
        s: The string to check
        
    Returns:
        Tuple of (is_palindrome, list of visualization steps)
        
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    steps: list[StringStep] = []
    step_count = 0
    
    clean_s = ''.join(c.lower() for c in s if c.isalnum())
    
    step_count += 1
    steps.append(StringStep(
        step_number=step_count,
        operation="clean",
        description=f"Clean string: remove non-alphanumeric, lowercase",
        string_state=clean_s,
        new_string_created=True
    ))
    
    left, right = 0, len(clean_s) - 1
    
    while left < right:
        step_count += 1
        match = clean_s[left] == clean_s[right]
        steps.append(StringStep(
            step_number=step_count,
            operation="compare",
            description=f"Compare s[{left}]='{clean_s[left]}' with s[{right}]='{clean_s[right]}': {'MATCH' if match else 'NO MATCH'}",
            string_state=clean_s,
            indices_accessed=[left, right],
            comparison_indices=[(left, right)]
        ))
        
        if not match:
            step_count += 1
            steps.append(StringStep(
                step_number=step_count,
                operation="result",
                description="Not a palindrome - characters don't match",
                string_state=clean_s
            ))
            return False, steps
        
        left += 1
        right -= 1
    
    step_count += 1
    steps.append(StringStep(
        step_number=step_count,
        operation="result",
        description="Is a palindrome - all characters matched",
        string_state=clean_s
    ))
    return True, steps


def longest_common_prefix(strs: list[str]) -> tuple[str, list[StringStep]]:
    """
    Find the longest common prefix among a list of strings.
    
    Args:
        strs: List of strings
        
    Returns:
        Tuple of (longest common prefix, list of visualization steps)
        
    Time Complexity: O(S) where S is sum of all characters
    Space Complexity: O(1)
    """
    steps: list[StringStep] = []
    step_count = 0
    
    if not strs:
        return "", steps
    
    step_count += 1
    steps.append(StringStep(
        step_number=step_count,
        operation="initialize",
        description=f"Start with first string as prefix candidate",
        string_state=strs[0]
    ))
    
    prefix = strs[0]
    
    for i, s in enumerate(strs[1:], 1):
        step_count += 1
        steps.append(StringStep(
            step_number=step_count,
            operation="compare_string",
            description=f"Compare prefix '{prefix}' with string[{i}]='{s}'",
            string_state=prefix
        ))
        
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            step_count += 1
            steps.append(StringStep(
                step_number=step_count,
                operation="shorten",
                description=f"Shorten prefix to '{prefix}'",
                string_state=prefix,
                new_string_created=True
            ))
            
            if not prefix:
                step_count += 1
                steps.append(StringStep(
                    step_number=step_count,
                    operation="result",
                    description="No common prefix found",
                    string_state=""
                ))
                return "", steps
    
    step_count += 1
    steps.append(StringStep(
        step_number=step_count,
        operation="result",
        description=f"Longest common prefix: '{prefix}'",
        string_state=prefix
    ))
    return prefix, steps


def find_anagrams(s: str, p: str) -> tuple[list[int], list[StringStep]]:
    """
    Find all start indices of p's anagrams in s using sliding window.
    
    Args:
        s: The string to search in
        p: The pattern to find anagrams of
        
    Returns:
        Tuple of (list of starting indices, list of visualization steps)
        
    Time Complexity: O(n)
    Space Complexity: O(1) - fixed size character count arrays
    """
    steps: list[StringStep] = []
    step_count = 0
    result: list[int] = []
    
    if len(p) > len(s):
        return result, steps
    
    p_count: dict[str, int] = {}
    window_count: dict[str, int] = {}
    
    for c in p:
        p_count[c] = p_count.get(c, 0) + 1
    
    step_count += 1
    steps.append(StringStep(
        step_number=step_count,
        operation="initialize",
        description=f"Pattern '{p}' character counts: {p_count}",
        string_state=s
    ))
    
    for i in range(len(s)):
        char = s[i]
        window_count[char] = window_count.get(char, 0) + 1
        
        if i >= len(p):
            left_char = s[i - len(p)]
            window_count[left_char] -= 1
            if window_count[left_char] == 0:
                del window_count[left_char]
        
        if i >= len(p) - 1:
            window_start = i - len(p) + 1
            is_anagram = window_count == p_count
            
            step_count += 1
            steps.append(StringStep(
                step_number=step_count,
                operation="check_window",
                description=f"Window [{window_start}:{i+1}] = '{s[window_start:i+1]}': {'ANAGRAM' if is_anagram else 'not anagram'}",
                string_state=s,
                indices_accessed=list(range(window_start, i + 1))
            ))
            
            if is_anagram:
                result.append(window_start)
    
    step_count += 1
    steps.append(StringStep(
        step_number=step_count,
        operation="result",
        description=f"Found {len(result)} anagram(s) at indices: {result}",
        string_state=s
    ))
    return result, steps


def reverse_words(s: str) -> tuple[str, list[StringStep]]:
    """
    Reverse the order of words in a string.
    
    Args:
        s: The input string
        
    Returns:
        Tuple of (reversed string, list of visualization steps)
        
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    steps: list[StringStep] = []
    step_count = 0
    
    step_count += 1
    steps.append(StringStep(
        step_number=step_count,
        operation="input",
        description=f"Input string: '{s}'",
        string_state=s
    ))
    
    words = s.split()
    step_count += 1
    steps.append(StringStep(
        step_number=step_count,
        operation="split",
        description=f"Split into words: {words}",
        string_state=str(words),
        new_string_created=True
    ))
    
    words.reverse()
    step_count += 1
    steps.append(StringStep(
        step_number=step_count,
        operation="reverse",
        description=f"Reverse word order: {words}",
        string_state=str(words)
    ))
    
    result = ' '.join(words)
    step_count += 1
    steps.append(StringStep(
        step_number=step_count,
        operation="join",
        description=f"Join words: '{result}'",
        string_state=result,
        new_string_created=True
    ))
    
    return result, steps


def compress_string(s: str) -> tuple[str, list[StringStep]]:
    """
    Compress string using run-length encoding.
    
    Example: "aabcccccaaa" -> "a2b1c5a3"
    
    Args:
        s: The string to compress
        
    Returns:
        Tuple of (compressed string or original if not shorter, steps)
        
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    steps: list[StringStep] = []
    step_count = 0
    
    if not s:
        return s, steps
    
    step_count += 1
    steps.append(StringStep(
        step_number=step_count,
        operation="start",
        description=f"Compress string: '{s}'",
        string_state=s
    ))
    
    compressed: list[str] = []
    count = 1
    
    for i in range(1, len(s) + 1):
        if i < len(s) and s[i] == s[i - 1]:
            count += 1
        else:
            compressed.append(s[i - 1])
            compressed.append(str(count))
            
            step_count += 1
            steps.append(StringStep(
                step_number=step_count,
                operation="encode",
                description=f"Encode '{s[i-1]}' x {count} -> '{s[i-1]}{count}'",
                string_state=''.join(compressed),
                indices_accessed=[i - count, i - 1] if count > 1 else [i - 1]
            ))
            count = 1
    
    result = ''.join(compressed)
    
    if len(result) >= len(s):
        step_count += 1
        steps.append(StringStep(
            step_number=step_count,
            operation="result",
            description=f"Compressed '{result}' not shorter than original, return original",
            string_state=s
        ))
        return s, steps
    
    step_count += 1
    steps.append(StringStep(
        step_number=step_count,
        operation="result",
        description=f"Compressed: '{result}' (saved {len(s) - len(result)} characters)",
        string_state=result,
        new_string_created=True
    ))
    return result, steps


def demo() -> None:
    """Run demonstrations of string operations."""
    print("\n" + "="*60)
    print("STRING OPERATIONS DEMONSTRATIONS")
    print("="*60)
    
    # Immutability Demo
    print("\n--- String Immutability ---")
    visualizer = StringVisualizer()
    demonstrate_immutability(visualizer)
    visualizer.print_steps()
    
    # Palindrome Demo
    print("\n--- Palindrome Check ---")
    test_strings = ["A man a plan a canal Panama", "hello", "racecar"]
    for s in test_strings:
        is_pal, steps = is_palindrome(s)
        print(f"'{s}' is palindrome: {is_pal}")
    
    # Longest Common Prefix Demo
    print("\n--- Longest Common Prefix ---")
    strs = ["flower", "flow", "flight"]
    prefix, steps = longest_common_prefix(strs)
    print(f"Strings: {strs}")
    print(f"Longest common prefix: '{prefix}'")
    
    # Find Anagrams Demo
    print("\n--- Find Anagrams ---")
    s, p = "cbaebabacd", "abc"
    indices, steps = find_anagrams(s, p)
    print(f"String: '{s}', Pattern: '{p}'")
    print(f"Anagram indices: {indices}")
    
    # Reverse Words Demo
    print("\n--- Reverse Words ---")
    s = "the sky is blue"
    reversed_s, steps = reverse_words(s)
    print(f"Original: '{s}'")
    print(f"Reversed: '{reversed_s}'")
    
    # String Compression Demo
    print("\n--- String Compression ---")
    s = "aabcccccaaa"
    compressed, steps = compress_string(s)
    print(f"Original: '{s}'")
    print(f"Compressed: '{compressed}'")


if __name__ == "__main__":
    demo()
