# Visual Design: Sorting Algorithms

## Environment Overview

The Sorting Algorithms world presents arrays as animated bar charts where elements physically move, swap, and merge. The environment emphasizes the different mechanics of each sorting algorithm through distinct motion patterns.

### Background and Atmosphere

The scene is set in a sleek, modern visualization lab with a dark gradient background (#1a1a2e to #16213e). The bar chart sits on a reflective platform. Subtle grid lines provide spatial reference. The atmosphere is clean and focused on the data.

### Lighting

Bars have gradient coloring based on their values (cool blues for small values, warm oranges for large values). Active bars being compared or moved glow brighter. Sorted portions have a subtle green tint. The current operation area has enhanced lighting.

### Camera Behavior

The camera can orbit 360 degrees around the bar chart, zoom to see individual comparisons, and switch between overview and detail modes. For divide-and-conquer algorithms, the camera can show the recursive structure. Time-lapse mode shows the entire sort at high speed.

### Interaction Ideas

Clicking a bar shows its value and current index. Users can input custom arrays or generate random ones. Speed controls adjust animation pace. Algorithm selector switches between different sorting methods. Comparison counter tracks operations.

---

## Sub-Concept 1: Bubble Sort

### 3D Metaphor

Bubble sort is visualized as adjacent bars comparing and swapping, with larger values "bubbling" toward the right end through repeated passes.

**Comparison Animation**:
- Two adjacent bars highlighted
- Comparison indicator shows which is larger
- If left > right, bars swap with hopping animation
- Bars physically move past each other

**Pass Visualization**:
- Each pass moves the largest unsorted element to its final position
- Completed elements at right end glow green
- Pass counter shows current iteration
- Remaining unsorted portion highlighted

**Optimization Indicators**:
- Early termination if no swaps in a pass
- "Sorted!" indicator when complete
- Swap counter tracks total swaps

### Visual Elements

- Adjacent bar highlighting
- Swap hopping animation
- Sorted portion (green glow)
- Pass counter
- Swap counter

---

## Sub-Concept 2: Selection Sort

### 3D Metaphor

Selection sort is visualized as a scanner finding the minimum element in the unsorted portion, then placing it at the beginning of that portion.

**Minimum Finding**:
- Scanner beam moves through unsorted portion
- Current minimum highlighted in yellow
- When smaller element found, highlight transfers
- Final minimum pulses before moving

**Placement Animation**:
- Minimum element lifts up
- Slides to the front of unsorted portion
- Drops into position
- Sorted portion grows from left

**Boundary Visualization**:
- Clear divider between sorted (left) and unsorted (right)
- Sorted portion glows green
- Unsorted portion remains neutral
- Boundary moves right after each selection

### Visual Elements

- Scanner beam animation
- Current minimum highlight
- Lift and slide animation
- Sorted/unsorted boundary
- Selection counter

---

## Sub-Concept 3: Insertion Sort

### 3D Metaphor

Insertion sort is visualized as picking up each element and inserting it into its correct position in the sorted portion, like sorting playing cards.

**Pick Up Animation**:
- Current element lifts from its position
- Leaves a gap in the array
- Element hovers above the sorted portion

**Insertion Animation**:
- Element compares with sorted elements from right to left
- Larger elements shift right to make room
- Element drops into correct position
- Gap closes as element settles

**Sorted Portion Growth**:
- Sorted portion grows from left to right
- Each insertion maintains sorted order
- Comparison path shown as element finds its place

### Visual Elements

- Element lift animation
- Shift animation for larger elements
- Drop into position
- Sorted portion indicator
- Comparison path trail

---

## Sub-Concept 4: Merge Sort

### 3D Metaphor

Merge sort is visualized as the array splitting into smaller pieces, then merging back together in sorted order. The divide-and-conquer structure is shown spatially.

**Divide Phase**:
- Array splits in half
- Halves separate spatially (move apart)
- Splitting continues recursively
- Single elements are base case

**Merge Phase**:
- Two sorted halves shown side by side
- Elements from each half compared
- Smaller element moves to merged result
- Merged result builds from left to right

**Recursive Structure**:
- Tree-like visualization of splits
- Depth levels shown vertically
- Merging happens bottom-up
- Final merged array at top

**Auxiliary Space**:
- Temporary merge space shown
- Elements copy to temp during merge
- Final result copies back to original position

### Visual Elements

- Split animation (halves separate)
- Merge animation (interleaving)
- Recursive tree structure
- Temporary space visualization
- Depth level indicators

---

## Sub-Concept 5: Quick Sort

### 3D Metaphor

Quick sort is visualized as selecting a pivot, partitioning elements around it, then recursively sorting the partitions.

**Pivot Selection**:
- Pivot element highlighted in bright yellow
- Common strategies: first, last, middle, random, median-of-three
- Pivot glows throughout partition

**Partition Animation**:
- Two pointers (i and j) shown as markers
- Elements compared with pivot
- Smaller elements move to left side
- Larger elements move to right side
- Pivot placed in final position

**Recursive Visualization**:
- Left partition highlighted
- Right partition highlighted
- Recursion shown as nested operations
- Base case: single element partitions

**Pivot Final Position**:
- Pivot drops into its sorted position
- Elements to left are all smaller
- Elements to right are all larger
- Pivot turns green (in final position)

### Visual Elements

- Pivot highlight (yellow)
- Partition pointers (i, j markers)
- Element movement animations
- Recursive partition boundaries
- Final position indicator

---

## Sub-Concept 6: Algorithm Comparison

### 3D Metaphor

Side-by-side comparison of different sorting algorithms on the same data, showing their different approaches and speeds.

**Multi-Panel View**:
- 2-4 algorithms running simultaneously
- Same initial array for each
- Independent progress tracking
- Race to completion

**Metrics Display**:
- Comparison count for each
- Swap/move count for each
- Time elapsed
- Progress percentage

**Complexity Visualization**:
- O(n²) algorithms visibly slower on large arrays
- O(n log n) algorithms maintain speed
- Best/worst case scenarios demonstrated

### Visual Elements

- Split-screen layout
- Synchronized start
- Independent counters
- Winner indication
- Complexity labels

---

## Color Palette

| Element | Color | Hex Code |
|---------|-------|----------|
| Background | Dark Blue | #1a1a2e |
| Small Values | Cool Blue | #3498db |
| Large Values | Warm Orange | #e67e22 |
| Comparing | Bright Yellow | #f1c40f |
| Swapping | Electric Purple | #9b59b6 |
| Sorted | Success Green | #2ecc71 |
| Pivot | Gold | #f39c12 |
| Unsorted | Neutral Gray | #7f8c8d |
| Pointer i | Cyan | #00d4ff |
| Pointer j | Magenta | #ff6b9d |
| Merge Temp | Light Blue | #74b9ff |
| Platform | Dark Gray | #2d3436 |

---

## Animation Timing

- Comparison highlight: 200ms
- Swap animation: 400ms
- Element lift: 200ms
- Element drop: 200ms
- Shift animation: 150ms per element
- Split animation: 500ms
- Merge step: 300ms
- Pivot selection: 300ms
- Partition step: 250ms
- Pass completion: 400ms
- Sort completion: 800ms celebration
- Camera transitions: 500ms ease-in-out
