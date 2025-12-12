"""
Greedy Algorithms Implementation

This module provides implementations of various greedy algorithms
with step-by-step visualization tracking for 3D animation synchronization.

Algorithms included:
- Activity Selection: Select maximum non-overlapping activities
- Coin Change (Greedy): Make change with minimum coins (when greedy works)
- Huffman Coding: Build optimal prefix-free encoding
- Interval Scheduling: Schedule jobs to minimize conflicts
- Fractional Knapsack: Maximize value with fractional items

All functions include visualization step recording for 3D animation.
"""

from dataclasses import dataclass, field
from typing import TypeVar, Callable
from collections import Counter
import heapq
import json

T = TypeVar('T')


@dataclass
class GreedyStep:
    """Represents a single step in a greedy algorithm for visualization."""
    step_number: int
    action: str
    description: str
    choice: str = ""
    state: dict = field(default_factory=dict)
    extra: dict = field(default_factory=dict)


class GreedyVisualizer:
    """Tracks greedy algorithm steps for visualization."""
    
    def __init__(self) -> None:
        self.steps: list[GreedyStep] = []
        self.step_count: int = 0
    
    def record(self, action: str, description: str,
               choice: str = "",
               state: dict | None = None,
               **extra) -> None:
        """Record a visualization step."""
        self.step_count += 1
        step = GreedyStep(
            step_number=self.step_count,
            action=action,
            description=description,
            choice=choice,
            state=state or {},
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
            'choice': s.choice,
            'state': s.state,
            **s.extra
        } for s in self.steps], indent=2)


@dataclass
class Activity:
    """Represents an activity with start and end times."""
    name: str
    start: int
    end: int
    
    def __lt__(self, other: 'Activity') -> bool:
        return self.end < other.end


def activity_selection(activities: list[Activity],
                       visualizer: GreedyVisualizer | None = None) -> list[Activity]:
    """
    Select maximum number of non-overlapping activities.
    
    Greedy approach: Always select the activity that finishes earliest
    and doesn't conflict with previously selected activities.
    
    Args:
        activities: List of activities with start and end times
        visualizer: Optional visualizer for step tracking
    
    Returns:
        List of selected non-overlapping activities
    
    Time Complexity: O(n log n) for sorting
    Space Complexity: O(n) for result
    
    Example:
        >>> activities = [Activity("A", 1, 4), Activity("B", 3, 5), Activity("C", 0, 6)]
        >>> selected = activity_selection(activities)
        >>> [a.name for a in selected]
        ['A', 'B']  # or similar non-overlapping set
    """
    if not activities:
        return []
    
    if visualizer:
        visualizer.record("init", f"Starting activity selection with {len(activities)} activities",
                         state={"activities": [(a.name, a.start, a.end) for a in activities]})
    
    sorted_activities = sorted(activities, key=lambda a: a.end)
    
    if visualizer:
        visualizer.record("sort", "Sort activities by end time",
                         state={"sorted": [(a.name, a.start, a.end) for a in sorted_activities]})
    
    selected = [sorted_activities[0]]
    last_end = sorted_activities[0].end
    
    if visualizer:
        visualizer.record("select", f"Select first activity {sorted_activities[0].name}",
                         choice=sorted_activities[0].name,
                         state={"last_end": last_end, "selected": [sorted_activities[0].name]})
    
    for activity in sorted_activities[1:]:
        if visualizer:
            visualizer.record("check", f"Check activity {activity.name} [{activity.start}, {activity.end}]",
                             state={"checking": activity.name, "start": activity.start, "last_end": last_end})
        
        if activity.start >= last_end:
            selected.append(activity)
            last_end = activity.end
            
            if visualizer:
                visualizer.record("select", f"Select {activity.name} (start {activity.start} >= last_end {last_end - (activity.end - activity.start)})",
                                 choice=activity.name,
                                 state={"last_end": last_end, "selected": [a.name for a in selected]})
        else:
            if visualizer:
                visualizer.record("reject", f"Reject {activity.name} (start {activity.start} < last_end {last_end})",
                                 state={"rejected": activity.name})
    
    if visualizer:
        visualizer.record("complete", f"Activity selection complete: {len(selected)} activities selected",
                         state={"selected": [a.name for a in selected], "count": len(selected)})
    
    return selected


