# Time Complexity and Recursion

Welcome to the first world of your Data Structures and Algorithms journey. This foundational module introduces you to the essential concepts of measuring algorithm efficiency and understanding recursive problem-solving, visualized as a futuristic time-space observatory.

## Concept Overview

Time complexity describes how the runtime of an algorithm grows as the input size increases. Rather than measuring actual seconds, we use Big O notation to express the upper bound of growth rates. This abstraction allows us to compare algorithms independently of hardware or implementation details.

Recursion is a programming technique where a function calls itself to solve smaller instances of the same problem. Every recursive solution has a base case that stops the recursion and a recursive case that breaks the problem into smaller pieces. Understanding recursion is crucial because many advanced algorithms and data structures rely on recursive thinking.

## Learning Objectives

- Understand Big O notation and analyze the time complexity of simple algorithms
- Distinguish between constant, logarithmic, linear, quadratic, and exponential time complexities
- Write recursive functions with proper base cases and recursive cases
- Trace through recursive call stacks and understand how memory is used
- Convert between iterative and recursive implementations

## The 3D Metaphor: Time-Space Observatory

Imagine yourself inside a vast cosmic observatory floating in space. The observatory contains multiple chambers, each representing a different time complexity class. In the center stands a massive holographic clock whose hands move at different speeds depending on which complexity chamber you enter.

The O(1) chamber is a small, stable room where the clock barely moves regardless of how many stars (data points) appear outside. The O(n) chamber stretches into a long corridor where each additional star causes the clock to tick once more. The O(n²) chamber expands into a square arena where stars form a grid, and the clock accelerates dramatically as the grid grows. The O(log n) chamber features a binary tree of platforms that you descend through, halving your choices at each level while the clock ticks slowly.

For recursion, picture a tower of mirrors where each mirror reflects a slightly smaller version of yourself. As you solve a problem, you step into the mirror, becoming the smaller reflection that solves a simpler version. When the smallest reflection reaches the base case, the solutions cascade back up through the mirrors until you receive the final answer.

## How This Maps to the 3D World

When you run the Python code in this module, each operation corresponds to a visual event in the observatory. A single array access lights up one star in the O(1) chamber. A loop through n elements causes n stars to pulse sequentially in the O(n) corridor. Nested loops create expanding wavefronts across the O(n²) arena. Recursive calls manifest as stepping through successive mirrors in the recursion tower, with the call stack visualized as the chain of reflections leading back to you.

## Exercises

1. **Complexity Classification**: Given the following code snippet, determine its time complexity and explain your reasoning:
   ```python
   def mystery(arr):
       total = 0
       for i in range(len(arr)):
           for j in range(i, len(arr)):
               total += arr[j]
       return total
   ```

2. **Recursive Thinking**: Write a recursive function to calculate the sum of digits in a positive integer. For example, `sum_digits(1234)` should return `10`. Identify the base case and recursive case before coding.

3. **Iteration to Recursion**: Convert the following iterative function to a recursive one:
   ```python
   def factorial_iterative(n):
       result = 1
       for i in range(1, n + 1):
           result *= i
       return result
   ```
