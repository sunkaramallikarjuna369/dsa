# Visual Design: Heaps and Priority Queues

## Environment Overview

The Heaps world features a pyramid structure floating in space, surrounded by an array ring that shows the linear storage representation. The environment emphasizes the relationship between the tree structure and array indices.

### Background and Atmosphere

The scene is set in a cosmic void with deep purple and blue gradients. The heap pyramid floats in the center, constructed of glowing platforms at each level. An array ring circles the base, with glowing connections showing the index-to-node mapping. Particle effects flow upward to represent priority rising.

### Lighting

The root node at the apex glows brightest, with intensity decreasing at lower levels to represent priority hierarchy. During operations, active nodes pulse with increased brightness. The array ring has uniform soft lighting with highlights on active indices.

### Camera Behavior

The camera can orbit 360 degrees around the pyramid, zoom to examine individual nodes, and switch between "tree view" (pyramid) and "array view" (linear). A split-screen mode shows both representations simultaneously. The camera can follow elements during bubble-up and bubble-down operations.

### Interaction Ideas

Clicking a node shows its value, index, parent index, and children indices. Dragging allows rotation. Insert and extract buttons trigger animated operations. A "heapify" button transforms an unsorted array into a heap with animation.

---

## Sub-Concept 1: Heap Structure and Array Representation

### 3D Metaphor

The heap is visualized as a pyramid of floating platforms. Each platform holds a glowing orb representing a node value. The pyramid is complete (filled level by level), reflecting the complete binary tree property.

**Pyramid Structure**:
- Level 0 (apex): Single platform for root
- Level 1: Two platforms for root's children
- Level 2: Four platforms
- Each level doubles in width

**Array Ring**:
- Circular array of slots surrounding the pyramid base
- Each slot contains the same value as its corresponding node
- Glowing lines connect array indices to pyramid nodes
- Index labels visible on each slot

**Index Relationships**:
- Parent of index i: floor((i-1)/2)
- Left child of index i: 2i + 1
- Right child of index i: 2i + 2
- These formulas displayed when hovering over connections

### Visual Elements

- Pyramid of glowing platforms
- Array ring with index labels
- Connection lines between array and tree
- Index formula display panel
- Level indicators on pyramid

---

## Sub-Concept 2: Max-Heap vs Min-Heap

### 3D Metaphor

Max-heap and min-heap are shown side by side to contrast their properties. Color gradients reinforce the ordering: max-heap has warm colors (red/orange) at top cooling to blue at bottom; min-heap has cool colors (blue) at top warming to red at bottom.

**Max-Heap (Left)**:
- Root is maximum value
- Parent >= Children at every node
- Color gradient: Hot (top) to Cool (bottom)
- "MAX" label at apex
- Priority flows upward (larger values rise)

**Min-Heap (Right)**:
- Root is minimum value
- Parent <= Children at every node
- Color gradient: Cool (top) to Hot (bottom)
- "MIN" label at apex
- Priority flows upward (smaller values rise)

**Comparison Panel**:
- Side-by-side property comparison
- Same values, different arrangements
- Extract operation shows different results

### Visual Elements

- Dual pyramid display
- Color-coded priority gradients
- Property labels at each node
- Comparison information panel
- Synchronized operations option

---

## Sub-Concept 3: Insert Operation (Bubble-Up)

### 3D Metaphor

Insertion is visualized as a new element appearing at the bottom of the heap and "bubbling up" to its correct position. The element glows brighter as it rises (for max-heap) or dims as it rises (for min-heap).

**Insert Animation Sequence**:
1. New value appears at next available position (end of array)
2. Array slot lights up, connection to pyramid position shown
3. Element materializes at bottom of pyramid
4. Compare with parent: if heap property violated, swap
5. Element rises one level with swap animation
6. Repeat until heap property satisfied or root reached
7. Final position highlighted with success effect