def coin_change_greedy(amount: int, coins: list[int],
                       visualizer: GreedyVisualizer | None = None) -> list[int]:
    """
    Make change using greedy approach (works for standard denominations).
    
    Greedy approach: Always select the largest coin that doesn't exceed
    the remaining amount.
    
    Note: This doesn't always produce optimal results for arbitrary
    coin denominations. Use dynamic programming for general case.
    
    Args:
        amount: Target amount to make change for
        coins: List of coin denominations (sorted descending)
        visualizer: Optional visualizer for step tracking
    
    Returns:
        List of coins used (may not be optimal for all denominations)
    
    Time Complexity: O(amount / min_coin)
    Space Complexity: O(amount / min_coin) for result
    
    Example:
        >>> coin_change_greedy(67, [25, 10, 5, 1])
        [25, 25, 10, 5, 1, 1]
    """
    if visualizer:
        visualizer.record("init", f"Make change for {amount} cents",
                         state={"amount": amount, "coins": coins})
    
    sorted_coins = sorted(coins, reverse=True)
    result = []
    remaining = amount
    
    for coin in sorted_coins:
        while remaining >= coin:
            result.append(coin)
            remaining -= coin
            
            if visualizer:
                visualizer.record("select", f"Select coin {coin}, remaining: {remaining}",
                                 choice=str(coin),
                                 state={"remaining": remaining, "result": result.copy()})
    
    if visualizer:
        if remaining == 0:
            visualizer.record("complete", f"Change made with {len(result)} coins",
                             state={"result": result, "count": len(result)})
        else:
            visualizer.record("fail", f"Cannot make exact change, remaining: {remaining}",
                             state={"remaining": remaining})
    
    return result if remaining == 0 else []


@dataclass
class HuffmanNode:
    """Node in a Huffman tree."""
    char: str | None
    freq: int
    left: 'HuffmanNode | None' = None
    right: 'HuffmanNode | None' = None
    
    def __lt__(self, other: 'HuffmanNode') -> bool:
        return self.freq < other.freq
    
    def is_leaf(self) -> bool:
        return self.left is None and self.right is None


def huffman_encoding(frequencies: dict[str, int],
                     visualizer: GreedyVisualizer | None = None) -> dict[str, str]:
    """
    Build Huffman encoding for characters based on frequencies.
    
    Greedy approach: Repeatedly combine the two nodes with lowest
    frequencies until a single tree remains.
    
    Args:
        frequencies: Dictionary mapping characters to their frequencies
        visualizer: Optional visualizer for step tracking
    
    Returns:
        Dictionary mapping characters to their binary encodings
    
    Time Complexity: O(n log n) where n is number of unique characters
    Space Complexity: O(n) for the tree
    
    Example:
        >>> freqs = {'A': 5, 'B': 9, 'C': 12, 'D': 13, 'E': 16, 'F': 45}
        >>> codes = huffman_encoding(freqs)
        >>> codes['F']  # Most frequent, shortest code
        '0'
    """
    if not frequencies:
        return {}
    
    if len(frequencies) == 1:
        char = list(frequencies.keys())[0]
        return {char: '0'}
    
    if visualizer:
        visualizer.record("init", "Initialize Huffman encoding",
                         state={"frequencies": frequencies})
    
    heap: list[HuffmanNode] = []
    for char, freq in frequencies.items():
        heapq.heappush(heap, HuffmanNode(char=char, freq=freq))
    
    if visualizer:
        visualizer.record("heap", "Create min-heap of character nodes",
                         state={"nodes": [(n.char, n.freq) for n in sorted(heap)]})
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        
        merged = HuffmanNode(
            char=None,
            freq=left.freq + right.freq,
            left=left,
            right=right
        )
        heapq.heappush(heap, merged)
        
        if visualizer:
            left_label = left.char if left.char else f"({left.freq})"
            right_label = right.char if right.char else f"({right.freq})"
            visualizer.record("merge", f"Merge {left_label}({left.freq}) and {right_label}({right.freq})",
                             choice=f"{left_label}+{right_label}",
                             state={"merged_freq": merged.freq, "remaining": len(heap)})
    
    root = heap[0]
    codes: dict[str, str] = {}
    
    def build_codes(node: HuffmanNode | None, code: str) -> None:
        if node is None:
            return
        if node.is_leaf() and node.char:
            codes[node.char] = code if code else '0'
            return
        build_codes(node.left, code + '0')
        build_codes(node.right, code + '1')
    
    build_codes(root, '')
    
    if visualizer:
        visualizer.record("complete", "Huffman encoding complete",
                         state={"codes": codes})
    
    return codes


