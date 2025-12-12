"""
Dynamic Programming Implementation

This module provides implementations of classic dynamic programming algorithms
with step-by-step visualization tracking for 3D animation synchronization.

Algorithms included:
- Fibonacci: Classic introduction to DP (memoization and tabulation)
- 0/1 Knapsack: Maximize value within weight capacity
- Longest Common Subsequence (LCS): Find longest shared subsequence
- Coin Change: Minimum coins to make amount
- Edit Distance: Minimum operations to transform strings
- Longest Increasing Subsequence (LIS): Find longest increasing sequence

All functions include visualization step recording for 3D animation.
"""

from dataclasses import dataclass, field
from typing import TypeVar, Callable
from functools import lru_cache
import json

T = TypeVar('T')


@dataclass
class DPStep:
    """Represents a single step in a DP algorithm for visualization."""
    step_number: int
    action: str
    description: str
    cell: tuple[int, ...] = field(default_factory=tuple)
    value: int | float = 0
    dependencies: list[tuple[int, ...]] = field(default_factory=list)
    table_state: list = field(default_factory=list)
    extra: dict = field(default_factory=dict)


class DPVisualizer:
    """Tracks DP algorithm steps for visualization."""
    
    def __init__(self) -> None:
        self.steps: list[DPStep] = []
        self.step_count: int = 0
    
    def record(self, action: str, description: str,
               cell: tuple[int, ...] | None = None,
               value: int | float = 0,
               dependencies: list[tuple[int, ...]] | None = None,
               table_state: list | None = None,
               **extra) -> None:
        """Record a visualization step."""
        self.step_count += 1
        step = DPStep(
            step_number=self.step_count,
            action=action,
            description=description,
            cell=cell or (),
            value=value,
            dependencies=dependencies or [],
            table_state=table_state or [],
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
            'cell': s.cell,
            'value': s.value,
            'dependencies': s.dependencies,
            'table_state': s.table_state,
            **s.extra
        } for s in self.steps], indent=2)


def fibonacci_memo(n: int, visualizer: DPVisualizer | None = None) -> int:
    """
    Compute nth Fibonacci number using memoization (top-down DP).
    
    Args:
        n: Index of Fibonacci number to compute (0-indexed)
        visualizer: Optional visualizer for step tracking
    
    Returns:
        The nth Fibonacci number
    
    Time Complexity: O(n)
    Space Complexity: O(n) for memoization cache
    
    Example:
        >>> fibonacci_memo(10)
        55
    """
    memo: dict[int, int] = {}
    
    if visualizer:
        visualizer.record("init", f"Computing Fibonacci({n}) with memoization")
    
    def fib(k: int) -> int:
        if k in memo:
            if visualizer:
                visualizer.record("cache_hit", f"Cache hit for F({k}) = {memo[k]}",
                                 cell=(k,), value=memo[k])
            return memo[k]
        
        if k <= 1:
            memo[k] = k
            if visualizer:
                visualizer.record("base_case", f"Base case: F({k}) = {k}",
                                 cell=(k,), value=k)
            return k
        
        if visualizer:
            visualizer.record("compute", f"Computing F({k}) = F({k-1}) + F({k-2})",
                             cell=(k,), dependencies=[(k-1,), (k-2,)])
        
        result = fib(k - 1) + fib(k - 2)
        memo[k] = result
        
        if visualizer:
            visualizer.record("store", f"F({k}) = {result}",
                             cell=(k,), value=result,
                             table_state=list(memo.items()))
        
        return result
    
    result = fib(n)
    
    if visualizer:
        visualizer.record("complete", f"Fibonacci({n}) = {result}",
                         value=result)
    
    return result


