# 3D Generator Prompts: Stacks and Queues

These prompts are designed for use with 3D generation tools such as Three.js, WebGL, Blender scripting agents, or AI-powered 3D scene generators. Each prompt provides sufficient detail to create an educational, interactive 360-degree visualization.

---

## Prompt 1: Stack as Tower of Glowing Plates

Generate a 360-degree, interactive 3D scene showing a stack data structure as a tower of glowing translucent plates. The environment is a tall cylindrical chamber with dark walls (#1a1a2e) and vertical neon light strips.

Create a stack of 5 plates, each a flat disc (40cm diameter, 5cm thick) made of translucent glowing material (#4ecdc4 cyan). Each plate displays its value (numbers 10, 20, 30, 40, 50 from bottom to top) on the top surface in white holographic text. The plates are stacked vertically with 2cm gaps between them.

Include visual elements:
- A "TOP" arrow indicator pointing to the topmost plate
- A height meter on the side showing current stack size (5/10 capacity)
- Vertical guide rails suggesting the stack boundaries
- A platform base where the stack rests

**Push Animation**: Add a "Push" button. When clicked, prompt for a value, then:
1. A new plate materializes 50cm above the stack with a bright flash
2. The plate descends smoothly (400ms) onto the top
3. A subtle particle burst occurs on landing
4. The TOP arrow and height meter update

**Pop Animation**: Add a "Pop" button. When clicked:
1. The top plate glows brighter
2. The plate lifts off (300ms) while displaying its value prominently
3. The plate dissolves into cyan particles (500ms)
4. The TOP arrow and height meter update

**Peek Animation**: Add a "Peek" button that highlights the top plate and displays its value without removing it.

Include a "Stack Underflow" warning (red flash, error message) when popping from an empty stack. The camera can orbit 360 degrees and zoom. Add a code panel showing the current operation in Python syntax.

---

## Prompt 2: Queue as Elevator Waiting Line

Generate a 360-degree, interactive 3D scene showing a queue data structure as people waiting for an elevator in a futuristic lobby. The environment is a wide lobby space with a glowing purple floor path (#9b59b6) and sleek metallic walls.

Create a queue of 4 figures (stylized humanoid shapes like game pieces, 30cm tall) standing in a line. Each figure glows with a warm orange color (#f39c12) and has a floating number label above it (values: 10, 20, 30, 40 from front to back). The figures stand on circular floor markers along the glowing path.

At the front of the queue, place futuristic elevator doors (metallic silver, #bdc3c7) that can slide open. At the back, place an entry portal (glowing arch).

**Enqueue Animation**: Add an "Enqueue" button. When clicked, prompt for a value, then:
1. A new figure materializes at the entry portal with a flash
2. The figure walks forward (600ms) to join the back of the line
3. A new floor marker illuminates for the new position
4. Queue length counter updates

**Dequeue Animation**: Add a "Dequeue" button. When clicked:
1. The front figure highlights brighter
2. Elevator doors slide open (300ms)
3. The figure walks into the elevator (400ms)
4. Elevator doors close
5. All remaining figures step forward one position (400ms each, staggered)
6. Queue length counter updates

**Front Animation**: Add a "Front" button that highlights the front figure and displays its value without removing it.

Include "Queue Empty" message when dequeuing from empty queue. The camera can orbit and pan along the queue. Add FIFO label and comparison with stack's LIFO behavior.

---

## Prompt 3: Stack vs Queue Comparison

Generate a 360-degree, interactive 3D scene with a split view comparing stack and queue operations side by side. The left half shows the plate tower (stack), the right half shows the elevator queue.

Both structures start with the same 4 elements (values: A, B, C, D). The stack has plates labeled A (bottom) to D (top). The queue has figures labeled A (front) to D (back).

**Synchronized Operations**:
- Add an "Add E" button that simultaneously pushes E onto the stack and enqueues E into the queue
- Add a "Remove" button that simultaneously pops from the stack and dequeues from the queue

**Visual Comparison**:
After adding E and then removing one element:
- Stack removes E (last in, first out) - highlight this with "LIFO" label
- Queue removes A (first in, first out) - highlight this with "FIFO" label

Show the different results clearly with before/after states. Include a comparison panel:
- Stack: "Removed: E (most recent)"
- Queue: "Removed: A (oldest)"

The camera can view both structures or focus on one. Add educational labels explaining when to use each structure. Include step-by-step replay controls.

---

## Prompt 4: Call Stack During Recursion

Generate a 360-degree, interactive 3D scene showing the call stack during recursive function execution. The environment is a debugging console aesthetic with dark background and code panels.

Visualize the call stack for calculating factorial(4). Each stack frame is a larger plate (60cm x 40cm, 8cm thick) with:
- Function name: "factorial"
- Parameter value: n = 4, 3, 2, 1, 0
- Local variables section
- Return address indicator

**Animation Sequence**:
1. factorial(4) frame pushes onto empty stack
2. factorial(3) frame pushes (recursive call)
3. factorial(2) frame pushes
4. factorial(1) frame pushes
5. factorial(0) frame pushes - BASE CASE highlighted
6. factorial(0) returns 1 - frame pops, return value floats up
7. factorial(1) computes 1*1=1, returns - frame pops
8. factorial(2) computes 2*1=2, returns - frame pops
9. factorial(3) computes 3*2=6, returns - frame pops
10. factorial(4) computes 4*6=24, returns - final result displayed

Show the return values floating upward and being "caught" by the frame below. Include a code panel with the recursive function, highlighting the current line of execution.

Add controls: play/pause, step forward/backward, speed adjustment. Show stack depth indicator and "Stack Overflow Warning Zone" at the top of the chamber.

---

## Prompt 5: Postfix Expression Evaluation

Generate a 360-degree, interactive 3D scene showing postfix expression evaluation using a stack. The expression to evaluate is "3 4 + 2 * 7 /" (result: 2).

Create a conveyor belt on the left carrying expression tokens toward the stack tower on the right. Tokens are:
- Numbers (3, 4, 2, 7): Cubic blocks with the number displayed
- Operators (+, *, /): Flat circular tokens with the symbol

**Evaluation Animation**:
1. Token "3" arrives, transforms into plate, pushes onto stack
2. Token "4" arrives, transforms into plate, pushes onto stack
3. Token "+" arrives:
   - Top two plates (4, 3) pop off and float beside the operator
   - Visual calculation: 3 + 4 = 7
   - Result plate (7) pushes onto stack
4. Token "2" arrives, pushes onto stack
5. Token "*" arrives:
   - Plates (2, 7) pop, calculate 7 * 2 = 14
   - Result plate (14) pushes
6. Token "7" arrives, pushes onto stack
7. Token "/" arrives:
   - Plates (7, 14) pop, calculate 14 / 7 = 2
   - Result plate (2) pushes
8. Final result: Single plate showing "2" with celebration effect

Include a running calculation display showing the current stack state and operation. Add step-by-step controls and the ability to input custom expressions.

---

## Prompt 6: BFS Using Queue

Generate a 360-degree, interactive 3D scene showing Breadth-First Search using a queue. The upper portion shows a graph with 7 nodes (labeled A-G) connected by edges. The lower portion shows the queue lobby.

Graph structure:
- A connects to B, C
- B connects to D, E
- C connects to F
- D connects to G

**BFS Animation from node A**:
1. Node A highlights (start), enqueues into queue
2. Dequeue A, mark as visited (change color to green)
3. A's neighbors B, C enqueue (join queue)
4. Dequeue B, mark visited
5. B's unvisited neighbors D, E enqueue
6. Dequeue C, mark visited
7. C's unvisited neighbor F enqueues
8. Continue until queue is empty

**Visual Elements**:
- Unvisited nodes: Gray
- In queue (frontier): Orange
- Visited: Green
- Current processing: Bright white

Show the "wavefront" of BFS - nodes at the same distance from start have the same discovery time. Include a level indicator showing BFS levels (0, 1, 2, 3).

Add a traversal order display showing the sequence: A, B, C, D, E, F, G. Include comparison note: "Queue ensures level-by-level exploration (BFS). Stack would give depth-first exploration (DFS)."

---

## General Requirements for All Prompts

- All scenes must support 360-degree camera orbit and zoom in/out functionality
- Include educational labels with readable fonts (minimum 14pt equivalent in 3D space)
- Use color coding consistently across all scenes as defined in the color palette
- Ensure interactive elements have clear hover states and click feedback
- Animations should be smooth (60fps target) with adjustable speed controls
- Include accessibility considerations: high contrast mode option, colorblind-friendly palette alternative
- All text labels should remain readable from any camera angle (billboard text or smart orientation)
- Export scenes in formats compatible with web embedding (glTF, WebGL-ready)
- Include corresponding Python code snippets that highlight during relevant animation steps
- Add sound effects for push/pop/enqueue/dequeue operations (optional toggle)
