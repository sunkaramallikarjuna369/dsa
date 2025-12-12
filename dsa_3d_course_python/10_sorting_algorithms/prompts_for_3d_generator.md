# 3D Generator Prompts: Sorting Algorithms

These prompts are designed for use with 3D generation tools such as Three.js, WebGL, Blender scripting agents, or AI-powered 3D scene generators. Each prompt provides sufficient detail to create an educational, interactive 360-degree visualization.

---

## Prompt 1: Bubble Sort Visualization

Generate a 360-degree, interactive 3D scene demonstrating bubble sort on an array of 8 elements. The background is a dark gradient (#1a1a2e to #16213e).

**Array Setup**:
- Array: [64, 34, 25, 12, 22, 11, 90, 45]
- 8 vertical bars on a reflective platform
- Bar heights proportional to values
- Color gradient: blue (small) to orange (large)

**Bubble Sort Animation**:

Pass 1:
- Compare bars 0,1 (64,34): 64>34, swap with hopping animation
- Compare bars 1,2 (64,25): 64>25, swap
- Continue through array
- Largest element (90) bubbles to position 7
- Position 7 turns green (sorted)

Pass 2:
- Repeat for positions 0-6
- Second largest (64) reaches position 6
- Position 6 turns green

(Continue until sorted)

**Visual Elements**:
- Comparison highlight: Both bars glow yellow
- Swap animation: Bars hop over each other (400ms)
- Sorted indicator: Green glow on final positions
- Pass counter: "Pass: X of N"
- Swap counter: "Swaps: X"
- Comparison counter: "Comparisons: X"

**Controls**:
- Play/Pause, Step, Speed slider
- Reset button
- Custom array input

---

## Prompt 2: Selection Sort Visualization

Generate a 360-degree, interactive 3D scene demonstrating selection sort. Show the minimum-finding scanner and element placement.

**Array Setup**:
- Array: [29, 10, 14, 37, 13, 25, 18, 33]
- 8 vertical bars with value labels
- Unsorted portion: neutral gray
- Sorted portion: green tint

**Selection Sort Animation**:

Round 1:
- Scanner beam starts at index 0
- Current minimum: 29 (highlighted yellow)
- Scanner moves right, finds 10 < 29
- Minimum highlight transfers to 10
- Scanner continues, 10 remains minimum
- 10 lifts up, slides to position 0
- 29 shifts right to fill gap
- Position 0 now sorted (green)

Round 2:
- Scanner starts at index 1
- Find minimum in remaining unsorted portion
- Place at index 1
- Sorted boundary moves right

(Continue until sorted)

**Visual Elements**:
- Scanner beam: Cyan light moving right
- Current minimum: Yellow highlight
- Lift animation: Element rises 50cm
- Slide animation: Element moves horizontally
- Drop animation: Element descends to position
- Sorted boundary: Vertical divider line

---

## Prompt 3: Insertion Sort Visualization

Generate a 360-degree, interactive 3D scene demonstrating insertion sort. Show elements being picked up and inserted into the sorted portion.

**Array Setup**:
- Array: [12, 11, 13, 5, 6, 7, 15, 3]
- First element (12) starts as sorted portion
- Remaining elements are unsorted

**Insertion Sort Animation**:

Step 1: Insert 11
- Element 11 lifts from position 1
- Compare with 12: 11 < 12
- 12 shifts right
- 11 drops into position 0
- Sorted portion: [11, 12]

Step 2: Insert 13
- Element 13 lifts from position 2
- Compare with 12: 13 > 12, stop
- 13 drops into position 2 (no shift needed)
- Sorted portion: [11, 12, 13]

Step 3: Insert 5
- Element 5 lifts
- Compare with 13, 12, 11: all larger
- All three shift right
- 5 drops into position 0
- Sorted portion: [5, 11, 12, 13]

(Continue until sorted)

**Visual Elements**:
- Lift animation: Element rises with glow
- Comparison trail: Line connecting compared elements
- Shift animation: Elements slide right (150ms each)
- Drop animation: Element descends to final position
- Sorted portion: Subtle green background
- Current element: Bright yellow highlight

---

## Prompt 4: Merge Sort Visualization

Generate a 360-degree, interactive 3D scene demonstrating merge sort with divide-and-conquer visualization. Show the recursive splitting and merging.

**Array Setup**:
- Array: [38, 27, 43, 3, 9, 82, 10, 15]
- 8 bars on main platform
- Additional space below for merge operations

**Divide Phase**:

Level 1: Split into [38,27,43,3] and [9,82,10,15]
- Array splits in middle
- Halves separate horizontally (move apart)
- Connecting lines show relationship

Level 2: Split each half again
- [38,27] [43,3] | [9,82] [10,15]
- Four groups now visible

Level 3: Split to single elements
- [38] [27] [43] [3] | [9] [82] [10] [15]
- Base case reached

**Merge Phase**:

Merge Level 3 to 2:
- Merge [38] and [27] → [27, 38]
- Two elements compare, smaller goes first
- Merge [43] and [3] → [3, 43]
- Merge [9] and [82] → [9, 82]
- Merge [10] and [15] → [10, 15]

Merge Level 2 to 1:
- Merge [27,38] and [3,43] → [3, 27, 38, 43]
- Elements interleave based on comparison
- Merge [9,82] and [10,15] → [9, 10, 15, 82]

Merge Level 1 to 0:
- Merge [3,27,38,43] and [9,10,15,82]
- Final sorted array: [3, 9, 10, 15, 27, 38, 43, 82]

**Visual Elements**:
- Split animation: Groups separate horizontally
- Depth levels: Vertical positioning shows recursion depth
- Merge animation: Elements interleave with smooth motion
- Comparison indicator: Shows which elements being compared
- Auxiliary space: Temporary merge area highlighted

---

## Prompt 5: Quick Sort Visualization

Generate a 360-degree, interactive 3D scene demonstrating quick sort with pivot selection and partitioning.

**Array Setup**:
- Array: [10, 80, 30, 90, 40, 50, 70, 20]
- 8 bars on platform
- Pivot selection: Last element (20)

**Quick Sort Animation**:

Partition 1 (full array, pivot=20):
- Pivot (20) highlighted in gold
- Pointer i starts before array (index -1)
- Pointer j scans from left

- j=0: 10 < 20, i++, swap arr[i] with arr[j] (no change, same position)
- j=1: 80 > 20, no swap
- j=2: 30 > 20, no swap
- j=3: 90 > 20, no swap
- j=4: 40 > 20, no swap
- j=5: 50 > 20, no swap
- j=6: 70 > 20, no swap
- Final: swap pivot with arr[i+1]
- Result: [10, 20, 30, 90, 40, 50, 70, 80]
- Pivot 20 in final position (index 1), turns green

Partition 2 (left of pivot: [10]):
- Single element, already sorted

Partition 3 (right of pivot: [30, 90, 40, 50, 70, 80]):
- New pivot: 80
- Partition around 80
- Continue recursively

**Visual Elements**:
- Pivot: Gold highlight, stays visible during partition
- Pointer i: Cyan marker
- Pointer j: Magenta marker
- Swap animation: Elements exchange positions
- Partition boundaries: Vertical lines
- Final position: Green glow when pivot placed

---

## Prompt 6: Algorithm Comparison Race

Generate a 360-degree, interactive 3D scene showing multiple sorting algorithms racing on the same data.

**Setup**:
- 4 identical arrays of 20 elements (random values)
- 4 separate bar chart panels arranged in 2x2 grid
- Labels: "Bubble Sort", "Selection Sort", "Merge Sort", "Quick Sort"

**Race Animation**:
- All algorithms start simultaneously
- Each panel shows its algorithm's progress
- Speed normalized to show relative efficiency
- Counters for each: comparisons, swaps/moves

**Expected Results**:
- Bubble Sort: Slowest, many swaps
- Selection Sort: Fewer swaps than bubble
- Merge Sort: Fast, consistent
- Quick Sort: Fast, varies by pivot choice

**Metrics Display**:
- Real-time comparison count
- Real-time swap/move count
- Progress bar for each
- "FINISHED" indicator when complete
- Final ranking display

**Visual Elements**:
- Split-screen 2x2 layout
- Synchronized start signal
- Independent progress tracking
- Winner celebration effect
- Final statistics comparison table

---

## Prompt 7: Sorting Stability Demonstration

Generate a 360-degree, interactive 3D scene demonstrating the concept of sorting stability using colored elements with duplicate values.

**Setup**:
- Array of cards with values and colors
- Example: [3-Red, 1-Blue, 2-Green, 1-Red, 3-Blue, 2-Red]
- Cards have both number (for sorting) and color (for tracking)

**Stable Sort (Merge Sort)**:
- Sort by number value
- Equal values maintain original relative order
- Result: [1-Blue, 1-Red, 2-Green, 2-Red, 3-Red, 3-Blue]
- Blue 1 stays before Red 1 (original order preserved)

**Unstable Sort (Quick Sort)**:
- Sort same array
- Equal values may swap relative order
- Result might be: [1-Red, 1-Blue, 2-Red, 2-Green, 3-Blue, 3-Red]
- Original order of equal elements not guaranteed

**Visual Emphasis**:
- Highlight pairs of equal values
- Track their relative positions
- Show when order is preserved vs changed
- "Stable" vs "Unstable" labels

---

## General Requirements for All Prompts

- All scenes must support 360-degree camera orbit and zoom functionality
- Include educational labels with readable fonts (minimum 14pt equivalent)
- Use consistent color coding across all scenes as defined in the color palette
- Ensure interactive elements have clear hover states and click feedback
- Animations should be smooth (60fps target) with adjustable speed controls
- Include accessibility features: high contrast mode, colorblind-friendly palette
- All text labels should remain readable from any camera angle
- Export scenes in web-compatible formats (glTF, WebGL-ready)
- Include Python code snippets that highlight during relevant animation steps
- Provide step-by-step controls for educational walkthrough
- Show complexity information: O(n²) vs O(n log n) comparisons