def fibonacci_tab(n: int, visualizer: DPVisualizer | None = None) -> int:
    """
    Compute nth Fibonacci number using tabulation (bottom-up DP).
    
    Args:
        n: Index of Fibonacci number to compute (0-indexed)
        visualizer: Optional visualizer for step tracking
    
    Returns:
        The nth Fibonacci number
    
    Time Complexity: O(n)
    Space Complexity: O(n) for table, can be O(1) with optimization
    
    Example:
        >>> fibonacci_tab(10)
        55
    """
    if n <= 1:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    
    if visualizer:
        visualizer.record("init", f"Computing Fibonacci({n}) with tabulation",
                         table_state=dp.copy())
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
        
        if visualizer:
            visualizer.record("fill", f"F({i}) = F({i-1}) + F({i-2}) = {dp[i-1]} + {dp[i-2]} = {dp[i]}",
                             cell=(i,), value=dp[i],
                             dependencies=[(i-1,), (i-2,)],
                             table_state=dp.copy())
    
    if visualizer:
        visualizer.record("complete", f"Fibonacci({n}) = {dp[n]}",
                         value=dp[n], table_state=dp)
    
    return dp[n]


def knapsack_01(weights: list[int], values: list[int], capacity: int,
                visualizer: DPVisualizer | None = None) -> tuple[int, list[int]]:
    """
    Solve 0/1 knapsack problem using dynamic programming.
    
    Args:
        weights: List of item weights
        values: List of item values
        capacity: Maximum weight capacity
        visualizer: Optional visualizer for step tracking
    
    Returns:
        Tuple of (maximum value, list of selected item indices)
    
    Time Complexity: O(n * capacity)
    Space Complexity: O(n * capacity)
    
    Example:
        >>> knapsack_01([1, 3, 4, 5], [1, 4, 5, 7], 7)
        (9, [1, 2])
    """
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    if visualizer:
        visualizer.record("init", f"0/1 Knapsack: {n} items, capacity {capacity}",
                         extra={"weights": weights, "values": values})
    
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                include = values[i - 1] + dp[i - 1][w - weights[i - 1]]
                exclude = dp[i - 1][w]
                dp[i][w] = max(include, exclude)
                
                if visualizer:
                    choice = "include" if dp[i][w] == include else "exclude"
                    deps = [(i - 1, w)]
                    if weights[i - 1] <= w:
                        deps.append((i - 1, w - weights[i - 1]))
                    visualizer.record("fill", f"Item {i-1} (w={weights[i-1]}, v={values[i-1]}), cap={w}: {choice}",
                                     cell=(i, w), value=dp[i][w],
                                     dependencies=deps,
                                     extra={"choice": choice})
            else:
                dp[i][w] = dp[i - 1][w]
                
                if visualizer:
                    visualizer.record("fill", f"Item {i-1} too heavy for cap={w}, exclude",
                                     cell=(i, w), value=dp[i][w],
                                     dependencies=[(i - 1, w)])
    
    selected = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected.append(i - 1)
            w -= weights[i - 1]
    selected.reverse()
    
    if visualizer:
        visualizer.record("backtrack", f"Selected items: {selected}",
                         extra={"selected": selected})
        visualizer.record("complete", f"Maximum value: {dp[n][capacity]}",
                         value=dp[n][capacity])
    
    return dp[n][capacity], selected


