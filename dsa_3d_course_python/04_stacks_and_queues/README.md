# Stacks and Queues

Welcome to the Stacks and Queues world, where you will explore two fundamental abstract data types that control the order of element access. This module visualizes stacks as glowing plates and queues as elevator waiting lines, making these ordering concepts intuitive and memorable.

## Concept Overview

Stacks and queues are abstract data types that restrict how elements are added and removed, enforcing specific ordering disciplines that prove invaluable in countless algorithms and real-world applications.

A stack follows the Last-In-First-Out (LIFO) principle: the most recently added element is the first to be removed. Think of a stack of plates where you can only add or remove from the top. This simple constraint makes stacks perfect for tracking function calls, implementing undo operations, parsing expressions, and solving problems that require backtracking.

A queue follows the First-In-First-Out (FIFO) principle: the first element added is the first to be removed. Think of a line of people waiting for an elevator where the person who arrived first boards first. Queues are essential for breadth-first search, task scheduling, buffering data streams, and any scenario requiring fair ordering.

Both structures can be implemented using arrays or linked lists, each with different performance characteristics. Understanding when to use each implementation is key to writing efficient code.

## Learning Objectives

- Understand the LIFO principle of stacks and implement push, pop, and peek operations
- Understand the FIFO principle of queues and implement enqueue, dequeue, and front operations
- Recognize common applications of stacks including expression evaluation and backtracking
- Recognize common applications of queues including BFS and task scheduling
- Implement both array-based and linked-list-based versions of stacks and queues

## The 3D Metaphor: Glowing Plates and Elevator Queues

**Stack - Tower of Glowing Plates**: Imagine a vertical tower where glowing translucent plates stack on top of each other. Each plate represents an element, with its value displayed on the surface. When you push a new element, a plate materializes above the tower and descends onto the top. When you pop, the top plate lifts off and dissolves. You can only interact with the topmost plate, emphasizing the LIFO nature.

**Queue - Elevator Waiting Line**: Picture a futuristic building lobby with a glowing floor path leading to an elevator. People (represented as glowing figures) enter the queue from one end and exit through the elevator at the other end. New arrivals join at the back of the line, while the person at the front boards the elevator first. The line moves forward as each person departs, visualizing the FIFO principle.

The contrast between vertical (stack) and horizontal (queue) arrangements reinforces the different access patterns. The stack's restricted top-only access versus the queue's two-ended operation becomes visually obvious.

## How This Maps to the 3D World

For stacks, each Python operation corresponds to a plate animation. Calling `push(value)` creates a new glowing plate that descends onto the stack. Calling `pop()` lifts the top plate, displays its value, and dissolves it. Calling `peek()` illuminates the top plate without removing it. The stack height visually represents the current size.

For queues, `enqueue(value)` creates a new figure that walks to the back of the line. `dequeue()` has the front figure step into the elevator and disappear. `front()` highlights the first figure in line. The queue length is visible as the number of figures waiting.

Special visualizations show the call stack during recursion (nested function calls as stacked plates) and BFS traversal (nodes being added to and removed from the queue).

## Exercises

1. **Valid Parentheses**: Given a string containing only parentheses `()`, brackets `[]`, and braces `{}`, determine if the input string is valid. A string is valid if every opening bracket has a corresponding closing bracket of the same type, and brackets are closed in the correct order. Use a stack to solve this.

2. **Implement Queue Using Stacks**: Implement a queue data structure using only two stacks. The queue should support enqueue, dequeue, and front operations. Think about when to transfer elements between stacks.

3. **Sliding Window Maximum**: Given an array and a window size k, find the maximum element in each window as it slides from left to right. Consider using a deque (double-ended queue) to solve this efficiently in O(n) time.
