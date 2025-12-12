# 3D Generator Prompts: Searching Algorithms

These prompts are designed for use with 3D generation tools such as Three.js, WebGL, Blender scripting agents, or AI-powered 3D scene generators. Each prompt provides sufficient detail to create an educational, interactive 360-degree visualization.

---

## Prompt 1: Linear Search Visualization

Generate a 360-degree, interactive 3D scene demonstrating linear search on an unsorted array. The background is a dark metallic data center (#1a1a2e).

**Array Setup**:
- Array: [23, 45, 12, 67, 34, 89, 56, 78, 90, 11]
- 10 floor tiles in a corridor, each with a glowing cube
- Cubes display element values
- Tiles numbered 0-9 below each cube
- Target value: 89

**Linear Search Animation**:

Step 1: "Initialize search for 89"
- Target value displayed prominently
- Spotlight positioned at index 0
- All elements dimly lit

Step 2: "Check index 0: 23"
- Spotlight illuminates tile 0
- Comparison: "23 == 89? NO"
- Tile dims slightly after check

Step 3-5: "Check indices 1, 2, 3, 4"
- Spotlight moves right one tile at a time
- Each comparison shown
- "45 == 89? NO", "12 == 89? NO", etc.

Step 6: "Check index 5: 89 - FOUND!"
- Spotlight on tile 5
- Comparison: "89 == 89? YES"
- Tile 5 glows green with success particles
- "Found at index 5" message

**Statistics Display**:
- Comparisons made: 6
- Array size: 10
- Time complexity: O(n)

**Controls**:
- Play/Pause button
- Step forward/backward
- Speed slider
- Custom target input

---

## Prompt 2: Binary Search Visualization

Generate a 360-degree, interactive 3D scene demonstrating binary search on a sorted array. Show the divide-and-conquer approach with shrinking search space.

**Array Setup**:
- Sorted array: [11, 23, 34, 45, 56, 67, 78, 89, 90, 95]
- 10 tiles in ascending order
- Values clearly visible on cubes
- Target value: 78

**Pointer Markers**:
- Low pointer: Blue marker (index 0 initially)
- High pointer: Red marker (index 9 initially)
- Mid pointer: Yellow marker (calculated)

**Binary Search Animation**:

Step 1: "Initialize binary search"
- Entire corridor lit
- Low=0, High=9, Mid=4
- "Search space: indices 0-9"

Step 2: "Compare mid (index 4, value 56) with target 78"
- Mid tile highlighted bright yellow
- Comparison: "56 < 78"
- "Target is in right half"

Step 3: "Eliminate left half"
- Tiles 0-4 dim significantly
- Low moves to index 5
- "Search space: indices 5-9"

Step 4: "New mid is index 7 (value 89)"
- Mid tile highlighted
- Comparison: "89 > 78"
- "Target is in left half"

Step 5: "Eliminate right half"
- Tiles 8-9 dim
- High moves to index 6
- "Search space: indices 5-6"

Step 6: "New mid is index 5 (value 67)"
- Comparison: "67 < 78"
- Low moves to index 6

Step 7: "Check index 6 (value 78) - FOUND!"
- Tile 6 glows green
- "Found at index 6"
- Success animation

**Efficiency Comparison**:
- Binary search comparisons: 4
- Linear search would need: 7
- "O(log n) vs O(n)"

---

## Prompt 3: Binary Search - Not Found Case

Generate a 360-degree, interactive 3D scene showing binary search when the target is not in the array, demonstrating how the search space becomes empty.

**Array Setup**:
- Sorted array: [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
- Target value: 55 (not in array)

**Search Animation**:

Step 1: "Search for 55 in sorted array"
- Full corridor lit
- Low=0, High=9, Mid=4

Step 2: "Mid value 50 < 55, go right"
- Left half dims
- Low=5, High=9, Mid=7

Step 3: "Mid value 80 > 55, go left"
- Right portion dims
- Low=5, High=6, Mid=5

Step 4: "Mid value 60 > 55, go left"
- High=4
- "Low > High: Search space empty!"

Step 5: "Target 55 not found"
- Entire corridor dims to red tint
- "NOT FOUND" message
- "Would insert at index 5"

**Insert Position Visualization**:
- Gap between indices 4 and 5 highlighted
- "Insert position: 5"
- Shows where 55 would go to maintain sorted order

---

## Prompt 4: Binary Search Variations - First and Last Occurrence

Generate a 360-degree, interactive 3D scene showing how to find the first and last occurrence of a duplicate value using modified binary search.

**Array Setup**:
- Sorted array with duplicates: [1, 2, 3, 5, 5, 5, 5, 8, 9, 10]
- Target value: 5 (appears 4 times at indices 3-6)

**Find First Occurrence**:

Step 1: "Find first occurrence of 5"
- All 5's highlighted in yellow
- Standard binary search begins

Step 2: "Found 5 at index 4, but continue left"
- Index 4 marked as "candidate"
- Continue searching left half
- "Looking for earlier occurrence"

Step 3: "Found 5 at index 3, continue left"
- Index 3 marked as new candidate
- Left half has no more 5's

Step 4: "First occurrence at index 3"
- Index 3 glows green
- "First 5 found at index 3"

**Find Last Occurrence**:

Step 5: "Find last occurrence of 5"
- Reset, search for rightmost 5

Step 6: "Found 5 at index 4, continue right"
- Index 4 marked as candidate
- Continue searching right half

Step 7: "Found 5 at index 6, continue right"
- Index 6 marked as new candidate
- Right half has no more 5's

Step 8: "Last occurrence at index 6"
- Index 6 glows green
- "Last 5 found at index 6"

**Range Display**:
- "5 appears from index 3 to 6"
- "Count: 4 occurrences"
- Range highlighted in special color

---

## Prompt 5: BST Search Visualization

Generate a 360-degree, interactive 3D scene showing search in a Binary Search Tree, following the BST property to navigate to the target.

**BST Setup**:
- Tree with values: Root=50, Left subtree: 30(20, 40), Right subtree: 70(60, 80)
- Nodes as glowing spheres with values
- BST property visible: left < parent < right
- Target value: 40

**BST Search Animation**:

Step 1: "Search for 40 starting at root"
- Root node (50) highlighted cyan
- "Compare 40 with 50"

Step 2: "40 < 50, go left"
- Left arrow glows
- Path from 50 to 30 illuminates
- Right subtree dims
- "Eliminated right subtree"

Step 3: "Compare 40 with 30"
- Node 30 highlighted
- "40 > 30, go right"

Step 4: "Go right from 30"
- Right arrow from 30 glows
- Path to 40 illuminates
- Left child (20) dims

Step 5: "Compare 40 with 40 - FOUND!"
- Node 40 pulses green
- "Target found!"
- Complete path highlighted: 50 -> 30 -> 40

**Path Statistics**:
- Path length: 3 nodes
- Comparisons: 3
- Tree height: 3
- "O(log n) average case"

**Not Found Case**:
- Search for 35
- Path: 50 -> 30 -> 40 -> null (left child)
- "35 not found, would be left child of 40"

---

## Prompt 6: Search in Rotated Sorted Array

Generate a 360-degree, interactive 3D scene showing binary search in a rotated sorted array, where the array has been rotated at some pivot point.

**Rotated Array Setup**:
- Original sorted: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
- Rotated at index 4: [5, 6, 7, 8, 9, 10, 1, 2, 3, 4]
- Corridor "bent" at rotation point
- Two sorted segments visible
- Target: 2

**Rotation Visualization**:
- Pivot point (between 10 and 1) marked
- Left segment: [5, 6, 7, 8, 9, 10] - ascending
- Right segment: [1, 2, 3, 4] - ascending
- Visual "bend" in corridor

**Modified Binary Search**:

Step 1: "Identify rotation in array"
- Pivot point highlighted
- "Array rotated at index 6"

Step 2: "Mid = index 4 (value 9)"
- Check which half is sorted
- "Left half [5,6,7,8,9] is sorted"

Step 3: "Is target 2 in sorted left half?"
- "2 < 5, so NO"
- "Search right half"
- Left half dims

Step 4: "New search space: indices 5-9"
- Mid = index 7 (value 2)
- "Found target 2 at index 7!"

**Algorithm Explanation**:
- "At each step, one half is always sorted"
- "Check if target is in sorted half"
- "If yes, search there; if no, search other half"

---

## Prompt 7: Search Complexity Comparison

Generate a 360-degree, interactive 3D scene comparing linear search and binary search side by side, demonstrating the efficiency difference.

**Dual Corridor Setup**:
- Left side: Unsorted array for linear search
- Right side: Sorted array for binary search
- Same values, same target
- Array size: 16 elements
- Target: element at index 14

**Parallel Execution**:

Linear Search (Left):
- Spotlight scans from index 0
- One element at a time
- Counter shows comparisons: 1, 2, 3, ... 15

Binary Search (Right):
- Divide and conquer
- Search space halves each step
- Counter shows comparisons: 1, 2, 3, 4

**Race Visualization**:
- Both searches start simultaneously
- Binary search finishes much faster
- Linear search still scanning
- "Binary search: DONE in 4 comparisons"
- "Linear search: Still going... 15 comparisons"

**Scaling Demonstration**:
- Show array sizes: 16, 256, 65536
- Linear search comparisons: 16, 256, 65536
- Binary search comparisons: 4, 8, 16
- "As n doubles, binary search adds only 1 comparison"

**Complexity Graph**:
- 3D graph showing O(n) vs O(log n)
- X-axis: array size
- Y-axis: comparisons
- Linear: steep line
- Binary: nearly flat curve

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