def fractional_knapsack(capacity: int, items: list[tuple[int, int]],
                        visualizer: GreedyVisualizer | None = None) -> float:
    """
    Solve fractional knapsack problem using greedy approach.
    
    Greedy approach: Sort items by value/weight ratio and take
    items with highest ratio first. Can take fractions of items.
    
    Args:
        capacity: Maximum weight capacity
        items: List of (value, weight) tuples
        visualizer: Optional visualizer for step tracking
    
    Returns:
        Maximum value achievable
    
    Time Complexity: O(n log n) for sorting
    Space Complexity: O(n) for sorted items
    
    Example:
        >>> items = [(60, 10), (100, 20), (120, 30)]  # (value, weight)
        >>> fractional_knapsack(50, items)
        240.0
    """
    if not items or capacity <= 0:
        return 0.0
    
    if visualizer:
        visualizer.record("init", f"Fractional knapsack with capacity {capacity}",
                         state={"capacity": capacity, "items": items})
    
    items_with_ratio = [(v, w, v / w, i) for i, (v, w) in enumerate(items)]
    items_with_ratio.sort(key=lambda x: x[2], reverse=True)
    
    if visualizer:
        visualizer.record("sort", "Sort items by value/weight ratio",
                         state={"sorted": [(v, w, round(r, 2)) for v, w, r, _ in items_with_ratio]})
    
    total_value = 0.0
    remaining_capacity = capacity
    
    for value, weight, ratio, idx in items_with_ratio:
        if remaining_capacity <= 0:
            break
        
        if weight <= remaining_capacity:
            total_value += value
            remaining_capacity -= weight
            
            if visualizer:
                visualizer.record("take_full", f"Take full item {idx}: value={value}, weight={weight}",
                                 choice=f"item_{idx}_full",
                                 state={"remaining_capacity": remaining_capacity, "total_value": total_value})
        else:
            fraction = remaining_capacity / weight
            total_value += value * fraction
            
            if visualizer:
                visualizer.record("take_fraction", f"Take {fraction:.2%} of item {idx}: value={value * fraction:.2f}",
                                 choice=f"item_{idx}_{fraction:.2f}",
                                 state={"fraction": fraction, "total_value": total_value})
            
            remaining_capacity = 0
    
    if visualizer:
        visualizer.record("complete", f"Maximum value: {total_value}",
                         state={"total_value": total_value})
    
    return total_value


def jump_game(nums: list[int], visualizer: GreedyVisualizer | None = None) -> bool:
    """
    Determine if you can reach the last index.
    
    Greedy approach: Track the farthest reachable index. At each
    position, update the farthest reachable. If current position
    exceeds farthest, we're stuck.
    
    Args:
        nums: Array where nums[i] is max jump length from position i
        visualizer: Optional visualizer for step tracking
    
    Returns:
        True if last index is reachable
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Example:
        >>> jump_game([2, 3, 1, 1, 4])
        True
        >>> jump_game([3, 2, 1, 0, 4])
        False
    """
    if not nums:
        return True
    
    if visualizer:
        visualizer.record("init", f"Jump game with {len(nums)} positions",
                         state={"nums": nums})
    
    farthest = 0
    
    for i, jump in enumerate(nums):
        if i > farthest:
            if visualizer:
                visualizer.record("stuck", f"Position {i} unreachable (farthest was {farthest})",
                                 state={"position": i, "farthest": farthest})
            return False
        
        new_farthest = i + jump
        if new_farthest > farthest:
            farthest = new_farthest
            
            if visualizer:
                visualizer.record("update", f"Position {i}: can jump {jump}, farthest now {farthest}",
                                 choice=f"reach_{farthest}",
                                 state={"position": i, "jump": jump, "farthest": farthest})
        
        if farthest >= len(nums) - 1:
            if visualizer:
                visualizer.record("success", f"Can reach end (farthest {farthest} >= {len(nums) - 1})",
                                 state={"farthest": farthest, "target": len(nums) - 1})
            return True
    
    result = farthest >= len(nums) - 1
    
    if visualizer:
        visualizer.record("complete", f"Result: {'Can' if result else 'Cannot'} reach end",
                         state={"result": result, "farthest": farthest})
    
    return result


