# 3D Generator Prompts: Linked Lists

These prompts are designed for use with 3D generation tools such as Three.js, WebGL, Blender scripting agents, or AI-powered 3D scene generators. Each prompt provides sufficient detail to create an educational, interactive 360-degree visualization.

---

## Prompt 1: Singly Linked List Structure

Generate a 360-degree, interactive 3D scene showing a singly linked list floating in deep space. The background is a dark void (#0a0a14) with subtle purple nebula effects and distant twinkling stars.

Create 6 nodes represented as glowing cyan spheres (#4ecdc4) of 40cm diameter, floating at varying heights and distances to emphasize non-contiguous memory. Each sphere contains a holographic number display showing values: 10, 20, 30, 40, 50, 60.

Connect the nodes with luminous cyan chains (#00d4ff) that have directional flow indicated by small glowing particles traveling along the chain from source to destination. Each chain should have subtle arrow indicators showing the one-way direction.

Include a "HEAD" anchor platform (golden yellow, #f1c40f) positioned to the left of the first node, with a prominent chain connecting to node 1 (value 10). The last node's chain ends in a small dim gray orb (#555555) labeled "None" representing the null terminator.

The camera can orbit 360 degrees around the entire structure. Clicking any node displays a tooltip showing "Value: X, Address: 0xNNNN" (generate random hex addresses). Add a "Traverse" button that, when clicked, sends a white pulse of light along the chains from head to tail, briefly illuminating each node as it passes.

Include a side panel showing the Python class structure:
```
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
```

---

## Prompt 2: Doubly Linked List Comparison

Generate a 360-degree, interactive 3D scene comparing singly and doubly linked lists side by side. The scene is split into two regions in the same space environment.

**Left Region - Singly Linked List**: 4 nodes (values: A, B, C, D) connected by single cyan chains (#00d4ff) pointing forward only. Include HEAD anchor.

**Right Region - Doubly Linked List**: 4 nodes (values: A, B, C, D) connected by dual chains:
- Forward chains in cyan (#00d4ff) pointing to next
- Backward chains in magenta (#e91e63) pointing to prev

The doubly linked list has both HEAD (golden, #f1c40f) and TAIL (silver, #bdc3c7) anchor platforms.

Include interactive traversal buttons:
- "Forward Traverse" - sends cyan pulse from head to tail
- "Backward Traverse" (only for doubly linked) - sends magenta pulse from tail to head

When hovering over a node in the doubly linked list, zoom to show its internal structure: a central value display with two pointer indicators (prev arrow pointing left, next arrow pointing right).

Add a comparison panel showing:
- Singly: O(1) insert at head, O(n) insert at tail, O(n) delete, forward traversal only
- Doubly: O(1) insert at head/tail, O(1) delete with node reference, bidirectional traversal

The camera can orbit around both structures. Include a toggle to view them overlaid or separated.

---

## Prompt 3: Linked List Insertion Operations

Generate a 360-degree, interactive 3D scene demonstrating three types of insertion in a singly linked list. Start with a list of 4 nodes (values: 10, 20, 30, 40) floating in space with HEAD anchor.

**Insert at Head Animation** (insert value 5):
1. New node (value 5) materializes with a bright green flash (#2ecc71) near the HEAD anchor
2. The chain from HEAD to node(10) detaches with spark particles
3. New chain grows from HEAD to new node(5)
4. New chain grows from node(5) to node(10)
5. Structure smoothly repositions to accommodate new node
6. Display: "Insert at Head: O(1)"

**Insert at Tail Animation** (insert value 50):
1. White traversal pulse travels from HEAD through all nodes to the tail
2. New node(50) materializes beyond node(40) with green flash
3. The null terminator on node(40) fades
4. New chain grows from node(40) to node(50)
5. New null terminator appears after node(50)
6. Display: "Insert at Tail: O(n) - must traverse to find tail"

**Insert in Middle Animation** (insert value 25 after node 20):
1. Traversal pulse travels from HEAD, stopping at node(20)
2. Node(20) highlights as insertion point
3. Chain from node(20) to node(30) breaks with sparks
4. New node(25) materializes between them with green flash
5. New chain grows from node(20) to node(25)
6. New chain grows from node(25) to node(30)
7. Display: "Insert in Middle: O(n) - must traverse to position"

Include buttons to trigger each animation, a reset button, and step-by-step controls. The camera should follow the action, focusing on the relevant nodes during each operation.

---

## Prompt 4: Linked List Deletion Operations

Generate a 360-degree, interactive 3D scene demonstrating deletion operations in a singly linked list. Start with a list of 5 nodes (values: 10, 20, 30, 40, 50) with HEAD anchor.

**Delete Head Animation** (delete node 10):
1. Node(10) highlights in red (#e74c3c)
2. Chain from HEAD to node(10) detaches
3. Chain from node(10) to node(20) detaches
4. New chain grows directly from HEAD to node(20)
5. Node(10) fades to transparent and slowly drifts away (garbage collection)
6. Display: "Delete Head: O(1)"

**Delete Middle Animation** (delete node 30):
1. Traversal pulse travels from HEAD, stopping at node(20)
2. Node(30) highlights in red
3. Chain from node(20) to node(30) detaches
4. Chain from node(30) to node(40) detaches
5. New chain grows from node(20) directly to node(40)
6. Node(30) fades and drifts away
7. Display: "Delete Middle: O(n) - must find previous node"

**Delete Tail Animation** (delete node 50):
1. Traversal pulse travels through entire list to node(40)
2. Node(50) highlights in red
3. Chain from node(40) to node(50) detaches
4. Null terminator attaches to node(40)
5. Node(50) fades and drifts away
6. Display: "Delete Tail: O(n) - must find second-to-last"

Include a "Garbage Collection Zone" in the corner where deleted nodes drift to before disappearing completely. Add operation buttons, reset, and step controls. Show memory being "freed" as nodes disappear.

---

## Prompt 5: Linked List Reversal Algorithm

Generate a 360-degree, interactive 3D scene showing the in-place reversal of a singly linked list. Start with 5 nodes (values: 1, 2, 3, 4, 5) arranged left-to-right with HEAD anchor on the left.

Visualize three pointer variables as colored markers:
- `prev` pointer: Red marker, starts at None (off to the side)
- `curr` pointer: Green marker, starts at node(1)
- `next_temp` pointer: Blue marker, used to save next reference

**Reversal Animation Step-by-Step**:

Step 1: Initial state
- prev = None (red marker in void)
- curr = node(1) (green marker on node 1)
- Show all chains pointing right

Step 2: Save next, reverse link
- next_temp = node(2) (blue marker on node 2)
- Chain from node(1) breaks from node(2)
- New chain forms from node(1) pointing left to None
- Display: "curr.next = prev"

Step 3: Advance pointers
- prev moves to node(1)
- curr moves to node(2)
- next_temp moves to node(3)

Continue steps until curr reaches None, showing each chain reversing direction.

Final state: HEAD anchor now connects to node(5), all chains point left, node(1) points to None.

Include a code panel showing the Python algorithm with the current line highlighted:
```python
def reverse(head):
    prev = None
    curr = head
    while curr:
        next_temp = curr.next
        curr.next = prev  # Reverse the link
        prev = curr
        curr = next_temp
    return prev
```

Add play/pause, step forward/backward, speed control, and reset buttons.

---

## Prompt 6: Cycle Detection (Floyd's Tortoise and Hare)

Generate a 360-degree, interactive 3D scene demonstrating Floyd's cycle detection algorithm. Create a linked list with a cycle: nodes 1, 2, 3, 4, 5, 6 where node 6's next pointer connects back to node 3, forming a loop.

Arrange the non-cyclic portion (nodes 1, 2) in a line, then arrange the cyclic portion (nodes 3, 4, 5, 6) in a circular formation to make the loop visually obvious. The chain from node 6 visibly curves back to connect to node 3. Mark the cycle entry point (node 3) with a special indicator.

Create two traversal markers:
- **Tortoise**: A green glowing orb (#27ae60) that moves 1 node per step
- **Hare**: An orange glowing orb (#f39c12) that moves 2 nodes per step

**Animation Sequence**:
1. Both markers start at HEAD (node 1)
2. Step 1: Tortoise moves to node 2, Hare moves to node 3
3. Step 2: Tortoise moves to node 3, Hare moves to node 5
4. Step 3: Tortoise moves to node 4, Hare moves to node 3 (wrapped around)
5. Continue until they meet...
6. When markers occupy the same node, both flash brightly and text displays "CYCLE DETECTED!"

Include a step counter for each marker, showing their positions. Add a panel explaining the algorithm:
- "Tortoise moves 1 step at a time"
- "Hare moves 2 steps at a time"
- "If there's a cycle, they will eventually meet"
- "If no cycle, hare reaches None first"

Add a toggle to switch between "Cyclic List" and "Normal List" (where node 6 points to None) to demonstrate both outcomes. Include play/pause, step controls, and speed adjustment.

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
- Node addresses should be displayed as hexadecimal values for realism