def lcs(s1: str, s2: str, visualizer: DPVisualizer | None = None) -> tuple[int, str]:
    """
    Find longest common subsequence of two strings.
    
    Args:
        s1: First string
        s2: Second string
        visualizer: Optional visualizer for step tracking
    
    Returns:
        Tuple of (LCS length, LCS string)
    
    Time Complexity: O(m * n)
    Space Complexity: O(m * n)
    
    Example:
        >>> lcs("ABCDGH", "AEDFHR")
        (3, 'ADH')
    """
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    if visualizer:
        visualizer.record("init", f"LCS of '{s1}' and '{s2}'",
                         extra={"s1": s1, "s2": s2})
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                
                if visualizer:
                    visualizer.record("match", f"'{s1[i-1]}' == '{s2[j-1]}': diagonal + 1",
                                     cell=(i, j), value=dp[i][j],
                                     dependencies=[(i - 1, j - 1)],
                                     extra={"char": s1[i - 1]})
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                
                if visualizer:
                    source = "above" if dp[i][j] == dp[i - 1][j] else "left"
                    visualizer.record("no_match", f"'{s1[i-1]}' != '{s2[j-1]}': max({source})",
                                     cell=(i, j), value=dp[i][j],
                                     dependencies=[(i - 1, j), (i, j - 1)])
    
    lcs_str = []
    i, j = m, n
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            lcs_str.append(s1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    lcs_str.reverse()
    
    if visualizer:
        visualizer.record("backtrack", f"LCS: '{''.join(lcs_str)}'",
                         extra={"lcs": ''.join(lcs_str)})
        visualizer.record("complete", f"LCS length: {dp[m][n]}",
                         value=dp[m][n])
    
    return dp[m][n], ''.join(lcs_str)


def coin_change(coins: list[int], amount: int,
                visualizer: DPVisualizer | None = None) -> int:
    """
    Find minimum coins needed to make amount.
    
    Args:
        coins: List of coin denominations
        amount: Target amount
        visualizer: Optional visualizer for step tracking
    
    Returns:
        Minimum number of coins, or -1 if impossible
    
    Time Complexity: O(amount * len(coins))
    Space Complexity: O(amount)
    
    Example:
        >>> coin_change([1, 3, 4], 6)
        2
    """
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    if visualizer:
        visualizer.record("init", f"Coin change: amount={amount}, coins={coins}",
                         extra={"coins": coins, "amount": amount})
    
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                
                if visualizer:
                    visualizer.record("update", f"Amount {i}: use coin {coin}, total = {dp[i]}",
                                     cell=(i,), value=dp[i],
                                     dependencies=[(i - coin,)],
                                     extra={"coin_used": coin})
    
    result = dp[amount] if dp[amount] != float('inf') else -1
    
    if visualizer:
        visualizer.record("complete", f"Minimum coins for {amount}: {result}",
                         value=result, table_state=dp)
    
    return result


def edit_distance(s1: str, s2: str, visualizer: DPVisualizer | None = None) -> int:
    """
    Find minimum edit distance (Levenshtein distance) between two strings.
    
    Operations: insert, delete, replace (each costs 1)
    
    Args:
        s1: Source string
        s2: Target string
        visualizer: Optional visualizer for step tracking
    
    Returns:
        Minimum number of operations to transform s1 to s2
    
    Time Complexity: O(m * n)
    Space Complexity: O(m * n)
    
    Example:
        >>> edit_distance("horse", "ros")
        3
    """
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    if visualizer:
        visualizer.record("init", f"Edit distance: '{s1}' → '{s2}'",
                         extra={"s1": s1, "s2": s2})
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
                
                if visualizer:
                    visualizer.record("match", f"'{s1[i-1]}' == '{s2[j-1]}': no cost",
                                     cell=(i, j), value=dp[i][j],
                                     dependencies=[(i - 1, j - 1)],
                                     extra={"operation": "match"})
            else:
                replace = dp[i - 1][j - 1] + 1
                delete = dp[i - 1][j] + 1
                insert = dp[i][j - 1] + 1
                dp[i][j] = min(replace, delete, insert)
                
                if visualizer:
                    if dp[i][j] == replace:
                        op = "replace"
                    elif dp[i][j] == delete:
                        op = "delete"
                    else:
                        op = "insert"
                    visualizer.record("edit", f"'{s1[i-1]}' → '{s2[j-1]}': {op}",
                                     cell=(i, j), value=dp[i][j],
                                     dependencies=[(i-1, j-1), (i-1, j), (i, j-1)],
                                     extra={"operation": op})
    
    if visualizer:
        visualizer.record("complete", f"Edit distance: {dp[m][n]}",
                         value=dp[m][n])
    
    return dp[m][n]


def lis(nums: list[int], visualizer: DPVisualizer | None = None) -> int:
    """
    Find length of longest increasing subsequence.
    
    Args:
        nums: List of integers
        visualizer: Optional visualizer for step tracking
    
    Returns:
        Length of longest increasing subsequence
    
    Time Complexity: O(n²) for this implementation, O(n log n) possible
    Space Complexity: O(n)
    
    Example:
        >>> lis([10, 9, 2, 5, 3, 7, 101, 18])
        4
    """
    if not nums:
        return 0
    
    n = len(nums)
    dp = [1] * n
    
    if visualizer:
        visualizer.record("init", f"LIS of {nums}",
                         extra={"nums": nums})
    
    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    
                    if visualizer:
                        visualizer.record("extend", f"Extend LIS ending at {j} ({nums[j]}) to {i} ({nums[i]})",
                                         cell=(i,), value=dp[i],
                                         dependencies=[(j,)],
                                         extra={"from_idx": j, "to_idx": i})
    
    result = max(dp)
    
    if visualizer:
        visualizer.record("complete", f"LIS length: {result}",
                         value=result, table_state=dp)
    
    return result


def climbing_stairs(n: int, visualizer: DPVisualizer | None = None) -> int:
    """
    Count distinct ways to climb n stairs (1 or 2 steps at a time).
    
    Args:
        n: Number of stairs
        visualizer: Optional visualizer for step tracking
    
    Returns:
        Number of distinct ways to climb
    
    Time Complexity: O(n)
    Space Complexity: O(1) with optimization
    
    Example:
        >>> climbing_stairs(5)
        8
    """
    if n <= 2:
        return n
    
    if visualizer:
        visualizer.record("init", f"Climbing {n} stairs")
    
    prev2, prev1 = 1, 2
    
    for i in range(3, n + 1):
        current = prev1 + prev2
        
        if visualizer:
            visualizer.record("compute", f"Ways to reach stair {i} = {prev1} + {prev2} = {current}",
                             cell=(i,), value=current,
                             dependencies=[(i-1,), (i-2,)])
        
        prev2, prev1 = prev1, current
    
    if visualizer:
        visualizer.record("complete", f"Total ways: {prev1}",
                         value=prev1)
    
    return prev1


def demo() -> None:
    """Demonstrate dynamic programming algorithms with visualization."""
    print("=" * 60)
    print("DYNAMIC PROGRAMMING DEMONSTRATION")
    print("=" * 60)
    
    print("\n1. FIBONACCI (MEMOIZATION)")
    print("-" * 40)
    vis = DPVisualizer()
    result = fibonacci_memo(10, vis)
    print(f"Fibonacci(10) = {result}")
    print(f"Steps recorded: {len(vis.steps)}")
    
    print("\n2. FIBONACCI (TABULATION)")
    print("-" * 40)
    vis = DPVisualizer()
    result = fibonacci_tab(10, vis)
    print(f"Fibonacci(10) = {result}")
    
    print("\n3. 0/1 KNAPSACK")
    print("-" * 40)
    weights = [1, 3, 4, 5]
    values = [1, 4, 5, 7]
    capacity = 7
    vis = DPVisualizer()
    max_val, selected = knapsack_01(weights, values, capacity, vis)
    print(f"Items: weights={weights}, values={values}")
    print(f"Capacity: {capacity}")
    print(f"Maximum value: {max_val}")
    print(f"Selected items: {selected}")
    
    print("\n4. LONGEST COMMON SUBSEQUENCE")
    print("-" * 40)
    s1, s2 = "ABCDGH", "AEDFHR"
    vis = DPVisualizer()
    length, lcs_str = lcs(s1, s2, vis)
    print(f"Strings: '{s1}' and '{s2}'")
    print(f"LCS length: {length}")
    print(f"LCS: '{lcs_str}'")
    
    print("\n5. COIN CHANGE")
    print("-" * 40)
    coins = [1, 3, 4]
    amount = 6
    vis = DPVisualizer()
    min_coins = coin_change(coins, amount, vis)
    print(f"Coins: {coins}")
    print(f"Amount: {amount}")
    print(f"Minimum coins: {min_coins}")
    
    print("\n6. EDIT DISTANCE")
    print("-" * 40)
    s1, s2 = "horse", "ros"
    vis = DPVisualizer()
    dist = edit_distance(s1, s2, vis)
    print(f"Transform '{s1}' → '{s2}'")
    print(f"Edit distance: {dist}")
    
    print("\n7. LONGEST INCREASING SUBSEQUENCE")
    print("-" * 40)
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    vis = DPVisualizer()
    length = lis(nums, vis)
    print(f"Array: {nums}")
    print(f"LIS length: {length}")
    
    print("\n8. CLIMBING STAIRS")
    print("-" * 40)
    n = 5
    vis = DPVisualizer()
    ways = climbing_stairs(n, vis)
    print(f"Stairs: {n}")
    print(f"Distinct ways: {ways}")
    
    print("\n" + "=" * 60)


if __name__ == "__main__":
    demo()