def gas_station(gas: list[int], cost: list[int],
                visualizer: GreedyVisualizer | None = None) -> int:
    """
    Find starting gas station to complete circular route.
    
    Greedy approach: If total gas >= total cost, solution exists.
    Start from the station after the one where we run out of gas.
    
    Args:
        gas: Gas available at each station
        cost: Cost to travel to next station
        visualizer: Optional visualizer for step tracking
    
    Returns:
        Starting station index, or -1 if impossible
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Example:
        >>> gas_station([1, 2, 3, 4, 5], [3, 4, 5, 1, 2])
        3
    """
    if visualizer:
        visualizer.record("init", f"Gas station problem with {len(gas)} stations",
                         state={"gas": gas, "cost": cost})
    
    total_tank = 0
    current_tank = 0
    start_station = 0
    
    for i in range(len(gas)):
        diff = gas[i] - cost[i]
        total_tank += diff
        current_tank += diff
        
        if visualizer:
            visualizer.record("visit", f"Station {i}: gas={gas[i]}, cost={cost[i]}, tank={current_tank}",
                             state={"station": i, "current_tank": current_tank, "start": start_station})
        
        if current_tank < 0:
            start_station = i + 1
            current_tank = 0
            
            if visualizer:
                visualizer.record("reset", f"Tank empty at {i}, try starting from {start_station}",
                                 choice=f"start_{start_station}",
                                 state={"new_start": start_station})
    
    result = start_station if total_tank >= 0 else -1
    
    if visualizer:
        if result >= 0:
            visualizer.record("complete", f"Start from station {result}",
                             state={"start_station": result, "total_tank": total_tank})
        else:
            visualizer.record("impossible", "Cannot complete circuit",
                             state={"total_tank": total_tank})
    
    return result


def demo() -> None:
    """Demonstrate greedy algorithms with visualization."""
    print("=" * 60)
    print("GREEDY ALGORITHMS DEMONSTRATION")
    print("=" * 60)
    
    print("\n1. ACTIVITY SELECTION")
    print("-" * 40)
    activities = [
        Activity("A1", 1, 4),
        Activity("A2", 3, 5),
        Activity("A3", 0, 6),
        Activity("A4", 5, 7),
        Activity("A5", 3, 9),
        Activity("A6", 5, 9),
    ]
    vis = GreedyVisualizer()
    selected = activity_selection(activities, vis)
    print(f"Activities: {[(a.name, a.start, a.end) for a in activities]}")
    print(f"Selected: {[a.name for a in selected]}")
    print(f"Count: {len(selected)}")
    
    print("\n2. COIN CHANGE (GREEDY)")
    print("-" * 40)
    vis = GreedyVisualizer()
    coins = coin_change_greedy(67, [25, 10, 5, 1], vis)
    print(f"Amount: 67 cents")
    print(f"Coins used: {coins}")
    print(f"Count: {len(coins)}")
    
    print("\n3. HUFFMAN ENCODING")
    print("-" * 40)
    frequencies = {'A': 5, 'B': 9, 'C': 12, 'D': 13, 'E': 16, 'F': 45}
    vis = GreedyVisualizer()
    codes = huffman_encoding(frequencies, vis)
    print(f"Frequencies: {frequencies}")
    print(f"Codes: {codes}")
    
    print("\n4. FRACTIONAL KNAPSACK")
    print("-" * 40)
    items = [(60, 10), (100, 20), (120, 30)]
    vis = GreedyVisualizer()
    max_value = fractional_knapsack(50, items, vis)
    print(f"Items (value, weight): {items}")
    print(f"Capacity: 50")
    print(f"Maximum value: {max_value}")
    
    print("\n5. JUMP GAME")
    print("-" * 40)
    nums = [2, 3, 1, 1, 4]
    vis = GreedyVisualizer()
    can_reach = jump_game(nums, vis)
    print(f"Array: {nums}")
    print(f"Can reach end: {can_reach}")
    
    nums = [3, 2, 1, 0, 4]
    vis = GreedyVisualizer()
    can_reach = jump_game(nums, vis)
    print(f"Array: {nums}")
    print(f"Can reach end: {can_reach}")
    
    print("\n6. GAS STATION")
    print("-" * 40)
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    vis = GreedyVisualizer()
    start = gas_station(gas, cost, vis)
    print(f"Gas: {gas}")
    print(f"Cost: {cost}")
    print(f"Start station: {start}")
    
    print("\n" + "=" * 60)


if __name__ == "__main__":
    demo()