**Bubble-Up Path**:
- Glowing trail shows the path taken
- Each comparison shown with result indicator
- Swap animations show values exchanging positions
- Parent-child relationships highlighted during comparisons

### Visual Elements

- New element materialization effect
- Rising/bubbling animation
- Comparison result indicators (swap/stay)
- Path trail visualization
- Array updates synchronized with tree

---

## Sub-Concept 4: Extract Operation (Bubble-Down)

### 3D Metaphor

Extraction removes the root and reorganizes the heap. The root lifts off, the last element teleports to the apex, then "bubbles down" to its correct position.

**Extract Animation Sequence**:
1. Root element highlighted as target
2. Root lifts off pyramid apex with extraction effect
3. Last element in array highlighted
4. Last element teleports to apex position
5. Compare with children: swap with larger (max) or smaller (min) child
6. Element descends one level with swap animation
7. Repeat until heap property satisfied or leaf reached
8. Extracted value displayed prominently

**Bubble-Down Path**:
- Descending trail shows the path taken
- Child comparison shown (which child to swap with)
- Swap animations show values exchanging
- Leaf detection when no more children

### Visual Elements

- Root extraction lift-off effect
- Teleportation animation for last element
- Descending/sinking animation
- Child comparison visualization
- Extracted value display

---

## Sub-Concept 5: Heapify Operation

### 3D Metaphor

Heapify transforms an unsorted array into a valid heap. The visualization shows the bottom-up approach, starting from the last non-leaf node and working up to the root.

**Heapify Animation**:
1. Unsorted array displayed in ring
2. Corresponding unordered pyramid shown
3. Last non-leaf node highlighted (index n/2 - 1)
4. Bubble-down from this node
5. Move to previous node, bubble-down
6. Continue until root is processed
7. Final heap structure revealed

**Bottom-Up Process**:
- Progress indicator showing current node
- Each sub-heap becomes valid before moving up
- Efficiency note: O(n) not O(n log n)
- Comparison with naive insert-one-by-one approach

### Visual Elements

- Unsorted to sorted transformation
- Progress indicator
- Sub-heap validity markers
- Complexity comparison display
- Step-by-step controls

---

## Sub-Concept 6: Priority Queue Applications

### 3D Metaphor

Real-world applications of priority queues are visualized with contextual scenes.

**Task Scheduling**:
- Tasks as colored blocks with priority numbers
- Heap organizes tasks by priority
- Highest priority task extracted for execution
- New tasks inserted and bubble to correct position

**K Largest Elements**:
- Stream of numbers flowing in
- Min-heap of size k maintained
- Numbers larger than heap minimum replace it
- Final heap contains k largest elements

**Merge K Sorted Lists**:
- K sorted lists displayed as columns
- Min-heap contains one element from each list
- Smallest extracted, next from same list inserted
- Merged result builds incrementally

### Visual Elements

- Application-specific contexts
- Real-world analogies
- Step-by-step problem solving
- Result visualization

---

## Color Palette

| Element | Color | Hex Code |
|---------|-------|----------|
| Background | Deep Purple | #1a0a2e |
| Max-heap high priority | Hot Orange | #ff6b35 |
| Max-heap low priority | Cool Blue | #4ecdc4 |
| Min-heap high priority | Cool Cyan | #00d4ff |
| Min-heap low priority | Warm Coral | #ff6b6b |
| Array ring | Soft White | #e8e8f0 |
| Active node | Bright Yellow | #ffd93d |
| Swap animation | Electric Purple | #9b59b6 |
| Success | Green | #2ecc71 |
| Connection lines | Dim Gray | #7f8c8d |
| Index labels | White | #ffffff |

---

## Animation Timing

- Insert element appearance: 300ms
- Bubble-up per level: 400ms
- Comparison indicator: 200ms
- Swap animation: 350ms
- Extract lift-off: 500ms
- Teleport to apex: 300ms
- Bubble-down per level: 400ms
- Heapify per node: 500ms
- Array update sync: 100ms
- Camera transitions: 500ms ease-in-out
