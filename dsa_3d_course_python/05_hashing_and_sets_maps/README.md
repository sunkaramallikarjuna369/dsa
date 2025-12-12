# Hashing and Sets/Maps

Welcome to the Hashing world, where you will explore one of the most powerful techniques in computer science for achieving near-constant time lookups. This module visualizes hash tables as glowing honeycomb grids of buckets, making collision handling and hash distribution intuitive.

## Concept Overview

Hashing is a technique that maps data of arbitrary size to fixed-size values, enabling extremely fast data retrieval. A hash table uses a hash function to compute an index into an array of buckets, from which the desired value can be found.

The key insight is that instead of searching through all elements (O(n) for arrays), we can compute exactly where an element should be stored or found (O(1) average case). This makes hash tables ideal for implementing dictionaries, sets, caches, and many other data structures.

However, hash tables face a fundamental challenge: collisions. When two different keys hash to the same index, we need a strategy to handle this. The two main approaches are separate chaining (storing multiple elements in each bucket using a linked list) and open addressing (finding another empty slot using probing).

Understanding load factor (ratio of elements to buckets) is crucial for maintaining performance. As the load factor increases, collisions become more frequent, degrading performance. Good hash tables resize dynamically to keep the load factor reasonable.

## Learning Objectives

- Understand how hash functions map keys to array indices
- Implement a hash table with separate chaining for collision resolution
- Implement a hash table with open addressing (linear and quadratic probing)
- Analyze the relationship between load factor and performance
- Use Python's built-in dict and set effectively for common operations

## The 3D Metaphor: Honeycomb Grid of Glowing Buckets

**Hash Table as Honeycomb**: Imagine a 3D honeycomb structure where each hexagonal cell is a bucket. The cells glow with different intensities based on how many elements they contain. Empty cells are dim, cells with one element glow softly, and cells with multiple elements (collisions) glow brighter with visible chains extending from them.

**Hash Function as Light Beam**: When inserting a key, a beam of light shoots from the key through a prism (the hash function) and lands on a specific bucket. The prism transforms the key into a bucket index, visualizing how different keys map to different locations.

**Separate Chaining**: When collisions occur, small glowing orbs chain together extending outward from the bucket, like a string of pearls. Each orb represents an element that hashed to the same bucket.

**Open Addressing**: When a collision occurs with open addressing, the light beam bounces to the next available bucket, leaving a trail showing the probing sequence. Linear probing creates straight trails, while quadratic probing creates curved, expanding trails.

## How This Maps to the 3D World

When you call `hash_table.insert(key, value)`, the visualization shows the key passing through the hash function prism, the resulting beam landing on a bucket, and either the element settling into an empty bucket or joining a chain (chaining) or bouncing to find an empty slot (open addressing).

When you call `hash_table.get(key)`, the same beam traces the path to the bucket, then searches through any chain or follows the probing sequence until the key is found or confirmed absent.

The load factor is displayed as a meter showing how full the table is. When it exceeds a threshold, a resize animation shows all elements being rehashed into a larger honeycomb structure.

## Exercises

1. **Two Sum with Hash Map**: Given an array of integers and a target sum, find two numbers that add up to the target. Return their indices. Use a hash map to achieve O(n) time complexity instead of the naive O(n^2) approach.

2. **First Non-Repeating Character**: Given a string, find the first character that appears only once. Use a hash map to count character frequencies, then scan the string again to find the first character with count 1.

3. **Group Anagrams**: Given a list of strings, group the anagrams together. Two strings are anagrams if they contain the same characters in different orders. Use a hash map where the key is the sorted characters of each string.
