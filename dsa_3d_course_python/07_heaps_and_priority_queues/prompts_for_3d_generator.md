# 3D Generator Prompts: Heaps and Priority Queues

These prompts are designed for use with 3D generation tools such as Three.js, WebGL, Blender scripting agents, or AI-powered 3D scene generators. Each prompt provides sufficient detail to create an educational, interactive 360-degree visualization.

---

## Prompt 1: Heap Structure with Array Mapping

Generate a 360-degree, interactive 3D scene showing a max-heap as a pyramid structure with its corresponding array representation. The background is a cosmic void with deep purple gradients (#1a0a2e).

Create a max-heap with values [90, 80, 70, 60, 50, 40, 30] arranged as a pyramid:
- Level 0 (apex): Node 90 (index 0)
- Level 1: Nodes 80 (index 1), 70 (index 2)
- Level 2: Nodes 60 (index 3), 50 (index 4), 40 (index 5), 30 (index 6)

**Pyramid Structure**:
- Each node is a glowing platform (30cm diameter) with a floating orb containing the value
- Platforms arranged in pyramid formation, 50cm vertical spacing between levels
- Horizontal spacing doubles at each level
- Root at apex glows brightest (#ff6b35), intensity decreases at lower levels

**Array Ring**:
- Circular array of 7 slots surrounding the pyramid base (radius 150cm)
- Each slot shows: index number and value
- Glowing connection lines link each array slot to its corresponding pyramid node
- Lines are semi-transparent (#7f8c8d at 50% opacity)

**Index Formula Display**:
When hovering over any node, show:
- "Parent: floor((i-1)/2)"
- "Left Child: 2i + 1"
- "Right Child: 2i + 2"
With actual calculated values for that node

**Interactive Elements**:
- Click node to highlight its parent and children
- Toggle button to show/hide array connections
- "Array View" button to flatten pyramid into linear array
- Index labels toggle

The camera can orbit 360 degrees, zoom, and has preset views: front, top-down, array-focus.

---

## Prompt 2: Max-Heap vs Min-Heap Comparison

Generate a 360-degree, interactive 3D scene with split view comparing max-heap (left) and min-heap (right) using the same set of values [50, 30, 70, 20, 40, 60, 80].

**Max-Heap (Left Side)**:
- Root: 80 (maximum value)
- Arrangement satisfies: parent >= children
- Color gradient: Hot orange (#ff6b35) at top, cooling to cyan (#4ecdc4) at bottom
- "MAX-HEAP" label above pyramid
- "Root = Maximum" indicator

**Min-Heap (Right Side)**:
- Root: 20 (minimum value)
- Arrangement satisfies: parent <= children
- Color gradient: Cool cyan (#00d4ff) at top, warming to coral (#ff6b6b) at bottom
- "MIN-HEAP" label above pyramid
- "Root = Minimum" indicator

**Comparison Features**:
- Central panel showing property comparison
- "Extract" button that removes root from both heaps simultaneously
- Shows different values extracted (80 vs 20)
- Synchronized insert operation showing same value going to different positions

**Visual Distinction**:
- Max-heap has upward-pointing arrow particles (priority rises)
- Min-heap has downward-pointing arrow particles (smallest rises to top)
- Clear visual separation between the two heaps

Include educational labels explaining when to use each type (max-heap for largest elements, min-heap for smallest).

---

## Prompt 3: Insert Operation with Bubble-Up

Generate a 360-degree, interactive 3D scene demonstrating heap insertion with bubble-up animation. Start with a max-heap [90, 80, 70, 60, 50].

**Insert Value 85**:

Step 1: "New element 85 arrives"
- Value 85 appears as a glowing orb above the array ring
- Next available position (index 5) highlighted in array

Step 2: "Place at end of heap"
- Orb moves to array position 5
- Corresponding pyramid position (level 2, rightmost) lights up
- Element materializes at bottom of pyramid

Step 3: "Compare with parent (index 2, value 70)"
- Connection line to parent glows
- Comparison display: "85 > 70? YES - SWAP"
- Parent node highlighted

Step 4: "Bubble up - swap with parent"
- Smooth swap animation: 85 rises, 70 descends
- Array positions 2 and 5 swap values
- Trail shows upward movement

Step 5: "Compare with new parent (index 0, value 90)"
- Connection to root glows
- Comparison display: "85 > 90? NO - STOP"
- Element settles in final position

Step 6: "Insert complete"
- Final heap: [90, 80, 85, 60, 50, 70]
- Success effect on inserted element
- Bubble-up path trail fades

**Controls**:
- Input field for custom value
- "Insert" button
- Speed slider for animation
- Step-by-step mode toggle

---

## Prompt 4: Extract Operation with Bubble-Down

Generate a 360-degree, interactive 3D scene demonstrating heap extraction with bubble-down animation. Start with a max-heap [90, 80, 70, 60, 50, 40, 30].

**Extract Maximum (90)**:

Step 1: "Extract root element"
- Root node (90) highlighted and pulses
- "Extracting maximum: 90" label

Step 2: "Remove root"
- Root orb lifts off pyramid apex with particle trail
- Floats to "Extracted" display area
- Empty position at apex

Step 3: "Move last element to root"
- Last element (30, index 6) highlighted
- Teleportation animation: 30 moves from bottom to apex
- Array shows: last element moves to index 0

Step 4: "Bubble down - compare with children"
- Children (80 at index 1, 70 at index 2) highlighted
- Comparison: "Larger child is 80"
- "30 < 80? YES - SWAP"

Step 5: "Swap with larger child"
- 30 and 80 swap positions
- 30 descends to level 1, 80 rises to root
- Array updates: indices 0 and 1 swap

Step 6: "Continue bubble down"
- New children (60 at index 3, 50 at index 4) highlighted
- "30 < 60? YES - SWAP"
- 30 and 60 swap

Step 7: "Bubble down complete"
- 30 is now a leaf (no children to compare)
- Final heap: [80, 60, 70, 30, 50, 40]
- Extracted value 90 displayed prominently

**Controls**:
- "Extract" button
- Speed slider
- Step-by-step mode
- "Reset" to restore original heap

---

## Prompt 5: Heapify Array Transformation

Generate a 360-degree, interactive 3D scene showing the heapify operation that transforms an unsorted array into a valid max-heap.

**Input**: Unsorted array [30, 50, 80, 20, 60, 40, 90]

**Initial State**:
- Array ring shows unsorted values
- Pyramid shows same arrangement (not a valid heap)
- "Invalid Heap" warning indicator
- Violations highlighted (e.g., 30 < 50, 30 < 80)

**Heapify Process** (bottom-up):

Step 1: "Start from last non-leaf node"
- Index calculation: floor(7/2) - 1 = 2
- Node at index 2 (value 80) highlighted
- "Processing index 2"

Step 2: "Bubble down from index 2"
- Children: 40 (index 5), 90 (index 6)
- 80 < 90, swap needed
- After swap: 90 at index 2, 80 at index 6

Step 3: "Move to index 1"
- Node at index 1 (value 50) highlighted
- Children: 20 (index 3), 60 (index 4)
- 50 < 60, swap needed
- After swap: 60 at index 1, 50 at index 4

Step 4: "Move to index 0 (root)"
- Node at index 0 (value 30) highlighted
- Children: 60 (index 1), 90 (index 2)
- 30 < 90, swap with larger child (90)
- Continue bubble down...

Step 5: "Heapify complete"
- Final valid max-heap displayed
- "Valid Heap" success indicator
- All heap properties satisfied

**Efficiency Display**:
- "Heapify: O(n)" vs "Insert one-by-one: O(n log n)"
- Operation count comparison

---

## Prompt 6: K Largest Elements Problem

Generate a 360-degree, interactive 3D scene showing how to find the k largest elements using a min-heap. Problem: Find 3 largest elements from stream [5, 2, 9, 1, 7, 6, 3].

**Setup**:
- Stream of numbers displayed as incoming blocks on a conveyor
- Min-heap of size k=3 (pyramid with 3 positions)
- "K Largest" result area

**Algorithm Visualization**:

Step 1: "Process 5" - Heap has space, insert 5
- Heap: [5]

Step 2: "Process 2" - Heap has space, insert 2
- Heap: [2, 5] (min-heap, 2 at root)

Step 3: "Process 9" - Heap has space, insert 9
- Heap: [2, 5, 9]

Step 4: "Process 1" - Heap full, compare with min (2)
- 1 < 2, discard 1
- "1 is smaller than heap minimum, skip"

Step 5: "Process 7" - Compare with min (2)
- 7 > 2, extract 2, insert 7
- Heap: [5, 7, 9]

Step 6: "Process 6" - Compare with min (5)
- 6 > 5, extract 5, insert 6
- Heap: [6, 7, 9]

Step 7: "Process 3" - Compare with min (6)
- 3 < 6, discard 3

**Result**:
- Final heap contains [6, 7, 9]
- "3 Largest Elements: 9, 7, 6"
- Complexity: O(n log k)

---

## Prompt 7: Priority Queue Task Scheduler

Generate a 360-degree, interactive 3D scene showing a task scheduler using a max-heap priority queue. Tasks have different priorities.

**Setup**:
- Task queue visualized as max-heap
- Tasks are colored blocks with priority numbers
- "CPU" processing area
- Completed tasks area

**Tasks**:
- Task A (priority 3): Blue block
- Task B (priority 7): Red block
- Task C (priority 1): Green block
- Task D (priority 5): Yellow block

**Scheduling Animation**:

Step 1: "Add all tasks to priority queue"
- Tasks inserted into max-heap
- Heap arranges by priority: [B(7), D(5), C(1), A(3)]

Step 2: "Execute highest priority task"
- B(7) extracted from heap
- B moves to CPU area
- "Executing Task B (priority 7)"

Step 3: "Next highest priority"
- D(5) now at root
- D extracted and executed

Step 4: "Continue until empty"
- A(3) executed
- C(1) executed last

**New Task Arrival**:
- Task E (priority 6) arrives mid-execution
- Inserted into heap, bubbles to appropriate position
- Demonstrates dynamic priority handling

**Real-World Context**:
- "Operating System Process Scheduling"
- "Emergency Room Triage"
- "Print Job Queue"

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
- Pyramid structures should have subtle glow effects and particle systems for visual appeal
