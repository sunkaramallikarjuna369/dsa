"""
Hash Table Module

This module provides implementations of hash table data structures
with step-by-step tracking for 3D visualization synchronization.

Includes both separate chaining and open addressing implementations.
"""

from typing import Any, TypeVar, Generic
from dataclasses import dataclass, field

K = TypeVar('K')
V = TypeVar('V')


@dataclass
class HashStep:
    """Represents a single step in hash table visualization."""
    step_number: int
    operation: str
    description: str
    key: Any = None
    value: Any = None
    hash_value: int | None = None
    bucket_index: int | None = None
    probe_sequence: list[int] = field(default_factory=list)
    collision: bool = False
    load_factor: float = 0.0


class HashTableChaining(Generic[K, V]):
    """
    Hash table implementation using separate chaining for collision resolution.
    
    Each bucket contains a list of (key, value) pairs.
    Average case: O(1) for insert, search, delete.
    Worst case: O(n) when all keys hash to the same bucket.
    """
    
    def __init__(self, initial_capacity: int = 16, load_factor_threshold: float = 0.75) -> None:
        """
        Initialize hash table with separate chaining.
        
        Args:
            initial_capacity: Initial number of buckets
            load_factor_threshold: Threshold for triggering resize
        """
        self._capacity = initial_capacity
        self._size = 0
        self._load_factor_threshold = load_factor_threshold
        self._buckets: list[list[tuple[K, V]]] = [[] for _ in range(initial_capacity)]
        self._steps: list[HashStep] = []
        self._step_count = 0
    
    def _record_step(
        self,
        operation: str,
        description: str,
        key: Any = None,
        value: Any = None,
        hash_value: int | None = None,
        bucket_index: int | None = None,
        probe_sequence: list[int] | None = None,
        collision: bool = False
    ) -> None:
        """Record a visualization step."""
        self._step_count += 1
        step = HashStep(
            step_number=self._step_count,
            operation=operation,
            description=description,
            key=key,
            value=value,
            hash_value=hash_value,
            bucket_index=bucket_index,
            probe_sequence=probe_sequence or [],
            collision=collision,
            load_factor=self.load_factor
        )
        self._steps.append(step)
    
    def clear_steps(self) -> None:
        """Clear recorded steps."""
        self._steps = []
        self._step_count = 0
    
    @property
    def steps(self) -> list[HashStep]:
        """Return all recorded steps."""
        return self._steps
    
    @property
    def load_factor(self) -> float:
        """Return current load factor."""
        return self._size / self._capacity
    
    def _hash(self, key: K) -> int:
        """Compute hash value for a key."""
        return hash(key) % self._capacity
    
    def put(self, key: K, value: V) -> None:
        """
        Insert or update a key-value pair.
        
        Time Complexity: O(1) average, O(n) worst case
        """
        hash_value = hash(key)
        bucket_index = hash_value % self._capacity
        
        self._record_step(
            "hash_compute",
            f"Computing hash for key '{key}': hash={hash_value}, bucket={bucket_index}",
            key=key,
            value=value,
            hash_value=hash_value,
            bucket_index=bucket_index
        )
        
        bucket = self._buckets[bucket_index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                self._record_step(
                    "update",
                    f"Key '{key}' already exists, updating value to {value}",
                    key=key,
                    value=value,
                    bucket_index=bucket_index
                )
                return
        
        collision = len(bucket) > 0
        if collision:
            self._record_step(
                "collision",
                f"Collision at bucket {bucket_index}! Adding to chain (length: {len(bucket) + 1})",
                key=key,
                value=value,
                bucket_index=bucket_index,
                collision=True
            )
        
        bucket.append((key, value))
        self._size += 1
        
        self._record_step(
            "insert",
            f"Inserted ({key}, {value}) at bucket {bucket_index}",
            key=key,
            value=value,
            bucket_index=bucket_index
        )
        
        if self.load_factor > self._load_factor_threshold:
            self._resize()
    
    def get(self, key: K) -> V | None:
        """
        Retrieve value for a key.
        
        Time Complexity: O(1) average, O(n) worst case
        """
        hash_value = hash(key)
        bucket_index = hash_value % self._capacity
        
        self._record_step(
            "hash_compute",
            f"Looking up key '{key}': hash={hash_value}, bucket={bucket_index}",
            key=key,
            hash_value=hash_value,
            bucket_index=bucket_index
        )
        
        bucket = self._buckets[bucket_index]
        
        for i, (k, v) in enumerate(bucket):
            self._record_step(
                "chain_search",
                f"Checking chain position {i}: key='{k}'",
                key=k,
                bucket_index=bucket_index
            )
            if k == key:
                self._record_step(
                    "found",
                    f"Found key '{key}' with value {v}",
                    key=key,
                    value=v,
                    bucket_index=bucket_index
                )
                return v
        
        self._record_step(
            "not_found",
            f"Key '{key}' not found in bucket {bucket_index}",
            key=key,
            bucket_index=bucket_index
        )
        return None
    
    def remove(self, key: K) -> V | None:
        """
        Remove a key-value pair.
        
        Time Complexity: O(1) average, O(n) worst case
        """
        bucket_index = self._hash(key)
        bucket = self._buckets[bucket_index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self._size -= 1
                self._record_step(
                    "remove",
                    f"Removed key '{key}' from bucket {bucket_index}",
                    key=key,
                    value=v,
                    bucket_index=bucket_index
                )
                return v
        
        return None
    
    def _resize(self) -> None:
        """Double the capacity and rehash all elements."""
        old_buckets = self._buckets
        old_capacity = self._capacity
        
        self._capacity *= 2
        self._buckets = [[] for _ in range(self._capacity)]
        self._size = 0
        
        self._record_step(
            "resize_start",
            f"Resizing from {old_capacity} to {self._capacity} buckets"
        )
        
        for bucket in old_buckets:
            for key, value in bucket:
                self.put(key, value)
        
        self._record_step(
            "resize_complete",
            f"Resize complete. New load factor: {self.load_factor:.2f}"
        )
    
    def __len__(self) -> int:
        return self._size
    
    def __contains__(self, key: K) -> bool:
        return self.get(key) is not None
    
    def keys(self) -> list[K]:
        """Return all keys."""
        result: list[K] = []
        for bucket in self._buckets:
            for key, _ in bucket:
                result.append(key)
        return result
    
    def values(self) -> list[V]:
        """Return all values."""
        result: list[V] = []
        for bucket in self._buckets:
            for _, value in bucket:
                result.append(value)
        return result
    
    def items(self) -> list[tuple[K, V]]:
        """Return all key-value pairs."""
        result: list[tuple[K, V]] = []
        for bucket in self._buckets:
            result.extend(bucket)
        return result
    
    def bucket_sizes(self) -> list[int]:
        """Return the size of each bucket (for visualization)."""
        return [len(bucket) for bucket in self._buckets]


class HashTableOpenAddressing(Generic[K, V]):
    """
    Hash table implementation using open addressing with linear probing.
    
    Each bucket holds at most one element.
    When collision occurs, probe for next empty slot.
    """
    
    DELETED = object()  # Sentinel for deleted entries
    
    def __init__(self, initial_capacity: int = 16, load_factor_threshold: float = 0.5) -> None:
        """
        Initialize hash table with open addressing.
        
        Args:
            initial_capacity: Initial number of buckets
            load_factor_threshold: Threshold for triggering resize (lower for open addressing)
        """
        self._capacity = initial_capacity
        self._size = 0
        self._load_factor_threshold = load_factor_threshold
        self._keys: list[K | None | object] = [None] * initial_capacity
        self._values: list[V | None] = [None] * initial_capacity
        self._steps: list[HashStep] = []
        self._step_count = 0
    
    def _record_step(
        self,
        operation: str,
        description: str,
        key: Any = None,
        value: Any = None,
        hash_value: int | None = None,
        bucket_index: int | None = None,
        probe_sequence: list[int] | None = None,
        collision: bool = False
    ) -> None:
        """Record a visualization step."""
        self._step_count += 1
        step = HashStep(
            step_number=self._step_count,
            operation=operation,
            description=description,
            key=key,
            value=value,
            hash_value=hash_value,
            bucket_index=bucket_index,
            probe_sequence=probe_sequence or [],
            collision=collision,
            load_factor=self.load_factor
        )
        self._steps.append(step)
    
    def clear_steps(self) -> None:
        """Clear recorded steps."""
        self._steps = []
        self._step_count = 0
    
    @property
    def steps(self) -> list[HashStep]:
        """Return all recorded steps."""
        return self._steps
    
    @property
    def load_factor(self) -> float:
        """Return current load factor."""
        return self._size / self._capacity
    
    def _hash(self, key: K) -> int:
        """Compute initial hash value."""
        return hash(key) % self._capacity
    
    def _probe(self, key: K, for_insert: bool = False) -> tuple[int, list[int]]:
        """
        Linear probing to find slot for key.
        
        Args:
            key: The key to find slot for
            for_insert: If True, find empty slot; if False, find existing key
            
        Returns:
            Tuple of (final_index, probe_sequence)
        """
        index = self._hash(key)
        probe_sequence = [index]
        
        for _ in range(self._capacity):
            current_key = self._keys[index]
            
            if for_insert:
                if current_key is None or current_key is self.DELETED:
                    return index, probe_sequence
                if current_key == key:
                    return index, probe_sequence
            else:
                if current_key is None:
                    return -1, probe_sequence
                if current_key == key:
                    return index, probe_sequence
            
            index = (index + 1) % self._capacity
            probe_sequence.append(index)
        
        return -1, probe_sequence
    
    def put(self, key: K, value: V) -> None:
        """
        Insert or update a key-value pair using linear probing.
        
        Time Complexity: O(1) average, O(n) worst case
        """
        if self.load_factor > self._load_factor_threshold:
            self._resize()
        
        initial_hash = self._hash(key)
        index, probe_sequence = self._probe(key, for_insert=True)
        
        collision = len(probe_sequence) > 1
        
        self._record_step(
            "hash_compute",
            f"Hash for '{key}': initial bucket={initial_hash}",
            key=key,
            value=value,
            hash_value=hash(key),
            bucket_index=initial_hash,
            probe_sequence=probe_sequence,
            collision=collision
        )
        
        if collision:
            self._record_step(
                "probe",
                f"Collision! Probing sequence: {probe_sequence}",
                key=key,
                probe_sequence=probe_sequence,
                collision=True
            )
        
        if self._keys[index] != key:
            self._size += 1
        
        self._keys[index] = key
        self._values[index] = value
        
        self._record_step(
            "insert",
            f"Inserted ({key}, {value}) at bucket {index}",
            key=key,
            value=value,
            bucket_index=index,
            probe_sequence=probe_sequence
        )
    
    def get(self, key: K) -> V | None:
        """
        Retrieve value for a key using linear probing.
        
        Time Complexity: O(1) average, O(n) worst case
        """
        index, probe_sequence = self._probe(key, for_insert=False)
        
        self._record_step(
            "lookup",
            f"Looking up '{key}': probe sequence {probe_sequence}",
            key=key,
            probe_sequence=probe_sequence
        )
        
        if index == -1:
            self._record_step(
                "not_found",
                f"Key '{key}' not found",
                key=key
            )
            return None
        
        value = self._values[index]
        self._record_step(
            "found",
            f"Found '{key}' at bucket {index} with value {value}",
            key=key,
            value=value,
            bucket_index=index
        )
        return value
    
    def remove(self, key: K) -> V | None:
        """
        Remove a key-value pair (mark as deleted).
        
        Time Complexity: O(1) average, O(n) worst case
        """
        index, _ = self._probe(key, for_insert=False)
        
        if index == -1:
            return None
        
        value = self._values[index]
        self._keys[index] = self.DELETED
        self._values[index] = None
        self._size -= 1
        
        self._record_step(
            "remove",
            f"Removed '{key}' from bucket {index}",
            key=key,
            value=value,
            bucket_index=index
        )
        
        return value
    
    def _resize(self) -> None:
        """Double capacity and rehash all elements."""
        old_keys = self._keys
        old_values = self._values
        old_capacity = self._capacity
        
        self._capacity *= 2
        self._keys = [None] * self._capacity
        self._values = [None] * self._capacity
        self._size = 0
        
        self._record_step(
            "resize_start",
            f"Resizing from {old_capacity} to {self._capacity} buckets"
        )
        
        for i in range(old_capacity):
            if old_keys[i] is not None and old_keys[i] is not self.DELETED:
                self.put(old_keys[i], old_values[i])  # type: ignore
        
        self._record_step(
            "resize_complete",
            f"Resize complete. New load factor: {self.load_factor:.2f}"
        )
    
    def __len__(self) -> int:
        return self._size
    
    def __contains__(self, key: K) -> bool:
        return self.get(key) is not None


def demo() -> None:
    """Run demonstrations of hash table operations."""
    print("\n" + "="*60)
    print("HASH TABLE DEMONSTRATIONS")
    print("="*60)
    
    # Separate Chaining
    print("\n--- Hash Table with Separate Chaining ---")
    ht_chain = HashTableChaining[str, int](initial_capacity=8)
    
    keys = ["apple", "banana", "cherry", "date", "elderberry", "fig"]
    for i, key in enumerate(keys):
        ht_chain.put(key, i * 10)
        print(f"Inserted '{key}': {i * 10}")
    
    print(f"\nBucket sizes: {ht_chain.bucket_sizes()}")
    print(f"Load factor: {ht_chain.load_factor:.2f}")
    
    print(f"\nLookup 'cherry': {ht_chain.get('cherry')}")
    print(f"Lookup 'grape': {ht_chain.get('grape')}")
    
    # Open Addressing
    print("\n--- Hash Table with Open Addressing (Linear Probing) ---")
    ht_open = HashTableOpenAddressing[str, int](initial_capacity=8)
    
    for i, key in enumerate(keys):
        ht_open.put(key, i * 10)
        print(f"Inserted '{key}': {i * 10}")
    
    print(f"\nLoad factor: {ht_open.load_factor:.2f}")
    print(f"Lookup 'cherry': {ht_open.get('cherry')}")
    
    # Show steps for visualization
    print("\n--- Visualization Steps (last few) ---")
    for step in ht_chain.steps[-5:]:
        print(f"Step {step.step_number}: [{step.operation}] {step.description}")


if __name__ == "__main__":
    demo()
